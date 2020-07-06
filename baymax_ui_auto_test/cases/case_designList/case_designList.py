# -*- coding: utf-8 -*-
from PageObject.data_integration_page.resourceMan_page.resourceMan_page import ResourceManPage
from PageObject.designList.designList import DesignListPage
from PageObject.home.home_page import HomePage
from cases.case_login import LoginTest
from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys, time
from PageObject.login.login_page import LoginTestPage
from common.ElementParam import ElementParam
from common.case_false_rerun import rerun
from common.login_who import who_login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class DesignList(ParametrizedTestCase):
    designList_url = ElementParam.DESIGN_LIST_URL


    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path":  PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()
        print("login")

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/home/designList.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        print("to_resource_dir")


    #链接到某url装饰器
    def get_url(to_url=""):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if to_url != "":
                    self.driver.get(to_url)
                    time.sleep(1)
                rerun(self, to_url, func)
            return wrapper
        return decorator

    def test_a0399_design_list_login(self):
        self.to_resource_dir()
        print("测试designList的登录")

    @get_url(designList_url)
    def test_a0400_design_list_create_dataflow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-新建-批处理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a0401_design_list_delete_dataflow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-删除-批处理.yaml"),
           "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    # @get_url(designList_url)
    # def test_a0402_design_list_create_workflow(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-新建-工作流.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a0403_design_list_delete_workflow(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-删除-工作流.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a0404_design_list_create_streamflow(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-新建-流处理.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a0405_design_list_delete_streamflow(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-删除-流处理.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a0406_design_list_create_RtcFlow(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-新建-RtcFlow.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a0407_design_list_delete_RtcFlow(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-删除-RtcFlow.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #




    @classmethod
    def setUpClass(cls):
        super(DesignList, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(DesignList, cls).tearDownClass()
#
# if __name__ == "__main__":
#     unittest.main()
#







