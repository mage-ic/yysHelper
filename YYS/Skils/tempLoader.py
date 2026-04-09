import cv2
import json


class JsonLoader:
    @staticmethod
    def load_json(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)


class TempLoader:
    def __init__(self, config_path='./Config/ComTempConfig.json'):
        self.templates = {}
        self.rois = {}
        self.config = JsonLoader.load_json(config_path)

    def init_sub_process(self, sub_temp_config):
        sub_config = JsonLoader.load_json(sub_temp_config)
        self.config.update(sub_config)
        self.load_all_templates()

    def load_all_templates(self):
        self.templates.clear()
        self.rois.clear()
        for temp_name, (temp_path, roi_list) in self.config.items():
            img = cv2.imread(temp_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                raise Exception(f"模板加载失败: {temp_path}")
            self.templates[temp_name] = img
            self.rois[temp_name] = tuple(roi_list)
        # print(self.config)

    def get_template(self, temp_name):
        return self.templates.get(temp_name)

    def get_roi(self, temp_name):
        return self.rois.get(temp_name)
