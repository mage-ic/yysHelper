from Skils.adbConnect import AdbTools
from Skils.tempFind import TempFind
from Skils.tempLoader import TempLoader, JsonLoader

# 实例化所有工具类（只在模块加载时执行一次）
JsonLoader = JsonLoader()
TempLoader = TempLoader()
TempMatch = TempFind()
AdbT = AdbTools()

# 对外暴露这些对象，供其他文件导入
__all__ = ["JsonLoader", "TempLoader", "TempMatch", "AdbT"]
