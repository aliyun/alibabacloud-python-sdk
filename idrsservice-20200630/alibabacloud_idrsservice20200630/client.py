# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_idrsservice20200630 import models as idrsservice_20200630_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'idrsservice.aliyuncs.com',
            'ap-northeast-2-pop': 'idrsservice.aliyuncs.com',
            'ap-south-1': 'idrsservice.aliyuncs.com',
            'ap-southeast-1': 'idrsservice.aliyuncs.com',
            'ap-southeast-2': 'idrsservice.aliyuncs.com',
            'ap-southeast-3': 'idrsservice.aliyuncs.com',
            'ap-southeast-5': 'idrsservice.aliyuncs.com',
            'cn-beijing': 'idrsservice.aliyuncs.com',
            'cn-beijing-finance-1': 'idrsservice.aliyuncs.com',
            'cn-beijing-finance-pop': 'idrsservice.aliyuncs.com',
            'cn-beijing-gov-1': 'idrsservice.aliyuncs.com',
            'cn-beijing-nu16-b01': 'idrsservice.aliyuncs.com',
            'cn-chengdu': 'idrsservice.aliyuncs.com',
            'cn-edge-1': 'idrsservice.aliyuncs.com',
            'cn-fujian': 'idrsservice.aliyuncs.com',
            'cn-haidian-cm12-c01': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-finance': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'idrsservice.aliyuncs.com',
            'cn-hangzhou-test-306': 'idrsservice.aliyuncs.com',
            'cn-hongkong': 'idrsservice.aliyuncs.com',
            'cn-hongkong-finance-pop': 'idrsservice.aliyuncs.com',
            'cn-huhehaote': 'idrsservice.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'idrsservice.aliyuncs.com',
            'cn-north-2-gov-1': 'idrsservice.aliyuncs.com',
            'cn-qingdao': 'idrsservice.aliyuncs.com',
            'cn-qingdao-nebula': 'idrsservice.aliyuncs.com',
            'cn-shanghai': 'idrsservice.aliyuncs.com',
            'cn-shanghai-et15-b01': 'idrsservice.aliyuncs.com',
            'cn-shanghai-et2-b01': 'idrsservice.aliyuncs.com',
            'cn-shanghai-inner': 'idrsservice.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'idrsservice.aliyuncs.com',
            'cn-shenzhen': 'idrsservice.aliyuncs.com',
            'cn-shenzhen-finance-1': 'idrsservice.aliyuncs.com',
            'cn-shenzhen-inner': 'idrsservice.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'idrsservice.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'idrsservice.aliyuncs.com',
            'cn-wuhan': 'idrsservice.aliyuncs.com',
            'cn-wulanchabu': 'idrsservice.aliyuncs.com',
            'cn-yushanfang': 'idrsservice.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'idrsservice.aliyuncs.com',
            'cn-zhangjiakou': 'idrsservice.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'idrsservice.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'idrsservice.aliyuncs.com',
            'eu-central-1': 'idrsservice.aliyuncs.com',
            'eu-west-1': 'idrsservice.aliyuncs.com',
            'eu-west-1-oxs': 'idrsservice.aliyuncs.com',
            'me-east-1': 'idrsservice.aliyuncs.com',
            'rus-west-1-pop': 'idrsservice.aliyuncs.com',
            'us-east-1': 'idrsservice.aliyuncs.com',
            'us-west-1': 'idrsservice.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('idrsservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def check_service_linked_role_with_options(
        self,
        request: idrsservice_20200630_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CheckServiceLinkedRoleResponse(),
            self.do_rpcrequest('CheckServiceLinkedRole', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: idrsservice_20200630_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CheckServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CheckServiceLinkedRole', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_linked_role(
        self,
        request: idrsservice_20200630_models.CheckServiceLinkedRoleRequest,
    ) -> idrsservice_20200630_models.CheckServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: idrsservice_20200630_models.CheckServiceLinkedRoleRequest,
    ) -> idrsservice_20200630_models.CheckServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: idrsservice_20200630_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateAppResponse(),
            self.do_rpcrequest('CreateApp', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateAppResponse(),
            await self.do_rpcrequest_async('CreateApp', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app(
        self,
        request: idrsservice_20200630_models.CreateAppRequest,
    ) -> idrsservice_20200630_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: idrsservice_20200630_models.CreateAppRequest,
    ) -> idrsservice_20200630_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_department_with_options(
        self,
        request: idrsservice_20200630_models.CreateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateDepartmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateDepartmentResponse(),
            self.do_rpcrequest('CreateDepartment', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_department_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateDepartmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateDepartmentResponse(),
            await self.do_rpcrequest_async('CreateDepartment', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_department(
        self,
        request: idrsservice_20200630_models.CreateDepartmentRequest,
    ) -> idrsservice_20200630_models.CreateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_department_with_options(request, runtime)

    async def create_department_async(
        self,
        request: idrsservice_20200630_models.CreateDepartmentRequest,
    ) -> idrsservice_20200630_models.CreateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_department_with_options_async(request, runtime)

    def create_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.CreateDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateDetectProcessResponse(),
            self.do_rpcrequest('CreateDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateDetectProcessResponse(),
            await self.do_rpcrequest_async('CreateDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_detect_process(
        self,
        request: idrsservice_20200630_models.CreateDetectProcessRequest,
    ) -> idrsservice_20200630_models.CreateDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_detect_process_with_options(request, runtime)

    async def create_detect_process_async(
        self,
        request: idrsservice_20200630_models.CreateDetectProcessRequest,
    ) -> idrsservice_20200630_models.CreateDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_detect_process_with_options_async(request, runtime)

    def create_live_with_options(
        self,
        request: idrsservice_20200630_models.CreateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateLiveResponse(),
            self.do_rpcrequest('CreateLive', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_live_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateLiveResponse(),
            await self.do_rpcrequest_async('CreateLive', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_live(
        self,
        request: idrsservice_20200630_models.CreateLiveRequest,
    ) -> idrsservice_20200630_models.CreateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_with_options(request, runtime)

    async def create_live_async(
        self,
        request: idrsservice_20200630_models.CreateLiveRequest,
    ) -> idrsservice_20200630_models.CreateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_with_options_async(request, runtime)

    def create_live_detection_with_options(
        self,
        request: idrsservice_20200630_models.CreateLiveDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateLiveDetectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateLiveDetectionResponse(),
            self.do_rpcrequest('CreateLiveDetection', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_live_detection_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateLiveDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateLiveDetectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateLiveDetectionResponse(),
            await self.do_rpcrequest_async('CreateLiveDetection', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_live_detection(
        self,
        request: idrsservice_20200630_models.CreateLiveDetectionRequest,
    ) -> idrsservice_20200630_models.CreateLiveDetectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_detection_with_options(request, runtime)

    async def create_live_detection_async(
        self,
        request: idrsservice_20200630_models.CreateLiveDetectionRequest,
    ) -> idrsservice_20200630_models.CreateLiveDetectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_detection_with_options_async(request, runtime)

    def create_live_record_template_with_options(
        self,
        tmp_req: idrsservice_20200630_models.CreateLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateLiveRecordTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.CreateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backgrounds):
            request.backgrounds_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backgrounds, 'Backgrounds', 'json')
        if not UtilClient.is_unset(tmp_req.watermarks):
            request.watermarks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermarks, 'Watermarks', 'json')
        if not UtilClient.is_unset(tmp_req.clock_widgets):
            request.clock_widgets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clock_widgets, 'ClockWidgets', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateLiveRecordTemplateResponse(),
            self.do_rpcrequest('CreateLiveRecordTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_live_record_template_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.CreateLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateLiveRecordTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.CreateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backgrounds):
            request.backgrounds_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backgrounds, 'Backgrounds', 'json')
        if not UtilClient.is_unset(tmp_req.watermarks):
            request.watermarks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermarks, 'Watermarks', 'json')
        if not UtilClient.is_unset(tmp_req.clock_widgets):
            request.clock_widgets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clock_widgets, 'ClockWidgets', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateLiveRecordTemplateResponse(),
            await self.do_rpcrequest_async('CreateLiveRecordTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_live_record_template(
        self,
        request: idrsservice_20200630_models.CreateLiveRecordTemplateRequest,
    ) -> idrsservice_20200630_models.CreateLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_record_template_with_options(request, runtime)

    async def create_live_record_template_async(
        self,
        request: idrsservice_20200630_models.CreateLiveRecordTemplateRequest,
    ) -> idrsservice_20200630_models.CreateLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_record_template_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: idrsservice_20200630_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateRuleResponse(),
            self.do_rpcrequest('CreateRule', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateRuleResponse(),
            await self.do_rpcrequest_async('CreateRule', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule(
        self,
        request: idrsservice_20200630_models.CreateRuleRequest,
    ) -> idrsservice_20200630_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: idrsservice_20200630_models.CreateRuleRequest,
    ) -> idrsservice_20200630_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_statistics_record_with_options(
        self,
        request: idrsservice_20200630_models.CreateStatisticsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateStatisticsRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateStatisticsRecordResponse(),
            self.do_rpcrequest('CreateStatisticsRecord', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_statistics_record_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateStatisticsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateStatisticsRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateStatisticsRecordResponse(),
            await self.do_rpcrequest_async('CreateStatisticsRecord', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_statistics_record(
        self,
        request: idrsservice_20200630_models.CreateStatisticsRecordRequest,
    ) -> idrsservice_20200630_models.CreateStatisticsRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_statistics_record_with_options(request, runtime)

    async def create_statistics_record_async(
        self,
        request: idrsservice_20200630_models.CreateStatisticsRecordRequest,
    ) -> idrsservice_20200630_models.CreateStatisticsRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_statistics_record_with_options_async(request, runtime)

    def create_statistics_task_with_options(
        self,
        request: idrsservice_20200630_models.CreateStatisticsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateStatisticsTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateStatisticsTaskResponse(),
            self.do_rpcrequest('CreateStatisticsTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_statistics_task_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateStatisticsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateStatisticsTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateStatisticsTaskResponse(),
            await self.do_rpcrequest_async('CreateStatisticsTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_statistics_task(
        self,
        request: idrsservice_20200630_models.CreateStatisticsTaskRequest,
    ) -> idrsservice_20200630_models.CreateStatisticsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_statistics_task_with_options(request, runtime)

    async def create_statistics_task_async(
        self,
        request: idrsservice_20200630_models.CreateStatisticsTaskRequest,
    ) -> idrsservice_20200630_models.CreateStatisticsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_statistics_task_with_options_async(request, runtime)

    def create_task_group_with_options(
        self,
        request: idrsservice_20200630_models.CreateTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateTaskGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateTaskGroupResponse(),
            self.do_rpcrequest('CreateTaskGroup', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_task_group_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateTaskGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateTaskGroupResponse(),
            await self.do_rpcrequest_async('CreateTaskGroup', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_task_group(
        self,
        request: idrsservice_20200630_models.CreateTaskGroupRequest,
    ) -> idrsservice_20200630_models.CreateTaskGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_task_group_with_options(request, runtime)

    async def create_task_group_async(
        self,
        request: idrsservice_20200630_models.CreateTaskGroupRequest,
    ) -> idrsservice_20200630_models.CreateTaskGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_task_group_with_options_async(request, runtime)

    def create_user_departments_with_options(
        self,
        request: idrsservice_20200630_models.CreateUserDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateUserDepartmentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateUserDepartmentsResponse(),
            self.do_rpcrequest('CreateUserDepartments', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_departments_with_options_async(
        self,
        request: idrsservice_20200630_models.CreateUserDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.CreateUserDepartmentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.CreateUserDepartmentsResponse(),
            await self.do_rpcrequest_async('CreateUserDepartments', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user_departments(
        self,
        request: idrsservice_20200630_models.CreateUserDepartmentsRequest,
    ) -> idrsservice_20200630_models.CreateUserDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_departments_with_options(request, runtime)

    async def create_user_departments_async(
        self,
        request: idrsservice_20200630_models.CreateUserDepartmentsRequest,
    ) -> idrsservice_20200630_models.CreateUserDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_departments_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: idrsservice_20200630_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteAppResponse(),
            self.do_rpcrequest('DeleteApp', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteAppResponse(),
            await self.do_rpcrequest_async('DeleteApp', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app(
        self,
        request: idrsservice_20200630_models.DeleteAppRequest,
    ) -> idrsservice_20200630_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: idrsservice_20200630_models.DeleteAppRequest,
    ) -> idrsservice_20200630_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_department_with_options(
        self,
        request: idrsservice_20200630_models.DeleteDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteDepartmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteDepartmentResponse(),
            self.do_rpcrequest('DeleteDepartment', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_department_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteDepartmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteDepartmentResponse(),
            await self.do_rpcrequest_async('DeleteDepartment', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_department(
        self,
        request: idrsservice_20200630_models.DeleteDepartmentRequest,
    ) -> idrsservice_20200630_models.DeleteDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_department_with_options(request, runtime)

    async def delete_department_async(
        self,
        request: idrsservice_20200630_models.DeleteDepartmentRequest,
    ) -> idrsservice_20200630_models.DeleteDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_department_with_options_async(request, runtime)

    def delete_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.DeleteDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteDetectProcessResponse(),
            self.do_rpcrequest('DeleteDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteDetectProcessResponse(),
            await self.do_rpcrequest_async('DeleteDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_detect_process(
        self,
        request: idrsservice_20200630_models.DeleteDetectProcessRequest,
    ) -> idrsservice_20200630_models.DeleteDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_detect_process_with_options(request, runtime)

    async def delete_detect_process_async(
        self,
        request: idrsservice_20200630_models.DeleteDetectProcessRequest,
    ) -> idrsservice_20200630_models.DeleteDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_detect_process_with_options_async(request, runtime)

    def delete_live_record_template_with_options(
        self,
        request: idrsservice_20200630_models.DeleteLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteLiveRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteLiveRecordTemplateResponse(),
            self.do_rpcrequest('DeleteLiveRecordTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_record_template_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteLiveRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteLiveRecordTemplateResponse(),
            await self.do_rpcrequest_async('DeleteLiveRecordTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_live_record_template(
        self,
        request: idrsservice_20200630_models.DeleteLiveRecordTemplateRequest,
    ) -> idrsservice_20200630_models.DeleteLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_template_with_options(request, runtime)

    async def delete_live_record_template_async(
        self,
        request: idrsservice_20200630_models.DeleteLiveRecordTemplateRequest,
    ) -> idrsservice_20200630_models.DeleteLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_record_template_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: idrsservice_20200630_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteRuleResponse(),
            self.do_rpcrequest('DeleteRule', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteRuleResponse(),
            await self.do_rpcrequest_async('DeleteRule', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rule(
        self,
        request: idrsservice_20200630_models.DeleteRuleRequest,
    ) -> idrsservice_20200630_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: idrsservice_20200630_models.DeleteRuleRequest,
    ) -> idrsservice_20200630_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: idrsservice_20200630_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteUserResponse(),
            self.do_rpcrequest('DeleteUser', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteUserResponse(),
            await self.do_rpcrequest_async('DeleteUser', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(
        self,
        request: idrsservice_20200630_models.DeleteUserRequest,
    ) -> idrsservice_20200630_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: idrsservice_20200630_models.DeleteUserRequest,
    ) -> idrsservice_20200630_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_departments_with_options(
        self,
        request: idrsservice_20200630_models.DeleteUserDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteUserDepartmentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteUserDepartmentsResponse(),
            self.do_rpcrequest('DeleteUserDepartments', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_departments_with_options_async(
        self,
        request: idrsservice_20200630_models.DeleteUserDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.DeleteUserDepartmentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.DeleteUserDepartmentsResponse(),
            await self.do_rpcrequest_async('DeleteUserDepartments', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_departments(
        self,
        request: idrsservice_20200630_models.DeleteUserDepartmentsRequest,
    ) -> idrsservice_20200630_models.DeleteUserDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_departments_with_options(request, runtime)

    async def delete_user_departments_async(
        self,
        request: idrsservice_20200630_models.DeleteUserDepartmentsRequest,
    ) -> idrsservice_20200630_models.DeleteUserDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_departments_with_options_async(request, runtime)

    def exit_live_with_options(
        self,
        request: idrsservice_20200630_models.ExitLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ExitLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ExitLiveResponse(),
            self.do_rpcrequest('ExitLive', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def exit_live_with_options_async(
        self,
        request: idrsservice_20200630_models.ExitLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ExitLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ExitLiveResponse(),
            await self.do_rpcrequest_async('ExitLive', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def exit_live(
        self,
        request: idrsservice_20200630_models.ExitLiveRequest,
    ) -> idrsservice_20200630_models.ExitLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.exit_live_with_options(request, runtime)

    async def exit_live_async(
        self,
        request: idrsservice_20200630_models.ExitLiveRequest,
    ) -> idrsservice_20200630_models.ExitLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.exit_live_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: idrsservice_20200630_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetAppResponse(),
            self.do_rpcrequest('GetApp', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: idrsservice_20200630_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetAppResponse(),
            await self.do_rpcrequest_async('GetApp', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app(
        self,
        request: idrsservice_20200630_models.GetAppRequest,
    ) -> idrsservice_20200630_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: idrsservice_20200630_models.GetAppRequest,
    ) -> idrsservice_20200630_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_batch_signed_url_with_options(
        self,
        request: idrsservice_20200630_models.GetBatchSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetBatchSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetBatchSignedUrlResponse(),
            self.do_rpcrequest('GetBatchSignedUrl', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_batch_signed_url_with_options_async(
        self,
        request: idrsservice_20200630_models.GetBatchSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetBatchSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetBatchSignedUrlResponse(),
            await self.do_rpcrequest_async('GetBatchSignedUrl', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_batch_signed_url(
        self,
        request: idrsservice_20200630_models.GetBatchSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetBatchSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_batch_signed_url_with_options(request, runtime)

    async def get_batch_signed_url_async(
        self,
        request: idrsservice_20200630_models.GetBatchSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetBatchSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_signed_url_with_options_async(request, runtime)

    def get_department_with_options(
        self,
        request: idrsservice_20200630_models.GetDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDepartmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDepartmentResponse(),
            self.do_rpcrequest('GetDepartment', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_department_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDepartmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDepartmentResponse(),
            await self.do_rpcrequest_async('GetDepartment', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_department(
        self,
        request: idrsservice_20200630_models.GetDepartmentRequest,
    ) -> idrsservice_20200630_models.GetDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_department_with_options(request, runtime)

    async def get_department_async(
        self,
        request: idrsservice_20200630_models.GetDepartmentRequest,
    ) -> idrsservice_20200630_models.GetDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_department_with_options_async(request, runtime)

    def get_detect_evaluation_with_options(
        self,
        request: idrsservice_20200630_models.GetDetectEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectEvaluationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectEvaluationResponse(),
            self.do_rpcrequest('GetDetectEvaluation', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_detect_evaluation_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDetectEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectEvaluationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectEvaluationResponse(),
            await self.do_rpcrequest_async('GetDetectEvaluation', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_detect_evaluation(
        self,
        request: idrsservice_20200630_models.GetDetectEvaluationRequest,
    ) -> idrsservice_20200630_models.GetDetectEvaluationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detect_evaluation_with_options(request, runtime)

    async def get_detect_evaluation_async(
        self,
        request: idrsservice_20200630_models.GetDetectEvaluationRequest,
    ) -> idrsservice_20200630_models.GetDetectEvaluationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_evaluation_with_options_async(request, runtime)

    def get_detection_with_options(
        self,
        request: idrsservice_20200630_models.GetDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectionResponse(),
            self.do_rpcrequest('GetDetection', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_detection_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectionResponse(),
            await self.do_rpcrequest_async('GetDetection', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_detection(
        self,
        request: idrsservice_20200630_models.GetDetectionRequest,
    ) -> idrsservice_20200630_models.GetDetectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detection_with_options(request, runtime)

    async def get_detection_async(
        self,
        request: idrsservice_20200630_models.GetDetectionRequest,
    ) -> idrsservice_20200630_models.GetDetectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detection_with_options_async(request, runtime)

    def get_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.GetDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessResponse(),
            self.do_rpcrequest('GetDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessResponse(),
            await self.do_rpcrequest_async('GetDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_detect_process(
        self,
        request: idrsservice_20200630_models.GetDetectProcessRequest,
    ) -> idrsservice_20200630_models.GetDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detect_process_with_options(request, runtime)

    async def get_detect_process_async(
        self,
        request: idrsservice_20200630_models.GetDetectProcessRequest,
    ) -> idrsservice_20200630_models.GetDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_process_with_options_async(request, runtime)

    def get_detect_process_json_file_with_options(
        self,
        request: idrsservice_20200630_models.GetDetectProcessJsonFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessJsonFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessJsonFileResponse(),
            self.do_rpcrequest('GetDetectProcessJsonFile', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_detect_process_json_file_with_options_async(
        self,
        request: idrsservice_20200630_models.GetDetectProcessJsonFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessJsonFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessJsonFileResponse(),
            await self.do_rpcrequest_async('GetDetectProcessJsonFile', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_detect_process_json_file(
        self,
        request: idrsservice_20200630_models.GetDetectProcessJsonFileRequest,
    ) -> idrsservice_20200630_models.GetDetectProcessJsonFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detect_process_json_file_with_options(request, runtime)

    async def get_detect_process_json_file_async(
        self,
        request: idrsservice_20200630_models.GetDetectProcessJsonFileRequest,
    ) -> idrsservice_20200630_models.GetDetectProcessJsonFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_process_json_file_with_options_async(request, runtime)

    def get_detect_process_template_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessTemplateResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessTemplateResponse(),
            self.do_rpcrequest('GetDetectProcessTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_detect_process_template_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetDetectProcessTemplateResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            idrsservice_20200630_models.GetDetectProcessTemplateResponse(),
            await self.do_rpcrequest_async('GetDetectProcessTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_detect_process_template(self) -> idrsservice_20200630_models.GetDetectProcessTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detect_process_template_with_options(runtime)

    async def get_detect_process_template_async(self) -> idrsservice_20200630_models.GetDetectProcessTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_process_template_with_options_async(runtime)

    def get_global_config_with_options(
        self,
        request: idrsservice_20200630_models.GetGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetGlobalConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetGlobalConfigResponse(),
            self.do_rpcrequest('GetGlobalConfig', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_global_config_with_options_async(
        self,
        request: idrsservice_20200630_models.GetGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetGlobalConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetGlobalConfigResponse(),
            await self.do_rpcrequest_async('GetGlobalConfig', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_global_config(
        self,
        request: idrsservice_20200630_models.GetGlobalConfigRequest,
    ) -> idrsservice_20200630_models.GetGlobalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_global_config_with_options(request, runtime)

    async def get_global_config_async(
        self,
        request: idrsservice_20200630_models.GetGlobalConfigRequest,
    ) -> idrsservice_20200630_models.GetGlobalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_global_config_with_options_async(request, runtime)

    def get_live_record_template_with_options(
        self,
        request: idrsservice_20200630_models.GetLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetLiveRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetLiveRecordTemplateResponse(),
            self.do_rpcrequest('GetLiveRecordTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_live_record_template_with_options_async(
        self,
        request: idrsservice_20200630_models.GetLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetLiveRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetLiveRecordTemplateResponse(),
            await self.do_rpcrequest_async('GetLiveRecordTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_live_record_template(
        self,
        request: idrsservice_20200630_models.GetLiveRecordTemplateRequest,
    ) -> idrsservice_20200630_models.GetLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_record_template_with_options(request, runtime)

    async def get_live_record_template_async(
        self,
        request: idrsservice_20200630_models.GetLiveRecordTemplateRequest,
    ) -> idrsservice_20200630_models.GetLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_record_template_with_options_async(request, runtime)

    def get_model_signed_url_with_options(
        self,
        request: idrsservice_20200630_models.GetModelSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetModelSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetModelSignedUrlResponse(),
            self.do_rpcrequest('GetModelSignedUrl', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_model_signed_url_with_options_async(
        self,
        request: idrsservice_20200630_models.GetModelSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetModelSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetModelSignedUrlResponse(),
            await self.do_rpcrequest_async('GetModelSignedUrl', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_model_signed_url(
        self,
        request: idrsservice_20200630_models.GetModelSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetModelSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_model_signed_url_with_options(request, runtime)

    async def get_model_signed_url_async(
        self,
        request: idrsservice_20200630_models.GetModelSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetModelSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_model_signed_url_with_options_async(request, runtime)

    def get_pre_signed_url_with_options(
        self,
        request: idrsservice_20200630_models.GetPreSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetPreSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetPreSignedUrlResponse(),
            self.do_rpcrequest('GetPreSignedUrl', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pre_signed_url_with_options_async(
        self,
        request: idrsservice_20200630_models.GetPreSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetPreSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetPreSignedUrlResponse(),
            await self.do_rpcrequest_async('GetPreSignedUrl', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pre_signed_url(
        self,
        request: idrsservice_20200630_models.GetPreSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetPreSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pre_signed_url_with_options(request, runtime)

    async def get_pre_signed_url_async(
        self,
        request: idrsservice_20200630_models.GetPreSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetPreSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pre_signed_url_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: idrsservice_20200630_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRuleResponse(),
            self.do_rpcrequest('GetRule', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: idrsservice_20200630_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetRuleResponse(),
            await self.do_rpcrequest_async('GetRule', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule(
        self,
        request: idrsservice_20200630_models.GetRuleRequest,
    ) -> idrsservice_20200630_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: idrsservice_20200630_models.GetRuleRequest,
    ) -> idrsservice_20200630_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_service_configuration_with_options(
        self,
        request: idrsservice_20200630_models.GetServiceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetServiceConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetServiceConfigurationResponse(),
            self.do_rpcrequest('GetServiceConfiguration', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_configuration_with_options_async(
        self,
        request: idrsservice_20200630_models.GetServiceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetServiceConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetServiceConfigurationResponse(),
            await self.do_rpcrequest_async('GetServiceConfiguration', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_configuration(
        self,
        request: idrsservice_20200630_models.GetServiceConfigurationRequest,
    ) -> idrsservice_20200630_models.GetServiceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_configuration_with_options(request, runtime)

    async def get_service_configuration_async(
        self,
        request: idrsservice_20200630_models.GetServiceConfigurationRequest,
    ) -> idrsservice_20200630_models.GetServiceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_configuration_with_options_async(request, runtime)

    def get_signed_url_with_options(
        self,
        request: idrsservice_20200630_models.GetSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetSignedUrlResponse(),
            self.do_rpcrequest('GetSignedUrl', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_signed_url_with_options_async(
        self,
        request: idrsservice_20200630_models.GetSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetSignedUrlResponse(),
            await self.do_rpcrequest_async('GetSignedUrl', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_signed_url(
        self,
        request: idrsservice_20200630_models.GetSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_signed_url_with_options(request, runtime)

    async def get_signed_url_async(
        self,
        request: idrsservice_20200630_models.GetSignedUrlRequest,
    ) -> idrsservice_20200630_models.GetSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_signed_url_with_options_async(request, runtime)

    def get_slr_configuration_with_options(
        self,
        request: idrsservice_20200630_models.GetSlrConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetSlrConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetSlrConfigurationResponse(),
            self.do_rpcrequest('GetSlrConfiguration', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_slr_configuration_with_options_async(
        self,
        request: idrsservice_20200630_models.GetSlrConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetSlrConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetSlrConfigurationResponse(),
            await self.do_rpcrequest_async('GetSlrConfiguration', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_slr_configuration(
        self,
        request: idrsservice_20200630_models.GetSlrConfigurationRequest,
    ) -> idrsservice_20200630_models.GetSlrConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_slr_configuration_with_options(request, runtime)

    async def get_slr_configuration_async(
        self,
        request: idrsservice_20200630_models.GetSlrConfigurationRequest,
    ) -> idrsservice_20200630_models.GetSlrConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_slr_configuration_with_options_async(request, runtime)

    def get_statistics_with_options(
        self,
        request: idrsservice_20200630_models.GetStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetStatisticsResponse(),
            self.do_rpcrequest('GetStatistics', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_statistics_with_options_async(
        self,
        request: idrsservice_20200630_models.GetStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetStatisticsResponse(),
            await self.do_rpcrequest_async('GetStatistics', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_statistics(
        self,
        request: idrsservice_20200630_models.GetStatisticsRequest,
    ) -> idrsservice_20200630_models.GetStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_statistics_with_options(request, runtime)

    async def get_statistics_async(
        self,
        request: idrsservice_20200630_models.GetStatisticsRequest,
    ) -> idrsservice_20200630_models.GetStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_statistics_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: idrsservice_20200630_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTaskResponse(),
            self.do_rpcrequest('GetTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: idrsservice_20200630_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTaskResponse(),
            await self.do_rpcrequest_async('GetTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task(
        self,
        request: idrsservice_20200630_models.GetTaskRequest,
    ) -> idrsservice_20200630_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: idrsservice_20200630_models.GetTaskRequest,
    ) -> idrsservice_20200630_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_task_group_with_options(
        self,
        request: idrsservice_20200630_models.GetTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTaskGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTaskGroupResponse(),
            self.do_rpcrequest('GetTaskGroup', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_group_with_options_async(
        self,
        request: idrsservice_20200630_models.GetTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetTaskGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetTaskGroupResponse(),
            await self.do_rpcrequest_async('GetTaskGroup', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_group(
        self,
        request: idrsservice_20200630_models.GetTaskGroupRequest,
    ) -> idrsservice_20200630_models.GetTaskGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_group_with_options(request, runtime)

    async def get_task_group_async(
        self,
        request: idrsservice_20200630_models.GetTaskGroupRequest,
    ) -> idrsservice_20200630_models.GetTaskGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_group_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: idrsservice_20200630_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetUserResponse(),
            self.do_rpcrequest('GetUser', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: idrsservice_20200630_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.GetUserResponse(),
            await self.do_rpcrequest_async('GetUser', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(
        self,
        request: idrsservice_20200630_models.GetUserRequest,
    ) -> idrsservice_20200630_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: idrsservice_20200630_models.GetUserRequest,
    ) -> idrsservice_20200630_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def initialize_service_linked_role_with_options(
        self,
        request: idrsservice_20200630_models.InitializeServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.InitializeServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.InitializeServiceLinkedRoleResponse(),
            self.do_rpcrequest('InitializeServiceLinkedRole', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def initialize_service_linked_role_with_options_async(
        self,
        request: idrsservice_20200630_models.InitializeServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.InitializeServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.InitializeServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('InitializeServiceLinkedRole', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def initialize_service_linked_role(
        self,
        request: idrsservice_20200630_models.InitializeServiceLinkedRoleRequest,
    ) -> idrsservice_20200630_models.InitializeServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_service_linked_role_with_options(request, runtime)

    async def initialize_service_linked_role_async(
        self,
        request: idrsservice_20200630_models.InitializeServiceLinkedRoleRequest,
    ) -> idrsservice_20200630_models.InitializeServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_service_linked_role_with_options_async(request, runtime)

    def join_live_with_options(
        self,
        request: idrsservice_20200630_models.JoinLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.JoinLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.JoinLiveResponse(),
            self.do_rpcrequest('JoinLive', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_live_with_options_async(
        self,
        request: idrsservice_20200630_models.JoinLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.JoinLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.JoinLiveResponse(),
            await self.do_rpcrequest_async('JoinLive', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_live(
        self,
        request: idrsservice_20200630_models.JoinLiveRequest,
    ) -> idrsservice_20200630_models.JoinLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_live_with_options(request, runtime)

    async def join_live_async(
        self,
        request: idrsservice_20200630_models.JoinLiveRequest,
    ) -> idrsservice_20200630_models.JoinLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_live_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: idrsservice_20200630_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListAppsResponse(),
            self.do_rpcrequest('ListApps', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: idrsservice_20200630_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListAppsResponse(),
            await self.do_rpcrequest_async('ListApps', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_apps(
        self,
        request: idrsservice_20200630_models.ListAppsRequest,
    ) -> idrsservice_20200630_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: idrsservice_20200630_models.ListAppsRequest,
    ) -> idrsservice_20200630_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_departments_with_options(
        self,
        request: idrsservice_20200630_models.ListDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDepartmentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDepartmentsResponse(),
            self.do_rpcrequest('ListDepartments', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_departments_with_options_async(
        self,
        request: idrsservice_20200630_models.ListDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDepartmentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDepartmentsResponse(),
            await self.do_rpcrequest_async('ListDepartments', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_departments(
        self,
        request: idrsservice_20200630_models.ListDepartmentsRequest,
    ) -> idrsservice_20200630_models.ListDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_departments_with_options(request, runtime)

    async def list_departments_async(
        self,
        request: idrsservice_20200630_models.ListDepartmentsRequest,
    ) -> idrsservice_20200630_models.ListDepartmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_departments_with_options_async(request, runtime)

    def list_detections_with_options(
        self,
        request: idrsservice_20200630_models.ListDetectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDetectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDetectionsResponse(),
            self.do_rpcrequest('ListDetections', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_detections_with_options_async(
        self,
        request: idrsservice_20200630_models.ListDetectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDetectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDetectionsResponse(),
            await self.do_rpcrequest_async('ListDetections', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_detections(
        self,
        request: idrsservice_20200630_models.ListDetectionsRequest,
    ) -> idrsservice_20200630_models.ListDetectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_detections_with_options(request, runtime)

    async def list_detections_async(
        self,
        request: idrsservice_20200630_models.ListDetectionsRequest,
    ) -> idrsservice_20200630_models.ListDetectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_detections_with_options_async(request, runtime)

    def list_detect_processes_with_options(
        self,
        request: idrsservice_20200630_models.ListDetectProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDetectProcessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDetectProcessesResponse(),
            self.do_rpcrequest('ListDetectProcesses', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_detect_processes_with_options_async(
        self,
        request: idrsservice_20200630_models.ListDetectProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListDetectProcessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListDetectProcessesResponse(),
            await self.do_rpcrequest_async('ListDetectProcesses', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_detect_processes(
        self,
        request: idrsservice_20200630_models.ListDetectProcessesRequest,
    ) -> idrsservice_20200630_models.ListDetectProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_detect_processes_with_options(request, runtime)

    async def list_detect_processes_async(
        self,
        request: idrsservice_20200630_models.ListDetectProcessesRequest,
    ) -> idrsservice_20200630_models.ListDetectProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_detect_processes_with_options_async(request, runtime)

    def list_files_with_options(
        self,
        request: idrsservice_20200630_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListFilesResponse(),
            self.do_rpcrequest('ListFiles', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_files_with_options_async(
        self,
        request: idrsservice_20200630_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListFilesResponse(),
            await self.do_rpcrequest_async('ListFiles', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_files(
        self,
        request: idrsservice_20200630_models.ListFilesRequest,
    ) -> idrsservice_20200630_models.ListFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    async def list_files_async(
        self,
        request: idrsservice_20200630_models.ListFilesRequest,
    ) -> idrsservice_20200630_models.ListFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_files_with_options_async(request, runtime)

    def list_live_apps_with_options(
        self,
        request: idrsservice_20200630_models.ListLiveAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListLiveAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListLiveAppsResponse(),
            self.do_rpcrequest('ListLiveApps', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_live_apps_with_options_async(
        self,
        request: idrsservice_20200630_models.ListLiveAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListLiveAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListLiveAppsResponse(),
            await self.do_rpcrequest_async('ListLiveApps', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_live_apps(
        self,
        request: idrsservice_20200630_models.ListLiveAppsRequest,
    ) -> idrsservice_20200630_models.ListLiveAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_apps_with_options(request, runtime)

    async def list_live_apps_async(
        self,
        request: idrsservice_20200630_models.ListLiveAppsRequest,
    ) -> idrsservice_20200630_models.ListLiveAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_apps_with_options_async(request, runtime)

    def list_live_record_templates_with_options(
        self,
        request: idrsservice_20200630_models.ListLiveRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListLiveRecordTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListLiveRecordTemplatesResponse(),
            self.do_rpcrequest('ListLiveRecordTemplates', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_live_record_templates_with_options_async(
        self,
        request: idrsservice_20200630_models.ListLiveRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListLiveRecordTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListLiveRecordTemplatesResponse(),
            await self.do_rpcrequest_async('ListLiveRecordTemplates', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_live_record_templates(
        self,
        request: idrsservice_20200630_models.ListLiveRecordTemplatesRequest,
    ) -> idrsservice_20200630_models.ListLiveRecordTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_templates_with_options(request, runtime)

    async def list_live_record_templates_async(
        self,
        request: idrsservice_20200630_models.ListLiveRecordTemplatesRequest,
    ) -> idrsservice_20200630_models.ListLiveRecordTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_record_templates_with_options_async(request, runtime)

    def list_lives_with_options(
        self,
        request: idrsservice_20200630_models.ListLivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListLivesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListLivesResponse(),
            self.do_rpcrequest('ListLives', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_lives_with_options_async(
        self,
        request: idrsservice_20200630_models.ListLivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListLivesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListLivesResponse(),
            await self.do_rpcrequest_async('ListLives', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_lives(
        self,
        request: idrsservice_20200630_models.ListLivesRequest,
    ) -> idrsservice_20200630_models.ListLivesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_lives_with_options(request, runtime)

    async def list_lives_async(
        self,
        request: idrsservice_20200630_models.ListLivesRequest,
    ) -> idrsservice_20200630_models.ListLivesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_lives_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListRolesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            idrsservice_20200630_models.ListRolesResponse(),
            self.do_rpcrequest('ListRoles', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListRolesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            idrsservice_20200630_models.ListRolesResponse(),
            await self.do_rpcrequest_async('ListRoles', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_roles(self) -> idrsservice_20200630_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(runtime)

    async def list_roles_async(self) -> idrsservice_20200630_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(runtime)

    def list_rules_with_options(
        self,
        request: idrsservice_20200630_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListRulesResponse(),
            self.do_rpcrequest('ListRules', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: idrsservice_20200630_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListRulesResponse(),
            await self.do_rpcrequest_async('ListRules', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rules(
        self,
        request: idrsservice_20200630_models.ListRulesRequest,
    ) -> idrsservice_20200630_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: idrsservice_20200630_models.ListRulesRequest,
    ) -> idrsservice_20200630_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_statistics_task_with_options(
        self,
        request: idrsservice_20200630_models.ListStatisticsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListStatisticsTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListStatisticsTaskResponse(),
            self.do_rpcrequest('ListStatisticsTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_statistics_task_with_options_async(
        self,
        request: idrsservice_20200630_models.ListStatisticsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListStatisticsTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListStatisticsTaskResponse(),
            await self.do_rpcrequest_async('ListStatisticsTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_statistics_task(
        self,
        request: idrsservice_20200630_models.ListStatisticsTaskRequest,
    ) -> idrsservice_20200630_models.ListStatisticsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_statistics_task_with_options(request, runtime)

    async def list_statistics_task_async(
        self,
        request: idrsservice_20200630_models.ListStatisticsTaskRequest,
    ) -> idrsservice_20200630_models.ListStatisticsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_statistics_task_with_options_async(request, runtime)

    def list_task_groups_with_options(
        self,
        request: idrsservice_20200630_models.ListTaskGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTaskGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTaskGroupsResponse(),
            self.do_rpcrequest('ListTaskGroups', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_task_groups_with_options_async(
        self,
        request: idrsservice_20200630_models.ListTaskGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTaskGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTaskGroupsResponse(),
            await self.do_rpcrequest_async('ListTaskGroups', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_task_groups(
        self,
        request: idrsservice_20200630_models.ListTaskGroupsRequest,
    ) -> idrsservice_20200630_models.ListTaskGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_groups_with_options(request, runtime)

    async def list_task_groups_async(
        self,
        request: idrsservice_20200630_models.ListTaskGroupsRequest,
    ) -> idrsservice_20200630_models.ListTaskGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_groups_with_options_async(request, runtime)

    def list_task_items_with_options(
        self,
        request: idrsservice_20200630_models.ListTaskItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTaskItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTaskItemsResponse(),
            self.do_rpcrequest('ListTaskItems', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_task_items_with_options_async(
        self,
        request: idrsservice_20200630_models.ListTaskItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTaskItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTaskItemsResponse(),
            await self.do_rpcrequest_async('ListTaskItems', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_task_items(
        self,
        request: idrsservice_20200630_models.ListTaskItemsRequest,
    ) -> idrsservice_20200630_models.ListTaskItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_items_with_options(request, runtime)

    async def list_task_items_async(
        self,
        request: idrsservice_20200630_models.ListTaskItemsRequest,
    ) -> idrsservice_20200630_models.ListTaskItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_items_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: idrsservice_20200630_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTasksResponse(),
            self.do_rpcrequest('ListTasks', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: idrsservice_20200630_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListTasksResponse(),
            await self.do_rpcrequest_async('ListTasks', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tasks(
        self,
        request: idrsservice_20200630_models.ListTasksRequest,
    ) -> idrsservice_20200630_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: idrsservice_20200630_models.ListTasksRequest,
    ) -> idrsservice_20200630_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: idrsservice_20200630_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: idrsservice_20200630_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.ListUsersResponse(),
            await self.do_rpcrequest_async('ListUsers', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: idrsservice_20200630_models.ListUsersRequest,
    ) -> idrsservice_20200630_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: idrsservice_20200630_models.ListUsersRequest,
    ) -> idrsservice_20200630_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def rename_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.RenameDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.RenameDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.RenameDetectProcessResponse(),
            self.do_rpcrequest('RenameDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rename_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.RenameDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.RenameDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.RenameDetectProcessResponse(),
            await self.do_rpcrequest_async('RenameDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rename_detect_process(
        self,
        request: idrsservice_20200630_models.RenameDetectProcessRequest,
    ) -> idrsservice_20200630_models.RenameDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_detect_process_with_options(request, runtime)

    async def rename_detect_process_async(
        self,
        request: idrsservice_20200630_models.RenameDetectProcessRequest,
    ) -> idrsservice_20200630_models.RenameDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_detect_process_with_options_async(request, runtime)

    def start_live_record_task_with_options(
        self,
        tmp_req: idrsservice_20200630_models.StartLiveRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.StartLiveRecordTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.StartLiveRecordTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.clock_widgets):
            request.clock_widgets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clock_widgets, 'ClockWidgets', 'json')
        if not UtilClient.is_unset(tmp_req.user_panes):
            request.user_panes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_panes, 'UserPanes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.StartLiveRecordTaskResponse(),
            self.do_rpcrequest('StartLiveRecordTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_live_record_task_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.StartLiveRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.StartLiveRecordTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.StartLiveRecordTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.clock_widgets):
            request.clock_widgets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clock_widgets, 'ClockWidgets', 'json')
        if not UtilClient.is_unset(tmp_req.user_panes):
            request.user_panes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_panes, 'UserPanes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.StartLiveRecordTaskResponse(),
            await self.do_rpcrequest_async('StartLiveRecordTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_live_record_task(
        self,
        request: idrsservice_20200630_models.StartLiveRecordTaskRequest,
    ) -> idrsservice_20200630_models.StartLiveRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_live_record_task_with_options(request, runtime)

    async def start_live_record_task_async(
        self,
        request: idrsservice_20200630_models.StartLiveRecordTaskRequest,
    ) -> idrsservice_20200630_models.StartLiveRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_live_record_task_with_options_async(request, runtime)

    def stop_live_record_task_with_options(
        self,
        request: idrsservice_20200630_models.StopLiveRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.StopLiveRecordTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.StopLiveRecordTaskResponse(),
            self.do_rpcrequest('StopLiveRecordTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_live_record_task_with_options_async(
        self,
        request: idrsservice_20200630_models.StopLiveRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.StopLiveRecordTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.StopLiveRecordTaskResponse(),
            await self.do_rpcrequest_async('StopLiveRecordTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_live_record_task(
        self,
        request: idrsservice_20200630_models.StopLiveRecordTaskRequest,
    ) -> idrsservice_20200630_models.StopLiveRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_live_record_task_with_options(request, runtime)

    async def stop_live_record_task_async(
        self,
        request: idrsservice_20200630_models.StopLiveRecordTaskRequest,
    ) -> idrsservice_20200630_models.StopLiveRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_live_record_task_with_options_async(request, runtime)

    def update_app_with_options(
        self,
        request: idrsservice_20200630_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateAppResponse(),
            self.do_rpcrequest('UpdateApp', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateAppResponse(),
            await self.do_rpcrequest_async('UpdateApp', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app(
        self,
        request: idrsservice_20200630_models.UpdateAppRequest,
    ) -> idrsservice_20200630_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: idrsservice_20200630_models.UpdateAppRequest,
    ) -> idrsservice_20200630_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)

    def update_department_with_options(
        self,
        request: idrsservice_20200630_models.UpdateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateDepartmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateDepartmentResponse(),
            self.do_rpcrequest('UpdateDepartment', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_department_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateDepartmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateDepartmentResponse(),
            await self.do_rpcrequest_async('UpdateDepartment', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_department(
        self,
        request: idrsservice_20200630_models.UpdateDepartmentRequest,
    ) -> idrsservice_20200630_models.UpdateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_department_with_options(request, runtime)

    async def update_department_async(
        self,
        request: idrsservice_20200630_models.UpdateDepartmentRequest,
    ) -> idrsservice_20200630_models.UpdateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_department_with_options_async(request, runtime)

    def update_detect_process_with_options(
        self,
        request: idrsservice_20200630_models.UpdateDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateDetectProcessResponse(),
            self.do_rpcrequest('UpdateDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_detect_process_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateDetectProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateDetectProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateDetectProcessResponse(),
            await self.do_rpcrequest_async('UpdateDetectProcess', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_detect_process(
        self,
        request: idrsservice_20200630_models.UpdateDetectProcessRequest,
    ) -> idrsservice_20200630_models.UpdateDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_detect_process_with_options(request, runtime)

    async def update_detect_process_async(
        self,
        request: idrsservice_20200630_models.UpdateDetectProcessRequest,
    ) -> idrsservice_20200630_models.UpdateDetectProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_detect_process_with_options_async(request, runtime)

    def update_live_with_options(
        self,
        request: idrsservice_20200630_models.UpdateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateLiveResponse(),
            self.do_rpcrequest('UpdateLive', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateLiveResponse(),
            await self.do_rpcrequest_async('UpdateLive', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_live(
        self,
        request: idrsservice_20200630_models.UpdateLiveRequest,
    ) -> idrsservice_20200630_models.UpdateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_with_options(request, runtime)

    async def update_live_async(
        self,
        request: idrsservice_20200630_models.UpdateLiveRequest,
    ) -> idrsservice_20200630_models.UpdateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_with_options_async(request, runtime)

    def update_live_record_task_with_options(
        self,
        tmp_req: idrsservice_20200630_models.UpdateLiveRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateLiveRecordTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.UpdateLiveRecordTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.clock_widgets):
            request.clock_widgets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clock_widgets, 'ClockWidgets', 'json')
        if not UtilClient.is_unset(tmp_req.user_panes):
            request.user_panes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_panes, 'UserPanes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateLiveRecordTaskResponse(),
            self.do_rpcrequest('UpdateLiveRecordTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_record_task_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.UpdateLiveRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateLiveRecordTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.UpdateLiveRecordTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.clock_widgets):
            request.clock_widgets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clock_widgets, 'ClockWidgets', 'json')
        if not UtilClient.is_unset(tmp_req.user_panes):
            request.user_panes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_panes, 'UserPanes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateLiveRecordTaskResponse(),
            await self.do_rpcrequest_async('UpdateLiveRecordTask', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_live_record_task(
        self,
        request: idrsservice_20200630_models.UpdateLiveRecordTaskRequest,
    ) -> idrsservice_20200630_models.UpdateLiveRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_record_task_with_options(request, runtime)

    async def update_live_record_task_async(
        self,
        request: idrsservice_20200630_models.UpdateLiveRecordTaskRequest,
    ) -> idrsservice_20200630_models.UpdateLiveRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_record_task_with_options_async(request, runtime)

    def update_live_record_template_with_options(
        self,
        tmp_req: idrsservice_20200630_models.UpdateLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateLiveRecordTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.UpdateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backgrounds):
            request.backgrounds_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backgrounds, 'Backgrounds', 'json')
        if not UtilClient.is_unset(tmp_req.watermarks):
            request.watermarks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermarks, 'Watermarks', 'json')
        if not UtilClient.is_unset(tmp_req.clock_widgets):
            request.clock_widgets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clock_widgets, 'ClockWidgets', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateLiveRecordTemplateResponse(),
            self.do_rpcrequest('UpdateLiveRecordTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_record_template_with_options_async(
        self,
        tmp_req: idrsservice_20200630_models.UpdateLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateLiveRecordTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = idrsservice_20200630_models.UpdateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backgrounds):
            request.backgrounds_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backgrounds, 'Backgrounds', 'json')
        if not UtilClient.is_unset(tmp_req.watermarks):
            request.watermarks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermarks, 'Watermarks', 'json')
        if not UtilClient.is_unset(tmp_req.clock_widgets):
            request.clock_widgets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clock_widgets, 'ClockWidgets', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateLiveRecordTemplateResponse(),
            await self.do_rpcrequest_async('UpdateLiveRecordTemplate', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_live_record_template(
        self,
        request: idrsservice_20200630_models.UpdateLiveRecordTemplateRequest,
    ) -> idrsservice_20200630_models.UpdateLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_record_template_with_options(request, runtime)

    async def update_live_record_template_async(
        self,
        request: idrsservice_20200630_models.UpdateLiveRecordTemplateRequest,
    ) -> idrsservice_20200630_models.UpdateLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_record_template_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: idrsservice_20200630_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateRuleResponse(),
            self.do_rpcrequest('UpdateRule', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateRuleResponse(),
            await self.do_rpcrequest_async('UpdateRule', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_rule(
        self,
        request: idrsservice_20200630_models.UpdateRuleRequest,
    ) -> idrsservice_20200630_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: idrsservice_20200630_models.UpdateRuleRequest,
    ) -> idrsservice_20200630_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)

    def update_service_configuration_with_options(
        self,
        request: idrsservice_20200630_models.UpdateServiceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateServiceConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateServiceConfigurationResponse(),
            self.do_rpcrequest('UpdateServiceConfiguration', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_service_configuration_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateServiceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateServiceConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateServiceConfigurationResponse(),
            await self.do_rpcrequest_async('UpdateServiceConfiguration', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_service_configuration(
        self,
        request: idrsservice_20200630_models.UpdateServiceConfigurationRequest,
    ) -> idrsservice_20200630_models.UpdateServiceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_service_configuration_with_options(request, runtime)

    async def update_service_configuration_async(
        self,
        request: idrsservice_20200630_models.UpdateServiceConfigurationRequest,
    ) -> idrsservice_20200630_models.UpdateServiceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_configuration_with_options_async(request, runtime)

    def update_slr_configuration_with_options(
        self,
        request: idrsservice_20200630_models.UpdateSlrConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateSlrConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateSlrConfigurationResponse(),
            self.do_rpcrequest('UpdateSlrConfiguration', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_slr_configuration_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateSlrConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateSlrConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateSlrConfigurationResponse(),
            await self.do_rpcrequest_async('UpdateSlrConfiguration', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_slr_configuration(
        self,
        request: idrsservice_20200630_models.UpdateSlrConfigurationRequest,
    ) -> idrsservice_20200630_models.UpdateSlrConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_slr_configuration_with_options(request, runtime)

    async def update_slr_configuration_async(
        self,
        request: idrsservice_20200630_models.UpdateSlrConfigurationRequest,
    ) -> idrsservice_20200630_models.UpdateSlrConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_slr_configuration_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: idrsservice_20200630_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateUserResponse(),
            self.do_rpcrequest('UpdateUser', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: idrsservice_20200630_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idrsservice_20200630_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idrsservice_20200630_models.UpdateUserResponse(),
            await self.do_rpcrequest_async('UpdateUser', '2020-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user(
        self,
        request: idrsservice_20200630_models.UpdateUserRequest,
    ) -> idrsservice_20200630_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: idrsservice_20200630_models.UpdateUserRequest,
    ) -> idrsservice_20200630_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
