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
    resourceMan_url = ElementParam.RESOURCE_MEN_URL


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

    def test_a399_design_list_login(self):
        self.to_resource_dir()
        print("测试designList的登录")

    # ========================================= dataflow start ========================================================================================
    @get_url(designList_url)
    def test_a400_designList_create_dataflow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-新建-批处理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a401_designList_flow_copy(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a402_designList_flow_export(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-导出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()


    @get_url(designList_url)
    def test_a403_designList_flow_rename(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-重命名.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a404_designList_flow_move(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-移动.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #

    @get_url(designList_url)
    def test_a405_design_list_delete_dataflow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-删除-批处理.yaml"),
           "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()


    @get_url(designList_url)
    def test_a406_design_list_create_workflow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-新建-工作流.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()



    @get_url(designList_url)
    def test_a408_design_list_create_streamflow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-新建-流处理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a409_design_list_delete_streamflow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-删除-流处理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a410_design_list_create_RtcFlow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-新建-RtcFlow.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a411_design_list_delete_RtcFlow(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-删除-RtcFlow.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()



    @get_url(designList_url)
    def test_a413_designList_create_list(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-流程目录-新建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a414_designList_export_list(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-流程目录-导出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a415_designList_move_list(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-流程目录-移动.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a416_designList_rename_list(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-流程目录-重命名.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a417_designList_flow_step_drag(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-step-拖拽.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a418_designList_flow_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-step-保存.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a419_designList_flow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-step-历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a420_designList_flow_step_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-step-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()


    #
    @get_url(designList_url)
    def test_a424_designList_flow_step_clear(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-step-清空.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a423_designList_flow_step_back(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-step-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a421_designList_flow_step_reset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/designList-flow-step-重置.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()



    @get_url(designList_url)
    def test_a424_dataflow_sample_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-sample-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a425_dataflow_sample_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-sample-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a426_dataflow_colsplit_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-colsplit-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()


    @get_url(designList_url)
    def test_a427_dataflow_colsplit_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-colsplit-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a428_dataflow_explode_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-explode-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a429_dataflow_explode_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-explode-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a430_dataflow_filter_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-filter-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a431_dataflow_filter_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-filter-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a432_dataflow_pivot_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-pivot-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a433_dataflow_pivot_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-pivot-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a434_dataflow_sql_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-sql-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a435_dataflow_sql_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-sql-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a436_dataflow_transform_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-transform-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a437_dataflow_transfrom_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-transform-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    # #
    @get_url(designList_url)
    def test_a438_dataflow_unpivot_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-unpivot-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a439_dataflow_unpivot_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-unpivot-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a440_dataflow_aggregate_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-aggregate-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a441_dataflow_aggregate_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-aggregate-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    #
    @get_url(designList_url)
    def test_a442_dataflow_top_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-top-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a443_dataflow_top_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-top-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a444_dataflow_decision_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-decision-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a445_dataflow_decision_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-decision-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #


    @get_url(designList_url)
    def test_a448_dataflow_supplement_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-supplement-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a449_dataflow_supplement_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-supplement-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a450_dataflow_validate_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-validate-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a451_dataflow_validate_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-validate-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a452_dataflow_deduplication_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-deduplication-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a453_dataflow_deduplication_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-deduplication-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a454_dataflow_intersect_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-intersect-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a455_dataflow_intersect_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-intersect-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    # #
    @get_url(designList_url)
    def test_a456_dataflow_minus_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-minus-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a457_dataflow_minus_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-minus-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #

    @get_url(designList_url)
    def test_a458_dataflow_split_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-split-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a459_dataflow_split_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-split-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a460_dataflow_union_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-union-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a461_dataflow_union_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-union-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    # #
    @get_url(designList_url)
    def test_a462_dataflow_join_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-join-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a463_dataflow_join_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-join-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a464_dataflow_outer_join_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-outer_join-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a465_dataflow_outer_join_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-outer_join-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()


    @get_url(designList_url)
    def test_a466_dataflow_left_outer_join_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-left_outer_join-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()


    @get_url(designList_url)
    def test_a467_dataflow_left_outer_join_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-left_outer_join-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a468_dataflow_right_outer_join_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-right_outer_join-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a469_dataflow_right_outer_join_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-right_outer_join-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a470_dataflow_leftsemi_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-leftsemi-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a471_dataflow_leftsemi_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-leftsemi-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a472_dataflow_productjoin_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-productjoin-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a473_dataflow_productjoin_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-productjoin-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a474_dataflow_rangejoin_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-rangejoin-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a475_dataflow_rangejoin_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-rangejoin-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #

    @get_url(designList_url)
    def test_a476_dataflow_starjoin_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-starjoin-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a477_dataflow_starjoin_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-starjoin-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a478_dataflow_sqlsource_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-sqlsource-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a479_dataflow_sqlsource_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-sqlsource-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a482_dataflow_lookup_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-lookup-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a483_dataflow_lookup_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-lookup-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a480_dataflow_lookupTable_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-lookupTable-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a481_dataflow_lookupTable_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-lookupTable-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()
    #
    @get_url(designList_url)
    def test_a484_dataflow_win_aggregate_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-win_aggregate-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a485_dataflow_win_aggregate_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-win_aggregate-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a486_dataflow_win_analyze_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-win_analyze-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a487_dataflow_win_analyze_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-win_analyze-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a488_dataflow_win_rank_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-win_rank-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a489_dataflow_win_rank_step_view_result(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow_yaml/dataflow-win_rank-step-查看运行结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

    @get_url(designList_url)
    def test_a491_dataflow_transfrom_step_batch_upload(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/dataflow-transform-step-批量上传.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DesignListPage(app)
        page.operate()
        page.check_point()

##========================================= dataflow end ========================================================================================

# ##========================================= stream start ========================================================================================
#     @get_url(designList_url)
#     def test_a500_streamflow_aggregate_step_submit(self):
#         app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-aggregate-step-提交.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = DesignListPage(app)
#         page.operate()
#         page.check_point()
#
    # @get_url(designList_url)
    # def test_a501_streamflow_aggregate_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-aggregate-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()


    # @get_url(designList_url)
    # def test_a502_streamflow_deduplication_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-deduplication-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a503_streamflow_deduplication_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-deduplication-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    # #
    # @get_url(designList_url)
    # def test_a504_streamflow_intersect_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-intersect-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a505_streamflow_intersect_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-intersect-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a506_streamflow_minus_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-minus-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a507_streamflow_minus_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-minus-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a508_streamflow_split_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-split-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a509_streamflow_split_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-split-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a509_streamflow_union_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-union-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a510_streamflow_union_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-union-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a511_streamflow_filter_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-filter-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a512_streamflow_filter_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-filter-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    # #
    # @get_url(designList_url)
    # def test_a513_streamflow_sql_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-sql-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a514_streamflow_sql_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-sql-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    # #
    # @get_url(designList_url)
    # def test_a515_streamflow_transform_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-transform-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a516_streamflow_transform_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-transform-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    # #
    # @get_url(designList_url)
    # def test_a517_streamflow_join_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-join-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a518_streamflow_join_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-join-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a519_streamflow_starjoin_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-starjoin-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a520_streamflow_starjoin_step_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/streamflow_yaml/streamflow-starjoin-step-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()





    #========================================= streamflow end ========================================================================================



    #========================================= rtcflow start ========================================================================================

    # @get_url(designList_url)
    # def test_a519_rtcflow_aggregate_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-aggregate-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    # #
    # @get_url(designList_url)
    # def test_a520_rtcflow_filter_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-filter-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a521_rtcflow_interval_filter_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-interval_filter-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    #
    # @get_url(designList_url)
    # def test_a522_rtcflow_join_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-join-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url) #disacrd 默认是开启状态
    # def test_a523_rtcflow_merge_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-merge-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a524_rtcflow_split_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-split-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url) #sql step有点问题
    # def test_a525_rtcflow_sql_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-sql-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    #
    # @get_url(designList_url)
    # def test_a526_rtcflow_watermark_transform_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-watermark-transform-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a527_rtcflow_lookup_mapdb_mapping_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-lookup-step-mapdb-mapping-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # #
    # @get_url(designList_url)
    # def test_a528_rtcflow_lookup_mapdb_chain_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-lookup-step-mapdb-chain-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a529_rtcflow_lookup_redis_mapping_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-lookup-step-redis-mapping-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    #
    # @get_url(designList_url)
    # def test_a530_rtcflow_lookup_redis_chain_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-lookup-step-redis-chain-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(resourceMan_url)
    # def test_a530_rtcflow_create_hbase_single_family(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-HbaseDataset-单列族.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(resourceMan_url)
    # def test_a531_rtcflow_create_hbase_multiple_family(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-HbaseDataset-多列族.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(resourceMan_url)
    # def test_a532_rtcflow_create_redis(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-RedisDataset.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(resourceMan_url)
    # def test_a533_rtcflow_create_kafka_json(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-kafka-json.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(resourceMan_url)
    # def test_a534_rtcflow_create_HDFS_parquet(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-HDFSDataset-parquet.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(resourceMan_url)
    # def test_a535_rtcflow_create_Kafka_csv(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-kafka-csv.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    #
    # @get_url(resourceMan_url)
    # def test_a536_rtcflow_create_mysql(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-mysql.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    #
    # @get_url(resourceMan_url)
    # def test_a537_rtcflow_create_ESDataset(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-ESDataset.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(resourceMan_url)
    # def test_a530_rtcflow_create_hbase_single_family(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-HbaseDataset-非默认表空间.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()











    # @get_url(designList_url)
    # def test_a540_rtcflow_sink_hbase_single_family(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-hbase-单列族.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a541_rtcflow_sink_hbase_single_family_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-hbase-单列族-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a542_rtcflow_sink_hbase_multiple_family(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-hbase-多列族.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a543_rtcflow_sink_hbase_multiple_family_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-hbase-多列族-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a544_rtcflow_sink_redis(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-redis.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    # #
    # @get_url(designList_url)
    # def test_a545_rtcflow_sink_redis_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-redis-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    # #
    # @get_url(designList_url)
    # def test_a546_rtcflow_sink_kafka_json(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-kafka-json.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a547_rtcflow_sink_redis_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-kafka-json-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a548_rtcflow_sink_hdfs_parquet(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-HDFS-parquet.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a549_rtcflow_sink_hdfs_parquet_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-HDFS-parquet-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a550_rtcflow_sink_kafka_csv(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-kafka-csv.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a551_rtcflow_sink_kafka_csv_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-kafka-csv-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()


    # @get_url(designList_url)
    # def test_a552_rtcflow_sink_mysql(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-mysql.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a553_rtcflow_sink_mysql_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-mysql-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()


    # @get_url(designList_url)
    # def test_a554_rtcflow_sink_es(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-es.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a555_rtcflow_sink_es_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-es-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a560_rtcflow_source_Kafaka_json(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-source-kafka-单级json.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    #
    # @get_url(designList_url)
    # def test_a560_rtcflow_source_Kafaka_multiple_json(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-source-kafka-多级json.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a561_rtcflow_sink_hbase_非默认表空间(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-hbase-非默认表空间.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # @get_url(designList_url)
    # def test_a562_rtcflow_sink_hbase_非默认表空间_view_result(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-sink-hbase-非默认表空间-查看运行结果.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a563_rtcflow_source_hdfs_csv(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/source_sink_type_yaml/rtcflow-source-hdfs-csv.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()



    # @get_url(designList_url)
    # def test_a563_rtcflow_transform_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/steps_submit_yaml/rtcflow-transform-step-别名-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()

    # @get_url(designList_url)
    # def test_a563_rtcflow_state_acc_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/state_acc/rtcflow-state_acc-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()


    # @get_url(designList_url)
    # def test_a564_rtcflow_state_acc_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/rtcflow_yaml/rtc_udf/rtcflow-transform-step-udf-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()






    #========================================= rtcflow end ========================================================================================

    #========================================= workflow start ========================================================================================
    # @get_url(designList_url)
    # def test_a600_workflow_exclusion_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/workflow_yaml/workflow-exclusive-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()


    # @get_url(designList_url)
    # def test_a601_workflow_parallel_step_submit(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../../YAML/designList_yaml/workflow_yaml/workflow-parallel-step-提交.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = DesignListPage(app)
    #     page.operate()
    #     page.check_point()




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







