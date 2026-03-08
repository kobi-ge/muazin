from utils import extract_fields, set_mapping, generate_unique_id
from stt import speech_to_text
from hostility_level_logic import manager
import time


hostile_list = "R2Vub2NpZGUvV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUvT2NjdXBhdGlvYixSZWZ1Z2VlcyxJQ0MsQkRT"
least_hostile_list = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="



class ProcessorOrchestrator:
    def __init__(self, logger, consumer, elastic, mongo):
        self.logger = logger
        self.consumer = consumer
        self.elastic = elastic
        self.mongo = mongo

    def run(self, index_name):
        while True:
            message = self.consumer.consume()
            path, ctime, size, metadata = extract_fields(message)
            text = speech_to_text(path)
            metadata["text"] = text
            metadata['hostility_stats'] = manager(hostile_list, least_hostile_list, text)
            new_id = generate_unique_id(path, ctime, size)
            self.elastic.insert(index_name, metadata, new_id)
            self.mongo.insert(path, new_id)

    def init_svcs(self, topic_name, index_name):
        while True:
            try:
                self.logger.info("connecting to services")
                self.consumer.set_consumer(topic_name)
                self.elastic.connect()
                if not self.elastic.es.ping():
                    raise ConnectionError("Elasticsearch not responding to ping")
                if not self.elastic.es.indices.exists(index=index_name):
                    self.elastic.create_index(index_name, set_mapping())
                self.mongo.connect()
                self.mongo.create_fs()
                self.logger.info("All services ready!")
                break
            except Exception as e:
                self.logger.warning(f"Services not ready: {e}. Retrying in 5s...")
                time.sleep(5)
