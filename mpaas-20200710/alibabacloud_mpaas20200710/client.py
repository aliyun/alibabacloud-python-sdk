# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_mpaas20200710 import models as main_models
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
            'cn-hangzhou': 'mpaas.aliyuncs.com',
            'ap-northeast-1': 'mpaas.aliyuncs.com',
            'ap-northeast-2-pop': 'mpaas.aliyuncs.com',
            'ap-south-1': 'mpaas.aliyuncs.com',
            'ap-southeast-1': 'mpaas.aliyuncs.com',
            'ap-southeast-2': 'mpaas.aliyuncs.com',
            'ap-southeast-3': 'mpaas.aliyuncs.com',
            'ap-southeast-5': 'mpaas.aliyuncs.com',
            'cn-beijing': 'mpaas.aliyuncs.com',
            'cn-beijing-finance-1': 'mpaas.aliyuncs.com',
            'cn-beijing-finance-pop': 'mpaas.aliyuncs.com',
            'cn-beijing-gov-1': 'mpaas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mpaas.aliyuncs.com',
            'cn-chengdu': 'mpaas.aliyuncs.com',
            'cn-edge-1': 'mpaas.aliyuncs.com',
            'cn-fujian': 'mpaas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mpaas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mpaas.aliyuncs.com',
            'cn-hangzhou-finance': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mpaas.aliyuncs.com',
            'cn-hangzhou-test-306': 'mpaas.aliyuncs.com',
            'cn-hongkong': 'mpaas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mpaas.aliyuncs.com',
            'cn-huhehaote': 'mpaas.aliyuncs.com',
            'cn-north-2-gov-1': 'mpaas.aliyuncs.com',
            'cn-qingdao': 'mpaas.aliyuncs.com',
            'cn-qingdao-nebula': 'mpaas.aliyuncs.com',
            'cn-shanghai': 'mpaas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mpaas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mpaas.aliyuncs.com',
            'cn-shanghai-finance-1': 'mpaas.aliyuncs.com',
            'cn-shanghai-inner': 'mpaas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mpaas.aliyuncs.com',
            'cn-shenzhen': 'mpaas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mpaas.aliyuncs.com',
            'cn-shenzhen-inner': 'mpaas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mpaas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mpaas.aliyuncs.com',
            'cn-wuhan': 'mpaas.aliyuncs.com',
            'cn-yushanfang': 'mpaas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mpaas.aliyuncs.com',
            'cn-zhangjiakou': 'mpaas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mpaas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mpaas.aliyuncs.com',
            'eu-central-1': 'mpaas.aliyuncs.com',
            'eu-west-1': 'mpaas.aliyuncs.com',
            'eu-west-1-oxs': 'mpaas.aliyuncs.com',
            'me-east-1': 'mpaas.aliyuncs.com',
            'rus-west-1-pop': 'mpaas.aliyuncs.com',
            'us-east-1': 'mpaas.aliyuncs.com',
            'us-west-1': 'mpaas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mpaas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_mps_scheduler_with_options(
        self,
        request: main_models.CancelMpsSchedulerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelMpsSchedulerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unique_ids):
            body['UniqueIds'] = request.unique_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelMpsScheduler',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelMpsSchedulerResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_mps_scheduler_with_options_async(
        self,
        request: main_models.CancelMpsSchedulerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelMpsSchedulerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unique_ids):
            body['UniqueIds'] = request.unique_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelMpsScheduler',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelMpsSchedulerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_mps_scheduler(
        self,
        request: main_models.CancelMpsSchedulerRequest,
    ) -> main_models.CancelMpsSchedulerResponse:
        runtime = RuntimeOptions()
        return self.cancel_mps_scheduler_with_options(request, runtime)

    async def cancel_mps_scheduler_async(
        self,
        request: main_models.CancelMpsSchedulerRequest,
    ) -> main_models.CancelMpsSchedulerResponse:
        runtime = RuntimeOptions()
        return await self.cancel_mps_scheduler_with_options_async(request, runtime)

    def cancel_push_scheduler_with_options(
        self,
        request: main_models.CancelPushSchedulerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPushSchedulerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unique_ids):
            body['UniqueIds'] = request.unique_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelPushScheduler',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPushSchedulerResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_push_scheduler_with_options_async(
        self,
        request: main_models.CancelPushSchedulerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPushSchedulerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unique_ids):
            body['UniqueIds'] = request.unique_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelPushScheduler',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPushSchedulerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_push_scheduler(
        self,
        request: main_models.CancelPushSchedulerRequest,
    ) -> main_models.CancelPushSchedulerResponse:
        runtime = RuntimeOptions()
        return self.cancel_push_scheduler_with_options(request, runtime)

    async def cancel_push_scheduler_async(
        self,
        request: main_models.CancelPushSchedulerRequest,
    ) -> main_models.CancelPushSchedulerResponse:
        runtime = RuntimeOptions()
        return await self.cancel_push_scheduler_with_options_async(request, runtime)

    def change_mcube_mini_task_status_with_options(
        self,
        request: main_models.ChangeMcubeMiniTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMcubeMiniTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMcubeMiniTaskStatus',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMcubeMiniTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_mcube_mini_task_status_with_options_async(
        self,
        request: main_models.ChangeMcubeMiniTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMcubeMiniTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMcubeMiniTaskStatus',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMcubeMiniTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_mcube_mini_task_status(
        self,
        request: main_models.ChangeMcubeMiniTaskStatusRequest,
    ) -> main_models.ChangeMcubeMiniTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.change_mcube_mini_task_status_with_options(request, runtime)

    async def change_mcube_mini_task_status_async(
        self,
        request: main_models.ChangeMcubeMiniTaskStatusRequest,
    ) -> main_models.ChangeMcubeMiniTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.change_mcube_mini_task_status_with_options_async(request, runtime)

    def change_mcube_nebula_task_status_with_options(
        self,
        request: main_models.ChangeMcubeNebulaTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMcubeNebulaTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMcubeNebulaTaskStatus',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMcubeNebulaTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_mcube_nebula_task_status_with_options_async(
        self,
        request: main_models.ChangeMcubeNebulaTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMcubeNebulaTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMcubeNebulaTaskStatus',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMcubeNebulaTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_mcube_nebula_task_status(
        self,
        request: main_models.ChangeMcubeNebulaTaskStatusRequest,
    ) -> main_models.ChangeMcubeNebulaTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.change_mcube_nebula_task_status_with_options(request, runtime)

    async def change_mcube_nebula_task_status_async(
        self,
        request: main_models.ChangeMcubeNebulaTaskStatusRequest,
    ) -> main_models.ChangeMcubeNebulaTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.change_mcube_nebula_task_status_with_options_async(request, runtime)

    def change_mcube_public_task_status_with_options(
        self,
        request: main_models.ChangeMcubePublicTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMcubePublicTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMcubePublicTaskStatus',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMcubePublicTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_mcube_public_task_status_with_options_async(
        self,
        request: main_models.ChangeMcubePublicTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMcubePublicTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMcubePublicTaskStatus',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMcubePublicTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_mcube_public_task_status(
        self,
        request: main_models.ChangeMcubePublicTaskStatusRequest,
    ) -> main_models.ChangeMcubePublicTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.change_mcube_public_task_status_with_options(request, runtime)

    async def change_mcube_public_task_status_async(
        self,
        request: main_models.ChangeMcubePublicTaskStatusRequest,
    ) -> main_models.ChangeMcubePublicTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.change_mcube_public_task_status_with_options_async(request, runtime)

    def create_mcube_mini_app_with_options(
        self,
        request: main_models.CreateMcubeMiniAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeMiniAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.h_5name):
            body['H5Name'] = request.h_5name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeMiniApp',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeMiniAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_mini_app_with_options_async(
        self,
        request: main_models.CreateMcubeMiniAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeMiniAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.h_5name):
            body['H5Name'] = request.h_5name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeMiniApp',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeMiniAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_mini_app(
        self,
        request: main_models.CreateMcubeMiniAppRequest,
    ) -> main_models.CreateMcubeMiniAppResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_mini_app_with_options(request, runtime)

    async def create_mcube_mini_app_async(
        self,
        request: main_models.CreateMcubeMiniAppRequest,
    ) -> main_models.CreateMcubeMiniAppResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_mini_app_with_options_async(request, runtime)

    def create_mcube_mini_task_with_options(
        self,
        request: main_models.CreateMcubeMiniTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeMiniTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not DaraCore.is_null(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not DaraCore.is_null(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not DaraCore.is_null(request.memo):
            body['Memo'] = request.memo
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeMiniTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeMiniTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_mini_task_with_options_async(
        self,
        request: main_models.CreateMcubeMiniTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeMiniTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not DaraCore.is_null(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not DaraCore.is_null(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not DaraCore.is_null(request.memo):
            body['Memo'] = request.memo
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeMiniTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeMiniTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_mini_task(
        self,
        request: main_models.CreateMcubeMiniTaskRequest,
    ) -> main_models.CreateMcubeMiniTaskResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_mini_task_with_options(request, runtime)

    async def create_mcube_mini_task_async(
        self,
        request: main_models.CreateMcubeMiniTaskRequest,
    ) -> main_models.CreateMcubeMiniTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_mini_task_with_options_async(request, runtime)

    def create_mcube_nebula_app_with_options(
        self,
        request: main_models.CreateMcubeNebulaAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeNebulaAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.h_5name):
            body['H5Name'] = request.h_5name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeNebulaApp',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeNebulaAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_nebula_app_with_options_async(
        self,
        request: main_models.CreateMcubeNebulaAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeNebulaAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.h_5name):
            body['H5Name'] = request.h_5name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeNebulaApp',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeNebulaAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_nebula_app(
        self,
        request: main_models.CreateMcubeNebulaAppRequest,
    ) -> main_models.CreateMcubeNebulaAppResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_nebula_app_with_options(request, runtime)

    async def create_mcube_nebula_app_async(
        self,
        request: main_models.CreateMcubeNebulaAppRequest,
    ) -> main_models.CreateMcubeNebulaAppResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_nebula_app_with_options_async(request, runtime)

    def create_mcube_nebula_resource_with_options(
        self,
        request: main_models.CreateMcubeNebulaResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeNebulaResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not DaraCore.is_null(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not DaraCore.is_null(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not DaraCore.is_null(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.h_5name):
            body['H5Name'] = request.h_5name
        if not DaraCore.is_null(request.h_5version):
            body['H5Version'] = request.h_5version
        if not DaraCore.is_null(request.install_type):
            body['InstallType'] = request.install_type
        if not DaraCore.is_null(request.main_url):
            body['MainUrl'] = request.main_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.repeat_nebula):
            body['RepeatNebula'] = request.repeat_nebula
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sub_url):
            body['SubUrl'] = request.sub_url
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.vhost):
            body['Vhost'] = request.vhost
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeNebulaResource',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeNebulaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_nebula_resource_with_options_async(
        self,
        request: main_models.CreateMcubeNebulaResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeNebulaResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not DaraCore.is_null(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not DaraCore.is_null(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not DaraCore.is_null(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.h_5name):
            body['H5Name'] = request.h_5name
        if not DaraCore.is_null(request.h_5version):
            body['H5Version'] = request.h_5version
        if not DaraCore.is_null(request.install_type):
            body['InstallType'] = request.install_type
        if not DaraCore.is_null(request.main_url):
            body['MainUrl'] = request.main_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.repeat_nebula):
            body['RepeatNebula'] = request.repeat_nebula
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sub_url):
            body['SubUrl'] = request.sub_url
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.vhost):
            body['Vhost'] = request.vhost
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeNebulaResource',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeNebulaResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_nebula_resource(
        self,
        request: main_models.CreateMcubeNebulaResourceRequest,
    ) -> main_models.CreateMcubeNebulaResourceResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_nebula_resource_with_options(request, runtime)

    async def create_mcube_nebula_resource_async(
        self,
        request: main_models.CreateMcubeNebulaResourceRequest,
    ) -> main_models.CreateMcubeNebulaResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_nebula_resource_with_options_async(request, runtime)

    def create_mcube_nebula_task_with_options(
        self,
        request: main_models.CreateMcubeNebulaTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeNebulaTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_code):
            body['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.creator):
            body['Creator'] = request.creator
        if not DaraCore.is_null(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.gmt_modified):
            body['GmtModified'] = request.gmt_modified
        if not DaraCore.is_null(request.gmt_modified_str):
            body['GmtModifiedStr'] = request.gmt_modified_str
        if not DaraCore.is_null(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not DaraCore.is_null(request.grey_endtime):
            body['GreyEndtime'] = request.grey_endtime
        if not DaraCore.is_null(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not DaraCore.is_null(request.grey_endtime_str):
            body['GreyEndtimeStr'] = request.grey_endtime_str
        if not DaraCore.is_null(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not DaraCore.is_null(request.grey_url):
            body['GreyUrl'] = request.grey_url
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.memo):
            body['Memo'] = request.memo
        if not DaraCore.is_null(request.modifier):
            body['Modifier'] = request.modifier
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.percent):
            body['Percent'] = request.percent
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version):
            body['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.res_ids):
            body['ResIds'] = request.res_ids
        if not DaraCore.is_null(request.serial_version_uid):
            body['SerialVersionUID'] = request.serial_version_uid
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.sync_mode):
            body['SyncMode'] = request.sync_mode
        if not DaraCore.is_null(request.sync_result):
            body['SyncResult'] = request.sync_result
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.task_version):
            body['TaskVersion'] = request.task_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.upgrade_notice_num):
            body['UpgradeNoticeNum'] = request.upgrade_notice_num
        if not DaraCore.is_null(request.upgrade_progress):
            body['UpgradeProgress'] = request.upgrade_progress
        if not DaraCore.is_null(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeNebulaTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeNebulaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_nebula_task_with_options_async(
        self,
        request: main_models.CreateMcubeNebulaTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeNebulaTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_code):
            body['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.creator):
            body['Creator'] = request.creator
        if not DaraCore.is_null(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.gmt_modified):
            body['GmtModified'] = request.gmt_modified
        if not DaraCore.is_null(request.gmt_modified_str):
            body['GmtModifiedStr'] = request.gmt_modified_str
        if not DaraCore.is_null(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not DaraCore.is_null(request.grey_endtime):
            body['GreyEndtime'] = request.grey_endtime
        if not DaraCore.is_null(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not DaraCore.is_null(request.grey_endtime_str):
            body['GreyEndtimeStr'] = request.grey_endtime_str
        if not DaraCore.is_null(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not DaraCore.is_null(request.grey_url):
            body['GreyUrl'] = request.grey_url
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.memo):
            body['Memo'] = request.memo
        if not DaraCore.is_null(request.modifier):
            body['Modifier'] = request.modifier
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.percent):
            body['Percent'] = request.percent
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version):
            body['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.res_ids):
            body['ResIds'] = request.res_ids
        if not DaraCore.is_null(request.serial_version_uid):
            body['SerialVersionUID'] = request.serial_version_uid
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.sync_mode):
            body['SyncMode'] = request.sync_mode
        if not DaraCore.is_null(request.sync_result):
            body['SyncResult'] = request.sync_result
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.task_version):
            body['TaskVersion'] = request.task_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.upgrade_notice_num):
            body['UpgradeNoticeNum'] = request.upgrade_notice_num
        if not DaraCore.is_null(request.upgrade_progress):
            body['UpgradeProgress'] = request.upgrade_progress
        if not DaraCore.is_null(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeNebulaTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeNebulaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_nebula_task(
        self,
        request: main_models.CreateMcubeNebulaTaskRequest,
    ) -> main_models.CreateMcubeNebulaTaskResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_nebula_task_with_options(request, runtime)

    async def create_mcube_nebula_task_async(
        self,
        request: main_models.CreateMcubeNebulaTaskRequest,
    ) -> main_models.CreateMcubeNebulaTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_nebula_task_with_options_async(request, runtime)

    def create_mcube_upgrade_package_with_options(
        self,
        request: main_models.CreateMcubeUpgradePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeUpgradePackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.appstore_url):
            body['AppstoreUrl'] = request.appstore_url
        if not DaraCore.is_null(request.bundle_id):
            body['BundleId'] = request.bundle_id
        if not DaraCore.is_null(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not DaraCore.is_null(request.desc):
            body['Desc'] = request.desc
        if not DaraCore.is_null(request.download_url):
            body['DownloadUrl'] = request.download_url
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not DaraCore.is_null(request.install_amount):
            body['InstallAmount'] = request.install_amount
        if not DaraCore.is_null(request.ios_symbolfile_url):
            body['IosSymbolfileUrl'] = request.ios_symbolfile_url
        if not DaraCore.is_null(request.is_enterprise):
            body['IsEnterprise'] = request.is_enterprise
        if not DaraCore.is_null(request.need_check):
            body['NeedCheck'] = request.need_check
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.valid_days):
            body['ValidDays'] = request.valid_days
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeUpgradePackage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeUpgradePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_upgrade_package_with_options_async(
        self,
        request: main_models.CreateMcubeUpgradePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeUpgradePackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.appstore_url):
            body['AppstoreUrl'] = request.appstore_url
        if not DaraCore.is_null(request.bundle_id):
            body['BundleId'] = request.bundle_id
        if not DaraCore.is_null(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not DaraCore.is_null(request.desc):
            body['Desc'] = request.desc
        if not DaraCore.is_null(request.download_url):
            body['DownloadUrl'] = request.download_url
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not DaraCore.is_null(request.install_amount):
            body['InstallAmount'] = request.install_amount
        if not DaraCore.is_null(request.ios_symbolfile_url):
            body['IosSymbolfileUrl'] = request.ios_symbolfile_url
        if not DaraCore.is_null(request.is_enterprise):
            body['IsEnterprise'] = request.is_enterprise
        if not DaraCore.is_null(request.need_check):
            body['NeedCheck'] = request.need_check
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.valid_days):
            body['ValidDays'] = request.valid_days
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeUpgradePackage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeUpgradePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_upgrade_package(
        self,
        request: main_models.CreateMcubeUpgradePackageRequest,
    ) -> main_models.CreateMcubeUpgradePackageResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_upgrade_package_with_options(request, runtime)

    async def create_mcube_upgrade_package_async(
        self,
        request: main_models.CreateMcubeUpgradePackageRequest,
    ) -> main_models.CreateMcubeUpgradePackageResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_upgrade_package_with_options_async(request, runtime)

    def create_mcube_upgrade_task_with_options(
        self,
        request: main_models.CreateMcubeUpgradeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeUpgradeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not DaraCore.is_null(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not DaraCore.is_null(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not DaraCore.is_null(request.history_force):
            body['HistoryForce'] = request.history_force
        if not DaraCore.is_null(request.memo):
            body['Memo'] = request.memo
        if not DaraCore.is_null(request.package_info_id):
            body['PackageInfoId'] = request.package_info_id
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.upgrade_content):
            body['UpgradeContent'] = request.upgrade_content
        if not DaraCore.is_null(request.upgrade_type):
            body['UpgradeType'] = request.upgrade_type
        if not DaraCore.is_null(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeUpgradeTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeUpgradeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_upgrade_task_with_options_async(
        self,
        request: main_models.CreateMcubeUpgradeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeUpgradeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not DaraCore.is_null(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not DaraCore.is_null(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not DaraCore.is_null(request.history_force):
            body['HistoryForce'] = request.history_force
        if not DaraCore.is_null(request.memo):
            body['Memo'] = request.memo
        if not DaraCore.is_null(request.package_info_id):
            body['PackageInfoId'] = request.package_info_id
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.upgrade_content):
            body['UpgradeContent'] = request.upgrade_content
        if not DaraCore.is_null(request.upgrade_type):
            body['UpgradeType'] = request.upgrade_type
        if not DaraCore.is_null(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeUpgradeTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeUpgradeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_upgrade_task(
        self,
        request: main_models.CreateMcubeUpgradeTaskRequest,
    ) -> main_models.CreateMcubeUpgradeTaskResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_upgrade_task_with_options(request, runtime)

    async def create_mcube_upgrade_task_async(
        self,
        request: main_models.CreateMcubeUpgradeTaskRequest,
    ) -> main_models.CreateMcubeUpgradeTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_upgrade_task_with_options_async(request, runtime)

    def create_mcube_vhost_with_options(
        self,
        request: main_models.CreateMcubeVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeVhostResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.vhost):
            body['Vhost'] = request.vhost
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeVhost',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_vhost_with_options_async(
        self,
        request: main_models.CreateMcubeVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeVhostResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.vhost):
            body['Vhost'] = request.vhost
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeVhost',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_vhost(
        self,
        request: main_models.CreateMcubeVhostRequest,
    ) -> main_models.CreateMcubeVhostResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_vhost_with_options(request, runtime)

    async def create_mcube_vhost_async(
        self,
        request: main_models.CreateMcubeVhostRequest,
    ) -> main_models.CreateMcubeVhostResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_vhost_with_options_async(request, runtime)

    def create_mcube_whitelist_with_options(
        self,
        request: main_models.CreateMcubeWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeWhitelistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.white_list_name):
            body['WhiteListName'] = request.white_list_name
        if not DaraCore.is_null(request.whitelist_type):
            body['WhitelistType'] = request.whitelist_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeWhitelist',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_whitelist_with_options_async(
        self,
        request: main_models.CreateMcubeWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeWhitelistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.white_list_name):
            body['WhiteListName'] = request.white_list_name
        if not DaraCore.is_null(request.whitelist_type):
            body['WhitelistType'] = request.whitelist_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeWhitelist',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_whitelist(
        self,
        request: main_models.CreateMcubeWhitelistRequest,
    ) -> main_models.CreateMcubeWhitelistResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_whitelist_with_options(request, runtime)

    async def create_mcube_whitelist_async(
        self,
        request: main_models.CreateMcubeWhitelistRequest,
    ) -> main_models.CreateMcubeWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_whitelist_with_options_async(request, runtime)

    def create_mcube_whitelist_for_ide_with_options(
        self,
        request: main_models.CreateMcubeWhitelistForIdeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeWhitelistForIdeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeWhitelistForIde',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeWhitelistForIdeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_whitelist_for_ide_with_options_async(
        self,
        request: main_models.CreateMcubeWhitelistForIdeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeWhitelistForIdeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeWhitelistForIde',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeWhitelistForIdeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_whitelist_for_ide(
        self,
        request: main_models.CreateMcubeWhitelistForIdeRequest,
    ) -> main_models.CreateMcubeWhitelistForIdeResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_whitelist_for_ide_with_options(request, runtime)

    async def create_mcube_whitelist_for_ide_async(
        self,
        request: main_models.CreateMcubeWhitelistForIdeRequest,
    ) -> main_models.CreateMcubeWhitelistForIdeResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_whitelist_for_ide_with_options_async(request, runtime)

    def create_open_global_data_with_options(
        self,
        request: main_models.CreateOpenGlobalDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOpenGlobalDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not DaraCore.is_null(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not DaraCore.is_null(request.max_uid):
            body['MaxUid'] = request.max_uid
        if not DaraCore.is_null(request.min_uid):
            body['MinUid'] = request.min_uid
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not DaraCore.is_null(request.uids):
            body['Uids'] = request.uids
        if not DaraCore.is_null(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not DaraCore.is_null(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOpenGlobalData',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOpenGlobalDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_open_global_data_with_options_async(
        self,
        request: main_models.CreateOpenGlobalDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOpenGlobalDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not DaraCore.is_null(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not DaraCore.is_null(request.max_uid):
            body['MaxUid'] = request.max_uid
        if not DaraCore.is_null(request.min_uid):
            body['MinUid'] = request.min_uid
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not DaraCore.is_null(request.uids):
            body['Uids'] = request.uids
        if not DaraCore.is_null(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not DaraCore.is_null(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOpenGlobalData',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOpenGlobalDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_open_global_data(
        self,
        request: main_models.CreateOpenGlobalDataRequest,
    ) -> main_models.CreateOpenGlobalDataResponse:
        runtime = RuntimeOptions()
        return self.create_open_global_data_with_options(request, runtime)

    async def create_open_global_data_async(
        self,
        request: main_models.CreateOpenGlobalDataRequest,
    ) -> main_models.CreateOpenGlobalDataResponse:
        runtime = RuntimeOptions()
        return await self.create_open_global_data_with_options_async(request, runtime)

    def create_open_single_data_with_options(
        self,
        request: main_models.CreateOpenSingleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOpenSingleDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not DaraCore.is_null(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.check_online):
            body['CheckOnline'] = request.check_online
        if not DaraCore.is_null(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not DaraCore.is_null(request.link_token):
            body['LinkToken'] = request.link_token
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not DaraCore.is_null(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not DaraCore.is_null(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOpenSingleData',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOpenSingleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_open_single_data_with_options_async(
        self,
        request: main_models.CreateOpenSingleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOpenSingleDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not DaraCore.is_null(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.check_online):
            body['CheckOnline'] = request.check_online
        if not DaraCore.is_null(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not DaraCore.is_null(request.link_token):
            body['LinkToken'] = request.link_token
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not DaraCore.is_null(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not DaraCore.is_null(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOpenSingleData',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOpenSingleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_open_single_data(
        self,
        request: main_models.CreateOpenSingleDataRequest,
    ) -> main_models.CreateOpenSingleDataResponse:
        runtime = RuntimeOptions()
        return self.create_open_single_data_with_options(request, runtime)

    async def create_open_single_data_async(
        self,
        request: main_models.CreateOpenSingleDataRequest,
    ) -> main_models.CreateOpenSingleDataResponse:
        runtime = RuntimeOptions()
        return await self.create_open_single_data_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.desc_info):
            body['DescInfo'] = request.desc_info
        if not DaraCore.is_null(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not DaraCore.is_null(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not DaraCore.is_null(request.jump_action):
            body['JumpAction'] = request.jump_action
        if not DaraCore.is_null(request.push_style):
            body['PushStyle'] = request.push_style
        if not DaraCore.is_null(request.show_style):
            body['ShowStyle'] = request.show_style
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.variables):
            body['Variables'] = request.variables
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.desc_info):
            body['DescInfo'] = request.desc_info
        if not DaraCore.is_null(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not DaraCore.is_null(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not DaraCore.is_null(request.jump_action):
            body['JumpAction'] = request.jump_action
        if not DaraCore.is_null(request.push_style):
            body['PushStyle'] = request.push_style
        if not DaraCore.is_null(request.show_style):
            body['ShowStyle'] = request.show_style
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.variables):
            body['Variables'] = request.variables
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_cubecard_whitelist_content_with_options(
        self,
        request: main_models.DeleteCubecardWhitelistContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCubecardWhitelistContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not DaraCore.is_null(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCubecardWhitelistContent',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCubecardWhitelistContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cubecard_whitelist_content_with_options_async(
        self,
        request: main_models.DeleteCubecardWhitelistContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCubecardWhitelistContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not DaraCore.is_null(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCubecardWhitelistContent',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCubecardWhitelistContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cubecard_whitelist_content(
        self,
        request: main_models.DeleteCubecardWhitelistContentRequest,
    ) -> main_models.DeleteCubecardWhitelistContentResponse:
        runtime = RuntimeOptions()
        return self.delete_cubecard_whitelist_content_with_options(request, runtime)

    async def delete_cubecard_whitelist_content_async(
        self,
        request: main_models.DeleteCubecardWhitelistContentRequest,
    ) -> main_models.DeleteCubecardWhitelistContentResponse:
        runtime = RuntimeOptions()
        return await self.delete_cubecard_whitelist_content_with_options_async(request, runtime)

    def delete_mcube_mini_app_with_options(
        self,
        request: main_models.DeleteMcubeMiniAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeMiniAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcubeMiniApp',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeMiniAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_mini_app_with_options_async(
        self,
        request: main_models.DeleteMcubeMiniAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeMiniAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcubeMiniApp',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeMiniAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_mini_app(
        self,
        request: main_models.DeleteMcubeMiniAppRequest,
    ) -> main_models.DeleteMcubeMiniAppResponse:
        runtime = RuntimeOptions()
        return self.delete_mcube_mini_app_with_options(request, runtime)

    async def delete_mcube_mini_app_async(
        self,
        request: main_models.DeleteMcubeMiniAppRequest,
    ) -> main_models.DeleteMcubeMiniAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcube_mini_app_with_options_async(request, runtime)

    def delete_mcube_nebula_app_with_options(
        self,
        request: main_models.DeleteMcubeNebulaAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeNebulaAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcubeNebulaApp',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeNebulaAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_nebula_app_with_options_async(
        self,
        request: main_models.DeleteMcubeNebulaAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeNebulaAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcubeNebulaApp',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeNebulaAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_nebula_app(
        self,
        request: main_models.DeleteMcubeNebulaAppRequest,
    ) -> main_models.DeleteMcubeNebulaAppResponse:
        runtime = RuntimeOptions()
        return self.delete_mcube_nebula_app_with_options(request, runtime)

    async def delete_mcube_nebula_app_async(
        self,
        request: main_models.DeleteMcubeNebulaAppRequest,
    ) -> main_models.DeleteMcubeNebulaAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcube_nebula_app_with_options_async(request, runtime)

    def delete_mcube_upgrade_resource_with_options(
        self,
        request: main_models.DeleteMcubeUpgradeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeUpgradeResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcubeUpgradeResource',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeUpgradeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_upgrade_resource_with_options_async(
        self,
        request: main_models.DeleteMcubeUpgradeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeUpgradeResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcubeUpgradeResource',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeUpgradeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_upgrade_resource(
        self,
        request: main_models.DeleteMcubeUpgradeResourceRequest,
    ) -> main_models.DeleteMcubeUpgradeResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_mcube_upgrade_resource_with_options(request, runtime)

    async def delete_mcube_upgrade_resource_async(
        self,
        request: main_models.DeleteMcubeUpgradeResourceRequest,
    ) -> main_models.DeleteMcubeUpgradeResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcube_upgrade_resource_with_options_async(request, runtime)

    def delete_mcube_whitelist_with_options(
        self,
        request: main_models.DeleteMcubeWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeWhitelistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcubeWhitelist',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_whitelist_with_options_async(
        self,
        request: main_models.DeleteMcubeWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeWhitelistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcubeWhitelist',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_whitelist(
        self,
        request: main_models.DeleteMcubeWhitelistRequest,
    ) -> main_models.DeleteMcubeWhitelistResponse:
        runtime = RuntimeOptions()
        return self.delete_mcube_whitelist_with_options(request, runtime)

    async def delete_mcube_whitelist_async(
        self,
        request: main_models.DeleteMcubeWhitelistRequest,
    ) -> main_models.DeleteMcubeWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcube_whitelist_with_options_async(request, runtime)

    def delete_mds_whitelist_content_with_options(
        self,
        request: main_models.DeleteMdsWhitelistContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMdsWhitelistContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not DaraCore.is_null(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMdsWhitelistContent',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMdsWhitelistContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mds_whitelist_content_with_options_async(
        self,
        request: main_models.DeleteMdsWhitelistContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMdsWhitelistContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not DaraCore.is_null(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMdsWhitelistContent',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMdsWhitelistContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mds_whitelist_content(
        self,
        request: main_models.DeleteMdsWhitelistContentRequest,
    ) -> main_models.DeleteMdsWhitelistContentResponse:
        runtime = RuntimeOptions()
        return self.delete_mds_whitelist_content_with_options(request, runtime)

    async def delete_mds_whitelist_content_async(
        self,
        request: main_models.DeleteMdsWhitelistContentRequest,
    ) -> main_models.DeleteMdsWhitelistContentResponse:
        runtime = RuntimeOptions()
        return await self.delete_mds_whitelist_content_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def exist_mcube_rsa_key_with_options(
        self,
        request: main_models.ExistMcubeRsaKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExistMcubeRsaKeyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExistMcubeRsaKey',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExistMcubeRsaKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def exist_mcube_rsa_key_with_options_async(
        self,
        request: main_models.ExistMcubeRsaKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExistMcubeRsaKeyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExistMcubeRsaKey',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExistMcubeRsaKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exist_mcube_rsa_key(
        self,
        request: main_models.ExistMcubeRsaKeyRequest,
    ) -> main_models.ExistMcubeRsaKeyResponse:
        runtime = RuntimeOptions()
        return self.exist_mcube_rsa_key_with_options(request, runtime)

    async def exist_mcube_rsa_key_async(
        self,
        request: main_models.ExistMcubeRsaKeyRequest,
    ) -> main_models.ExistMcubeRsaKeyResponse:
        runtime = RuntimeOptions()
        return await self.exist_mcube_rsa_key_with_options_async(request, runtime)

    def get_mcube_file_token_with_options(
        self,
        request: main_models.GetMcubeFileTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeFileTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeFileToken',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeFileTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_file_token_with_options_async(
        self,
        request: main_models.GetMcubeFileTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeFileTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeFileToken',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeFileTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_file_token(
        self,
        request: main_models.GetMcubeFileTokenRequest,
    ) -> main_models.GetMcubeFileTokenResponse:
        runtime = RuntimeOptions()
        return self.get_mcube_file_token_with_options(request, runtime)

    async def get_mcube_file_token_async(
        self,
        request: main_models.GetMcubeFileTokenRequest,
    ) -> main_models.GetMcubeFileTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_mcube_file_token_with_options_async(request, runtime)

    def get_mcube_nebula_resource_with_options(
        self,
        request: main_models.GetMcubeNebulaResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeNebulaResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeNebulaResource',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeNebulaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_nebula_resource_with_options_async(
        self,
        request: main_models.GetMcubeNebulaResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeNebulaResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeNebulaResource',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeNebulaResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_nebula_resource(
        self,
        request: main_models.GetMcubeNebulaResourceRequest,
    ) -> main_models.GetMcubeNebulaResourceResponse:
        runtime = RuntimeOptions()
        return self.get_mcube_nebula_resource_with_options(request, runtime)

    async def get_mcube_nebula_resource_async(
        self,
        request: main_models.GetMcubeNebulaResourceRequest,
    ) -> main_models.GetMcubeNebulaResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_mcube_nebula_resource_with_options_async(request, runtime)

    def get_mcube_nebula_task_detail_with_options(
        self,
        request: main_models.GetMcubeNebulaTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeNebulaTaskDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeNebulaTaskDetail',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeNebulaTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_nebula_task_detail_with_options_async(
        self,
        request: main_models.GetMcubeNebulaTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeNebulaTaskDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeNebulaTaskDetail',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeNebulaTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_nebula_task_detail(
        self,
        request: main_models.GetMcubeNebulaTaskDetailRequest,
    ) -> main_models.GetMcubeNebulaTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.get_mcube_nebula_task_detail_with_options(request, runtime)

    async def get_mcube_nebula_task_detail_async(
        self,
        request: main_models.GetMcubeNebulaTaskDetailRequest,
    ) -> main_models.GetMcubeNebulaTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_mcube_nebula_task_detail_with_options_async(request, runtime)

    def get_mcube_upgrade_package_info_with_options(
        self,
        request: main_models.GetMcubeUpgradePackageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeUpgradePackageInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeUpgradePackageInfo',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeUpgradePackageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_upgrade_package_info_with_options_async(
        self,
        request: main_models.GetMcubeUpgradePackageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeUpgradePackageInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeUpgradePackageInfo',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeUpgradePackageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_upgrade_package_info(
        self,
        request: main_models.GetMcubeUpgradePackageInfoRequest,
    ) -> main_models.GetMcubeUpgradePackageInfoResponse:
        runtime = RuntimeOptions()
        return self.get_mcube_upgrade_package_info_with_options(request, runtime)

    async def get_mcube_upgrade_package_info_async(
        self,
        request: main_models.GetMcubeUpgradePackageInfoRequest,
    ) -> main_models.GetMcubeUpgradePackageInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_mcube_upgrade_package_info_with_options_async(request, runtime)

    def get_mcube_upgrade_task_info_with_options(
        self,
        request: main_models.GetMcubeUpgradeTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeUpgradeTaskInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeUpgradeTaskInfo',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeUpgradeTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_upgrade_task_info_with_options_async(
        self,
        request: main_models.GetMcubeUpgradeTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMcubeUpgradeTaskInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMcubeUpgradeTaskInfo',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcubeUpgradeTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_upgrade_task_info(
        self,
        request: main_models.GetMcubeUpgradeTaskInfoRequest,
    ) -> main_models.GetMcubeUpgradeTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.get_mcube_upgrade_task_info_with_options(request, runtime)

    async def get_mcube_upgrade_task_info_async(
        self,
        request: main_models.GetMcubeUpgradeTaskInfoRequest,
    ) -> main_models.GetMcubeUpgradeTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_mcube_upgrade_task_info_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: main_models.GetTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: main_models.GetTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def list_analysis_core_index_with_options(
        self,
        request: main_models.ListAnalysisCoreIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnalysisCoreIndexResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAnalysisCoreIndex',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnalysisCoreIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_analysis_core_index_with_options_async(
        self,
        request: main_models.ListAnalysisCoreIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnalysisCoreIndexResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAnalysisCoreIndex',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnalysisCoreIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_analysis_core_index(
        self,
        request: main_models.ListAnalysisCoreIndexRequest,
    ) -> main_models.ListAnalysisCoreIndexResponse:
        runtime = RuntimeOptions()
        return self.list_analysis_core_index_with_options(request, runtime)

    async def list_analysis_core_index_async(
        self,
        request: main_models.ListAnalysisCoreIndexRequest,
    ) -> main_models.ListAnalysisCoreIndexResponse:
        runtime = RuntimeOptions()
        return await self.list_analysis_core_index_with_options_async(request, runtime)

    def list_mcube_mini_apps_with_options(
        self,
        request: main_models.ListMcubeMiniAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeMiniAppsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeMiniApps',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeMiniAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_mini_apps_with_options_async(
        self,
        request: main_models.ListMcubeMiniAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeMiniAppsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeMiniApps',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeMiniAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_mini_apps(
        self,
        request: main_models.ListMcubeMiniAppsRequest,
    ) -> main_models.ListMcubeMiniAppsResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_mini_apps_with_options(request, runtime)

    async def list_mcube_mini_apps_async(
        self,
        request: main_models.ListMcubeMiniAppsRequest,
    ) -> main_models.ListMcubeMiniAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_mini_apps_with_options_async(request, runtime)

    def list_mcube_mini_packages_with_options(
        self,
        request: main_models.ListMcubeMiniPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeMiniPackagesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.package_types):
            body['PackageTypes'] = request.package_types
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeMiniPackages',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeMiniPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_mini_packages_with_options_async(
        self,
        request: main_models.ListMcubeMiniPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeMiniPackagesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.package_types):
            body['PackageTypes'] = request.package_types
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeMiniPackages',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeMiniPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_mini_packages(
        self,
        request: main_models.ListMcubeMiniPackagesRequest,
    ) -> main_models.ListMcubeMiniPackagesResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_mini_packages_with_options(request, runtime)

    async def list_mcube_mini_packages_async(
        self,
        request: main_models.ListMcubeMiniPackagesRequest,
    ) -> main_models.ListMcubeMiniPackagesResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_mini_packages_with_options_async(request, runtime)

    def list_mcube_mini_tasks_with_options(
        self,
        request: main_models.ListMcubeMiniTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeMiniTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeMiniTasks',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeMiniTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_mini_tasks_with_options_async(
        self,
        request: main_models.ListMcubeMiniTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeMiniTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeMiniTasks',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeMiniTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_mini_tasks(
        self,
        request: main_models.ListMcubeMiniTasksRequest,
    ) -> main_models.ListMcubeMiniTasksResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_mini_tasks_with_options(request, runtime)

    async def list_mcube_mini_tasks_async(
        self,
        request: main_models.ListMcubeMiniTasksRequest,
    ) -> main_models.ListMcubeMiniTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_mini_tasks_with_options_async(request, runtime)

    def list_mcube_nebula_apps_with_options(
        self,
        request: main_models.ListMcubeNebulaAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeNebulaAppsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeNebulaApps',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeNebulaAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_nebula_apps_with_options_async(
        self,
        request: main_models.ListMcubeNebulaAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeNebulaAppsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeNebulaApps',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeNebulaAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_nebula_apps(
        self,
        request: main_models.ListMcubeNebulaAppsRequest,
    ) -> main_models.ListMcubeNebulaAppsResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_nebula_apps_with_options(request, runtime)

    async def list_mcube_nebula_apps_async(
        self,
        request: main_models.ListMcubeNebulaAppsRequest,
    ) -> main_models.ListMcubeNebulaAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_nebula_apps_with_options_async(request, runtime)

    def list_mcube_nebula_resources_with_options(
        self,
        request: main_models.ListMcubeNebulaResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeNebulaResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeNebulaResources',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeNebulaResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_nebula_resources_with_options_async(
        self,
        request: main_models.ListMcubeNebulaResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeNebulaResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeNebulaResources',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeNebulaResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_nebula_resources(
        self,
        request: main_models.ListMcubeNebulaResourcesRequest,
    ) -> main_models.ListMcubeNebulaResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_nebula_resources_with_options(request, runtime)

    async def list_mcube_nebula_resources_async(
        self,
        request: main_models.ListMcubeNebulaResourcesRequest,
    ) -> main_models.ListMcubeNebulaResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_nebula_resources_with_options_async(request, runtime)

    def list_mcube_nebula_tasks_with_options(
        self,
        request: main_models.ListMcubeNebulaTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeNebulaTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeNebulaTasks',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeNebulaTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_nebula_tasks_with_options_async(
        self,
        request: main_models.ListMcubeNebulaTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeNebulaTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeNebulaTasks',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeNebulaTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_nebula_tasks(
        self,
        request: main_models.ListMcubeNebulaTasksRequest,
    ) -> main_models.ListMcubeNebulaTasksResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_nebula_tasks_with_options(request, runtime)

    async def list_mcube_nebula_tasks_async(
        self,
        request: main_models.ListMcubeNebulaTasksRequest,
    ) -> main_models.ListMcubeNebulaTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_nebula_tasks_with_options_async(request, runtime)

    def list_mcube_upgrade_packages_with_options(
        self,
        request: main_models.ListMcubeUpgradePackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeUpgradePackagesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeUpgradePackages',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeUpgradePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_upgrade_packages_with_options_async(
        self,
        request: main_models.ListMcubeUpgradePackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeUpgradePackagesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeUpgradePackages',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeUpgradePackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_upgrade_packages(
        self,
        request: main_models.ListMcubeUpgradePackagesRequest,
    ) -> main_models.ListMcubeUpgradePackagesResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_upgrade_packages_with_options(request, runtime)

    async def list_mcube_upgrade_packages_async(
        self,
        request: main_models.ListMcubeUpgradePackagesRequest,
    ) -> main_models.ListMcubeUpgradePackagesResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_upgrade_packages_with_options_async(request, runtime)

    def list_mcube_upgrade_tasks_with_options(
        self,
        request: main_models.ListMcubeUpgradeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeUpgradeTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeUpgradeTasks',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeUpgradeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_upgrade_tasks_with_options_async(
        self,
        request: main_models.ListMcubeUpgradeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeUpgradeTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeUpgradeTasks',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeUpgradeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_upgrade_tasks(
        self,
        request: main_models.ListMcubeUpgradeTasksRequest,
    ) -> main_models.ListMcubeUpgradeTasksResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_upgrade_tasks_with_options(request, runtime)

    async def list_mcube_upgrade_tasks_async(
        self,
        request: main_models.ListMcubeUpgradeTasksRequest,
    ) -> main_models.ListMcubeUpgradeTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_upgrade_tasks_with_options_async(request, runtime)

    def list_mcube_whitelists_with_options(
        self,
        request: main_models.ListMcubeWhitelistsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeWhitelistsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.whitelist_name):
            body['WhitelistName'] = request.whitelist_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeWhitelists',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeWhitelistsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_whitelists_with_options_async(
        self,
        request: main_models.ListMcubeWhitelistsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeWhitelistsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.whitelist_name):
            body['WhitelistName'] = request.whitelist_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMcubeWhitelists',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeWhitelistsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_whitelists(
        self,
        request: main_models.ListMcubeWhitelistsRequest,
    ) -> main_models.ListMcubeWhitelistsResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_whitelists_with_options(request, runtime)

    async def list_mcube_whitelists_async(
        self,
        request: main_models.ListMcubeWhitelistsRequest,
    ) -> main_models.ListMcubeWhitelistsResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_whitelists_with_options_async(request, runtime)

    def list_template_page_with_options(
        self,
        request: main_models.ListTemplatePageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatePageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplatePage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_page_with_options_async(
        self,
        request: main_models.ListTemplatePageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatePageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplatePage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_page(
        self,
        request: main_models.ListTemplatePageRequest,
    ) -> main_models.ListTemplatePageResponse:
        runtime = RuntimeOptions()
        return self.list_template_page_with_options(request, runtime)

    async def list_template_page_async(
        self,
        request: main_models.ListTemplatePageRequest,
    ) -> main_models.ListTemplatePageResponse:
        runtime = RuntimeOptions()
        return await self.list_template_page_with_options_async(request, runtime)

    def push_broadcast_with_options(
        self,
        tmp_req: main_models.PushBroadcastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushBroadcastResponse:
        tmp_req.validate()
        request = main_models.PushBroadcastShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notify_level):
            request.notify_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not DaraCore.is_null(tmp_req.third_channel_category):
            request.third_channel_category_shrink = Utils.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not DaraCore.is_null(request.android_channel):
            body['AndroidChannel'] = request.android_channel
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.bind_end_time):
            body['BindEndTime'] = request.bind_end_time
        if not DaraCore.is_null(request.bind_start_time):
            body['BindStartTime'] = request.bind_start_time
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.classification):
            body['Classification'] = request.classification
        if not DaraCore.is_null(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not DaraCore.is_null(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not DaraCore.is_null(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not DaraCore.is_null(request.msgkey):
            body['Msgkey'] = request.msgkey
        if not DaraCore.is_null(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.push_action):
            body['PushAction'] = request.push_action
        if not DaraCore.is_null(request.push_status):
            body['PushStatus'] = request.push_status
        if not DaraCore.is_null(request.silent):
            body['Silent'] = request.silent
        if not DaraCore.is_null(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not DaraCore.is_null(request.time_mode):
            body['TimeMode'] = request.time_mode
        if not DaraCore.is_null(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not DaraCore.is_null(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not DaraCore.is_null(request.un_bind_end_time):
            body['UnBindEndTime'] = request.un_bind_end_time
        if not DaraCore.is_null(request.un_bind_period):
            body['UnBindPeriod'] = request.un_bind_period
        if not DaraCore.is_null(request.un_bind_start_time):
            body['UnBindStartTime'] = request.un_bind_start_time
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushBroadcast',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushBroadcastResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_broadcast_with_options_async(
        self,
        tmp_req: main_models.PushBroadcastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushBroadcastResponse:
        tmp_req.validate()
        request = main_models.PushBroadcastShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notify_level):
            request.notify_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not DaraCore.is_null(tmp_req.third_channel_category):
            request.third_channel_category_shrink = Utils.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not DaraCore.is_null(request.android_channel):
            body['AndroidChannel'] = request.android_channel
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.bind_end_time):
            body['BindEndTime'] = request.bind_end_time
        if not DaraCore.is_null(request.bind_start_time):
            body['BindStartTime'] = request.bind_start_time
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.classification):
            body['Classification'] = request.classification
        if not DaraCore.is_null(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not DaraCore.is_null(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not DaraCore.is_null(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not DaraCore.is_null(request.msgkey):
            body['Msgkey'] = request.msgkey
        if not DaraCore.is_null(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.push_action):
            body['PushAction'] = request.push_action
        if not DaraCore.is_null(request.push_status):
            body['PushStatus'] = request.push_status
        if not DaraCore.is_null(request.silent):
            body['Silent'] = request.silent
        if not DaraCore.is_null(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not DaraCore.is_null(request.time_mode):
            body['TimeMode'] = request.time_mode
        if not DaraCore.is_null(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not DaraCore.is_null(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not DaraCore.is_null(request.un_bind_end_time):
            body['UnBindEndTime'] = request.un_bind_end_time
        if not DaraCore.is_null(request.un_bind_period):
            body['UnBindPeriod'] = request.un_bind_period
        if not DaraCore.is_null(request.un_bind_start_time):
            body['UnBindStartTime'] = request.un_bind_start_time
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushBroadcast',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushBroadcastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_broadcast(
        self,
        request: main_models.PushBroadcastRequest,
    ) -> main_models.PushBroadcastResponse:
        runtime = RuntimeOptions()
        return self.push_broadcast_with_options(request, runtime)

    async def push_broadcast_async(
        self,
        request: main_models.PushBroadcastRequest,
    ) -> main_models.PushBroadcastResponse:
        runtime = RuntimeOptions()
        return await self.push_broadcast_with_options_async(request, runtime)

    def push_multiple_with_options(
        self,
        tmp_req: main_models.PushMultipleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMultipleResponse:
        tmp_req.validate()
        request = main_models.PushMultipleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notify_level):
            request.notify_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not DaraCore.is_null(tmp_req.third_channel_category):
            request.third_channel_category_shrink = Utils.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not DaraCore.is_null(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not DaraCore.is_null(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.classification):
            body['Classification'] = request.classification
        if not DaraCore.is_null(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not DaraCore.is_null(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not DaraCore.is_null(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not DaraCore.is_null(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not DaraCore.is_null(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.push_action):
            body['PushAction'] = request.push_action
        if not DaraCore.is_null(request.silent):
            body['Silent'] = request.silent
        if not DaraCore.is_null(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not DaraCore.is_null(request.target_msg):
            body['TargetMsg'] = request.target_msg
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not DaraCore.is_null(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not DaraCore.is_null(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushMultiple',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMultipleResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_multiple_with_options_async(
        self,
        tmp_req: main_models.PushMultipleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMultipleResponse:
        tmp_req.validate()
        request = main_models.PushMultipleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notify_level):
            request.notify_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not DaraCore.is_null(tmp_req.third_channel_category):
            request.third_channel_category_shrink = Utils.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not DaraCore.is_null(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not DaraCore.is_null(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.classification):
            body['Classification'] = request.classification
        if not DaraCore.is_null(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not DaraCore.is_null(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not DaraCore.is_null(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not DaraCore.is_null(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not DaraCore.is_null(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.push_action):
            body['PushAction'] = request.push_action
        if not DaraCore.is_null(request.silent):
            body['Silent'] = request.silent
        if not DaraCore.is_null(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not DaraCore.is_null(request.target_msg):
            body['TargetMsg'] = request.target_msg
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not DaraCore.is_null(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not DaraCore.is_null(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushMultiple',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMultipleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_multiple(
        self,
        request: main_models.PushMultipleRequest,
    ) -> main_models.PushMultipleResponse:
        runtime = RuntimeOptions()
        return self.push_multiple_with_options(request, runtime)

    async def push_multiple_async(
        self,
        request: main_models.PushMultipleRequest,
    ) -> main_models.PushMultipleResponse:
        runtime = RuntimeOptions()
        return await self.push_multiple_with_options_async(request, runtime)

    def push_query_device_state_with_options(
        self,
        request: main_models.PushQueryDeviceStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushQueryDeviceStateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        if not DaraCore.is_null(request.target_type):
            body['TargetType'] = request.target_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushQueryDeviceState',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushQueryDeviceStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_query_device_state_with_options_async(
        self,
        request: main_models.PushQueryDeviceStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushQueryDeviceStateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        if not DaraCore.is_null(request.target_type):
            body['TargetType'] = request.target_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushQueryDeviceState',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushQueryDeviceStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_query_device_state(
        self,
        request: main_models.PushQueryDeviceStateRequest,
    ) -> main_models.PushQueryDeviceStateResponse:
        runtime = RuntimeOptions()
        return self.push_query_device_state_with_options(request, runtime)

    async def push_query_device_state_async(
        self,
        request: main_models.PushQueryDeviceStateRequest,
    ) -> main_models.PushQueryDeviceStateResponse:
        runtime = RuntimeOptions()
        return await self.push_query_device_state_with_options_async(request, runtime)

    def push_simple_with_options(
        self,
        tmp_req: main_models.PushSimpleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushSimpleResponse:
        tmp_req.validate()
        request = main_models.PushSimpleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notify_level):
            request.notify_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not DaraCore.is_null(tmp_req.third_channel_category):
            request.third_channel_category_shrink = Utils.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not DaraCore.is_null(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not DaraCore.is_null(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.classification):
            body['Classification'] = request.classification
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not DaraCore.is_null(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not DaraCore.is_null(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not DaraCore.is_null(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not DaraCore.is_null(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not DaraCore.is_null(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not DaraCore.is_null(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.push_action):
            body['PushAction'] = request.push_action
        if not DaraCore.is_null(request.push_style):
            body['PushStyle'] = request.push_style
        if not DaraCore.is_null(request.silent):
            body['Silent'] = request.silent
        if not DaraCore.is_null(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not DaraCore.is_null(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not DaraCore.is_null(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushSimple',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushSimpleResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_simple_with_options_async(
        self,
        tmp_req: main_models.PushSimpleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushSimpleResponse:
        tmp_req.validate()
        request = main_models.PushSimpleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notify_level):
            request.notify_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not DaraCore.is_null(tmp_req.third_channel_category):
            request.third_channel_category_shrink = Utils.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not DaraCore.is_null(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not DaraCore.is_null(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.classification):
            body['Classification'] = request.classification
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not DaraCore.is_null(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not DaraCore.is_null(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not DaraCore.is_null(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not DaraCore.is_null(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not DaraCore.is_null(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not DaraCore.is_null(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.push_action):
            body['PushAction'] = request.push_action
        if not DaraCore.is_null(request.push_style):
            body['PushStyle'] = request.push_style
        if not DaraCore.is_null(request.silent):
            body['Silent'] = request.silent
        if not DaraCore.is_null(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not DaraCore.is_null(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not DaraCore.is_null(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushSimple',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushSimpleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_simple(
        self,
        request: main_models.PushSimpleRequest,
    ) -> main_models.PushSimpleResponse:
        runtime = RuntimeOptions()
        return self.push_simple_with_options(request, runtime)

    async def push_simple_async(
        self,
        request: main_models.PushSimpleRequest,
    ) -> main_models.PushSimpleResponse:
        runtime = RuntimeOptions()
        return await self.push_simple_with_options_async(request, runtime)

    def push_template_with_options(
        self,
        tmp_req: main_models.PushTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushTemplateResponse:
        tmp_req.validate()
        request = main_models.PushTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notify_level):
            request.notify_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not DaraCore.is_null(tmp_req.third_channel_category):
            request.third_channel_category_shrink = Utils.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not DaraCore.is_null(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not DaraCore.is_null(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.classification):
            body['Classification'] = request.classification
        if not DaraCore.is_null(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not DaraCore.is_null(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not DaraCore.is_null(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not DaraCore.is_null(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not DaraCore.is_null(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.push_action):
            body['PushAction'] = request.push_action
        if not DaraCore.is_null(request.silent):
            body['Silent'] = request.silent
        if not DaraCore.is_null(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not DaraCore.is_null(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not DaraCore.is_null(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not DaraCore.is_null(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushTemplate',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_template_with_options_async(
        self,
        tmp_req: main_models.PushTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushTemplateResponse:
        tmp_req.validate()
        request = main_models.PushTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notify_level):
            request.notify_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not DaraCore.is_null(tmp_req.third_channel_category):
            request.third_channel_category_shrink = Utils.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not DaraCore.is_null(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not DaraCore.is_null(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.classification):
            body['Classification'] = request.classification
        if not DaraCore.is_null(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not DaraCore.is_null(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not DaraCore.is_null(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not DaraCore.is_null(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not DaraCore.is_null(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.push_action):
            body['PushAction'] = request.push_action
        if not DaraCore.is_null(request.silent):
            body['Silent'] = request.silent
        if not DaraCore.is_null(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not DaraCore.is_null(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not DaraCore.is_null(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not DaraCore.is_null(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushTemplate',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_template(
        self,
        request: main_models.PushTemplateRequest,
    ) -> main_models.PushTemplateResponse:
        runtime = RuntimeOptions()
        return self.push_template_with_options(request, runtime)

    async def push_template_async(
        self,
        request: main_models.PushTemplateRequest,
    ) -> main_models.PushTemplateResponse:
        runtime = RuntimeOptions()
        return await self.push_template_with_options_async(request, runtime)

    def query_mcube_mini_package_with_options(
        self,
        request: main_models.QueryMcubeMiniPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcubeMiniPackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMcubeMiniPackage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcubeMiniPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcube_mini_package_with_options_async(
        self,
        request: main_models.QueryMcubeMiniPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcubeMiniPackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMcubeMiniPackage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcubeMiniPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcube_mini_package(
        self,
        request: main_models.QueryMcubeMiniPackageRequest,
    ) -> main_models.QueryMcubeMiniPackageResponse:
        runtime = RuntimeOptions()
        return self.query_mcube_mini_package_with_options(request, runtime)

    async def query_mcube_mini_package_async(
        self,
        request: main_models.QueryMcubeMiniPackageRequest,
    ) -> main_models.QueryMcubeMiniPackageResponse:
        runtime = RuntimeOptions()
        return await self.query_mcube_mini_package_with_options_async(request, runtime)

    def query_mcube_mini_task_with_options(
        self,
        request: main_models.QueryMcubeMiniTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcubeMiniTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMcubeMiniTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcubeMiniTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcube_mini_task_with_options_async(
        self,
        request: main_models.QueryMcubeMiniTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcubeMiniTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMcubeMiniTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcubeMiniTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcube_mini_task(
        self,
        request: main_models.QueryMcubeMiniTaskRequest,
    ) -> main_models.QueryMcubeMiniTaskResponse:
        runtime = RuntimeOptions()
        return self.query_mcube_mini_task_with_options(request, runtime)

    async def query_mcube_mini_task_async(
        self,
        request: main_models.QueryMcubeMiniTaskRequest,
    ) -> main_models.QueryMcubeMiniTaskResponse:
        runtime = RuntimeOptions()
        return await self.query_mcube_mini_task_with_options_async(request, runtime)

    def query_mcube_vhost_with_options(
        self,
        request: main_models.QueryMcubeVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcubeVhostResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMcubeVhost',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcubeVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcube_vhost_with_options_async(
        self,
        request: main_models.QueryMcubeVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcubeVhostResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMcubeVhost',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcubeVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcube_vhost(
        self,
        request: main_models.QueryMcubeVhostRequest,
    ) -> main_models.QueryMcubeVhostResponse:
        runtime = RuntimeOptions()
        return self.query_mcube_vhost_with_options(request, runtime)

    async def query_mcube_vhost_async(
        self,
        request: main_models.QueryMcubeVhostRequest,
    ) -> main_models.QueryMcubeVhostResponse:
        runtime = RuntimeOptions()
        return await self.query_mcube_vhost_with_options_async(request, runtime)

    def query_mps_scheduler_list_with_options(
        self,
        request: main_models.QueryMpsSchedulerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMpsSchedulerListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMpsSchedulerList',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMpsSchedulerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mps_scheduler_list_with_options_async(
        self,
        request: main_models.QueryMpsSchedulerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMpsSchedulerListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMpsSchedulerList',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMpsSchedulerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mps_scheduler_list(
        self,
        request: main_models.QueryMpsSchedulerListRequest,
    ) -> main_models.QueryMpsSchedulerListResponse:
        runtime = RuntimeOptions()
        return self.query_mps_scheduler_list_with_options(request, runtime)

    async def query_mps_scheduler_list_async(
        self,
        request: main_models.QueryMpsSchedulerListRequest,
    ) -> main_models.QueryMpsSchedulerListResponse:
        runtime = RuntimeOptions()
        return await self.query_mps_scheduler_list_with_options_async(request, runtime)

    def query_push_analysis_core_index_with_options(
        self,
        request: main_models.QueryPushAnalysisCoreIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushAnalysisCoreIndexResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushAnalysisCoreIndex',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushAnalysisCoreIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_analysis_core_index_with_options_async(
        self,
        request: main_models.QueryPushAnalysisCoreIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushAnalysisCoreIndexResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushAnalysisCoreIndex',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushAnalysisCoreIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_analysis_core_index(
        self,
        request: main_models.QueryPushAnalysisCoreIndexRequest,
    ) -> main_models.QueryPushAnalysisCoreIndexResponse:
        runtime = RuntimeOptions()
        return self.query_push_analysis_core_index_with_options(request, runtime)

    async def query_push_analysis_core_index_async(
        self,
        request: main_models.QueryPushAnalysisCoreIndexRequest,
    ) -> main_models.QueryPushAnalysisCoreIndexResponse:
        runtime = RuntimeOptions()
        return await self.query_push_analysis_core_index_with_options_async(request, runtime)

    def query_push_analysis_task_detail_with_options(
        self,
        request: main_models.QueryPushAnalysisTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushAnalysisTaskDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushAnalysisTaskDetail',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushAnalysisTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_analysis_task_detail_with_options_async(
        self,
        request: main_models.QueryPushAnalysisTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushAnalysisTaskDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushAnalysisTaskDetail',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushAnalysisTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_analysis_task_detail(
        self,
        request: main_models.QueryPushAnalysisTaskDetailRequest,
    ) -> main_models.QueryPushAnalysisTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.query_push_analysis_task_detail_with_options(request, runtime)

    async def query_push_analysis_task_detail_async(
        self,
        request: main_models.QueryPushAnalysisTaskDetailRequest,
    ) -> main_models.QueryPushAnalysisTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_push_analysis_task_detail_with_options_async(request, runtime)

    def query_push_analysis_task_list_with_options(
        self,
        request: main_models.QueryPushAnalysisTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushAnalysisTaskListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushAnalysisTaskList',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushAnalysisTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_analysis_task_list_with_options_async(
        self,
        request: main_models.QueryPushAnalysisTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushAnalysisTaskListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushAnalysisTaskList',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushAnalysisTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_analysis_task_list(
        self,
        request: main_models.QueryPushAnalysisTaskListRequest,
    ) -> main_models.QueryPushAnalysisTaskListResponse:
        runtime = RuntimeOptions()
        return self.query_push_analysis_task_list_with_options(request, runtime)

    async def query_push_analysis_task_list_async(
        self,
        request: main_models.QueryPushAnalysisTaskListRequest,
    ) -> main_models.QueryPushAnalysisTaskListResponse:
        runtime = RuntimeOptions()
        return await self.query_push_analysis_task_list_with_options_async(request, runtime)

    def query_push_scheduler_list_with_options(
        self,
        request: main_models.QueryPushSchedulerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushSchedulerListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushSchedulerList',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushSchedulerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_scheduler_list_with_options_async(
        self,
        request: main_models.QueryPushSchedulerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPushSchedulerListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPushSchedulerList',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPushSchedulerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_scheduler_list(
        self,
        request: main_models.QueryPushSchedulerListRequest,
    ) -> main_models.QueryPushSchedulerListResponse:
        runtime = RuntimeOptions()
        return self.query_push_scheduler_list_with_options(request, runtime)

    async def query_push_scheduler_list_async(
        self,
        request: main_models.QueryPushSchedulerListRequest,
    ) -> main_models.QueryPushSchedulerListResponse:
        runtime = RuntimeOptions()
        return await self.query_push_scheduler_list_with_options_async(request, runtime)

    def revoke_push_message_with_options(
        self,
        request: main_models.RevokePushMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokePushMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        if not DaraCore.is_null(request.target_id):
            body['TargetId'] = request.target_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokePushMessage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokePushMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_push_message_with_options_async(
        self,
        request: main_models.RevokePushMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokePushMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        if not DaraCore.is_null(request.target_id):
            body['TargetId'] = request.target_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokePushMessage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokePushMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_push_message(
        self,
        request: main_models.RevokePushMessageRequest,
    ) -> main_models.RevokePushMessageResponse:
        runtime = RuntimeOptions()
        return self.revoke_push_message_with_options(request, runtime)

    async def revoke_push_message_async(
        self,
        request: main_models.RevokePushMessageRequest,
    ) -> main_models.RevokePushMessageResponse:
        runtime = RuntimeOptions()
        return await self.revoke_push_message_with_options_async(request, runtime)

    def revoke_push_task_with_options(
        self,
        request: main_models.RevokePushTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokePushTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokePushTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokePushTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_push_task_with_options_async(
        self,
        request: main_models.RevokePushTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokePushTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokePushTask',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokePushTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_push_task(
        self,
        request: main_models.RevokePushTaskRequest,
    ) -> main_models.RevokePushTaskResponse:
        runtime = RuntimeOptions()
        return self.revoke_push_task_with_options(request, runtime)

    async def revoke_push_task_async(
        self,
        request: main_models.RevokePushTaskRequest,
    ) -> main_models.RevokePushTaskResponse:
        runtime = RuntimeOptions()
        return await self.revoke_push_task_with_options_async(request, runtime)

    def update_mcube_whitelist_with_options(
        self,
        request: main_models.UpdateMcubeWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcubeWhitelistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.key_ids):
            body['KeyIds'] = request.key_ids
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.oss_url):
            body['OssUrl'] = request.oss_url
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcubeWhitelist',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcube_whitelist_with_options_async(
        self,
        request: main_models.UpdateMcubeWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcubeWhitelistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.key_ids):
            body['KeyIds'] = request.key_ids
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.oss_url):
            body['OssUrl'] = request.oss_url
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcubeWhitelist',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcubeWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mcube_whitelist(
        self,
        request: main_models.UpdateMcubeWhitelistRequest,
    ) -> main_models.UpdateMcubeWhitelistResponse:
        runtime = RuntimeOptions()
        return self.update_mcube_whitelist_with_options(request, runtime)

    async def update_mcube_whitelist_async(
        self,
        request: main_models.UpdateMcubeWhitelistRequest,
    ) -> main_models.UpdateMcubeWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.update_mcube_whitelist_with_options_async(request, runtime)

    def upload_mcube_mini_package_with_options(
        self,
        request: main_models.UploadMcubeMiniPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadMcubeMiniPackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not DaraCore.is_null(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not DaraCore.is_null(request.enable_keep_alive):
            body['EnableKeepAlive'] = request.enable_keep_alive
        if not DaraCore.is_null(request.enable_option_menu):
            body['EnableOptionMenu'] = request.enable_option_menu
        if not DaraCore.is_null(request.enable_tab_bar):
            body['EnableTabBar'] = request.enable_tab_bar
        if not DaraCore.is_null(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.h_5name):
            body['H5Name'] = request.h_5name
        if not DaraCore.is_null(request.h_5version):
            body['H5Version'] = request.h_5version
        if not DaraCore.is_null(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not DaraCore.is_null(request.install_type):
            body['InstallType'] = request.install_type
        if not DaraCore.is_null(request.main_url):
            body['MainUrl'] = request.main_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.package_type):
            body['PackageType'] = request.package_type
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_file_url):
            body['ResourceFileUrl'] = request.resource_file_url
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        if not DaraCore.is_null(request.vhost):
            body['Vhost'] = request.vhost
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadMcubeMiniPackage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadMcubeMiniPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_mcube_mini_package_with_options_async(
        self,
        request: main_models.UploadMcubeMiniPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadMcubeMiniPackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not DaraCore.is_null(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not DaraCore.is_null(request.enable_keep_alive):
            body['EnableKeepAlive'] = request.enable_keep_alive
        if not DaraCore.is_null(request.enable_option_menu):
            body['EnableOptionMenu'] = request.enable_option_menu
        if not DaraCore.is_null(request.enable_tab_bar):
            body['EnableTabBar'] = request.enable_tab_bar
        if not DaraCore.is_null(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.h_5name):
            body['H5Name'] = request.h_5name
        if not DaraCore.is_null(request.h_5version):
            body['H5Version'] = request.h_5version
        if not DaraCore.is_null(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not DaraCore.is_null(request.install_type):
            body['InstallType'] = request.install_type
        if not DaraCore.is_null(request.main_url):
            body['MainUrl'] = request.main_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.package_type):
            body['PackageType'] = request.package_type
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_file_url):
            body['ResourceFileUrl'] = request.resource_file_url
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        if not DaraCore.is_null(request.vhost):
            body['Vhost'] = request.vhost
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadMcubeMiniPackage',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadMcubeMiniPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_mcube_mini_package(
        self,
        request: main_models.UploadMcubeMiniPackageRequest,
    ) -> main_models.UploadMcubeMiniPackageResponse:
        runtime = RuntimeOptions()
        return self.upload_mcube_mini_package_with_options(request, runtime)

    async def upload_mcube_mini_package_async(
        self,
        request: main_models.UploadMcubeMiniPackageRequest,
    ) -> main_models.UploadMcubeMiniPackageResponse:
        runtime = RuntimeOptions()
        return await self.upload_mcube_mini_package_with_options_async(request, runtime)

    def upload_mcube_rsa_key_with_options(
        self,
        request: main_models.UploadMcubeRsaKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadMcubeRsaKeyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadMcubeRsaKey',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadMcubeRsaKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_mcube_rsa_key_with_options_async(
        self,
        request: main_models.UploadMcubeRsaKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadMcubeRsaKeyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadMcubeRsaKey',
            version = '2020-07-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadMcubeRsaKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_mcube_rsa_key(
        self,
        request: main_models.UploadMcubeRsaKeyRequest,
    ) -> main_models.UploadMcubeRsaKeyResponse:
        runtime = RuntimeOptions()
        return self.upload_mcube_rsa_key_with_options(request, runtime)

    async def upload_mcube_rsa_key_async(
        self,
        request: main_models.UploadMcubeRsaKeyRequest,
    ) -> main_models.UploadMcubeRsaKeyResponse:
        runtime = RuntimeOptions()
        return await self.upload_mcube_rsa_key_with_options_async(request, runtime)
