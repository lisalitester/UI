# -*- coding: utf-8 -*-
from common.BaseRunner import ParametrizedTestCase
from PageObject.login.login_page import LoginTestPage
from PageObject.home.home_page import HomePage
import sys, os, time
from common.case_false_rerun import rerun
from common.login_who import who_login
from common.ElementParam import ElementParam
from PageObject.real_time_computation_page.task_operation_page.task_operation_page import TaskOperationPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)


#作业管理页面测试用例
class TaskOperationTest(ParametrizedTestCase):
    T_A_U= ElementParam.TASK_ADMINISTRATION_URL
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)  # 登录
        page.operate()

#     def to_resource_dir(self):
#         self.login()
#         app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/real_time_computation_yaml/task_administration_yaml/实时计算-作业管理页面校验.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = HomePage(app)  # page页实例化
#         page.operate()

    def get_url(to_url=""):
        # 连接到某个url且失败重跑的装饰器
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if to_url != "":
                    self.driver.get(to_url)
                    time.sleep(1)
                rerun(self, to_url, func)
            return wrapper
        return decorator

#   校验“实时计算-作业运维页面校验”
    @get_url()
    def test_01_task_operation_page_verification(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/real_time_computation_yaml/task_operation_yaml/实时计算-作业运维页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskOperationPage(app)
        page.operate()
        page.check_point()

#   校验“作业运维-启动”
    @get_url()
    def test_02_task_operation_page_verification(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/real_time_computation_yaml/task_operation_yaml/实时计算-作业运维页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskOperationPage(app)
        page.operate()
        page.check_point()

# ========================================= 提交 end ========================================================================================


    @classmethod
    def setUpClass(cls):
        super(TaskOperationTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TaskOperationTest, cls).tearDownClass()
