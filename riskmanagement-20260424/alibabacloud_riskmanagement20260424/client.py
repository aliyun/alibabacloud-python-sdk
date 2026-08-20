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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'public': 'riskmanagement.aliyuncs.com'
        }
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

    def describe_version_config_with_options(
        self,
        tmp_req: main_models.DescribeVersionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVersionConfigResponse:
        tmp_req.validate()
        request = main_models.DescribeVersionConfigShrinkRequest()
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
            action = 'DescribeVersionConfig',
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
            main_models.DescribeVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_version_config_with_options_async(
        self,
        tmp_req: main_models.DescribeVersionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVersionConfigResponse:
        tmp_req.validate()
        request = main_models.DescribeVersionConfigShrinkRequest()
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
            action = 'DescribeVersionConfig',
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
            main_models.DescribeVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_version_config(
        self,
        request: main_models.DescribeVersionConfigRequest,
    ) -> main_models.DescribeVersionConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_version_config_with_options(request, runtime)

    async def describe_version_config_async(
        self,
        request: main_models.DescribeVersionConfigRequest,
    ) -> main_models.DescribeVersionConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_version_config_with_options_async(request, runtime)

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

    def get_compliance_pack_id_with_options(
        self,
        request: main_models.GetCompliancePackIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCompliancePackIdResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetCompliancePackId',
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
            main_models.GetCompliancePackIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compliance_pack_id_with_options_async(
        self,
        request: main_models.GetCompliancePackIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCompliancePackIdResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetCompliancePackId',
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
            main_models.GetCompliancePackIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compliance_pack_id(
        self,
        request: main_models.GetCompliancePackIdRequest,
    ) -> main_models.GetCompliancePackIdResponse:
        runtime = RuntimeOptions()
        return self.get_compliance_pack_id_with_options(request, runtime)

    async def get_compliance_pack_id_async(
        self,
        request: main_models.GetCompliancePackIdRequest,
    ) -> main_models.GetCompliancePackIdResponse:
        runtime = RuntimeOptions()
        return await self.get_compliance_pack_id_with_options_async(request, runtime)

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

    def get_notification_click_record_with_options(
        self,
        request: main_models.GetNotificationClickRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotificationClickRecordResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetNotificationClickRecord',
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
            main_models.GetNotificationClickRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_notification_click_record_with_options_async(
        self,
        request: main_models.GetNotificationClickRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotificationClickRecordResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetNotificationClickRecord',
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
            main_models.GetNotificationClickRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_notification_click_record(
        self,
        request: main_models.GetNotificationClickRecordRequest,
    ) -> main_models.GetNotificationClickRecordResponse:
        runtime = RuntimeOptions()
        return self.get_notification_click_record_with_options(request, runtime)

    async def get_notification_click_record_async(
        self,
        request: main_models.GetNotificationClickRecordRequest,
    ) -> main_models.GetNotificationClickRecordResponse:
        runtime = RuntimeOptions()
        return await self.get_notification_click_record_with_options_async(request, runtime)

    def get_notification_contacts_with_options(
        self,
        request: main_models.GetNotificationContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotificationContactsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetNotificationContacts',
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
            main_models.GetNotificationContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_notification_contacts_with_options_async(
        self,
        request: main_models.GetNotificationContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotificationContactsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetNotificationContacts',
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
            main_models.GetNotificationContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_notification_contacts(
        self,
        request: main_models.GetNotificationContactsRequest,
    ) -> main_models.GetNotificationContactsResponse:
        runtime = RuntimeOptions()
        return self.get_notification_contacts_with_options(request, runtime)

    async def get_notification_contacts_async(
        self,
        request: main_models.GetNotificationContactsRequest,
    ) -> main_models.GetNotificationContactsResponse:
        runtime = RuntimeOptions()
        return await self.get_notification_contacts_with_options_async(request, runtime)

    def get_notification_pend_number_with_options(
        self,
        request: main_models.GetNotificationPendNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotificationPendNumberResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetNotificationPendNumber',
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
            main_models.GetNotificationPendNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_notification_pend_number_with_options_async(
        self,
        request: main_models.GetNotificationPendNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotificationPendNumberResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetNotificationPendNumber',
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
            main_models.GetNotificationPendNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_notification_pend_number(
        self,
        request: main_models.GetNotificationPendNumberRequest,
    ) -> main_models.GetNotificationPendNumberResponse:
        runtime = RuntimeOptions()
        return self.get_notification_pend_number_with_options(request, runtime)

    async def get_notification_pend_number_async(
        self,
        request: main_models.GetNotificationPendNumberRequest,
    ) -> main_models.GetNotificationPendNumberResponse:
        runtime = RuntimeOptions()
        return await self.get_notification_pend_number_with_options_async(request, runtime)

    def get_resource_control_event_with_options(
        self,
        tmp_req: main_models.GetResourceControlEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceControlEventResponse:
        tmp_req.validate()
        request = main_models.GetResourceControlEventShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_id_list):
            request.event_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_id_list, 'EventIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_id_list_shrink):
            query['EventIdList'] = request.event_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceControlEvent',
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
            main_models.GetResourceControlEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_control_event_with_options_async(
        self,
        tmp_req: main_models.GetResourceControlEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceControlEventResponse:
        tmp_req.validate()
        request = main_models.GetResourceControlEventShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_id_list):
            request.event_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_id_list, 'EventIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_id_list_shrink):
            query['EventIdList'] = request.event_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceControlEvent',
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
            main_models.GetResourceControlEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_control_event(
        self,
        request: main_models.GetResourceControlEventRequest,
    ) -> main_models.GetResourceControlEventResponse:
        runtime = RuntimeOptions()
        return self.get_resource_control_event_with_options(request, runtime)

    async def get_resource_control_event_async(
        self,
        request: main_models.GetResourceControlEventRequest,
    ) -> main_models.GetResourceControlEventResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_control_event_with_options_async(request, runtime)

    def get_security_check_base_info_with_options(
        self,
        request: main_models.GetSecurityCheckBaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityCheckBaseInfoResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecurityCheckBaseInfo',
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
            main_models.GetSecurityCheckBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_check_base_info_with_options_async(
        self,
        request: main_models.GetSecurityCheckBaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityCheckBaseInfoResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecurityCheckBaseInfo',
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
            main_models.GetSecurityCheckBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_check_base_info(
        self,
        request: main_models.GetSecurityCheckBaseInfoRequest,
    ) -> main_models.GetSecurityCheckBaseInfoResponse:
        runtime = RuntimeOptions()
        return self.get_security_check_base_info_with_options(request, runtime)

    async def get_security_check_base_info_async(
        self,
        request: main_models.GetSecurityCheckBaseInfoRequest,
    ) -> main_models.GetSecurityCheckBaseInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_security_check_base_info_with_options_async(request, runtime)

    def get_security_check_result_base_info_with_options(
        self,
        request: main_models.GetSecurityCheckResultBaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityCheckResultBaseInfoResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecurityCheckResultBaseInfo',
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
            main_models.GetSecurityCheckResultBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_check_result_base_info_with_options_async(
        self,
        request: main_models.GetSecurityCheckResultBaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityCheckResultBaseInfoResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecurityCheckResultBaseInfo',
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
            main_models.GetSecurityCheckResultBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_check_result_base_info(
        self,
        request: main_models.GetSecurityCheckResultBaseInfoRequest,
    ) -> main_models.GetSecurityCheckResultBaseInfoResponse:
        runtime = RuntimeOptions()
        return self.get_security_check_result_base_info_with_options(request, runtime)

    async def get_security_check_result_base_info_async(
        self,
        request: main_models.GetSecurityCheckResultBaseInfoRequest,
    ) -> main_models.GetSecurityCheckResultBaseInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_security_check_result_base_info_with_options_async(request, runtime)

    def get_security_suggestion_list_with_options(
        self,
        tmp_req: main_models.GetSecuritySuggestionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecuritySuggestionListResponse:
        tmp_req.validate()
        request = main_models.GetSecuritySuggestionListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_config_rules_request):
            request.list_config_rules_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_config_rules_request, 'ListConfigRulesRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.list_config_rules_request_shrink):
            query['ListConfigRulesRequest'] = request.list_config_rules_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecuritySuggestionList',
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
            main_models.GetSecuritySuggestionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_suggestion_list_with_options_async(
        self,
        tmp_req: main_models.GetSecuritySuggestionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecuritySuggestionListResponse:
        tmp_req.validate()
        request = main_models.GetSecuritySuggestionListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_config_rules_request):
            request.list_config_rules_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_config_rules_request, 'ListConfigRulesRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.list_config_rules_request_shrink):
            query['ListConfigRulesRequest'] = request.list_config_rules_request_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecuritySuggestionList',
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
            main_models.GetSecuritySuggestionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_suggestion_list(
        self,
        request: main_models.GetSecuritySuggestionListRequest,
    ) -> main_models.GetSecuritySuggestionListResponse:
        runtime = RuntimeOptions()
        return self.get_security_suggestion_list_with_options(request, runtime)

    async def get_security_suggestion_list_async(
        self,
        request: main_models.GetSecuritySuggestionListRequest,
    ) -> main_models.GetSecuritySuggestionListResponse:
        runtime = RuntimeOptions()
        return await self.get_security_suggestion_list_with_options_async(request, runtime)

    def get_security_suggestion_number_with_options(
        self,
        request: main_models.GetSecuritySuggestionNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecuritySuggestionNumberResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecuritySuggestionNumber',
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
            main_models.GetSecuritySuggestionNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_suggestion_number_with_options_async(
        self,
        request: main_models.GetSecuritySuggestionNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecuritySuggestionNumberResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecuritySuggestionNumber',
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
            main_models.GetSecuritySuggestionNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_suggestion_number(
        self,
        request: main_models.GetSecuritySuggestionNumberRequest,
    ) -> main_models.GetSecuritySuggestionNumberResponse:
        runtime = RuntimeOptions()
        return self.get_security_suggestion_number_with_options(request, runtime)

    async def get_security_suggestion_number_async(
        self,
        request: main_models.GetSecuritySuggestionNumberRequest,
    ) -> main_models.GetSecuritySuggestionNumberResponse:
        runtime = RuntimeOptions()
        return await self.get_security_suggestion_number_with_options_async(request, runtime)

    def get_service_linked_role_status_with_options(
        self,
        request: main_models.GetServiceLinkedRoleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceLinkedRoleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceLinkedRoleStatus',
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
            main_models.GetServiceLinkedRoleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_linked_role_status_with_options_async(
        self,
        request: main_models.GetServiceLinkedRoleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceLinkedRoleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceLinkedRoleStatus',
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
            main_models.GetServiceLinkedRoleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_linked_role_status(
        self,
        request: main_models.GetServiceLinkedRoleStatusRequest,
    ) -> main_models.GetServiceLinkedRoleStatusResponse:
        runtime = RuntimeOptions()
        return self.get_service_linked_role_status_with_options(request, runtime)

    async def get_service_linked_role_status_async(
        self,
        request: main_models.GetServiceLinkedRoleStatusRequest,
    ) -> main_models.GetServiceLinkedRoleStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_service_linked_role_status_with_options_async(request, runtime)

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

    def query_account_safety_incident_with_options(
        self,
        tmp_req: main_models.QueryAccountSafetyIncidentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountSafetyIncidentResponse:
        tmp_req.validate()
        request = main_models.QueryAccountSafetyIncidentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.action_codes):
            request.action_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.action_codes, 'ActionCodes', 'json')
        if not DaraCore.is_null(tmp_req.case_codes):
            request.case_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.case_codes, 'CaseCodes', 'json')
        if not DaraCore.is_null(tmp_req.event_ids):
            request.event_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_ids, 'EventIds', 'json')
        if not DaraCore.is_null(tmp_req.statuses):
            request.statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        query = {}
        if not DaraCore.is_null(request.action_codes_shrink):
            query['ActionCodes'] = request.action_codes_shrink
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.case_code):
            query['CaseCode'] = request.case_code
        if not DaraCore.is_null(request.case_codes_shrink):
            query['CaseCodes'] = request.case_codes_shrink
        if not DaraCore.is_null(request.current):
            query['Current'] = request.current
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_ids_shrink):
            query['EventIds'] = request.event_ids_shrink
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.punish_end_time):
            query['PunishEndTime'] = request.punish_end_time
        if not DaraCore.is_null(request.punish_start_time):
            query['PunishStartTime'] = request.punish_start_time
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.statuses_shrink):
            query['Statuses'] = request.statuses_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountSafetyIncident',
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
            main_models.QueryAccountSafetyIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_safety_incident_with_options_async(
        self,
        tmp_req: main_models.QueryAccountSafetyIncidentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountSafetyIncidentResponse:
        tmp_req.validate()
        request = main_models.QueryAccountSafetyIncidentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.action_codes):
            request.action_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.action_codes, 'ActionCodes', 'json')
        if not DaraCore.is_null(tmp_req.case_codes):
            request.case_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.case_codes, 'CaseCodes', 'json')
        if not DaraCore.is_null(tmp_req.event_ids):
            request.event_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_ids, 'EventIds', 'json')
        if not DaraCore.is_null(tmp_req.statuses):
            request.statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        query = {}
        if not DaraCore.is_null(request.action_codes_shrink):
            query['ActionCodes'] = request.action_codes_shrink
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.case_code):
            query['CaseCode'] = request.case_code
        if not DaraCore.is_null(request.case_codes_shrink):
            query['CaseCodes'] = request.case_codes_shrink
        if not DaraCore.is_null(request.current):
            query['Current'] = request.current
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_ids_shrink):
            query['EventIds'] = request.event_ids_shrink
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.punish_end_time):
            query['PunishEndTime'] = request.punish_end_time
        if not DaraCore.is_null(request.punish_start_time):
            query['PunishStartTime'] = request.punish_start_time
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.statuses_shrink):
            query['Statuses'] = request.statuses_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountSafetyIncident',
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
            main_models.QueryAccountSafetyIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_safety_incident(
        self,
        request: main_models.QueryAccountSafetyIncidentRequest,
    ) -> main_models.QueryAccountSafetyIncidentResponse:
        runtime = RuntimeOptions()
        return self.query_account_safety_incident_with_options(request, runtime)

    async def query_account_safety_incident_async(
        self,
        request: main_models.QueryAccountSafetyIncidentRequest,
    ) -> main_models.QueryAccountSafetyIncidentResponse:
        runtime = RuntimeOptions()
        return await self.query_account_safety_incident_with_options_async(request, runtime)

    def query_guide_sub_status_with_options(
        self,
        request: main_models.QueryGuideSubStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGuideSubStatusResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryGuideSubStatus',
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
            main_models.QueryGuideSubStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_guide_sub_status_with_options_async(
        self,
        request: main_models.QueryGuideSubStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGuideSubStatusResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryGuideSubStatus',
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
            main_models.QueryGuideSubStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_guide_sub_status(
        self,
        request: main_models.QueryGuideSubStatusRequest,
    ) -> main_models.QueryGuideSubStatusResponse:
        runtime = RuntimeOptions()
        return self.query_guide_sub_status_with_options(request, runtime)

    async def query_guide_sub_status_async(
        self,
        request: main_models.QueryGuideSubStatusRequest,
    ) -> main_models.QueryGuideSubStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_guide_sub_status_with_options_async(request, runtime)

    def query_resource_control_events_with_options(
        self,
        tmp_req: main_models.QueryResourceControlEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryResourceControlEventsResponse:
        tmp_req.validate()
        request = main_models.QueryResourceControlEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.action_codes):
            request.action_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.action_codes, 'ActionCodes', 'json')
        if not DaraCore.is_null(tmp_req.business_codes):
            request.business_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.business_codes, 'BusinessCodes', 'json')
        if not DaraCore.is_null(tmp_req.case_codes_prefix):
            request.case_codes_prefix_shrink = Utils.array_to_string_with_specified_style(tmp_req.case_codes_prefix, 'CaseCodesPrefix', 'json')
        if not DaraCore.is_null(tmp_req.event_codes):
            request.event_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_codes, 'EventCodes', 'json')
        if not DaraCore.is_null(tmp_req.event_id_list):
            request.event_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_id_list, 'EventIdList', 'json')
        if not DaraCore.is_null(tmp_req.exclude_action_codes):
            request.exclude_action_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_action_codes, 'ExcludeActionCodes', 'json')
        if not DaraCore.is_null(tmp_req.exclude_event_codes):
            request.exclude_event_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_event_codes, 'ExcludeEventCodes', 'json')
        if not DaraCore.is_null(tmp_req.exclude_reasons):
            request.exclude_reasons_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_reasons, 'ExcludeReasons', 'json')
        if not DaraCore.is_null(tmp_req.include_reasons):
            request.include_reasons_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_reasons, 'IncludeReasons', 'json')
        if not DaraCore.is_null(tmp_req.source_codes):
            request.source_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_codes, 'SourceCodes', 'json')
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        query = {}
        if not DaraCore.is_null(request.action_code):
            query['ActionCode'] = request.action_code
        if not DaraCore.is_null(request.action_codes_shrink):
            query['ActionCodes'] = request.action_codes_shrink
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.business_code):
            query['BusinessCode'] = request.business_code
        if not DaraCore.is_null(request.business_codes_shrink):
            query['BusinessCodes'] = request.business_codes_shrink
        if not DaraCore.is_null(request.case_codes_prefix_shrink):
            query['CaseCodesPrefix'] = request.case_codes_prefix_shrink
        if not DaraCore.is_null(request.current):
            query['Current'] = request.current
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.event_code):
            query['EventCode'] = request.event_code
        if not DaraCore.is_null(request.event_codes_shrink):
            query['EventCodes'] = request.event_codes_shrink
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_id_list_shrink):
            query['EventIdList'] = request.event_id_list_shrink
        if not DaraCore.is_null(request.exclude_action_codes_shrink):
            query['ExcludeActionCodes'] = request.exclude_action_codes_shrink
        if not DaraCore.is_null(request.exclude_event_codes_shrink):
            query['ExcludeEventCodes'] = request.exclude_event_codes_shrink
        if not DaraCore.is_null(request.exclude_reasons_shrink):
            query['ExcludeReasons'] = request.exclude_reasons_shrink
        if not DaraCore.is_null(request.include_reasons_shrink):
            query['IncludeReasons'] = request.include_reasons_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.punish_end_time):
            query['PunishEndTime'] = request.punish_end_time
        if not DaraCore.is_null(request.punish_start_time):
            query['PunishStartTime'] = request.punish_start_time
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.source_codes_shrink):
            query['SourceCodes'] = request.source_codes_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResourceControlEvents',
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
            main_models.QueryResourceControlEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_resource_control_events_with_options_async(
        self,
        tmp_req: main_models.QueryResourceControlEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryResourceControlEventsResponse:
        tmp_req.validate()
        request = main_models.QueryResourceControlEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.action_codes):
            request.action_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.action_codes, 'ActionCodes', 'json')
        if not DaraCore.is_null(tmp_req.business_codes):
            request.business_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.business_codes, 'BusinessCodes', 'json')
        if not DaraCore.is_null(tmp_req.case_codes_prefix):
            request.case_codes_prefix_shrink = Utils.array_to_string_with_specified_style(tmp_req.case_codes_prefix, 'CaseCodesPrefix', 'json')
        if not DaraCore.is_null(tmp_req.event_codes):
            request.event_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_codes, 'EventCodes', 'json')
        if not DaraCore.is_null(tmp_req.event_id_list):
            request.event_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_id_list, 'EventIdList', 'json')
        if not DaraCore.is_null(tmp_req.exclude_action_codes):
            request.exclude_action_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_action_codes, 'ExcludeActionCodes', 'json')
        if not DaraCore.is_null(tmp_req.exclude_event_codes):
            request.exclude_event_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_event_codes, 'ExcludeEventCodes', 'json')
        if not DaraCore.is_null(tmp_req.exclude_reasons):
            request.exclude_reasons_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_reasons, 'ExcludeReasons', 'json')
        if not DaraCore.is_null(tmp_req.include_reasons):
            request.include_reasons_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_reasons, 'IncludeReasons', 'json')
        if not DaraCore.is_null(tmp_req.source_codes):
            request.source_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_codes, 'SourceCodes', 'json')
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        query = {}
        if not DaraCore.is_null(request.action_code):
            query['ActionCode'] = request.action_code
        if not DaraCore.is_null(request.action_codes_shrink):
            query['ActionCodes'] = request.action_codes_shrink
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.business_code):
            query['BusinessCode'] = request.business_code
        if not DaraCore.is_null(request.business_codes_shrink):
            query['BusinessCodes'] = request.business_codes_shrink
        if not DaraCore.is_null(request.case_codes_prefix_shrink):
            query['CaseCodesPrefix'] = request.case_codes_prefix_shrink
        if not DaraCore.is_null(request.current):
            query['Current'] = request.current
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.event_code):
            query['EventCode'] = request.event_code
        if not DaraCore.is_null(request.event_codes_shrink):
            query['EventCodes'] = request.event_codes_shrink
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_id_list_shrink):
            query['EventIdList'] = request.event_id_list_shrink
        if not DaraCore.is_null(request.exclude_action_codes_shrink):
            query['ExcludeActionCodes'] = request.exclude_action_codes_shrink
        if not DaraCore.is_null(request.exclude_event_codes_shrink):
            query['ExcludeEventCodes'] = request.exclude_event_codes_shrink
        if not DaraCore.is_null(request.exclude_reasons_shrink):
            query['ExcludeReasons'] = request.exclude_reasons_shrink
        if not DaraCore.is_null(request.include_reasons_shrink):
            query['IncludeReasons'] = request.include_reasons_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.punish_end_time):
            query['PunishEndTime'] = request.punish_end_time
        if not DaraCore.is_null(request.punish_start_time):
            query['PunishStartTime'] = request.punish_start_time
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.source_codes_shrink):
            query['SourceCodes'] = request.source_codes_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResourceControlEvents',
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
            main_models.QueryResourceControlEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_resource_control_events(
        self,
        request: main_models.QueryResourceControlEventsRequest,
    ) -> main_models.QueryResourceControlEventsResponse:
        runtime = RuntimeOptions()
        return self.query_resource_control_events_with_options(request, runtime)

    async def query_resource_control_events_async(
        self,
        request: main_models.QueryResourceControlEventsRequest,
    ) -> main_models.QueryResourceControlEventsResponse:
        runtime = RuntimeOptions()
        return await self.query_resource_control_events_with_options_async(request, runtime)

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

    def start_security_check_service_with_options(
        self,
        request: main_models.StartSecurityCheckServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSecurityCheckServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'StartSecurityCheckService',
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
            main_models.StartSecurityCheckServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_security_check_service_with_options_async(
        self,
        request: main_models.StartSecurityCheckServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSecurityCheckServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'StartSecurityCheckService',
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
            main_models.StartSecurityCheckServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_security_check_service(
        self,
        request: main_models.StartSecurityCheckServiceRequest,
    ) -> main_models.StartSecurityCheckServiceResponse:
        runtime = RuntimeOptions()
        return self.start_security_check_service_with_options(request, runtime)

    async def start_security_check_service_async(
        self,
        request: main_models.StartSecurityCheckServiceRequest,
    ) -> main_models.StartSecurityCheckServiceResponse:
        runtime = RuntimeOptions()
        return await self.start_security_check_service_with_options_async(request, runtime)

    def submit_apply_record_with_options(
        self,
        tmp_req: main_models.SubmitApplyRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitApplyRecordResponse:
        tmp_req.validate()
        request = main_models.SubmitApplyRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_id_list):
            request.event_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_id_list, 'EventIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.apply_request):
            query['ApplyRequest'] = request.apply_request
        if not DaraCore.is_null(request.commitment_letter):
            query['CommitmentLetter'] = request.commitment_letter
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_id_list_shrink):
            query['EventIdList'] = request.event_id_list_shrink
        if not DaraCore.is_null(request.qualification_proof):
            query['QualificationProof'] = request.qualification_proof
        if not DaraCore.is_null(request.trial):
            query['Trial'] = request.trial
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitApplyRecord',
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
            main_models.SubmitApplyRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_apply_record_with_options_async(
        self,
        tmp_req: main_models.SubmitApplyRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitApplyRecordResponse:
        tmp_req.validate()
        request = main_models.SubmitApplyRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_id_list):
            request.event_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_id_list, 'EventIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.apply_request):
            query['ApplyRequest'] = request.apply_request
        if not DaraCore.is_null(request.commitment_letter):
            query['CommitmentLetter'] = request.commitment_letter
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_id_list_shrink):
            query['EventIdList'] = request.event_id_list_shrink
        if not DaraCore.is_null(request.qualification_proof):
            query['QualificationProof'] = request.qualification_proof
        if not DaraCore.is_null(request.trial):
            query['Trial'] = request.trial
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitApplyRecord',
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
            main_models.SubmitApplyRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_apply_record(
        self,
        request: main_models.SubmitApplyRecordRequest,
    ) -> main_models.SubmitApplyRecordResponse:
        runtime = RuntimeOptions()
        return self.submit_apply_record_with_options(request, runtime)

    async def submit_apply_record_async(
        self,
        request: main_models.SubmitApplyRecordRequest,
    ) -> main_models.SubmitApplyRecordResponse:
        runtime = RuntimeOptions()
        return await self.submit_apply_record_with_options_async(request, runtime)

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

    def update_security_check_result_with_options(
        self,
        request: main_models.UpdateSecurityCheckResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityCheckResultResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'UpdateSecurityCheckResult',
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
            main_models.UpdateSecurityCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_check_result_with_options_async(
        self,
        request: main_models.UpdateSecurityCheckResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityCheckResultResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'UpdateSecurityCheckResult',
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
            main_models.UpdateSecurityCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_check_result(
        self,
        request: main_models.UpdateSecurityCheckResultRequest,
    ) -> main_models.UpdateSecurityCheckResultResponse:
        runtime = RuntimeOptions()
        return self.update_security_check_result_with_options(request, runtime)

    async def update_security_check_result_async(
        self,
        request: main_models.UpdateSecurityCheckResultRequest,
    ) -> main_models.UpdateSecurityCheckResultResponse:
        runtime = RuntimeOptions()
        return await self.update_security_check_result_with_options_async(request, runtime)
