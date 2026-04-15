# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_mpaas20201028 import models as main_models
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

    def add_mds_mini_config_with_options(
        self,
        request: main_models.AddMdsMiniConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMdsMiniConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mini_config_add_json_str):
            body['MpaasMappcenterMiniConfigAddJsonStr'] = request.mpaas_mappcenter_mini_config_add_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMdsMiniConfig',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMdsMiniConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mds_mini_config_with_options_async(
        self,
        request: main_models.AddMdsMiniConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMdsMiniConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mini_config_add_json_str):
            body['MpaasMappcenterMiniConfigAddJsonStr'] = request.mpaas_mappcenter_mini_config_add_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMdsMiniConfig',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMdsMiniConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_mds_mini_config(
        self,
        request: main_models.AddMdsMiniConfigRequest,
    ) -> main_models.AddMdsMiniConfigResponse:
        runtime = RuntimeOptions()
        return self.add_mds_mini_config_with_options(request, runtime)

    async def add_mds_mini_config_async(
        self,
        request: main_models.AddMdsMiniConfigRequest,
    ) -> main_models.AddMdsMiniConfigResponse:
        runtime = RuntimeOptions()
        return await self.add_mds_mini_config_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def change_mds_cube_task_status_with_options(
        self,
        request: main_models.ChangeMdsCubeTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMdsCubeTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not DaraCore.is_null(request.template_task_id):
            body['TemplateTaskId'] = request.template_task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMdsCubeTaskStatus',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMdsCubeTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_mds_cube_task_status_with_options_async(
        self,
        request: main_models.ChangeMdsCubeTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMdsCubeTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not DaraCore.is_null(request.template_task_id):
            body['TemplateTaskId'] = request.template_task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMdsCubeTaskStatus',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMdsCubeTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_mds_cube_task_status(
        self,
        request: main_models.ChangeMdsCubeTaskStatusRequest,
    ) -> main_models.ChangeMdsCubeTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.change_mds_cube_task_status_with_options(request, runtime)

    async def change_mds_cube_task_status_async(
        self,
        request: main_models.ChangeMdsCubeTaskStatusRequest,
    ) -> main_models.ChangeMdsCubeTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.change_mds_cube_task_status_with_options_async(request, runtime)

    def copy_mcdp_group_with_options(
        self,
        request: main_models.CopyMcdpGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyMcdpGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_group_copy_json_str):
            body['MpaasMappcenterMcdpGroupCopyJsonStr'] = request.mpaas_mappcenter_mcdp_group_copy_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyMcdpGroup',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyMcdpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_mcdp_group_with_options_async(
        self,
        request: main_models.CopyMcdpGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyMcdpGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_group_copy_json_str):
            body['MpaasMappcenterMcdpGroupCopyJsonStr'] = request.mpaas_mappcenter_mcdp_group_copy_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyMcdpGroup',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyMcdpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_mcdp_group(
        self,
        request: main_models.CopyMcdpGroupRequest,
    ) -> main_models.CopyMcdpGroupResponse:
        runtime = RuntimeOptions()
        return self.copy_mcdp_group_with_options(request, runtime)

    async def copy_mcdp_group_async(
        self,
        request: main_models.CopyMcdpGroupRequest,
    ) -> main_models.CopyMcdpGroupResponse:
        runtime = RuntimeOptions()
        return await self.copy_mcdp_group_with_options_async(request, runtime)

    def create_link_with_options(
        self,
        request: main_models.CreateLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.cors):
            body['Cors'] = request.cors
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.dynamicfield):
            body['Dynamicfield'] = request.dynamicfield
        if not DaraCore.is_null(request.target_url):
            body['TargetUrl'] = request.target_url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLink',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_link_with_options_async(
        self,
        request: main_models.CreateLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.cors):
            body['Cors'] = request.cors
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.dynamicfield):
            body['Dynamicfield'] = request.dynamicfield
        if not DaraCore.is_null(request.target_url):
            body['TargetUrl'] = request.target_url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLink',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_link(
        self,
        request: main_models.CreateLinkRequest,
    ) -> main_models.CreateLinkResponse:
        runtime = RuntimeOptions()
        return self.create_link_with_options(request, runtime)

    async def create_link_async(
        self,
        request: main_models.CreateLinkRequest,
    ) -> main_models.CreateLinkResponse:
        runtime = RuntimeOptions()
        return await self.create_link_with_options_async(request, runtime)

    def create_mcdp_group_with_options(
        self,
        request: main_models.CreateMcdpGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcdpGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_group_create_json_str):
            body['MpaasMappcenterMcdpGroupCreateJsonStr'] = request.mpaas_mappcenter_mcdp_group_create_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcdpGroup',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcdpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcdp_group_with_options_async(
        self,
        request: main_models.CreateMcdpGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcdpGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_group_create_json_str):
            body['MpaasMappcenterMcdpGroupCreateJsonStr'] = request.mpaas_mappcenter_mcdp_group_create_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcdpGroup',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcdpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcdp_group(
        self,
        request: main_models.CreateMcdpGroupRequest,
    ) -> main_models.CreateMcdpGroupResponse:
        runtime = RuntimeOptions()
        return self.create_mcdp_group_with_options(request, runtime)

    async def create_mcdp_group_async(
        self,
        request: main_models.CreateMcdpGroupRequest,
    ) -> main_models.CreateMcdpGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_mcdp_group_with_options_async(request, runtime)

    def create_mcdp_material_with_options(
        self,
        request: main_models.CreateMcdpMaterialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcdpMaterialResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_material_create_json_str):
            body['MpaasMappcenterMcdpMaterialCreateJsonStr'] = request.mpaas_mappcenter_mcdp_material_create_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcdpMaterial',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcdpMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcdp_material_with_options_async(
        self,
        request: main_models.CreateMcdpMaterialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcdpMaterialResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_material_create_json_str):
            body['MpaasMappcenterMcdpMaterialCreateJsonStr'] = request.mpaas_mappcenter_mcdp_material_create_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcdpMaterial',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcdpMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcdp_material(
        self,
        request: main_models.CreateMcdpMaterialRequest,
    ) -> main_models.CreateMcdpMaterialResponse:
        runtime = RuntimeOptions()
        return self.create_mcdp_material_with_options(request, runtime)

    async def create_mcdp_material_async(
        self,
        request: main_models.CreateMcdpMaterialRequest,
    ) -> main_models.CreateMcdpMaterialResponse:
        runtime = RuntimeOptions()
        return await self.create_mcdp_material_with_options_async(request, runtime)

    def create_mcdp_zone_with_options(
        self,
        request: main_models.CreateMcdpZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcdpZoneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_zone_create_json_str):
            body['MpaasMappcenterMcdpZoneCreateJsonStr'] = request.mpaas_mappcenter_mcdp_zone_create_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcdpZone',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcdp_zone_with_options_async(
        self,
        request: main_models.CreateMcdpZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcdpZoneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_zone_create_json_str):
            body['MpaasMappcenterMcdpZoneCreateJsonStr'] = request.mpaas_mappcenter_mcdp_zone_create_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcdpZone',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcdpZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcdp_zone(
        self,
        request: main_models.CreateMcdpZoneRequest,
    ) -> main_models.CreateMcdpZoneResponse:
        runtime = RuntimeOptions()
        return self.create_mcdp_zone_with_options(request, runtime)

    async def create_mcdp_zone_async(
        self,
        request: main_models.CreateMcdpZoneRequest,
    ) -> main_models.CreateMcdpZoneResponse:
        runtime = RuntimeOptions()
        return await self.create_mcdp_zone_with_options_async(request, runtime)

    def create_mcube_hotpatch_resource_with_options(
        self,
        request: main_models.CreateMcubeHotpatchResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeHotpatchResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.fix_desc):
            body['FixDesc'] = request.fix_desc
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.product_version):
            body['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeHotpatchResource',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeHotpatchResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_hotpatch_resource_with_options_async(
        self,
        request: main_models.CreateMcubeHotpatchResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeHotpatchResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.fix_desc):
            body['FixDesc'] = request.fix_desc
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.product_version):
            body['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeHotpatchResource',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeHotpatchResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_hotpatch_resource(
        self,
        request: main_models.CreateMcubeHotpatchResourceRequest,
    ) -> main_models.CreateMcubeHotpatchResourceResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_hotpatch_resource_with_options(request, runtime)

    async def create_mcube_hotpatch_resource_async(
        self,
        request: main_models.CreateMcubeHotpatchResourceRequest,
    ) -> main_models.CreateMcubeHotpatchResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_hotpatch_resource_with_options_async(request, runtime)

    def create_mcube_hotpatch_rollback_task_with_options(
        self,
        request: main_models.CreateMcubeHotpatchRollbackTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeHotpatchRollbackTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version):
            body['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeHotpatchRollbackTask',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeHotpatchRollbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_hotpatch_rollback_task_with_options_async(
        self,
        request: main_models.CreateMcubeHotpatchRollbackTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeHotpatchRollbackTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version):
            body['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcubeHotpatchRollbackTask',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeHotpatchRollbackTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_hotpatch_rollback_task(
        self,
        request: main_models.CreateMcubeHotpatchRollbackTaskRequest,
    ) -> main_models.CreateMcubeHotpatchRollbackTaskResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_hotpatch_rollback_task_with_options(request, runtime)

    async def create_mcube_hotpatch_rollback_task_async(
        self,
        request: main_models.CreateMcubeHotpatchRollbackTaskRequest,
    ) -> main_models.CreateMcubeHotpatchRollbackTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_hotpatch_rollback_task_with_options_async(request, runtime)

    def create_mcube_hotpatch_task_with_options(
        self,
        request: main_models.CreateMcubeHotpatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeHotpatchTaskResponse:
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
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.sync_mode):
            body['SyncMode'] = request.sync_mode
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
            action = 'CreateMcubeHotpatchTask',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeHotpatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_hotpatch_task_with_options_async(
        self,
        request: main_models.CreateMcubeHotpatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcubeHotpatchTaskResponse:
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
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.sync_mode):
            body['SyncMode'] = request.sync_mode
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
            action = 'CreateMcubeHotpatchTask',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcubeHotpatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_hotpatch_task(
        self,
        request: main_models.CreateMcubeHotpatchTaskRequest,
    ) -> main_models.CreateMcubeHotpatchTaskResponse:
        runtime = RuntimeOptions()
        return self.create_mcube_hotpatch_task_with_options(request, runtime)

    async def create_mcube_hotpatch_task_async(
        self,
        request: main_models.CreateMcubeHotpatchTaskRequest,
    ) -> main_models.CreateMcubeHotpatchTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_mcube_hotpatch_task_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
        if not DaraCore.is_null(request.harmony_label):
            body['HarmonyLabel'] = request.harmony_label
        if not DaraCore.is_null(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not DaraCore.is_null(request.install_amount):
            body['InstallAmount'] = request.install_amount
        if not DaraCore.is_null(request.ios_symbolfile_url):
            body['IosSymbolfileUrl'] = request.ios_symbolfile_url
        if not DaraCore.is_null(request.is_enterprise):
            body['IsEnterprise'] = request.is_enterprise
        if not DaraCore.is_null(request.large_icon_url):
            body['LargeIconUrl'] = request.large_icon_url
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
            version = '2020-10-28',
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
        if not DaraCore.is_null(request.harmony_label):
            body['HarmonyLabel'] = request.harmony_label
        if not DaraCore.is_null(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not DaraCore.is_null(request.install_amount):
            body['InstallAmount'] = request.install_amount
        if not DaraCore.is_null(request.ios_symbolfile_url):
            body['IosSymbolfileUrl'] = request.ios_symbolfile_url
        if not DaraCore.is_null(request.is_enterprise):
            body['IsEnterprise'] = request.is_enterprise
        if not DaraCore.is_null(request.large_icon_url):
            body['LargeIconUrl'] = request.large_icon_url
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def create_mds_cube_resource_with_options(
        self,
        request: main_models.CreateMdsCubeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMdsCubeResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_max_version):
            body['AndroidMaxVersion'] = request.android_max_version
        if not DaraCore.is_null(request.android_min_version):
            body['AndroidMinVersion'] = request.android_min_version
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.ios_max_version):
            body['IosMaxVersion'] = request.ios_max_version
        if not DaraCore.is_null(request.ios_min_version):
            body['IosMinVersion'] = request.ios_min_version
        if not DaraCore.is_null(request.mock_data_url):
            body['MockDataUrl'] = request.mock_data_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.preview_picture_url):
            body['PreviewPictureUrl'] = request.preview_picture_url
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_resource_desc):
            body['TemplateResourceDesc'] = request.template_resource_desc
        if not DaraCore.is_null(request.template_resource_version):
            body['TemplateResourceVersion'] = request.template_resource_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMdsCubeResource',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMdsCubeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mds_cube_resource_with_options_async(
        self,
        request: main_models.CreateMdsCubeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMdsCubeResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_max_version):
            body['AndroidMaxVersion'] = request.android_max_version
        if not DaraCore.is_null(request.android_min_version):
            body['AndroidMinVersion'] = request.android_min_version
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.ios_max_version):
            body['IosMaxVersion'] = request.ios_max_version
        if not DaraCore.is_null(request.ios_min_version):
            body['IosMinVersion'] = request.ios_min_version
        if not DaraCore.is_null(request.mock_data_url):
            body['MockDataUrl'] = request.mock_data_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.preview_picture_url):
            body['PreviewPictureUrl'] = request.preview_picture_url
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_resource_desc):
            body['TemplateResourceDesc'] = request.template_resource_desc
        if not DaraCore.is_null(request.template_resource_version):
            body['TemplateResourceVersion'] = request.template_resource_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMdsCubeResource',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMdsCubeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mds_cube_resource(
        self,
        request: main_models.CreateMdsCubeResourceRequest,
    ) -> main_models.CreateMdsCubeResourceResponse:
        runtime = RuntimeOptions()
        return self.create_mds_cube_resource_with_options(request, runtime)

    async def create_mds_cube_resource_async(
        self,
        request: main_models.CreateMdsCubeResourceRequest,
    ) -> main_models.CreateMdsCubeResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_mds_cube_resource_with_options_async(request, runtime)

    def create_mds_cube_task_with_options(
        self,
        request: main_models.CreateMdsCubeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMdsCubeTaskResponse:
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
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.task_desc):
            body['TaskDesc'] = request.task_desc
        if not DaraCore.is_null(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
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
            action = 'CreateMdsCubeTask',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMdsCubeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mds_cube_task_with_options_async(
        self,
        request: main_models.CreateMdsCubeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMdsCubeTaskResponse:
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
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.task_desc):
            body['TaskDesc'] = request.task_desc
        if not DaraCore.is_null(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
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
            action = 'CreateMdsCubeTask',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMdsCubeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mds_cube_task(
        self,
        request: main_models.CreateMdsCubeTaskRequest,
    ) -> main_models.CreateMdsCubeTaskResponse:
        runtime = RuntimeOptions()
        return self.create_mds_cube_task_with_options(request, runtime)

    async def create_mds_cube_task_async(
        self,
        request: main_models.CreateMdsCubeTaskRequest,
    ) -> main_models.CreateMdsCubeTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_mds_cube_task_with_options_async(request, runtime)

    def create_mds_cube_template_with_options(
        self,
        request: main_models.CreateMdsCubeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMdsCubeTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_desc):
            body['TemplateDesc'] = request.template_desc
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
            action = 'CreateMdsCubeTemplate',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMdsCubeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mds_cube_template_with_options_async(
        self,
        request: main_models.CreateMdsCubeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMdsCubeTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_desc):
            body['TemplateDesc'] = request.template_desc
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
            action = 'CreateMdsCubeTemplate',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMdsCubeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mds_cube_template(
        self,
        request: main_models.CreateMdsCubeTemplateRequest,
    ) -> main_models.CreateMdsCubeTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_mds_cube_template_with_options(request, runtime)

    async def create_mds_cube_template_async(
        self,
        request: main_models.CreateMdsCubeTemplateRequest,
    ) -> main_models.CreateMdsCubeTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_mds_cube_template_with_options_async(request, runtime)

    def create_mds_miniprogram_task_with_options(
        self,
        request: main_models.CreateMdsMiniprogramTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMdsMiniprogramTaskResponse:
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
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.memo):
            body['Memo'] = request.memo
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.sync_mode):
            body['SyncMode'] = request.sync_mode
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
            action = 'CreateMdsMiniprogramTask',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMdsMiniprogramTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mds_miniprogram_task_with_options_async(
        self,
        request: main_models.CreateMdsMiniprogramTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMdsMiniprogramTaskResponse:
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
        if not DaraCore.is_null(request.h_5id):
            body['H5Id'] = request.h_5id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.memo):
            body['Memo'] = request.memo
        if not DaraCore.is_null(request.package_id):
            body['PackageId'] = request.package_id
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not DaraCore.is_null(request.publish_type):
            body['PublishType'] = request.publish_type
        if not DaraCore.is_null(request.sync_mode):
            body['SyncMode'] = request.sync_mode
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
            action = 'CreateMdsMiniprogramTask',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMdsMiniprogramTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mds_miniprogram_task(
        self,
        request: main_models.CreateMdsMiniprogramTaskRequest,
    ) -> main_models.CreateMdsMiniprogramTaskResponse:
        runtime = RuntimeOptions()
        return self.create_mds_miniprogram_task_with_options(request, runtime)

    async def create_mds_miniprogram_task_async(
        self,
        request: main_models.CreateMdsMiniprogramTaskRequest,
    ) -> main_models.CreateMdsMiniprogramTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_mds_miniprogram_task_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def create_pay_order_to_msence_with_options(
        self,
        tmp_req: main_models.CreatePayOrderToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePayOrderToMsenceResponse:
        tmp_req.validate()
        request = main_models.CreatePayOrderToMsenceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra_info):
            request.extra_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra_info, 'ExtraInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.amount):
            body['Amount'] = request.amount
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_token):
            body['AuthToken'] = request.auth_token
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.extra_info_shrink):
            body['ExtraInfo'] = request.extra_info_shrink
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePayOrderToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePayOrderToMsenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pay_order_to_msence_with_options_async(
        self,
        tmp_req: main_models.CreatePayOrderToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePayOrderToMsenceResponse:
        tmp_req.validate()
        request = main_models.CreatePayOrderToMsenceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra_info):
            request.extra_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra_info, 'ExtraInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.amount):
            body['Amount'] = request.amount
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_token):
            body['AuthToken'] = request.auth_token
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.extra_info_shrink):
            body['ExtraInfo'] = request.extra_info_shrink
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePayOrderToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePayOrderToMsenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pay_order_to_msence(
        self,
        request: main_models.CreatePayOrderToMsenceRequest,
    ) -> main_models.CreatePayOrderToMsenceResponse:
        runtime = RuntimeOptions()
        return self.create_pay_order_to_msence_with_options(request, runtime)

    async def create_pay_order_to_msence_async(
        self,
        request: main_models.CreatePayOrderToMsenceRequest,
    ) -> main_models.CreatePayOrderToMsenceResponse:
        runtime = RuntimeOptions()
        return await self.create_pay_order_to_msence_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def delete_mcdp_aim_with_options(
        self,
        request: main_models.DeleteMcdpAimRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcdpAimResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_aim_delete_json_str):
            body['MpaasMappcenterMcdpAimDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_aim_delete_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcdpAim',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcdp_aim_with_options_async(
        self,
        request: main_models.DeleteMcdpAimRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcdpAimResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_aim_delete_json_str):
            body['MpaasMappcenterMcdpAimDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_aim_delete_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcdpAim',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcdpAimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcdp_aim(
        self,
        request: main_models.DeleteMcdpAimRequest,
    ) -> main_models.DeleteMcdpAimResponse:
        runtime = RuntimeOptions()
        return self.delete_mcdp_aim_with_options(request, runtime)

    async def delete_mcdp_aim_async(
        self,
        request: main_models.DeleteMcdpAimRequest,
    ) -> main_models.DeleteMcdpAimResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcdp_aim_with_options_async(request, runtime)

    def delete_mcdp_crowd_with_options(
        self,
        request: main_models.DeleteMcdpCrowdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcdpCrowdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_crowd_delete_json_str):
            body['MpaasMappcenterMcdpCrowdDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_crowd_delete_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcdpCrowd',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcdpCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcdp_crowd_with_options_async(
        self,
        request: main_models.DeleteMcdpCrowdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcdpCrowdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_crowd_delete_json_str):
            body['MpaasMappcenterMcdpCrowdDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_crowd_delete_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcdpCrowd',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcdpCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcdp_crowd(
        self,
        request: main_models.DeleteMcdpCrowdRequest,
    ) -> main_models.DeleteMcdpCrowdResponse:
        runtime = RuntimeOptions()
        return self.delete_mcdp_crowd_with_options(request, runtime)

    async def delete_mcdp_crowd_async(
        self,
        request: main_models.DeleteMcdpCrowdRequest,
    ) -> main_models.DeleteMcdpCrowdResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcdp_crowd_with_options_async(request, runtime)

    def delete_mcdp_zone_with_options(
        self,
        request: main_models.DeleteMcdpZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcdpZoneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_zone_delete_json_str):
            body['MpaasMappcenterMcdpZoneDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_zone_delete_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcdpZone',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcdp_zone_with_options_async(
        self,
        request: main_models.DeleteMcdpZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcdpZoneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mcdp_zone_delete_json_str):
            body['MpaasMappcenterMcdpZoneDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_zone_delete_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcdpZone',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcdpZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcdp_zone(
        self,
        request: main_models.DeleteMcdpZoneRequest,
    ) -> main_models.DeleteMcdpZoneResponse:
        runtime = RuntimeOptions()
        return self.delete_mcdp_zone_with_options(request, runtime)

    async def delete_mcdp_zone_async(
        self,
        request: main_models.DeleteMcdpZoneRequest,
    ) -> main_models.DeleteMcdpZoneResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcdp_zone_with_options_async(request, runtime)

    def delete_mcube_hotpatch_resource_with_options(
        self,
        request: main_models.DeleteMcubeHotpatchResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeHotpatchResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_code):
            body['AppCode'] = request.app_code
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
            action = 'DeleteMcubeHotpatchResource',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeHotpatchResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_hotpatch_resource_with_options_async(
        self,
        request: main_models.DeleteMcubeHotpatchResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcubeHotpatchResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_code):
            body['AppCode'] = request.app_code
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
            action = 'DeleteMcubeHotpatchResource',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcubeHotpatchResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_hotpatch_resource(
        self,
        request: main_models.DeleteMcubeHotpatchResourceRequest,
    ) -> main_models.DeleteMcubeHotpatchResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_mcube_hotpatch_resource_with_options(request, runtime)

    async def delete_mcube_hotpatch_resource_async(
        self,
        request: main_models.DeleteMcubeHotpatchResourceRequest,
    ) -> main_models.DeleteMcubeHotpatchResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_mcube_hotpatch_resource_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def delete_mds_cube_template_with_options(
        self,
        request: main_models.DeleteMdsCubeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMdsCubeTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMdsCubeTemplate',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMdsCubeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mds_cube_template_with_options_async(
        self,
        request: main_models.DeleteMdsCubeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMdsCubeTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMdsCubeTemplate',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMdsCubeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mds_cube_template(
        self,
        request: main_models.DeleteMdsCubeTemplateRequest,
    ) -> main_models.DeleteMdsCubeTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_mds_cube_template_with_options(request, runtime)

    async def delete_mds_cube_template_async(
        self,
        request: main_models.DeleteMdsCubeTemplateRequest,
    ) -> main_models.DeleteMdsCubeTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_mds_cube_template_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def export_mapp_center_app_config_with_options(
        self,
        request: main_models.ExportMappCenterAppConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportMappCenterAppConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apk_file_url):
            body['ApkFileUrl'] = request.apk_file_url
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.cert_rsa_base_64):
            body['CertRsaBase64'] = request.cert_rsa_base_64
        if not DaraCore.is_null(request.identifier):
            body['Identifier'] = request.identifier
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportMappCenterAppConfig',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportMappCenterAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_mapp_center_app_config_with_options_async(
        self,
        request: main_models.ExportMappCenterAppConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportMappCenterAppConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apk_file_url):
            body['ApkFileUrl'] = request.apk_file_url
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.cert_rsa_base_64):
            body['CertRsaBase64'] = request.cert_rsa_base_64
        if not DaraCore.is_null(request.identifier):
            body['Identifier'] = request.identifier
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportMappCenterAppConfig',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportMappCenterAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_mapp_center_app_config(
        self,
        request: main_models.ExportMappCenterAppConfigRequest,
    ) -> main_models.ExportMappCenterAppConfigResponse:
        runtime = RuntimeOptions()
        return self.export_mapp_center_app_config_with_options(request, runtime)

    async def export_mapp_center_app_config_async(
        self,
        request: main_models.ExportMappCenterAppConfigRequest,
    ) -> main_models.ExportMappCenterAppConfigResponse:
        runtime = RuntimeOptions()
        return await self.export_mapp_center_app_config_with_options_async(request, runtime)

    def get_auth_token_to_msence_with_options(
        self,
        request: main_models.GetAuthTokenToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuthTokenToMsenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_code):
            body['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAuthTokenToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuthTokenToMsenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auth_token_to_msence_with_options_async(
        self,
        request: main_models.GetAuthTokenToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuthTokenToMsenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_code):
            body['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAuthTokenToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuthTokenToMsenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auth_token_to_msence(
        self,
        request: main_models.GetAuthTokenToMsenceRequest,
    ) -> main_models.GetAuthTokenToMsenceResponse:
        runtime = RuntimeOptions()
        return self.get_auth_token_to_msence_with_options(request, runtime)

    async def get_auth_token_to_msence_async(
        self,
        request: main_models.GetAuthTokenToMsenceRequest,
    ) -> main_models.GetAuthTokenToMsenceResponse:
        runtime = RuntimeOptions()
        return await self.get_auth_token_to_msence_with_options_async(request, runtime)

    def get_file_token_for_upload_to_msa_with_options(
        self,
        request: main_models.GetFileTokenForUploadToMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileTokenForUploadToMsaResponse:
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
            action = 'GetFileTokenForUploadToMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileTokenForUploadToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_token_for_upload_to_msa_with_options_async(
        self,
        request: main_models.GetFileTokenForUploadToMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileTokenForUploadToMsaResponse:
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
            action = 'GetFileTokenForUploadToMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileTokenForUploadToMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_token_for_upload_to_msa(
        self,
        request: main_models.GetFileTokenForUploadToMsaRequest,
    ) -> main_models.GetFileTokenForUploadToMsaResponse:
        runtime = RuntimeOptions()
        return self.get_file_token_for_upload_to_msa_with_options(request, runtime)

    async def get_file_token_for_upload_to_msa_async(
        self,
        request: main_models.GetFileTokenForUploadToMsaRequest,
    ) -> main_models.GetFileTokenForUploadToMsaResponse:
        runtime = RuntimeOptions()
        return await self.get_file_token_for_upload_to_msa_with_options_async(request, runtime)

    def get_game_review_by_status_with_options(
        self,
        request: main_models.GetGameReviewByStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGameReviewByStatusResponse:
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
        if not DaraCore.is_null(request.review_status):
            body['ReviewStatus'] = request.review_status
        if not DaraCore.is_null(request.sort_mode):
            body['SortMode'] = request.sort_mode
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGameReviewByStatus',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGameReviewByStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_game_review_by_status_with_options_async(
        self,
        request: main_models.GetGameReviewByStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGameReviewByStatusResponse:
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
        if not DaraCore.is_null(request.review_status):
            body['ReviewStatus'] = request.review_status
        if not DaraCore.is_null(request.sort_mode):
            body['SortMode'] = request.sort_mode
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGameReviewByStatus',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGameReviewByStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_game_review_by_status(
        self,
        request: main_models.GetGameReviewByStatusRequest,
    ) -> main_models.GetGameReviewByStatusResponse:
        runtime = RuntimeOptions()
        return self.get_game_review_by_status_with_options(request, runtime)

    async def get_game_review_by_status_async(
        self,
        request: main_models.GetGameReviewByStatusRequest,
    ) -> main_models.GetGameReviewByStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_game_review_by_status_with_options_async(request, runtime)

    def get_log_url_in_msa_with_options(
        self,
        request: main_models.GetLogUrlInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogUrlInMsaResponse:
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
            action = 'GetLogUrlInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogUrlInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_url_in_msa_with_options_async(
        self,
        request: main_models.GetLogUrlInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogUrlInMsaResponse:
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
            action = 'GetLogUrlInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogUrlInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_url_in_msa(
        self,
        request: main_models.GetLogUrlInMsaRequest,
    ) -> main_models.GetLogUrlInMsaResponse:
        runtime = RuntimeOptions()
        return self.get_log_url_in_msa_with_options(request, runtime)

    async def get_log_url_in_msa_async(
        self,
        request: main_models.GetLogUrlInMsaRequest,
    ) -> main_models.GetLogUrlInMsaResponse:
        runtime = RuntimeOptions()
        return await self.get_log_url_in_msa_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def get_mds_mini_config_with_options(
        self,
        request: main_models.GetMdsMiniConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMdsMiniConfigResponse:
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
            action = 'GetMdsMiniConfig',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMdsMiniConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mds_mini_config_with_options_async(
        self,
        request: main_models.GetMdsMiniConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMdsMiniConfigResponse:
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
            action = 'GetMdsMiniConfig',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMdsMiniConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mds_mini_config(
        self,
        request: main_models.GetMdsMiniConfigRequest,
    ) -> main_models.GetMdsMiniConfigResponse:
        runtime = RuntimeOptions()
        return self.get_mds_mini_config_with_options(request, runtime)

    async def get_mds_mini_config_async(
        self,
        request: main_models.GetMdsMiniConfigRequest,
    ) -> main_models.GetMdsMiniConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_mds_mini_config_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def get_user_app_donwload_url_in_msa_with_options(
        self,
        request: main_models.GetUserAppDonwloadUrlInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAppDonwloadUrlInMsaResponse:
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
            action = 'GetUserAppDonwloadUrlInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAppDonwloadUrlInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_app_donwload_url_in_msa_with_options_async(
        self,
        request: main_models.GetUserAppDonwloadUrlInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAppDonwloadUrlInMsaResponse:
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
            action = 'GetUserAppDonwloadUrlInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAppDonwloadUrlInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_app_donwload_url_in_msa(
        self,
        request: main_models.GetUserAppDonwloadUrlInMsaRequest,
    ) -> main_models.GetUserAppDonwloadUrlInMsaResponse:
        runtime = RuntimeOptions()
        return self.get_user_app_donwload_url_in_msa_with_options(request, runtime)

    async def get_user_app_donwload_url_in_msa_async(
        self,
        request: main_models.GetUserAppDonwloadUrlInMsaRequest,
    ) -> main_models.GetUserAppDonwloadUrlInMsaResponse:
        runtime = RuntimeOptions()
        return await self.get_user_app_donwload_url_in_msa_with_options_async(request, runtime)

    def get_user_app_enhance_process_in_msa_with_options(
        self,
        request: main_models.GetUserAppEnhanceProcessInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAppEnhanceProcessInMsaResponse:
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
            action = 'GetUserAppEnhanceProcessInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAppEnhanceProcessInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_app_enhance_process_in_msa_with_options_async(
        self,
        request: main_models.GetUserAppEnhanceProcessInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAppEnhanceProcessInMsaResponse:
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
            action = 'GetUserAppEnhanceProcessInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAppEnhanceProcessInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_app_enhance_process_in_msa(
        self,
        request: main_models.GetUserAppEnhanceProcessInMsaRequest,
    ) -> main_models.GetUserAppEnhanceProcessInMsaResponse:
        runtime = RuntimeOptions()
        return self.get_user_app_enhance_process_in_msa_with_options(request, runtime)

    async def get_user_app_enhance_process_in_msa_async(
        self,
        request: main_models.GetUserAppEnhanceProcessInMsaRequest,
    ) -> main_models.GetUserAppEnhanceProcessInMsaResponse:
        runtime = RuntimeOptions()
        return await self.get_user_app_enhance_process_in_msa_with_options_async(request, runtime)

    def get_user_app_upload_process_in_msa_with_options(
        self,
        request: main_models.GetUserAppUploadProcessInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAppUploadProcessInMsaResponse:
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
            action = 'GetUserAppUploadProcessInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAppUploadProcessInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_app_upload_process_in_msa_with_options_async(
        self,
        request: main_models.GetUserAppUploadProcessInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAppUploadProcessInMsaResponse:
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
            action = 'GetUserAppUploadProcessInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAppUploadProcessInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_app_upload_process_in_msa(
        self,
        request: main_models.GetUserAppUploadProcessInMsaRequest,
    ) -> main_models.GetUserAppUploadProcessInMsaResponse:
        runtime = RuntimeOptions()
        return self.get_user_app_upload_process_in_msa_with_options(request, runtime)

    async def get_user_app_upload_process_in_msa_async(
        self,
        request: main_models.GetUserAppUploadProcessInMsaRequest,
    ) -> main_models.GetUserAppUploadProcessInMsaResponse:
        runtime = RuntimeOptions()
        return await self.get_user_app_upload_process_in_msa_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def list_cubecard_apps_with_options(
        self,
        request: main_models.ListCubecardAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCubecardAppsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListCubecardApps',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCubecardAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cubecard_apps_with_options_async(
        self,
        request: main_models.ListCubecardAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCubecardAppsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListCubecardApps',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCubecardAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cubecard_apps(
        self,
        request: main_models.ListCubecardAppsRequest,
    ) -> main_models.ListCubecardAppsResponse:
        runtime = RuntimeOptions()
        return self.list_cubecard_apps_with_options(request, runtime)

    async def list_cubecard_apps_async(
        self,
        request: main_models.ListCubecardAppsRequest,
    ) -> main_models.ListCubecardAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_cubecard_apps_with_options_async(request, runtime)

    def list_mapp_center_apps_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListMappCenterAppsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListMappCenterApps',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMappCenterAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mapp_center_apps_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListMappCenterAppsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListMappCenterApps',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMappCenterAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mapp_center_apps(self) -> main_models.ListMappCenterAppsResponse:
        runtime = RuntimeOptions()
        return self.list_mapp_center_apps_with_options(runtime)

    async def list_mapp_center_apps_async(self) -> main_models.ListMappCenterAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_mapp_center_apps_with_options_async(runtime)

    def list_mapp_center_workspaces_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListMappCenterWorkspacesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListMappCenterWorkspaces',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMappCenterWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mapp_center_workspaces_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListMappCenterWorkspacesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListMappCenterWorkspaces',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMappCenterWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mapp_center_workspaces(self) -> main_models.ListMappCenterWorkspacesResponse:
        runtime = RuntimeOptions()
        return self.list_mapp_center_workspaces_with_options(runtime)

    async def list_mapp_center_workspaces_async(self) -> main_models.ListMappCenterWorkspacesResponse:
        runtime = RuntimeOptions()
        return await self.list_mapp_center_workspaces_with_options_async(runtime)

    def list_mcdp_aim_with_options(
        self,
        request: main_models.ListMcdpAimRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcdpAimResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.empty_tag):
            body['EmptyTag'] = request.empty_tag
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            body['Sort'] = request.sort
        if not DaraCore.is_null(request.sort_field):
            body['SortField'] = request.sort_field
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
            action = 'ListMcdpAim',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcdp_aim_with_options_async(
        self,
        request: main_models.ListMcdpAimRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcdpAimResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.empty_tag):
            body['EmptyTag'] = request.empty_tag
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            body['Sort'] = request.sort
        if not DaraCore.is_null(request.sort_field):
            body['SortField'] = request.sort_field
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
            action = 'ListMcdpAim',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcdpAimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcdp_aim(
        self,
        request: main_models.ListMcdpAimRequest,
    ) -> main_models.ListMcdpAimResponse:
        runtime = RuntimeOptions()
        return self.list_mcdp_aim_with_options(request, runtime)

    async def list_mcdp_aim_async(
        self,
        request: main_models.ListMcdpAimRequest,
    ) -> main_models.ListMcdpAimResponse:
        runtime = RuntimeOptions()
        return await self.list_mcdp_aim_with_options_async(request, runtime)

    def list_mcube_hotpatch_resources_with_options(
        self,
        request: main_models.ListMcubeHotpatchResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeHotpatchResourcesResponse:
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
            action = 'ListMcubeHotpatchResources',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeHotpatchResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_hotpatch_resources_with_options_async(
        self,
        request: main_models.ListMcubeHotpatchResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeHotpatchResourcesResponse:
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
            action = 'ListMcubeHotpatchResources',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeHotpatchResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_hotpatch_resources(
        self,
        request: main_models.ListMcubeHotpatchResourcesRequest,
    ) -> main_models.ListMcubeHotpatchResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_hotpatch_resources_with_options(request, runtime)

    async def list_mcube_hotpatch_resources_async(
        self,
        request: main_models.ListMcubeHotpatchResourcesRequest,
    ) -> main_models.ListMcubeHotpatchResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_hotpatch_resources_with_options_async(request, runtime)

    def list_mcube_hotpatch_tasks_with_options(
        self,
        request: main_models.ListMcubeHotpatchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeHotpatchTasksResponse:
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
            action = 'ListMcubeHotpatchTasks',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeHotpatchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_hotpatch_tasks_with_options_async(
        self,
        request: main_models.ListMcubeHotpatchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMcubeHotpatchTasksResponse:
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
            action = 'ListMcubeHotpatchTasks',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcubeHotpatchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_hotpatch_tasks(
        self,
        request: main_models.ListMcubeHotpatchTasksRequest,
    ) -> main_models.ListMcubeHotpatchTasksResponse:
        runtime = RuntimeOptions()
        return self.list_mcube_hotpatch_tasks_with_options(request, runtime)

    async def list_mcube_hotpatch_tasks_async(
        self,
        request: main_models.ListMcubeHotpatchTasksRequest,
    ) -> main_models.ListMcubeHotpatchTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_mcube_hotpatch_tasks_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def list_mds_cube_resources_with_options(
        self,
        request: main_models.ListMdsCubeResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMdsCubeResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.test):
            body['test'] = request.test
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMdsCubeResources',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMdsCubeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mds_cube_resources_with_options_async(
        self,
        request: main_models.ListMdsCubeResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMdsCubeResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.test):
            body['test'] = request.test
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMdsCubeResources',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMdsCubeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mds_cube_resources(
        self,
        request: main_models.ListMdsCubeResourcesRequest,
    ) -> main_models.ListMdsCubeResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_mds_cube_resources_with_options(request, runtime)

    async def list_mds_cube_resources_async(
        self,
        request: main_models.ListMdsCubeResourcesRequest,
    ) -> main_models.ListMdsCubeResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_mds_cube_resources_with_options_async(request, runtime)

    def list_mds_cube_tasks_with_options(
        self,
        request: main_models.ListMdsCubeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMdsCubeTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMdsCubeTasks',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMdsCubeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mds_cube_tasks_with_options_async(
        self,
        request: main_models.ListMdsCubeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMdsCubeTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMdsCubeTasks',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMdsCubeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mds_cube_tasks(
        self,
        request: main_models.ListMdsCubeTasksRequest,
    ) -> main_models.ListMdsCubeTasksResponse:
        runtime = RuntimeOptions()
        return self.list_mds_cube_tasks_with_options(request, runtime)

    async def list_mds_cube_tasks_async(
        self,
        request: main_models.ListMdsCubeTasksRequest,
    ) -> main_models.ListMdsCubeTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_mds_cube_tasks_with_options_async(request, runtime)

    def list_mds_cube_templates_with_options(
        self,
        request: main_models.ListMdsCubeTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMdsCubeTemplatesResponse:
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
            action = 'ListMdsCubeTemplates',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMdsCubeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mds_cube_templates_with_options_async(
        self,
        request: main_models.ListMdsCubeTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMdsCubeTemplatesResponse:
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
            action = 'ListMdsCubeTemplates',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMdsCubeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mds_cube_templates(
        self,
        request: main_models.ListMdsCubeTemplatesRequest,
    ) -> main_models.ListMdsCubeTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_mds_cube_templates_with_options(request, runtime)

    async def list_mds_cube_templates_async(
        self,
        request: main_models.ListMdsCubeTemplatesRequest,
    ) -> main_models.ListMdsCubeTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_mds_cube_templates_with_options_async(request, runtime)

    def list_mgs_api_with_options(
        self,
        request: main_models.ListMgsApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMgsApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_status):
            body['ApiStatus'] = request.api_status
        if not DaraCore.is_null(request.api_type):
            body['ApiType'] = request.api_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.host):
            body['Host'] = request.host
        if not DaraCore.is_null(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not DaraCore.is_null(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not DaraCore.is_null(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sys_id):
            body['SysId'] = request.sys_id
        if not DaraCore.is_null(request.sys_name):
            body['SysName'] = request.sys_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMgsApi',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMgsApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mgs_api_with_options_async(
        self,
        request: main_models.ListMgsApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMgsApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_status):
            body['ApiStatus'] = request.api_status
        if not DaraCore.is_null(request.api_type):
            body['ApiType'] = request.api_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.host):
            body['Host'] = request.host
        if not DaraCore.is_null(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not DaraCore.is_null(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not DaraCore.is_null(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sys_id):
            body['SysId'] = request.sys_id
        if not DaraCore.is_null(request.sys_name):
            body['SysName'] = request.sys_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMgsApi',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMgsApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mgs_api(
        self,
        request: main_models.ListMgsApiRequest,
    ) -> main_models.ListMgsApiResponse:
        runtime = RuntimeOptions()
        return self.list_mgs_api_with_options(request, runtime)

    async def list_mgs_api_async(
        self,
        request: main_models.ListMgsApiRequest,
    ) -> main_models.ListMgsApiResponse:
        runtime = RuntimeOptions()
        return await self.list_mgs_api_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def m_trsocrservice_with_options(
        self,
        request: main_models.MTRSOCRServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MTRSOCRServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.image_raw):
            body['ImageRaw'] = request.image_raw
        if not DaraCore.is_null(request.mask):
            body['Mask'] = request.mask
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
            action = 'MTRSOCRService',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MTRSOCRServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def m_trsocrservice_with_options_async(
        self,
        request: main_models.MTRSOCRServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MTRSOCRServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.image_raw):
            body['ImageRaw'] = request.image_raw
        if not DaraCore.is_null(request.mask):
            body['Mask'] = request.mask
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
            action = 'MTRSOCRService',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MTRSOCRServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def m_trsocrservice(
        self,
        request: main_models.MTRSOCRServiceRequest,
    ) -> main_models.MTRSOCRServiceResponse:
        runtime = RuntimeOptions()
        return self.m_trsocrservice_with_options(request, runtime)

    async def m_trsocrservice_async(
        self,
        request: main_models.MTRSOCRServiceRequest,
    ) -> main_models.MTRSOCRServiceResponse:
        runtime = RuntimeOptions()
        return await self.m_trsocrservice_with_options_async(request, runtime)

    def push_bind_with_options(
        self,
        request: main_models.PushBindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushBindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushBind',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_bind_with_options_async(
        self,
        request: main_models.PushBindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushBindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushBind',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_bind(
        self,
        request: main_models.PushBindRequest,
    ) -> main_models.PushBindResponse:
        runtime = RuntimeOptions()
        return self.push_bind_with_options(request, runtime)

    async def push_bind_async(
        self,
        request: main_models.PushBindRequest,
    ) -> main_models.PushBindResponse:
        runtime = RuntimeOptions()
        return await self.push_bind_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.bind_period):
            body['BindPeriod'] = request.bind_period
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
            version = '2020-10-28',
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
        if not DaraCore.is_null(request.bind_period):
            body['BindPeriod'] = request.bind_period
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def push_report_with_options(
        self,
        request: main_models.PushReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.connect_type):
            body['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not DaraCore.is_null(request.imei):
            body['Imei'] = request.imei
        if not DaraCore.is_null(request.imsi):
            body['Imsi'] = request.imsi
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.push_version):
            body['PushVersion'] = request.push_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel):
            body['ThirdChannel'] = request.third_channel
        if not DaraCore.is_null(request.third_channel_device_token):
            body['ThirdChannelDeviceToken'] = request.third_channel_device_token
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushReport',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_report_with_options_async(
        self,
        request: main_models.PushReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.connect_type):
            body['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not DaraCore.is_null(request.imei):
            body['Imei'] = request.imei
        if not DaraCore.is_null(request.imsi):
            body['Imsi'] = request.imsi
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.push_version):
            body['PushVersion'] = request.push_version
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.third_channel):
            body['ThirdChannel'] = request.third_channel
        if not DaraCore.is_null(request.third_channel_device_token):
            body['ThirdChannelDeviceToken'] = request.third_channel_device_token
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushReport',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_report(
        self,
        request: main_models.PushReportRequest,
    ) -> main_models.PushReportResponse:
        runtime = RuntimeOptions()
        return self.push_report_with_options(request, runtime)

    async def push_report_async(
        self,
        request: main_models.PushReportRequest,
    ) -> main_models.PushReportResponse:
        runtime = RuntimeOptions()
        return await self.push_report_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not DaraCore.is_null(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not DaraCore.is_null(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
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
            version = '2020-10-28',
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
        if not DaraCore.is_null(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not DaraCore.is_null(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not DaraCore.is_null(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
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
            version = '2020-10-28',
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
        if not DaraCore.is_null(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not DaraCore.is_null(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not DaraCore.is_null(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
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
            version = '2020-10-28',
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
        if not DaraCore.is_null(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not DaraCore.is_null(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not DaraCore.is_null(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
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
            version = '2020-10-28',
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

    def push_un_bind_with_options(
        self,
        request: main_models.PushUnBindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushUnBindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushUnBind',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushUnBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_un_bind_with_options_async(
        self,
        request: main_models.PushUnBindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushUnBindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushUnBind',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushUnBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_un_bind(
        self,
        request: main_models.PushUnBindRequest,
    ) -> main_models.PushUnBindResponse:
        runtime = RuntimeOptions()
        return self.push_un_bind_with_options(request, runtime)

    async def push_un_bind_async(
        self,
        request: main_models.PushUnBindRequest,
    ) -> main_models.PushUnBindResponse:
        runtime = RuntimeOptions()
        return await self.push_un_bind_with_options_async(request, runtime)

    def query_cubecard_filetoken_with_options(
        self,
        request: main_models.QueryCubecardFiletokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCubecardFiletokenResponse:
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
            action = 'QueryCubecardFiletoken',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCubecardFiletokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cubecard_filetoken_with_options_async(
        self,
        request: main_models.QueryCubecardFiletokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCubecardFiletokenResponse:
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
            action = 'QueryCubecardFiletoken',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCubecardFiletokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cubecard_filetoken(
        self,
        request: main_models.QueryCubecardFiletokenRequest,
    ) -> main_models.QueryCubecardFiletokenResponse:
        runtime = RuntimeOptions()
        return self.query_cubecard_filetoken_with_options(request, runtime)

    async def query_cubecard_filetoken_async(
        self,
        request: main_models.QueryCubecardFiletokenRequest,
    ) -> main_models.QueryCubecardFiletokenResponse:
        runtime = RuntimeOptions()
        return await self.query_cubecard_filetoken_with_options_async(request, runtime)

    def query_info_from_mdp_with_options(
        self,
        request: main_models.QueryInfoFromMdpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInfoFromMdpResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.mobile_md_5):
            body['MobileMd5'] = request.mobile_md_5
        if not DaraCore.is_null(request.mobile_sha_256):
            body['MobileSha256'] = request.mobile_sha_256
        if not DaraCore.is_null(request.mobile_sm_3):
            body['MobileSm3'] = request.mobile_sm_3
        if not DaraCore.is_null(request.risk_scene):
            body['RiskScene'] = request.risk_scene
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryInfoFromMdp',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInfoFromMdpResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_info_from_mdp_with_options_async(
        self,
        request: main_models.QueryInfoFromMdpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInfoFromMdpResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.mobile_md_5):
            body['MobileMd5'] = request.mobile_md_5
        if not DaraCore.is_null(request.mobile_sha_256):
            body['MobileSha256'] = request.mobile_sha_256
        if not DaraCore.is_null(request.mobile_sm_3):
            body['MobileSm3'] = request.mobile_sm_3
        if not DaraCore.is_null(request.risk_scene):
            body['RiskScene'] = request.risk_scene
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryInfoFromMdp',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInfoFromMdpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_info_from_mdp(
        self,
        request: main_models.QueryInfoFromMdpRequest,
    ) -> main_models.QueryInfoFromMdpResponse:
        runtime = RuntimeOptions()
        return self.query_info_from_mdp_with_options(request, runtime)

    async def query_info_from_mdp_async(
        self,
        request: main_models.QueryInfoFromMdpRequest,
    ) -> main_models.QueryInfoFromMdpResponse:
        runtime = RuntimeOptions()
        return await self.query_info_from_mdp_with_options_async(request, runtime)

    def query_link_with_options(
        self,
        request: main_models.QueryLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryLink',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_link_with_options_async(
        self,
        request: main_models.QueryLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryLink',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_link(
        self,
        request: main_models.QueryLinkRequest,
    ) -> main_models.QueryLinkResponse:
        runtime = RuntimeOptions()
        return self.query_link_with_options(request, runtime)

    async def query_link_async(
        self,
        request: main_models.QueryLinkRequest,
    ) -> main_models.QueryLinkResponse:
        runtime = RuntimeOptions()
        return await self.query_link_with_options_async(request, runtime)

    def query_mapp_center_app_with_options(
        self,
        request: main_models.QueryMappCenterAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMappCenterAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMappCenterApp',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMappCenterAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mapp_center_app_with_options_async(
        self,
        request: main_models.QueryMappCenterAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMappCenterAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMappCenterApp',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMappCenterAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mapp_center_app(
        self,
        request: main_models.QueryMappCenterAppRequest,
    ) -> main_models.QueryMappCenterAppResponse:
        runtime = RuntimeOptions()
        return self.query_mapp_center_app_with_options(request, runtime)

    async def query_mapp_center_app_async(
        self,
        request: main_models.QueryMappCenterAppRequest,
    ) -> main_models.QueryMappCenterAppResponse:
        runtime = RuntimeOptions()
        return await self.query_mapp_center_app_with_options_async(request, runtime)

    def query_mcdp_aim_with_options(
        self,
        request: main_models.QueryMcdpAimRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcdpAimResponse:
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
            action = 'QueryMcdpAim',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcdp_aim_with_options_async(
        self,
        request: main_models.QueryMcdpAimRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcdpAimResponse:
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
            action = 'QueryMcdpAim',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcdpAimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcdp_aim(
        self,
        request: main_models.QueryMcdpAimRequest,
    ) -> main_models.QueryMcdpAimResponse:
        runtime = RuntimeOptions()
        return self.query_mcdp_aim_with_options(request, runtime)

    async def query_mcdp_aim_async(
        self,
        request: main_models.QueryMcdpAimRequest,
    ) -> main_models.QueryMcdpAimResponse:
        runtime = RuntimeOptions()
        return await self.query_mcdp_aim_with_options_async(request, runtime)

    def query_mcdp_zone_with_options(
        self,
        request: main_models.QueryMcdpZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcdpZoneResponse:
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
            action = 'QueryMcdpZone',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcdp_zone_with_options_async(
        self,
        request: main_models.QueryMcdpZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcdpZoneResponse:
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
            action = 'QueryMcdpZone',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcdpZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcdp_zone(
        self,
        request: main_models.QueryMcdpZoneRequest,
    ) -> main_models.QueryMcdpZoneResponse:
        runtime = RuntimeOptions()
        return self.query_mcdp_zone_with_options(request, runtime)

    async def query_mcdp_zone_async(
        self,
        request: main_models.QueryMcdpZoneRequest,
    ) -> main_models.QueryMcdpZoneResponse:
        runtime = RuntimeOptions()
        return await self.query_mcdp_zone_with_options_async(request, runtime)

    def query_mcube_hotpatch_task_detail_with_options(
        self,
        request: main_models.QueryMcubeHotpatchTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcubeHotpatchTaskDetailResponse:
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
            action = 'QueryMcubeHotpatchTaskDetail',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcubeHotpatchTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcube_hotpatch_task_detail_with_options_async(
        self,
        request: main_models.QueryMcubeHotpatchTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMcubeHotpatchTaskDetailResponse:
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
            action = 'QueryMcubeHotpatchTaskDetail',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMcubeHotpatchTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcube_hotpatch_task_detail(
        self,
        request: main_models.QueryMcubeHotpatchTaskDetailRequest,
    ) -> main_models.QueryMcubeHotpatchTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.query_mcube_hotpatch_task_detail_with_options(request, runtime)

    async def query_mcube_hotpatch_task_detail_async(
        self,
        request: main_models.QueryMcubeHotpatchTaskDetailRequest,
    ) -> main_models.QueryMcubeHotpatchTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_mcube_hotpatch_task_detail_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def query_mds_upgrade_task_detail_with_options(
        self,
        request: main_models.QueryMdsUpgradeTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMdsUpgradeTaskDetailResponse:
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
            action = 'QueryMdsUpgradeTaskDetail',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMdsUpgradeTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mds_upgrade_task_detail_with_options_async(
        self,
        request: main_models.QueryMdsUpgradeTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMdsUpgradeTaskDetailResponse:
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
            action = 'QueryMdsUpgradeTaskDetail',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMdsUpgradeTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mds_upgrade_task_detail(
        self,
        request: main_models.QueryMdsUpgradeTaskDetailRequest,
    ) -> main_models.QueryMdsUpgradeTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.query_mds_upgrade_task_detail_with_options(request, runtime)

    async def query_mds_upgrade_task_detail_async(
        self,
        request: main_models.QueryMdsUpgradeTaskDetailRequest,
    ) -> main_models.QueryMdsUpgradeTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_mds_upgrade_task_detail_with_options_async(request, runtime)

    def query_mgs_apipage_with_options(
        self,
        request: main_models.QueryMgsApipageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMgsApipageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_status):
            body['ApiStatus'] = request.api_status
        if not DaraCore.is_null(request.api_type):
            body['ApiType'] = request.api_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.host):
            body['Host'] = request.host
        if not DaraCore.is_null(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not DaraCore.is_null(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not DaraCore.is_null(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sys_id):
            body['SysId'] = request.sys_id
        if not DaraCore.is_null(request.sys_name):
            body['SysName'] = request.sys_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMgsApipage',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMgsApipageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mgs_apipage_with_options_async(
        self,
        request: main_models.QueryMgsApipageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMgsApipageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_status):
            body['ApiStatus'] = request.api_status
        if not DaraCore.is_null(request.api_type):
            body['ApiType'] = request.api_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.host):
            body['Host'] = request.host
        if not DaraCore.is_null(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not DaraCore.is_null(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not DaraCore.is_null(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sys_id):
            body['SysId'] = request.sys_id
        if not DaraCore.is_null(request.sys_name):
            body['SysName'] = request.sys_name
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMgsApipage',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMgsApipageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mgs_apipage(
        self,
        request: main_models.QueryMgsApipageRequest,
    ) -> main_models.QueryMgsApipageResponse:
        runtime = RuntimeOptions()
        return self.query_mgs_apipage_with_options(request, runtime)

    async def query_mgs_apipage_async(
        self,
        request: main_models.QueryMgsApipageRequest,
    ) -> main_models.QueryMgsApipageResponse:
        runtime = RuntimeOptions()
        return await self.query_mgs_apipage_with_options_async(request, runtime)

    def query_mgs_apirest_with_options(
        self,
        request: main_models.QueryMgsApirestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMgsApirestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
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
            action = 'QueryMgsApirest',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMgsApirestResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mgs_apirest_with_options_async(
        self,
        request: main_models.QueryMgsApirestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMgsApirestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
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
            action = 'QueryMgsApirest',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMgsApirestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mgs_apirest(
        self,
        request: main_models.QueryMgsApirestRequest,
    ) -> main_models.QueryMgsApirestResponse:
        runtime = RuntimeOptions()
        return self.query_mgs_apirest_with_options(request, runtime)

    async def query_mgs_apirest_async(
        self,
        request: main_models.QueryMgsApirestRequest,
    ) -> main_models.QueryMgsApirestResponse:
        runtime = RuntimeOptions()
        return await self.query_mgs_apirest_with_options_async(request, runtime)

    def query_mgs_testreqbodyautogen_with_options(
        self,
        request: main_models.QueryMgsTestreqbodyautogenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMgsTestreqbodyautogenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str):
            body['MpaasMappcenterMgsTestreqbodyautogenQueryJsonStr'] = request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMgsTestreqbodyautogen',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMgsTestreqbodyautogenResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mgs_testreqbodyautogen_with_options_async(
        self,
        request: main_models.QueryMgsTestreqbodyautogenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMgsTestreqbodyautogenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str):
            body['MpaasMappcenterMgsTestreqbodyautogenQueryJsonStr'] = request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMgsTestreqbodyautogen',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMgsTestreqbodyautogenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mgs_testreqbodyautogen(
        self,
        request: main_models.QueryMgsTestreqbodyautogenRequest,
    ) -> main_models.QueryMgsTestreqbodyautogenResponse:
        runtime = RuntimeOptions()
        return self.query_mgs_testreqbodyautogen_with_options(request, runtime)

    async def query_mgs_testreqbodyautogen_async(
        self,
        request: main_models.QueryMgsTestreqbodyautogenRequest,
    ) -> main_models.QueryMgsTestreqbodyautogenResponse:
        runtime = RuntimeOptions()
        return await self.query_mgs_testreqbodyautogen_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def query_mscp_risk_info_with_options(
        self,
        request: main_models.QueryMscpRiskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMscpRiskInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apdid_token):
            body['ApdidToken'] = request.apdid_token
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.terminal_type):
            body['TerminalType'] = request.terminal_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMscpRiskInfo',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMscpRiskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mscp_risk_info_with_options_async(
        self,
        request: main_models.QueryMscpRiskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMscpRiskInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apdid_token):
            body['ApdidToken'] = request.apdid_token
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.terminal_type):
            body['TerminalType'] = request.terminal_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMscpRiskInfo',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMscpRiskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mscp_risk_info(
        self,
        request: main_models.QueryMscpRiskInfoRequest,
    ) -> main_models.QueryMscpRiskInfoResponse:
        runtime = RuntimeOptions()
        return self.query_mscp_risk_info_with_options(request, runtime)

    async def query_mscp_risk_info_async(
        self,
        request: main_models.QueryMscpRiskInfoRequest,
    ) -> main_models.QueryMscpRiskInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_mscp_risk_info_with_options_async(request, runtime)

    def query_pay_order_to_msence_with_options(
        self,
        request: main_models.QueryPayOrderToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPayOrderToMsenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPayOrderToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPayOrderToMsenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pay_order_to_msence_with_options_async(
        self,
        request: main_models.QueryPayOrderToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPayOrderToMsenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPayOrderToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPayOrderToMsenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pay_order_to_msence(
        self,
        request: main_models.QueryPayOrderToMsenceRequest,
    ) -> main_models.QueryPayOrderToMsenceResponse:
        runtime = RuntimeOptions()
        return self.query_pay_order_to_msence_with_options(request, runtime)

    async def query_pay_order_to_msence_async(
        self,
        request: main_models.QueryPayOrderToMsenceRequest,
    ) -> main_models.QueryPayOrderToMsenceResponse:
        runtime = RuntimeOptions()
        return await self.query_pay_order_to_msence_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def query_user_info_to_msence_with_options(
        self,
        request: main_models.QueryUserInfoToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserInfoToMsenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_token):
            body['AuthToken'] = request.auth_token
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserInfoToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserInfoToMsenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_info_to_msence_with_options_async(
        self,
        request: main_models.QueryUserInfoToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserInfoToMsenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_token):
            body['AuthToken'] = request.auth_token
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserInfoToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserInfoToMsenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_info_to_msence(
        self,
        request: main_models.QueryUserInfoToMsenceRequest,
    ) -> main_models.QueryUserInfoToMsenceResponse:
        runtime = RuntimeOptions()
        return self.query_user_info_to_msence_with_options(request, runtime)

    async def query_user_info_to_msence_async(
        self,
        request: main_models.QueryUserInfoToMsenceRequest,
    ) -> main_models.QueryUserInfoToMsenceResponse:
        runtime = RuntimeOptions()
        return await self.query_user_info_to_msence_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def run_msa_diff_with_options(
        self,
        request: main_models.RunMsaDiffRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunMsaDiffResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_msa_diff_run_json_str):
            body['MpaasMappcenterMsaDiffRunJsonStr'] = request.mpaas_mappcenter_msa_diff_run_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMsaDiff',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunMsaDiffResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_msa_diff_with_options_async(
        self,
        request: main_models.RunMsaDiffRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunMsaDiffResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_msa_diff_run_json_str):
            body['MpaasMappcenterMsaDiffRunJsonStr'] = request.mpaas_mappcenter_msa_diff_run_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMsaDiff',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunMsaDiffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_msa_diff(
        self,
        request: main_models.RunMsaDiffRequest,
    ) -> main_models.RunMsaDiffResponse:
        runtime = RuntimeOptions()
        return self.run_msa_diff_with_options(request, runtime)

    async def run_msa_diff_async(
        self,
        request: main_models.RunMsaDiffRequest,
    ) -> main_models.RunMsaDiffResponse:
        runtime = RuntimeOptions()
        return await self.run_msa_diff_with_options_async(request, runtime)

    def save_mgs_apirest_with_options(
        self,
        request: main_models.SaveMgsApirestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveMgsApirestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mgs_apirest_save_json_str):
            body['MpaasMappcenterMgsApirestSaveJsonStr'] = request.mpaas_mappcenter_mgs_apirest_save_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveMgsApirest',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveMgsApirestResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_mgs_apirest_with_options_async(
        self,
        request: main_models.SaveMgsApirestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveMgsApirestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mpaas_mappcenter_mgs_apirest_save_json_str):
            body['MpaasMappcenterMgsApirestSaveJsonStr'] = request.mpaas_mappcenter_mgs_apirest_save_json_str
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveMgsApirest',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveMgsApirestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_mgs_apirest(
        self,
        request: main_models.SaveMgsApirestRequest,
    ) -> main_models.SaveMgsApirestResponse:
        runtime = RuntimeOptions()
        return self.save_mgs_apirest_with_options(request, runtime)

    async def save_mgs_apirest_async(
        self,
        request: main_models.SaveMgsApirestRequest,
    ) -> main_models.SaveMgsApirestResponse:
        runtime = RuntimeOptions()
        return await self.save_mgs_apirest_with_options_async(request, runtime)

    def save_order_relation_info_to_msence_with_options(
        self,
        request: main_models.SaveOrderRelationInfoToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveOrderRelationInfoToMsenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['Amount'] = request.amount
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.biz_order_id):
            body['BizOrderId'] = request.biz_order_id
        if not DaraCore.is_null(request.biz_order_status):
            body['BizOrderStatus'] = request.biz_order_status
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.open_uid):
            body['OpenUid'] = request.open_uid
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveOrderRelationInfoToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveOrderRelationInfoToMsenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_order_relation_info_to_msence_with_options_async(
        self,
        request: main_models.SaveOrderRelationInfoToMsenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveOrderRelationInfoToMsenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['Amount'] = request.amount
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.biz_order_id):
            body['BizOrderId'] = request.biz_order_id
        if not DaraCore.is_null(request.biz_order_status):
            body['BizOrderStatus'] = request.biz_order_status
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.open_uid):
            body['OpenUid'] = request.open_uid
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveOrderRelationInfoToMsence',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveOrderRelationInfoToMsenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_order_relation_info_to_msence(
        self,
        request: main_models.SaveOrderRelationInfoToMsenceRequest,
    ) -> main_models.SaveOrderRelationInfoToMsenceResponse:
        runtime = RuntimeOptions()
        return self.save_order_relation_info_to_msence_with_options(request, runtime)

    async def save_order_relation_info_to_msence_async(
        self,
        request: main_models.SaveOrderRelationInfoToMsenceRequest,
    ) -> main_models.SaveOrderRelationInfoToMsenceResponse:
        runtime = RuntimeOptions()
        return await self.save_order_relation_info_to_msence_with_options_async(request, runtime)

    def start_user_app_async_enhance_in_msa_with_options(
        self,
        request: main_models.StartUserAppAsyncEnhanceInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartUserAppAsyncEnhanceInMsaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_shield_config):
            query['NewShieldConfig'] = request.new_shield_config
        body = {}
        if not DaraCore.is_null(request.apk_protector):
            body['ApkProtector'] = request.apk_protector
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.assets_file_list):
            body['AssetsFileList'] = request.assets_file_list
        if not DaraCore.is_null(request.classes):
            body['Classes'] = request.classes
        if not DaraCore.is_null(request.dalvik_debugger):
            body['DalvikDebugger'] = request.dalvik_debugger
        if not DaraCore.is_null(request.emulator_environment):
            body['EmulatorEnvironment'] = request.emulator_environment
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.java_hook):
            body['JavaHook'] = request.java_hook
        if not DaraCore.is_null(request.memory_dump):
            body['MemoryDump'] = request.memory_dump
        if not DaraCore.is_null(request.native_debugger):
            body['NativeDebugger'] = request.native_debugger
        if not DaraCore.is_null(request.native_hook):
            body['NativeHook'] = request.native_hook
        if not DaraCore.is_null(request.package_tampered):
            body['PackageTampered'] = request.package_tampered
        if not DaraCore.is_null(request.root):
            body['Root'] = request.root
        if not DaraCore.is_null(request.run_mode):
            body['RunMode'] = request.run_mode
        if not DaraCore.is_null(request.so_file_list):
            body['SoFileList'] = request.so_file_list
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.total_switch):
            body['TotalSwitch'] = request.total_switch
        if not DaraCore.is_null(request.use_ashield):
            body['UseAShield'] = request.use_ashield
        if not DaraCore.is_null(request.use_yshield):
            body['UseYShield'] = request.use_yshield
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartUserAppAsyncEnhanceInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartUserAppAsyncEnhanceInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_user_app_async_enhance_in_msa_with_options_async(
        self,
        request: main_models.StartUserAppAsyncEnhanceInMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartUserAppAsyncEnhanceInMsaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_shield_config):
            query['NewShieldConfig'] = request.new_shield_config
        body = {}
        if not DaraCore.is_null(request.apk_protector):
            body['ApkProtector'] = request.apk_protector
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.assets_file_list):
            body['AssetsFileList'] = request.assets_file_list
        if not DaraCore.is_null(request.classes):
            body['Classes'] = request.classes
        if not DaraCore.is_null(request.dalvik_debugger):
            body['DalvikDebugger'] = request.dalvik_debugger
        if not DaraCore.is_null(request.emulator_environment):
            body['EmulatorEnvironment'] = request.emulator_environment
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.java_hook):
            body['JavaHook'] = request.java_hook
        if not DaraCore.is_null(request.memory_dump):
            body['MemoryDump'] = request.memory_dump
        if not DaraCore.is_null(request.native_debugger):
            body['NativeDebugger'] = request.native_debugger
        if not DaraCore.is_null(request.native_hook):
            body['NativeHook'] = request.native_hook
        if not DaraCore.is_null(request.package_tampered):
            body['PackageTampered'] = request.package_tampered
        if not DaraCore.is_null(request.root):
            body['Root'] = request.root
        if not DaraCore.is_null(request.run_mode):
            body['RunMode'] = request.run_mode
        if not DaraCore.is_null(request.so_file_list):
            body['SoFileList'] = request.so_file_list
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.total_switch):
            body['TotalSwitch'] = request.total_switch
        if not DaraCore.is_null(request.use_ashield):
            body['UseAShield'] = request.use_ashield
        if not DaraCore.is_null(request.use_yshield):
            body['UseYShield'] = request.use_yshield
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartUserAppAsyncEnhanceInMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartUserAppAsyncEnhanceInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_user_app_async_enhance_in_msa(
        self,
        request: main_models.StartUserAppAsyncEnhanceInMsaRequest,
    ) -> main_models.StartUserAppAsyncEnhanceInMsaResponse:
        runtime = RuntimeOptions()
        return self.start_user_app_async_enhance_in_msa_with_options(request, runtime)

    async def start_user_app_async_enhance_in_msa_async(
        self,
        request: main_models.StartUserAppAsyncEnhanceInMsaRequest,
    ) -> main_models.StartUserAppAsyncEnhanceInMsaResponse:
        runtime = RuntimeOptions()
        return await self.start_user_app_async_enhance_in_msa_with_options_async(request, runtime)

    def update_link_with_options(
        self,
        request: main_models.UpdateLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.cors):
            body['Cors'] = request.cors
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.dynamicfield):
            body['Dynamicfield'] = request.dynamicfield
        if not DaraCore.is_null(request.target_url):
            body['TargetUrl'] = request.target_url
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLink',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_link_with_options_async(
        self,
        request: main_models.UpdateLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.cors):
            body['Cors'] = request.cors
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.dynamicfield):
            body['Dynamicfield'] = request.dynamicfield
        if not DaraCore.is_null(request.target_url):
            body['TargetUrl'] = request.target_url
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLink',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_link(
        self,
        request: main_models.UpdateLinkRequest,
    ) -> main_models.UpdateLinkResponse:
        runtime = RuntimeOptions()
        return self.update_link_with_options(request, runtime)

    async def update_link_async(
        self,
        request: main_models.UpdateLinkRequest,
    ) -> main_models.UpdateLinkResponse:
        runtime = RuntimeOptions()
        return await self.update_link_with_options_async(request, runtime)

    def update_mcube_hotpatch_task_status_with_options(
        self,
        request: main_models.UpdateMcubeHotpatchTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcubeHotpatchTaskStatusResponse:
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
            action = 'UpdateMcubeHotpatchTaskStatus',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcubeHotpatchTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcube_hotpatch_task_status_with_options_async(
        self,
        request: main_models.UpdateMcubeHotpatchTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcubeHotpatchTaskStatusResponse:
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
            action = 'UpdateMcubeHotpatchTaskStatus',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcubeHotpatchTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mcube_hotpatch_task_status(
        self,
        request: main_models.UpdateMcubeHotpatchTaskStatusRequest,
    ) -> main_models.UpdateMcubeHotpatchTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.update_mcube_hotpatch_task_status_with_options(request, runtime)

    async def update_mcube_hotpatch_task_status_async(
        self,
        request: main_models.UpdateMcubeHotpatchTaskStatusRequest,
    ) -> main_models.UpdateMcubeHotpatchTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_mcube_hotpatch_task_status_with_options_async(request, runtime)

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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def update_mds_cube_resource_with_options(
        self,
        request: main_models.UpdateMdsCubeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMdsCubeResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mock_data_url):
            body['MockDataUrl'] = request.mock_data_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMdsCubeResource',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMdsCubeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mds_cube_resource_with_options_async(
        self,
        request: main_models.UpdateMdsCubeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMdsCubeResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.mock_data_url):
            body['MockDataUrl'] = request.mock_data_url
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMdsCubeResource',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMdsCubeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mds_cube_resource(
        self,
        request: main_models.UpdateMdsCubeResourceRequest,
    ) -> main_models.UpdateMdsCubeResourceResponse:
        runtime = RuntimeOptions()
        return self.update_mds_cube_resource_with_options(request, runtime)

    async def update_mds_cube_resource_async(
        self,
        request: main_models.UpdateMdsCubeResourceRequest,
    ) -> main_models.UpdateMdsCubeResourceResponse:
        runtime = RuntimeOptions()
        return await self.update_mds_cube_resource_with_options_async(request, runtime)

    def update_mpaas_app_info_with_options(
        self,
        request: main_models.UpdateMpaasAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMpaasAppInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not DaraCore.is_null(request.identifier):
            body['Identifier'] = request.identifier
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMpaasAppInfo',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMpaasAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mpaas_app_info_with_options_async(
        self,
        request: main_models.UpdateMpaasAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMpaasAppInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not DaraCore.is_null(request.identifier):
            body['Identifier'] = request.identifier
        if not DaraCore.is_null(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMpaasAppInfo',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMpaasAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mpaas_app_info(
        self,
        request: main_models.UpdateMpaasAppInfoRequest,
    ) -> main_models.UpdateMpaasAppInfoResponse:
        runtime = RuntimeOptions()
        return self.update_mpaas_app_info_with_options(request, runtime)

    async def update_mpaas_app_info_async(
        self,
        request: main_models.UpdateMpaasAppInfoRequest,
    ) -> main_models.UpdateMpaasAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_mpaas_app_info_with_options_async(request, runtime)

    def upload_bitcode_to_msa_with_options(
        self,
        request: main_models.UploadBitcodeToMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadBitcodeToMsaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.bitcode):
            body['Bitcode'] = request.bitcode
        if not DaraCore.is_null(request.code_version):
            body['CodeVersion'] = request.code_version
        if not DaraCore.is_null(request.license):
            body['License'] = request.license
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
            action = 'UploadBitcodeToMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadBitcodeToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_bitcode_to_msa_with_options_async(
        self,
        request: main_models.UploadBitcodeToMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadBitcodeToMsaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.bitcode):
            body['Bitcode'] = request.bitcode
        if not DaraCore.is_null(request.code_version):
            body['CodeVersion'] = request.code_version
        if not DaraCore.is_null(request.license):
            body['License'] = request.license
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
            action = 'UploadBitcodeToMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadBitcodeToMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_bitcode_to_msa(
        self,
        request: main_models.UploadBitcodeToMsaRequest,
    ) -> main_models.UploadBitcodeToMsaResponse:
        runtime = RuntimeOptions()
        return self.upload_bitcode_to_msa_with_options(request, runtime)

    async def upload_bitcode_to_msa_async(
        self,
        request: main_models.UploadBitcodeToMsaRequest,
    ) -> main_models.UploadBitcodeToMsaResponse:
        runtime = RuntimeOptions()
        return await self.upload_bitcode_to_msa_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.icon_url):
            body['IconUrl'] = request.icon_url
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
            version = '2020-10-28',
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
        if not DaraCore.is_null(request.icon_url):
            body['IconUrl'] = request.icon_url
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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
            version = '2020-10-28',
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

    def upload_user_app_to_msa_with_options(
        self,
        request: main_models.UploadUserAppToMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadUserAppToMsaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.use_yshield):
            body['UseYShield'] = request.use_yshield
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadUserAppToMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadUserAppToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_user_app_to_msa_with_options_async(
        self,
        request: main_models.UploadUserAppToMsaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadUserAppToMsaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.use_yshield):
            body['UseYShield'] = request.use_yshield
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadUserAppToMsa',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadUserAppToMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_user_app_to_msa(
        self,
        request: main_models.UploadUserAppToMsaRequest,
    ) -> main_models.UploadUserAppToMsaResponse:
        runtime = RuntimeOptions()
        return self.upload_user_app_to_msa_with_options(request, runtime)

    async def upload_user_app_to_msa_async(
        self,
        request: main_models.UploadUserAppToMsaRequest,
    ) -> main_models.UploadUserAppToMsaResponse:
        runtime = RuntimeOptions()
        return await self.upload_user_app_to_msa_with_options_async(request, runtime)

    def virtual_delivery_to_mscene_with_options(
        self,
        request: main_models.VirtualDeliveryToMsceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VirtualDeliveryToMsceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VirtualDeliveryToMscene',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VirtualDeliveryToMsceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def virtual_delivery_to_mscene_with_options_async(
        self,
        request: main_models.VirtualDeliveryToMsceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VirtualDeliveryToMsceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.mini_program_id):
            body['MiniProgramId'] = request.mini_program_id
        if not DaraCore.is_null(request.platform_id):
            body['PlatformId'] = request.platform_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VirtualDeliveryToMscene',
            version = '2020-10-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VirtualDeliveryToMsceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def virtual_delivery_to_mscene(
        self,
        request: main_models.VirtualDeliveryToMsceneRequest,
    ) -> main_models.VirtualDeliveryToMsceneResponse:
        runtime = RuntimeOptions()
        return self.virtual_delivery_to_mscene_with_options(request, runtime)

    async def virtual_delivery_to_mscene_async(
        self,
        request: main_models.VirtualDeliveryToMsceneRequest,
    ) -> main_models.VirtualDeliveryToMsceneResponse:
        runtime = RuntimeOptions()
        return await self.virtual_delivery_to_mscene_with_options_async(request, runtime)
