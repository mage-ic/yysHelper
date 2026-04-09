from Flow import JsonLoader, TempLoader, TempMatch, AdbT
from TemplateFind.baseFlow import BaseFlow


class GetFlow:
    @staticmethod
    def get_flow(flow_name, flow_config='./Config/FlowConfig.json'):
        flow_config = JsonLoader.load_json(flow_config)
        return flow_config[flow_name]


class Flow:
    @staticmethod
    def activate(sub_temp_config='./Config/ActivateTempConfig.json'):
        flow_config = GetFlow.get_flow('Activate')
        activateFlow = BaseFlow(TempLoader, TempMatch, AdbT, sub_temp_config, flow_config)
        try:
            while 1:
                activateFlow.run()
        except Exception as e:
            print(f'子流程错误:{e}')
