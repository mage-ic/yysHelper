import time


class BaseFlow:
    def __init__(self, TempLoader, TempMatch, AdbT, sub_temp_config, flow_config):
        self.TempLoader = TempLoader
        self.TempMatch = TempMatch
        self.AdbT = AdbT
        self.add_temp(sub_temp_config)
        self.flow_config = flow_config

    def add_temp(self, sub_temp_config):
        if sub_temp_config is None:
            raise Exception('Error, 子流程配置缺失')
        self.TempLoader.init_sub_process(sub_temp_config)
        return '子流程配置加载成功'

    def check_template(self, template_name):
        if self.TempLoader.get_template(template_name) is None:
            raise Exception('模板未定义')
        return self.TempMatch.find_temp(self.AdbT.get_page(), self.TempLoader.get_template(template_name),
                                        self.TempLoader.get_roi(template_name))

    def run(self):
        if self.flow_config is None:
            raise Exception('流程文件未配置')
        for template_name in self.flow_config:
            code = True
            try:
                while code:
                    cx, cy = self.check_template(template_name)
                    if cx is None:
                        time.sleep(0.5)
                    else:
                        msg = self.AdbT.human_like_swipe(cx, cy)
                        print(msg)
                        code = False
            except Exception as e:
                print(f'模板匹配错误 {e}')
