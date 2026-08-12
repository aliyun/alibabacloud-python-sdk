# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aisc20260101 import models as main_models
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
            'cn-zhangjiakou': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-wulanchabu': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-shanghai': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-qingdao': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-nanjing': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-huhehaote': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-hangzhou': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-guangzhou': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-beijing': 'aisc.cn-shanghai.aliyuncs.com',
            'ap-southeast-7': 'aisc.ap-southeast-1.aliyuncs.com',
            'ap-southeast-6': 'aisc.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'aisc.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'aisc.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'aisc.ap-southeast-1.aliyuncs.com',
            'ap-northeast-1': 'aisc.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'aisc.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'aisc.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'aisc.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'aisc.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'aisc.ap-southeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-hangzhou-finance': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-heyuan-acdr-1': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-shanghai-finance-1': 'aisc.cn-shanghai.aliyuncs.com',
            'cn-shenzhen-finance-1': 'aisc.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('aisc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_skill_file_check_with_options(
        self,
        request: main_models.CreateSkillFileCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillFileCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.files):
            query['Files'] = request.files
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillFileCheck',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillFileCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_file_check_with_options_async(
        self,
        request: main_models.CreateSkillFileCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillFileCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.files):
            query['Files'] = request.files
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillFileCheck',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillFileCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_file_check(
        self,
        request: main_models.CreateSkillFileCheckRequest,
    ) -> main_models.CreateSkillFileCheckResponse:
        runtime = RuntimeOptions()
        return self.create_skill_file_check_with_options(request, runtime)

    async def create_skill_file_check_async(
        self,
        request: main_models.CreateSkillFileCheckRequest,
    ) -> main_models.CreateSkillFileCheckResponse:
        runtime = RuntimeOptions()
        return await self.create_skill_file_check_with_options_async(request, runtime)

    def list_aiagent_event_with_options(
        self,
        request: main_models.ListAIAgentEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIAgentEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.asset_name):
            query['AssetName'] = request.asset_name
        if not DaraCore.is_null(request.asset_type):
            query['AssetType'] = request.asset_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.infra_instance_id):
            query['InfraInstanceId'] = request.infra_instance_id
        if not DaraCore.is_null(request.infra_name):
            query['InfraName'] = request.infra_name
        if not DaraCore.is_null(request.infra_region_id):
            query['InfraRegionId'] = request.infra_region_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.risk_name):
            query['RiskName'] = request.risk_name
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAIAgentEvent',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIAgentEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aiagent_event_with_options_async(
        self,
        request: main_models.ListAIAgentEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIAgentEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.asset_name):
            query['AssetName'] = request.asset_name
        if not DaraCore.is_null(request.asset_type):
            query['AssetType'] = request.asset_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.infra_instance_id):
            query['InfraInstanceId'] = request.infra_instance_id
        if not DaraCore.is_null(request.infra_name):
            query['InfraName'] = request.infra_name
        if not DaraCore.is_null(request.infra_region_id):
            query['InfraRegionId'] = request.infra_region_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.risk_name):
            query['RiskName'] = request.risk_name
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAIAgentEvent',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIAgentEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aiagent_event(
        self,
        request: main_models.ListAIAgentEventRequest,
    ) -> main_models.ListAIAgentEventResponse:
        runtime = RuntimeOptions()
        return self.list_aiagent_event_with_options(request, runtime)

    async def list_aiagent_event_async(
        self,
        request: main_models.ListAIAgentEventRequest,
    ) -> main_models.ListAIAgentEventResponse:
        runtime = RuntimeOptions()
        return await self.list_aiagent_event_with_options_async(request, runtime)

    def list_sub_tasks_with_options(
        self,
        request: main_models.ListSubTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.root_task_id):
            query['RootTaskId'] = request.root_task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubTasks',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_tasks_with_options_async(
        self,
        request: main_models.ListSubTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.root_task_id):
            query['RootTaskId'] = request.root_task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubTasks',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_tasks(
        self,
        request: main_models.ListSubTasksRequest,
    ) -> main_models.ListSubTasksResponse:
        runtime = RuntimeOptions()
        return self.list_sub_tasks_with_options(request, runtime)

    async def list_sub_tasks_async(
        self,
        request: main_models.ListSubTasksRequest,
    ) -> main_models.ListSubTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_sub_tasks_with_options_async(request, runtime)
