# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_riskmanagement20260424 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('riskmanagement', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_auth_to_machine_with_options(
        self,
        tmp_req: main_models.BindAuthToMachineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAuthToMachineResponse:
        tmp_req.validate()
        request = main_models.BindAuthToMachineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAuthToMachine',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAuthToMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_auth_to_machine_with_options_async(
        self,
        tmp_req: main_models.BindAuthToMachineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAuthToMachineResponse:
        tmp_req.validate()
        request = main_models.BindAuthToMachineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAuthToMachine',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAuthToMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_auth_to_machine(
        self,
        request: main_models.BindAuthToMachineRequest,
    ) -> main_models.BindAuthToMachineResponse:
        runtime = RuntimeOptions()
        return self.bind_auth_to_machine_with_options(request, runtime)

    async def bind_auth_to_machine_async(
        self,
        request: main_models.BindAuthToMachineRequest,
    ) -> main_models.BindAuthToMachineResponse:
        runtime = RuntimeOptions()
        return await self.bind_auth_to_machine_with_options_async(request, runtime)

    def create_sas_trial_with_options(
        self,
        tmp_req: main_models.CreateSasTrialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSasTrialResponse:
        tmp_req.validate()
        request = main_models.CreateSasTrialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSasTrial',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSasTrialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sas_trial_with_options_async(
        self,
        tmp_req: main_models.CreateSasTrialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSasTrialResponse:
        tmp_req.validate()
        request = main_models.CreateSasTrialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSasTrial',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSasTrialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sas_trial(
        self,
        request: main_models.CreateSasTrialRequest,
    ) -> main_models.CreateSasTrialResponse:
        runtime = RuntimeOptions()
        return self.create_sas_trial_with_options(request, runtime)

    async def create_sas_trial_async(
        self,
        request: main_models.CreateSasTrialRequest,
    ) -> main_models.CreateSasTrialResponse:
        runtime = RuntimeOptions()
        return await self.create_sas_trial_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        tmp_req: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        tmp_req.validate()
        request = main_models.CreateServiceLinkedRoleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        tmp_req: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        tmp_req.validate()
        request = main_models.CreateServiceLinkedRoleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def create_virus_scan_once_task_with_options(
        self,
        request: main_models.CreateVirusScanOnceTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirusScanOnceTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirusScanOnceTask',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirusScanOnceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virus_scan_once_task_with_options_async(
        self,
        request: main_models.CreateVirusScanOnceTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirusScanOnceTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirusScanOnceTask',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirusScanOnceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virus_scan_once_task(
        self,
        request: main_models.CreateVirusScanOnceTaskRequest,
    ) -> main_models.CreateVirusScanOnceTaskResponse:
        runtime = RuntimeOptions()
        return self.create_virus_scan_once_task_with_options(request, runtime)

    async def create_virus_scan_once_task_async(
        self,
        request: main_models.CreateVirusScanOnceTaskRequest,
    ) -> main_models.CreateVirusScanOnceTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_virus_scan_once_task_with_options_async(request, runtime)

    def describe_cloud_center_instances_with_options(
        self,
        tmp_req: main_models.DescribeCloudCenterInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudCenterInstancesResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudCenterInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudCenterInstances',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudCenterInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_center_instances_with_options_async(
        self,
        tmp_req: main_models.DescribeCloudCenterInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudCenterInstancesResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudCenterInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudCenterInstances',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudCenterInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_center_instances(
        self,
        request: main_models.DescribeCloudCenterInstancesRequest,
    ) -> main_models.DescribeCloudCenterInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_center_instances_with_options(request, runtime)

    async def describe_cloud_center_instances_async(
        self,
        request: main_models.DescribeCloudCenterInstancesRequest,
    ) -> main_models.DescribeCloudCenterInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_center_instances_with_options_async(request, runtime)

    def describe_service_linked_role_status_with_options(
        self,
        tmp_req: main_models.DescribeServiceLinkedRoleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceLinkedRoleStatusResponse:
        tmp_req.validate()
        request = main_models.DescribeServiceLinkedRoleStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceLinkedRoleStatus',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceLinkedRoleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_linked_role_status_with_options_async(
        self,
        tmp_req: main_models.DescribeServiceLinkedRoleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceLinkedRoleStatusResponse:
        tmp_req.validate()
        request = main_models.DescribeServiceLinkedRoleStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceLinkedRoleStatus',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceLinkedRoleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_linked_role_status(
        self,
        request: main_models.DescribeServiceLinkedRoleStatusRequest,
    ) -> main_models.DescribeServiceLinkedRoleStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_service_linked_role_status_with_options(request, runtime)

    async def describe_service_linked_role_status_async(
        self,
        request: main_models.DescribeServiceLinkedRoleStatusRequest,
    ) -> main_models.DescribeServiceLinkedRoleStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_service_linked_role_status_with_options_async(request, runtime)

    def describe_susp_events_with_options(
        self,
        tmp_req: main_models.DescribeSuspEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSuspEventsResponse:
        tmp_req.validate()
        request = main_models.DescribeSuspEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSuspEvents',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_susp_events_with_options_async(
        self,
        tmp_req: main_models.DescribeSuspEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSuspEventsResponse:
        tmp_req.validate()
        request = main_models.DescribeSuspEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSuspEvents',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSuspEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_susp_events(
        self,
        request: main_models.DescribeSuspEventsRequest,
    ) -> main_models.DescribeSuspEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    async def describe_susp_events_async(
        self,
        request: main_models.DescribeSuspEventsRequest,
    ) -> main_models.DescribeSuspEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_susp_events_with_options_async(request, runtime)

    def get_alert_record_analysis_result_with_options(
        self,
        tmp_req: main_models.GetAlertRecordAnalysisResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertRecordAnalysisResultResponse:
        tmp_req.validate()
        request = main_models.GetAlertRecordAnalysisResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.unique_tag_list):
            request.unique_tag_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.unique_tag_list, 'UniqueTagList', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not DaraCore.is_null(request.unique_tag_list_shrink):
            query['UniqueTagList'] = request.unique_tag_list_shrink
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertRecordAnalysisResult',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertRecordAnalysisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_record_analysis_result_with_options_async(
        self,
        tmp_req: main_models.GetAlertRecordAnalysisResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertRecordAnalysisResultResponse:
        tmp_req.validate()
        request = main_models.GetAlertRecordAnalysisResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.unique_tag_list):
            request.unique_tag_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.unique_tag_list, 'UniqueTagList', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not DaraCore.is_null(request.unique_tag_list_shrink):
            query['UniqueTagList'] = request.unique_tag_list_shrink
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertRecordAnalysisResult',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertRecordAnalysisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_record_analysis_result(
        self,
        request: main_models.GetAlertRecordAnalysisResultRequest,
    ) -> main_models.GetAlertRecordAnalysisResultResponse:
        runtime = RuntimeOptions()
        return self.get_alert_record_analysis_result_with_options(request, runtime)

    async def get_alert_record_analysis_result_async(
        self,
        request: main_models.GetAlertRecordAnalysisResultRequest,
    ) -> main_models.GetAlertRecordAnalysisResultResponse:
        runtime = RuntimeOptions()
        return await self.get_alert_record_analysis_result_with_options_async(request, runtime)

    def get_ali_yun_safe_center_result_with_options(
        self,
        tmp_req: main_models.GetAliYunSafeCenterResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAliYunSafeCenterResultResponse:
        tmp_req.validate()
        request = main_models.GetAliYunSafeCenterResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_similar_security_events_query_task_request):
            request.create_similar_security_events_query_task_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_similar_security_events_query_task_request, 'CreateSimilarSecurityEventsQueryTaskRequest', 'json')
        if not DaraCore.is_null(tmp_req.describe_instances_full_status_request):
            request.describe_instances_full_status_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.describe_instances_full_status_request, 'DescribeInstancesFullStatusRequest', 'json')
        if not DaraCore.is_null(tmp_req.describe_security_event_operation_status_request):
            request.describe_security_event_operation_status_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.describe_security_event_operation_status_request, 'DescribeSecurityEventOperationStatusRequest', 'json')
        if not DaraCore.is_null(tmp_req.describe_similar_security_events_request):
            request.describe_similar_security_events_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.describe_similar_security_events_request, 'DescribeSimilarSecurityEventsRequest', 'json')
        if not DaraCore.is_null(tmp_req.get_asset_detail_by_uuid_request):
            request.get_asset_detail_by_uuid_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.get_asset_detail_by_uuid_request, 'GetAssetDetailByUuidRequest', 'json')
        if not DaraCore.is_null(tmp_req.handle_security_events_request):
            request.handle_security_events_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.handle_security_events_request, 'HandleSecurityEventsRequest', 'json')
        if not DaraCore.is_null(tmp_req.handle_similar_security_events_request):
            request.handle_similar_security_events_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.handle_similar_security_events_request, 'HandleSimilarSecurityEventsRequest', 'json')
        if not DaraCore.is_null(tmp_req.list_instances_request):
            request.list_instances_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_instances_request, 'ListInstancesRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.create_similar_security_events_query_task_request_shrink):
            query['CreateSimilarSecurityEventsQueryTaskRequest'] = request.create_similar_security_events_query_task_request_shrink
        if not DaraCore.is_null(request.describe_instances_full_status_request_shrink):
            query['DescribeInstancesFullStatusRequest'] = request.describe_instances_full_status_request_shrink
        if not DaraCore.is_null(request.describe_security_event_operation_status_request_shrink):
            query['DescribeSecurityEventOperationStatusRequest'] = request.describe_security_event_operation_status_request_shrink
        if not DaraCore.is_null(request.describe_similar_security_events_request_shrink):
            query['DescribeSimilarSecurityEventsRequest'] = request.describe_similar_security_events_request_shrink
        if not DaraCore.is_null(request.get_asset_detail_by_uuid_request_shrink):
            query['GetAssetDetailByUuidRequest'] = request.get_asset_detail_by_uuid_request_shrink
        if not DaraCore.is_null(request.handle_security_events_request_shrink):
            query['HandleSecurityEventsRequest'] = request.handle_security_events_request_shrink
        if not DaraCore.is_null(request.handle_similar_security_events_request_shrink):
            query['HandleSimilarSecurityEventsRequest'] = request.handle_similar_security_events_request_shrink
        if not DaraCore.is_null(request.interface_code):
            query['InterfaceCode'] = request.interface_code
        if not DaraCore.is_null(request.list_instances_request_shrink):
            query['ListInstancesRequest'] = request.list_instances_request_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAliYunSafeCenterResult',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAliYunSafeCenterResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ali_yun_safe_center_result_with_options_async(
        self,
        tmp_req: main_models.GetAliYunSafeCenterResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAliYunSafeCenterResultResponse:
        tmp_req.validate()
        request = main_models.GetAliYunSafeCenterResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_similar_security_events_query_task_request):
            request.create_similar_security_events_query_task_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_similar_security_events_query_task_request, 'CreateSimilarSecurityEventsQueryTaskRequest', 'json')
        if not DaraCore.is_null(tmp_req.describe_instances_full_status_request):
            request.describe_instances_full_status_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.describe_instances_full_status_request, 'DescribeInstancesFullStatusRequest', 'json')
        if not DaraCore.is_null(tmp_req.describe_security_event_operation_status_request):
            request.describe_security_event_operation_status_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.describe_security_event_operation_status_request, 'DescribeSecurityEventOperationStatusRequest', 'json')
        if not DaraCore.is_null(tmp_req.describe_similar_security_events_request):
            request.describe_similar_security_events_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.describe_similar_security_events_request, 'DescribeSimilarSecurityEventsRequest', 'json')
        if not DaraCore.is_null(tmp_req.get_asset_detail_by_uuid_request):
            request.get_asset_detail_by_uuid_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.get_asset_detail_by_uuid_request, 'GetAssetDetailByUuidRequest', 'json')
        if not DaraCore.is_null(tmp_req.handle_security_events_request):
            request.handle_security_events_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.handle_security_events_request, 'HandleSecurityEventsRequest', 'json')
        if not DaraCore.is_null(tmp_req.handle_similar_security_events_request):
            request.handle_similar_security_events_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.handle_similar_security_events_request, 'HandleSimilarSecurityEventsRequest', 'json')
        if not DaraCore.is_null(tmp_req.list_instances_request):
            request.list_instances_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_instances_request, 'ListInstancesRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.create_similar_security_events_query_task_request_shrink):
            query['CreateSimilarSecurityEventsQueryTaskRequest'] = request.create_similar_security_events_query_task_request_shrink
        if not DaraCore.is_null(request.describe_instances_full_status_request_shrink):
            query['DescribeInstancesFullStatusRequest'] = request.describe_instances_full_status_request_shrink
        if not DaraCore.is_null(request.describe_security_event_operation_status_request_shrink):
            query['DescribeSecurityEventOperationStatusRequest'] = request.describe_security_event_operation_status_request_shrink
        if not DaraCore.is_null(request.describe_similar_security_events_request_shrink):
            query['DescribeSimilarSecurityEventsRequest'] = request.describe_similar_security_events_request_shrink
        if not DaraCore.is_null(request.get_asset_detail_by_uuid_request_shrink):
            query['GetAssetDetailByUuidRequest'] = request.get_asset_detail_by_uuid_request_shrink
        if not DaraCore.is_null(request.handle_security_events_request_shrink):
            query['HandleSecurityEventsRequest'] = request.handle_security_events_request_shrink
        if not DaraCore.is_null(request.handle_similar_security_events_request_shrink):
            query['HandleSimilarSecurityEventsRequest'] = request.handle_similar_security_events_request_shrink
        if not DaraCore.is_null(request.interface_code):
            query['InterfaceCode'] = request.interface_code
        if not DaraCore.is_null(request.list_instances_request_shrink):
            query['ListInstancesRequest'] = request.list_instances_request_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAliYunSafeCenterResult',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAliYunSafeCenterResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ali_yun_safe_center_result(
        self,
        request: main_models.GetAliYunSafeCenterResultRequest,
    ) -> main_models.GetAliYunSafeCenterResultResponse:
        runtime = RuntimeOptions()
        return self.get_ali_yun_safe_center_result_with_options(request, runtime)

    async def get_ali_yun_safe_center_result_async(
        self,
        request: main_models.GetAliYunSafeCenterResultRequest,
    ) -> main_models.GetAliYunSafeCenterResultResponse:
        runtime = RuntimeOptions()
        return await self.get_ali_yun_safe_center_result_with_options_async(request, runtime)

    def get_can_try_sas_with_options(
        self,
        tmp_req: main_models.GetCanTrySasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCanTrySasResponse:
        tmp_req.validate()
        request = main_models.GetCanTrySasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCanTrySas',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCanTrySasResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_can_try_sas_with_options_async(
        self,
        tmp_req: main_models.GetCanTrySasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCanTrySasResponse:
        tmp_req.validate()
        request = main_models.GetCanTrySasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCanTrySas',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCanTrySasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_can_try_sas(
        self,
        request: main_models.GetCanTrySasRequest,
    ) -> main_models.GetCanTrySasResponse:
        runtime = RuntimeOptions()
        return self.get_can_try_sas_with_options(request, runtime)

    async def get_can_try_sas_async(
        self,
        request: main_models.GetCanTrySasRequest,
    ) -> main_models.GetCanTrySasResponse:
        runtime = RuntimeOptions()
        return await self.get_can_try_sas_with_options_async(request, runtime)

    def get_disposal_tool_status_with_options(
        self,
        request: main_models.GetDisposalToolStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDisposalToolStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDisposalToolStatus',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDisposalToolStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_disposal_tool_status_with_options_async(
        self,
        request: main_models.GetDisposalToolStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDisposalToolStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDisposalToolStatus',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDisposalToolStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_disposal_tool_status(
        self,
        request: main_models.GetDisposalToolStatusRequest,
    ) -> main_models.GetDisposalToolStatusResponse:
        runtime = RuntimeOptions()
        return self.get_disposal_tool_status_with_options(request, runtime)

    async def get_disposal_tool_status_async(
        self,
        request: main_models.GetDisposalToolStatusRequest,
    ) -> main_models.GetDisposalToolStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_disposal_tool_status_with_options_async(request, runtime)

    def get_valid_deduct_instances_with_options(
        self,
        tmp_req: main_models.GetValidDeductInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidDeductInstancesResponse:
        tmp_req.validate()
        request = main_models.GetValidDeductInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetValidDeductInstances',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidDeductInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_valid_deduct_instances_with_options_async(
        self,
        tmp_req: main_models.GetValidDeductInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidDeductInstancesResponse:
        tmp_req.validate()
        request = main_models.GetValidDeductInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetValidDeductInstances',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidDeductInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_valid_deduct_instances(
        self,
        request: main_models.GetValidDeductInstancesRequest,
    ) -> main_models.GetValidDeductInstancesResponse:
        runtime = RuntimeOptions()
        return self.get_valid_deduct_instances_with_options(request, runtime)

    async def get_valid_deduct_instances_async(
        self,
        request: main_models.GetValidDeductInstancesRequest,
    ) -> main_models.GetValidDeductInstancesResponse:
        runtime = RuntimeOptions()
        return await self.get_valid_deduct_instances_with_options_async(request, runtime)

    def init_sas_module_rule_with_options(
        self,
        tmp_req: main_models.InitSasModuleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitSasModuleRuleResponse:
        tmp_req.validate()
        request = main_models.InitSasModuleRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instances):
            request.instances_shrink = Utils.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_bind):
            query['AutoBind'] = request.auto_bind
        if not DaraCore.is_null(request.instances_shrink):
            query['Instances'] = request.instances_shrink
        if not DaraCore.is_null(request.is_trial):
            query['IsTrial'] = request.is_trial
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitSasModuleRule',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitSasModuleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_sas_module_rule_with_options_async(
        self,
        tmp_req: main_models.InitSasModuleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitSasModuleRuleResponse:
        tmp_req.validate()
        request = main_models.InitSasModuleRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instances):
            request.instances_shrink = Utils.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_bind):
            query['AutoBind'] = request.auto_bind
        if not DaraCore.is_null(request.instances_shrink):
            query['Instances'] = request.instances_shrink
        if not DaraCore.is_null(request.is_trial):
            query['IsTrial'] = request.is_trial
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitSasModuleRule',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitSasModuleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_sas_module_rule(
        self,
        request: main_models.InitSasModuleRuleRequest,
    ) -> main_models.InitSasModuleRuleResponse:
        runtime = RuntimeOptions()
        return self.init_sas_module_rule_with_options(request, runtime)

    async def init_sas_module_rule_async(
        self,
        request: main_models.InitSasModuleRuleRequest,
    ) -> main_models.InitSasModuleRuleResponse:
        runtime = RuntimeOptions()
        return await self.init_sas_module_rule_with_options_async(request, runtime)

    def list_virus_scan_machine_event_with_options(
        self,
        request: main_models.ListVirusScanMachineEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVirusScanMachineEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.operate_task_id):
            query['OperateTaskId'] = request.operate_task_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVirusScanMachineEvent',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVirusScanMachineEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virus_scan_machine_event_with_options_async(
        self,
        request: main_models.ListVirusScanMachineEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVirusScanMachineEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.operate_task_id):
            query['OperateTaskId'] = request.operate_task_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVirusScanMachineEvent',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVirusScanMachineEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virus_scan_machine_event(
        self,
        request: main_models.ListVirusScanMachineEventRequest,
    ) -> main_models.ListVirusScanMachineEventResponse:
        runtime = RuntimeOptions()
        return self.list_virus_scan_machine_event_with_options(request, runtime)

    async def list_virus_scan_machine_event_async(
        self,
        request: main_models.ListVirusScanMachineEventRequest,
    ) -> main_models.ListVirusScanMachineEventResponse:
        runtime = RuntimeOptions()
        return await self.list_virus_scan_machine_event_with_options_async(request, runtime)

    def open_trial_package_with_options(
        self,
        request: main_models.OpenTrialPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenTrialPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_close_switch):
            query['AutoCloseSwitch'] = request.auto_close_switch
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenTrialPackage',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenTrialPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_trial_package_with_options_async(
        self,
        request: main_models.OpenTrialPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenTrialPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_close_switch):
            query['AutoCloseSwitch'] = request.auto_close_switch
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenTrialPackage',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenTrialPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_trial_package(
        self,
        request: main_models.OpenTrialPackageRequest,
    ) -> main_models.OpenTrialPackageResponse:
        runtime = RuntimeOptions()
        return self.open_trial_package_with_options(request, runtime)

    async def open_trial_package_async(
        self,
        request: main_models.OpenTrialPackageRequest,
    ) -> main_models.OpenTrialPackageResponse:
        runtime = RuntimeOptions()
        return await self.open_trial_package_with_options_async(request, runtime)

    def query_security_check_report_with_options(
        self,
        request: main_models.QuerySecurityCheckReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecurityCheckReportResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QuerySecurityCheckReport',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecurityCheckReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_security_check_report_with_options_async(
        self,
        request: main_models.QuerySecurityCheckReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecurityCheckReportResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QuerySecurityCheckReport',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecurityCheckReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_security_check_report(
        self,
        request: main_models.QuerySecurityCheckReportRequest,
    ) -> main_models.QuerySecurityCheckReportResponse:
        runtime = RuntimeOptions()
        return self.query_security_check_report_with_options(request, runtime)

    async def query_security_check_report_async(
        self,
        request: main_models.QuerySecurityCheckReportRequest,
    ) -> main_models.QuerySecurityCheckReportResponse:
        runtime = RuntimeOptions()
        return await self.query_security_check_report_with_options_async(request, runtime)

    def start_disposal_tool_service_with_options(
        self,
        request: main_models.StartDisposalToolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDisposalToolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDisposalToolService',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDisposalToolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disposal_tool_service_with_options_async(
        self,
        request: main_models.StartDisposalToolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDisposalToolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDisposalToolService',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDisposalToolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disposal_tool_service(
        self,
        request: main_models.StartDisposalToolServiceRequest,
    ) -> main_models.StartDisposalToolServiceResponse:
        runtime = RuntimeOptions()
        return self.start_disposal_tool_service_with_options(request, runtime)

    async def start_disposal_tool_service_async(
        self,
        request: main_models.StartDisposalToolServiceRequest,
    ) -> main_models.StartDisposalToolServiceResponse:
        runtime = RuntimeOptions()
        return await self.start_disposal_tool_service_with_options_async(request, runtime)

    def update_post_paid_bind_rel_with_options(
        self,
        tmp_req: main_models.UpdatePostPaidBindRelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePostPaidBindRelResponse:
        tmp_req.validate()
        request = main_models.UpdatePostPaidBindRelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePostPaidBindRel',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePostPaidBindRelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_post_paid_bind_rel_with_options_async(
        self,
        tmp_req: main_models.UpdatePostPaidBindRelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePostPaidBindRelResponse:
        tmp_req.validate()
        request = main_models.UpdatePostPaidBindRelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sdk_request):
            request.sdk_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.sdk_request, 'SdkRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sdk_request_shrink):
            query['SdkRequest'] = request.sdk_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePostPaidBindRel',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePostPaidBindRelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_post_paid_bind_rel(
        self,
        request: main_models.UpdatePostPaidBindRelRequest,
    ) -> main_models.UpdatePostPaidBindRelResponse:
        runtime = RuntimeOptions()
        return self.update_post_paid_bind_rel_with_options(request, runtime)

    async def update_post_paid_bind_rel_async(
        self,
        request: main_models.UpdatePostPaidBindRelRequest,
    ) -> main_models.UpdatePostPaidBindRelResponse:
        runtime = RuntimeOptions()
        return await self.update_post_paid_bind_rel_with_options_async(request, runtime)
