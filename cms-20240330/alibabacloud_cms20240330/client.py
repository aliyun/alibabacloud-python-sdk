# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_cms20240330 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('cms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/resourcegroup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/resourcegroup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_addon_release_with_options(
        self,
        policy_id: str,
        request: main_models.CreateAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAddonReleaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.addon_name):
            body['addonName'] = request.addon_name
        if not DaraCore.is_null(request.aliyun_lang):
            body['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.entity_rules):
            body['entityRules'] = request.entity_rules
        if not DaraCore.is_null(request.env_type):
            body['envType'] = request.env_type
        if not DaraCore.is_null(request.parent_addon_release_id):
            body['parentAddonReleaseId'] = request.parent_addon_release_id
        if not DaraCore.is_null(request.release_name):
            body['releaseName'] = request.release_name
        if not DaraCore.is_null(request.values):
            body['values'] = request.values
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAddonRelease',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_addon_release_with_options_async(
        self,
        policy_id: str,
        request: main_models.CreateAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAddonReleaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.addon_name):
            body['addonName'] = request.addon_name
        if not DaraCore.is_null(request.aliyun_lang):
            body['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.entity_rules):
            body['entityRules'] = request.entity_rules
        if not DaraCore.is_null(request.env_type):
            body['envType'] = request.env_type
        if not DaraCore.is_null(request.parent_addon_release_id):
            body['parentAddonReleaseId'] = request.parent_addon_release_id
        if not DaraCore.is_null(request.release_name):
            body['releaseName'] = request.release_name
        if not DaraCore.is_null(request.values):
            body['values'] = request.values
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAddonRelease',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_addon_release(
        self,
        policy_id: str,
        request: main_models.CreateAddonReleaseRequest,
    ) -> main_models.CreateAddonReleaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_addon_release_with_options(policy_id, request, headers, runtime)

    async def create_addon_release_async(
        self,
        policy_id: str,
        request: main_models.CreateAddonReleaseRequest,
    ) -> main_models.CreateAddonReleaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_addon_release_with_options_async(policy_id, request, headers, runtime)

    def create_agg_task_group_with_options(
        self,
        instance_id: str,
        request: main_models.CreateAggTaskGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggTaskGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.override_if_exists):
            query['overrideIfExists'] = request.override_if_exists
        body = {}
        if not DaraCore.is_null(request.agg_task_group_config):
            body['aggTaskGroupConfig'] = request.agg_task_group_config
        if not DaraCore.is_null(request.agg_task_group_config_type):
            body['aggTaskGroupConfigType'] = request.agg_task_group_config_type
        if not DaraCore.is_null(request.agg_task_group_name):
            body['aggTaskGroupName'] = request.agg_task_group_name
        if not DaraCore.is_null(request.cron_expr):
            body['cronExpr'] = request.cron_expr
        if not DaraCore.is_null(request.delay):
            body['delay'] = request.delay
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.from_time):
            body['fromTime'] = request.from_time
        if not DaraCore.is_null(request.max_retries):
            body['maxRetries'] = request.max_retries
        if not DaraCore.is_null(request.max_run_time_in_seconds):
            body['maxRunTimeInSeconds'] = request.max_run_time_in_seconds
        if not DaraCore.is_null(request.precheck_string):
            body['precheckString'] = request.precheck_string
        if not DaraCore.is_null(request.schedule_mode):
            body['scheduleMode'] = request.schedule_mode
        if not DaraCore.is_null(request.schedule_time_expr):
            body['scheduleTimeExpr'] = request.schedule_time_expr
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.target_prometheus_id):
            body['targetPrometheusId'] = request.target_prometheus_id
        if not DaraCore.is_null(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggTaskGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agg_task_group_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateAggTaskGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggTaskGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.override_if_exists):
            query['overrideIfExists'] = request.override_if_exists
        body = {}
        if not DaraCore.is_null(request.agg_task_group_config):
            body['aggTaskGroupConfig'] = request.agg_task_group_config
        if not DaraCore.is_null(request.agg_task_group_config_type):
            body['aggTaskGroupConfigType'] = request.agg_task_group_config_type
        if not DaraCore.is_null(request.agg_task_group_name):
            body['aggTaskGroupName'] = request.agg_task_group_name
        if not DaraCore.is_null(request.cron_expr):
            body['cronExpr'] = request.cron_expr
        if not DaraCore.is_null(request.delay):
            body['delay'] = request.delay
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.from_time):
            body['fromTime'] = request.from_time
        if not DaraCore.is_null(request.max_retries):
            body['maxRetries'] = request.max_retries
        if not DaraCore.is_null(request.max_run_time_in_seconds):
            body['maxRunTimeInSeconds'] = request.max_run_time_in_seconds
        if not DaraCore.is_null(request.precheck_string):
            body['precheckString'] = request.precheck_string
        if not DaraCore.is_null(request.schedule_mode):
            body['scheduleMode'] = request.schedule_mode
        if not DaraCore.is_null(request.schedule_time_expr):
            body['scheduleTimeExpr'] = request.schedule_time_expr
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.target_prometheus_id):
            body['targetPrometheusId'] = request.target_prometheus_id
        if not DaraCore.is_null(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggTaskGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agg_task_group(
        self,
        instance_id: str,
        request: main_models.CreateAggTaskGroupRequest,
    ) -> main_models.CreateAggTaskGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agg_task_group_with_options(instance_id, request, headers, runtime)

    async def create_agg_task_group_async(
        self,
        instance_id: str,
        request: main_models.CreateAggTaskGroupRequest,
    ) -> main_models.CreateAggTaskGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agg_task_group_with_options_async(instance_id, request, headers, runtime)

    def create_biz_trace_with_options(
        self,
        request: main_models.CreateBizTraceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBizTraceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_config):
            body['advancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.biz_trace_code):
            body['bizTraceCode'] = request.biz_trace_code
        if not DaraCore.is_null(request.biz_trace_name):
            body['bizTraceName'] = request.biz_trace_name
        if not DaraCore.is_null(request.rule_config):
            body['ruleConfig'] = request.rule_config
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBizTrace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTrace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBizTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_biz_trace_with_options_async(
        self,
        request: main_models.CreateBizTraceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBizTraceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_config):
            body['advancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.biz_trace_code):
            body['bizTraceCode'] = request.biz_trace_code
        if not DaraCore.is_null(request.biz_trace_name):
            body['bizTraceName'] = request.biz_trace_name
        if not DaraCore.is_null(request.rule_config):
            body['ruleConfig'] = request.rule_config
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBizTrace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTrace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBizTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_biz_trace(
        self,
        request: main_models.CreateBizTraceRequest,
    ) -> main_models.CreateBizTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_biz_trace_with_options(request, headers, runtime)

    async def create_biz_trace_async(
        self,
        request: main_models.CreateBizTraceRequest,
    ) -> main_models.CreateBizTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_biz_trace_with_options_async(request, headers, runtime)

    def create_chat_with_sse(
        self,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.CreateChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.digital_employee_name):
            body['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.CreateChatResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def create_chat_with_sse_async(
        self,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.CreateChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.digital_employee_name):
            body['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.CreateChatResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def create_chat_with_options(
        self,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.digital_employee_name):
            body['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_with_options_async(
        self,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.digital_employee_name):
            body['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat(
        self,
        request: main_models.CreateChatRequest,
    ) -> main_models.CreateChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_chat_with_options(request, headers, runtime)

    async def create_chat_async(
        self,
        request: main_models.CreateChatRequest,
    ) -> main_models.CreateChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_chat_with_options_async(request, headers, runtime)

    def create_cloud_resource_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudResource',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cloudresource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_resource_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudResource',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cloudresource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_resource(self) -> main_models.CreateCloudResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_cloud_resource_with_options(headers, runtime)

    async def create_cloud_resource_async(self) -> main_models.CreateCloudResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_cloud_resource_with_options_async(headers, runtime)

    def create_digital_employee_with_options(
        self,
        request: main_models.CreateDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDigitalEmployeeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_rule):
            body['defaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.knowledges):
            body['knowledges'] = request.knowledges
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDigitalEmployee',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDigitalEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_digital_employee_with_options_async(
        self,
        request: main_models.CreateDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDigitalEmployeeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_rule):
            body['defaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.knowledges):
            body['knowledges'] = request.knowledges
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDigitalEmployee',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDigitalEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_digital_employee(
        self,
        request: main_models.CreateDigitalEmployeeRequest,
    ) -> main_models.CreateDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_digital_employee_with_options(request, headers, runtime)

    async def create_digital_employee_async(
        self,
        request: main_models.CreateDigitalEmployeeRequest,
    ) -> main_models.CreateDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_digital_employee_with_options_async(request, headers, runtime)

    def create_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEntityStoreResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateEntityStore',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}/entitystore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEntityStoreResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateEntityStore',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}/entitystore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_entity_store(
        self,
        workspace_name: str,
    ) -> main_models.CreateEntityStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_entity_store_with_options(workspace_name, headers, runtime)

    async def create_entity_store_async(
        self,
        workspace_name: str,
    ) -> main_models.CreateEntityStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_entity_store_with_options_async(workspace_name, headers, runtime)

    def create_integration_policy_with_options(
        self,
        request: main_models.CreateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntegrationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.entity_group):
            body['entityGroup'] = request.entity_group
        if not DaraCore.is_null(request.policy_name):
            body['policyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            body['policyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntegrationPolicy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntegrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_integration_policy_with_options_async(
        self,
        request: main_models.CreateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntegrationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.entity_group):
            body['entityGroup'] = request.entity_group
        if not DaraCore.is_null(request.policy_name):
            body['policyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            body['policyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntegrationPolicy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntegrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_integration_policy(
        self,
        request: main_models.CreateIntegrationPolicyRequest,
    ) -> main_models.CreateIntegrationPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_integration_policy_with_options(request, headers, runtime)

    async def create_integration_policy_async(
        self,
        request: main_models.CreateIntegrationPolicyRequest,
    ) -> main_models.CreateIntegrationPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_integration_policy_with_options_async(request, headers, runtime)

    def create_prometheus_instance_with_options(
        self,
        request: main_models.CreatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not DaraCore.is_null(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not DaraCore.is_null(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not DaraCore.is_null(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_instance_with_options_async(
        self,
        request: main_models.CreatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not DaraCore.is_null(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not DaraCore.is_null(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not DaraCore.is_null(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_instance(
        self,
        request: main_models.CreatePrometheusInstanceRequest,
    ) -> main_models.CreatePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_prometheus_instance_with_options(request, headers, runtime)

    async def create_prometheus_instance_async(
        self,
        request: main_models.CreatePrometheusInstanceRequest,
    ) -> main_models.CreatePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_prometheus_instance_with_options_async(request, headers, runtime)

    def create_prometheus_view_with_options(
        self,
        request: main_models.CreatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusViewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.prometheus_instances):
            body['prometheusInstances'] = request.prometheus_instances
        if not DaraCore.is_null(request.prometheus_view_name):
            body['prometheusViewName'] = request.prometheus_view_name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusView',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_view_with_options_async(
        self,
        request: main_models.CreatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusViewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.prometheus_instances):
            body['prometheusInstances'] = request.prometheus_instances
        if not DaraCore.is_null(request.prometheus_view_name):
            body['prometheusViewName'] = request.prometheus_view_name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusView',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_view(
        self,
        request: main_models.CreatePrometheusViewRequest,
    ) -> main_models.CreatePrometheusViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_prometheus_view_with_options(request, headers, runtime)

    async def create_prometheus_view_async(
        self,
        request: main_models.CreatePrometheusViewRequest,
    ) -> main_models.CreatePrometheusViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_prometheus_view_with_options_async(request, headers, runtime)

    def create_prometheus_virtual_instance_with_options(
        self,
        request: main_models.CreatePrometheusVirtualInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusVirtualInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusVirtualInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/virtual-instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusVirtualInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_virtual_instance_with_options_async(
        self,
        request: main_models.CreatePrometheusVirtualInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusVirtualInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusVirtualInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/virtual-instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusVirtualInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_virtual_instance(
        self,
        request: main_models.CreatePrometheusVirtualInstanceRequest,
    ) -> main_models.CreatePrometheusVirtualInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_prometheus_virtual_instance_with_options(request, headers, runtime)

    async def create_prometheus_virtual_instance_async(
        self,
        request: main_models.CreatePrometheusVirtualInstanceRequest,
    ) -> main_models.CreatePrometheusVirtualInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_prometheus_virtual_instance_with_options_async(request, headers, runtime)

    def create_service_with_options(
        self,
        workspace: str,
        request: main_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.pid):
            body['pid'] = request.pid
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_name):
            body['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_status):
            body['serviceStatus'] = request.service_status
        if not DaraCore.is_null(request.service_type):
            body['serviceType'] = request.service_type
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        workspace: str,
        request: main_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.pid):
            body['pid'] = request.pid
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_name):
            body['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_status):
            body['serviceStatus'] = request.service_status
        if not DaraCore.is_null(request.service_type):
            body['serviceType'] = request.service_type
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        workspace: str,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_with_options(workspace, request, headers, runtime)

    async def create_service_async(
        self,
        workspace: str,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(workspace, request, headers, runtime)

    def create_thread_with_options(
        self,
        name: str,
        request: main_models.CreateThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateThreadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateThread',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateThreadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_thread_with_options_async(
        self,
        name: str,
        request: main_models.CreateThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateThreadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateThread',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateThreadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_thread(
        self,
        name: str,
        request: main_models.CreateThreadRequest,
    ) -> main_models.CreateThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_thread_with_options(name, request, headers, runtime)

    async def create_thread_async(
        self,
        name: str,
        request: main_models.CreateThreadRequest,
    ) -> main_models.CreateThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_thread_with_options_async(name, request, headers, runtime)

    def create_ticket_with_options(
        self,
        request: main_models.CreateTicketRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not DaraCore.is_null(request.expiration_time):
            query['expirationTime'] = request.expiration_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/tickets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: main_models.CreateTicketRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not DaraCore.is_null(request.expiration_time):
            query['expirationTime'] = request.expiration_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/tickets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ticket_with_options(request, headers, runtime)

    async def create_ticket_async(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ticket_with_options_async(request, headers, runtime)

    def create_umodel_with_options(
        self,
        workspace: str,
        request: main_models.CreateUmodelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUmodelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUmodel',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_umodel_with_options_async(
        self,
        workspace: str,
        request: main_models.CreateUmodelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUmodelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUmodel',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_umodel(
        self,
        workspace: str,
        request: main_models.CreateUmodelRequest,
    ) -> main_models.CreateUmodelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_umodel_with_options(workspace, request, headers, runtime)

    async def create_umodel_async(
        self,
        workspace: str,
        request: main_models.CreateUmodelRequest,
    ) -> main_models.CreateUmodelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_umodel_with_options_async(workspace, request, headers, runtime)

    def delete_addon_release_with_options(
        self,
        policy_id: str,
        request: main_models.DeleteAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddonReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        if not DaraCore.is_null(request.release_name):
            query['releaseName'] = request.release_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddonRelease',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_addon_release_with_options_async(
        self,
        policy_id: str,
        request: main_models.DeleteAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddonReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        if not DaraCore.is_null(request.release_name):
            query['releaseName'] = request.release_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddonRelease',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_addon_release(
        self,
        policy_id: str,
        request: main_models.DeleteAddonReleaseRequest,
    ) -> main_models.DeleteAddonReleaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_addon_release_with_options(policy_id, request, headers, runtime)

    async def delete_addon_release_async(
        self,
        policy_id: str,
        request: main_models.DeleteAddonReleaseRequest,
    ) -> main_models.DeleteAddonReleaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_addon_release_with_options_async(policy_id, request, headers, runtime)

    def delete_agg_task_group_with_options(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggTaskGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggTaskGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agg_task_group_with_options_async(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggTaskGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggTaskGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agg_task_group(
        self,
        instance_id: str,
        group_id: str,
    ) -> main_models.DeleteAggTaskGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agg_task_group_with_options(instance_id, group_id, headers, runtime)

    async def delete_agg_task_group_async(
        self,
        instance_id: str,
        group_id: str,
    ) -> main_models.DeleteAggTaskGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agg_task_group_with_options_async(instance_id, group_id, headers, runtime)

    def delete_biz_trace_with_options(
        self,
        biz_trace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBizTraceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteBizTrace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTrace/{DaraURL.percent_encode(biz_trace_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBizTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_trace_with_options_async(
        self,
        biz_trace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBizTraceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteBizTrace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTrace/{DaraURL.percent_encode(biz_trace_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBizTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_trace(
        self,
        biz_trace_id: str,
    ) -> main_models.DeleteBizTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_biz_trace_with_options(biz_trace_id, headers, runtime)

    async def delete_biz_trace_async(
        self,
        biz_trace_id: str,
    ) -> main_models.DeleteBizTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_biz_trace_with_options_async(biz_trace_id, headers, runtime)

    def delete_cloud_resource_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudResource',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cloudresource',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_resource_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudResource',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cloudresource',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_resource(self) -> main_models.DeleteCloudResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_cloud_resource_with_options(headers, runtime)

    async def delete_cloud_resource_async(self) -> main_models.DeleteCloudResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_cloud_resource_with_options_async(headers, runtime)

    def delete_digital_employee_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDigitalEmployeeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDigitalEmployee',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDigitalEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_digital_employee_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDigitalEmployeeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDigitalEmployee',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDigitalEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_digital_employee(
        self,
        name: str,
    ) -> main_models.DeleteDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_digital_employee_with_options(name, headers, runtime)

    async def delete_digital_employee_async(
        self,
        name: str,
    ) -> main_models.DeleteDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_digital_employee_with_options_async(name, headers, runtime)

    def delete_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEntityStoreResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEntityStore',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}/entitystore',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEntityStoreResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEntityStore',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}/entitystore',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_entity_store(
        self,
        workspace_name: str,
    ) -> main_models.DeleteEntityStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_entity_store_with_options(workspace_name, headers, runtime)

    async def delete_entity_store_async(
        self,
        workspace_name: str,
    ) -> main_models.DeleteEntityStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_entity_store_with_options_async(workspace_name, headers, runtime)

    def delete_integration_policy_with_options(
        self,
        policy_id: str,
        request: main_models.DeleteIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntegrationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIntegrationPolicy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntegrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_integration_policy_with_options_async(
        self,
        policy_id: str,
        request: main_models.DeleteIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntegrationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIntegrationPolicy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntegrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_integration_policy(
        self,
        policy_id: str,
        request: main_models.DeleteIntegrationPolicyRequest,
    ) -> main_models.DeleteIntegrationPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_integration_policy_with_options(policy_id, request, headers, runtime)

    async def delete_integration_policy_async(
        self,
        policy_id: str,
        request: main_models.DeleteIntegrationPolicyRequest,
    ) -> main_models.DeleteIntegrationPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_integration_policy_with_options_async(policy_id, request, headers, runtime)

    def delete_prometheus_instance_with_options(
        self,
        prometheus_instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(prometheus_instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_instance_with_options_async(
        self,
        prometheus_instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(prometheus_instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_instance(
        self,
        prometheus_instance_id: str,
    ) -> main_models.DeletePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_prometheus_instance_with_options(prometheus_instance_id, headers, runtime)

    async def delete_prometheus_instance_async(
        self,
        prometheus_instance_id: str,
    ) -> main_models.DeletePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_prometheus_instance_with_options_async(prometheus_instance_id, headers, runtime)

    def delete_prometheus_view_with_options(
        self,
        prometheus_view_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusViewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusView',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views/{DaraURL.percent_encode(prometheus_view_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_view_with_options_async(
        self,
        prometheus_view_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusViewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusView',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views/{DaraURL.percent_encode(prometheus_view_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_view(
        self,
        prometheus_view_id: str,
    ) -> main_models.DeletePrometheusViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_prometheus_view_with_options(prometheus_view_id, headers, runtime)

    async def delete_prometheus_view_async(
        self,
        prometheus_view_id: str,
    ) -> main_models.DeletePrometheusViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_prometheus_view_with_options_async(prometheus_view_id, headers, runtime)

    def delete_service_with_options(
        self,
        workspace: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        workspace: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        workspace: str,
        service_id: str,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(workspace, service_id, headers, runtime)

    async def delete_service_async(
        self,
        workspace: str,
        service_id: str,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(workspace, service_id, headers, runtime)

    def delete_thread_with_options(
        self,
        name: str,
        thread_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteThreadResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteThread',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteThreadResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_thread_with_options_async(
        self,
        name: str,
        thread_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteThreadResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteThread',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteThreadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_thread(
        self,
        name: str,
        thread_id: str,
    ) -> main_models.DeleteThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_thread_with_options(name, thread_id, headers, runtime)

    async def delete_thread_async(
        self,
        name: str,
        thread_id: str,
    ) -> main_models.DeleteThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_thread_with_options_async(name, thread_id, headers, runtime)

    def delete_umodel_with_options(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUmodelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteUmodel',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_umodel_with_options_async(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUmodelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteUmodel',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_umodel(
        self,
        workspace: str,
    ) -> main_models.DeleteUmodelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_umodel_with_options(workspace, headers, runtime)

    async def delete_umodel_async(
        self,
        workspace: str,
    ) -> main_models.DeleteUmodelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_umodel_with_options_async(workspace, headers, runtime)

    def delete_umodel_common_schema_ref_with_options(
        self,
        workspace: str,
        request: main_models.DeleteUmodelCommonSchemaRefRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUmodelCommonSchemaRefResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUmodelCommonSchemaRef',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/common-schema-ref',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUmodelCommonSchemaRefResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_umodel_common_schema_ref_with_options_async(
        self,
        workspace: str,
        request: main_models.DeleteUmodelCommonSchemaRefRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUmodelCommonSchemaRefResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUmodelCommonSchemaRef',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/common-schema-ref',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUmodelCommonSchemaRefResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_umodel_common_schema_ref(
        self,
        workspace: str,
        request: main_models.DeleteUmodelCommonSchemaRefRequest,
    ) -> main_models.DeleteUmodelCommonSchemaRefResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_umodel_common_schema_ref_with_options(workspace, request, headers, runtime)

    async def delete_umodel_common_schema_ref_async(
        self,
        workspace: str,
        request: main_models.DeleteUmodelCommonSchemaRefRequest,
    ) -> main_models.DeleteUmodelCommonSchemaRefResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_umodel_common_schema_ref_with_options_async(workspace, request, headers, runtime)

    def delete_umodel_data_with_options(
        self,
        workspace: str,
        request: main_models.DeleteUmodelDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUmodelDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['domain'] = request.domain
        if not DaraCore.is_null(request.kind):
            query['kind'] = request.kind
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUmodelData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/data',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_umodel_data_with_options_async(
        self,
        workspace: str,
        request: main_models.DeleteUmodelDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUmodelDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['domain'] = request.domain
        if not DaraCore.is_null(request.kind):
            query['kind'] = request.kind
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUmodelData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/data',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_umodel_data(
        self,
        workspace: str,
        request: main_models.DeleteUmodelDataRequest,
    ) -> main_models.DeleteUmodelDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_umodel_data_with_options(workspace, request, headers, runtime)

    async def delete_umodel_data_async(
        self,
        workspace: str,
        request: main_models.DeleteUmodelDataRequest,
    ) -> main_models.DeleteUmodelDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_umodel_data_with_options_async(workspace, request, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        workspace_name: str,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_name, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_name: str,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_name, headers, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def get_addon_with_options(
        self,
        addon_name: str,
        request: main_models.GetAddonRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAddon',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/addons/{DaraURL.percent_encode(addon_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_with_options_async(
        self,
        addon_name: str,
        request: main_models.GetAddonRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAddon',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/addons/{DaraURL.percent_encode(addon_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon(
        self,
        addon_name: str,
        request: main_models.GetAddonRequest,
    ) -> main_models.GetAddonResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_addon_with_options(addon_name, request, headers, runtime)

    async def get_addon_async(
        self,
        addon_name: str,
        request: main_models.GetAddonRequest,
    ) -> main_models.GetAddonResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_addon_with_options_async(addon_name, request, headers, runtime)

    def get_addon_code_template_with_options(
        self,
        addon_name: str,
        request: main_models.GetAddonCodeTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonCodeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_type):
            query['environmentType'] = request.environment_type
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAddonCodeTemplate',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/addons/{DaraURL.percent_encode(addon_name)}/alert-code-template',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonCodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_code_template_with_options_async(
        self,
        addon_name: str,
        request: main_models.GetAddonCodeTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonCodeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_type):
            query['environmentType'] = request.environment_type
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAddonCodeTemplate',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/addons/{DaraURL.percent_encode(addon_name)}/alert-code-template',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonCodeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon_code_template(
        self,
        addon_name: str,
        request: main_models.GetAddonCodeTemplateRequest,
    ) -> main_models.GetAddonCodeTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_addon_code_template_with_options(addon_name, request, headers, runtime)

    async def get_addon_code_template_async(
        self,
        addon_name: str,
        request: main_models.GetAddonCodeTemplateRequest,
    ) -> main_models.GetAddonCodeTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_addon_code_template_with_options_async(addon_name, request, headers, runtime)

    def get_addon_release_with_options(
        self,
        release_name: str,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonReleaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAddonRelease',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases/{DaraURL.percent_encode(release_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_release_with_options_async(
        self,
        release_name: str,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonReleaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAddonRelease',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases/{DaraURL.percent_encode(release_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon_release(
        self,
        release_name: str,
        policy_id: str,
    ) -> main_models.GetAddonReleaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_addon_release_with_options(release_name, policy_id, headers, runtime)

    async def get_addon_release_async(
        self,
        release_name: str,
        policy_id: str,
    ) -> main_models.GetAddonReleaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_addon_release_with_options_async(release_name, policy_id, headers, runtime)

    def get_addon_schema_with_options(
        self,
        addon_name: str,
        request: main_models.GetAddonSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonSchemaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_type):
            query['environmentType'] = request.environment_type
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAddonSchema',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/addons/{DaraURL.percent_encode(addon_name)}/schema',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_schema_with_options_async(
        self,
        addon_name: str,
        request: main_models.GetAddonSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonSchemaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_type):
            query['environmentType'] = request.environment_type
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAddonSchema',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/addons/{DaraURL.percent_encode(addon_name)}/schema',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon_schema(
        self,
        addon_name: str,
        request: main_models.GetAddonSchemaRequest,
    ) -> main_models.GetAddonSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_addon_schema_with_options(addon_name, request, headers, runtime)

    async def get_addon_schema_async(
        self,
        addon_name: str,
        request: main_models.GetAddonSchemaRequest,
    ) -> main_models.GetAddonSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_addon_schema_with_options_async(addon_name, request, headers, runtime)

    def get_agg_task_group_with_options(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAggTaskGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAggTaskGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agg_task_group_with_options_async(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAggTaskGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAggTaskGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agg_task_group(
        self,
        instance_id: str,
        group_id: str,
    ) -> main_models.GetAggTaskGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agg_task_group_with_options(instance_id, group_id, headers, runtime)

    async def get_agg_task_group_async(
        self,
        instance_id: str,
        group_id: str,
    ) -> main_models.GetAggTaskGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agg_task_group_with_options_async(instance_id, group_id, headers, runtime)

    def get_biz_trace_with_options(
        self,
        biz_trace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBizTraceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBizTrace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTrace/{DaraURL.percent_encode(biz_trace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_trace_with_options_async(
        self,
        biz_trace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBizTraceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBizTrace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTrace/{DaraURL.percent_encode(biz_trace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_trace(
        self,
        biz_trace_id: str,
    ) -> main_models.GetBizTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_biz_trace_with_options(biz_trace_id, headers, runtime)

    async def get_biz_trace_async(
        self,
        biz_trace_id: str,
    ) -> main_models.GetBizTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_biz_trace_with_options_async(biz_trace_id, headers, runtime)

    def get_cloud_resource_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCloudResource',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cloudresource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_resource_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCloudResource',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cloudresource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_resource(self) -> main_models.GetCloudResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cloud_resource_with_options(headers, runtime)

    async def get_cloud_resource_async(self) -> main_models.GetCloudResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cloud_resource_with_options_async(headers, runtime)

    def get_cloud_resource_data_with_options(
        self,
        request: main_models.GetCloudResourceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudResourceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudResourceData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cloudresource/data',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudResourceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_resource_data_with_options_async(
        self,
        request: main_models.GetCloudResourceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudResourceDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudResourceData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cloudresource/data',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudResourceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_resource_data(
        self,
        request: main_models.GetCloudResourceDataRequest,
    ) -> main_models.GetCloudResourceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cloud_resource_data_with_options(request, headers, runtime)

    async def get_cloud_resource_data_async(
        self,
        request: main_models.GetCloudResourceDataRequest,
    ) -> main_models.GetCloudResourceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cloud_resource_data_with_options_async(request, headers, runtime)

    def get_cms_service_with_options(
        self,
        request: main_models.GetCmsServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCmsServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        if not DaraCore.is_null(request.service):
            query['service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCmsService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cmsservice',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cms_service_with_options_async(
        self,
        request: main_models.GetCmsServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCmsServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        if not DaraCore.is_null(request.service):
            query['service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCmsService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/cmsservice',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCmsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cms_service(
        self,
        request: main_models.GetCmsServiceRequest,
    ) -> main_models.GetCmsServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cms_service_with_options(request, headers, runtime)

    async def get_cms_service_async(
        self,
        request: main_models.GetCmsServiceRequest,
    ) -> main_models.GetCmsServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cms_service_with_options_async(request, headers, runtime)

    def get_digital_employee_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDigitalEmployeeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDigitalEmployee',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDigitalEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_digital_employee_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDigitalEmployeeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDigitalEmployee',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDigitalEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_digital_employee(
        self,
        name: str,
    ) -> main_models.GetDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_digital_employee_with_options(name, headers, runtime)

    async def get_digital_employee_async(
        self,
        name: str,
    ) -> main_models.GetDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_digital_employee_with_options_async(name, headers, runtime)

    def get_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEntityStoreResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEntityStore',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}/entitystore',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEntityStoreResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEntityStore',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}/entitystore',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_entity_store(
        self,
        workspace_name: str,
    ) -> main_models.GetEntityStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_entity_store_with_options(workspace_name, headers, runtime)

    async def get_entity_store_async(
        self,
        workspace_name: str,
    ) -> main_models.GetEntityStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_entity_store_with_options_async(workspace_name, headers, runtime)

    def get_entity_store_data_with_options(
        self,
        workspace: str,
        request: main_models.GetEntityStoreDataRequest,
        headers: main_models.GetEntityStoreDataHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetEntityStoreDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.from_):
            body['from'] = request.from_
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.to):
            body['to'] = request.to
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept_encoding):
            real_headers['acceptEncoding'] = str(headers.accept_encoding)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEntityStoreData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/entitiesAndRelations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEntityStoreDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_entity_store_data_with_options_async(
        self,
        workspace: str,
        request: main_models.GetEntityStoreDataRequest,
        headers: main_models.GetEntityStoreDataHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetEntityStoreDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.from_):
            body['from'] = request.from_
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.to):
            body['to'] = request.to
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept_encoding):
            real_headers['acceptEncoding'] = str(headers.accept_encoding)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEntityStoreData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/entitiesAndRelations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEntityStoreDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_entity_store_data(
        self,
        workspace: str,
        request: main_models.GetEntityStoreDataRequest,
    ) -> main_models.GetEntityStoreDataResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetEntityStoreDataHeaders()
        return self.get_entity_store_data_with_options(workspace, request, headers, runtime)

    async def get_entity_store_data_async(
        self,
        workspace: str,
        request: main_models.GetEntityStoreDataRequest,
    ) -> main_models.GetEntityStoreDataResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetEntityStoreDataHeaders()
        return await self.get_entity_store_data_with_options_async(workspace, request, headers, runtime)

    def get_integration_policy_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegrationPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIntegrationPolicy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_policy_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegrationPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIntegrationPolicy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_policy(
        self,
        policy_id: str,
    ) -> main_models.GetIntegrationPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_integration_policy_with_options(policy_id, headers, runtime)

    async def get_integration_policy_async(
        self,
        policy_id: str,
    ) -> main_models.GetIntegrationPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_integration_policy_with_options_async(policy_id, headers, runtime)

    def get_integration_version_for_cswith_options(
        self,
        request: main_models.GetIntegrationVersionForCSRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegrationVersionForCSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['clusterType'] = request.cluster_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIntegrationVersionForCS',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-version/cs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegrationVersionForCSResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_version_for_cswith_options_async(
        self,
        request: main_models.GetIntegrationVersionForCSRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegrationVersionForCSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['clusterType'] = request.cluster_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIntegrationVersionForCS',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-version/cs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegrationVersionForCSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_version_for_cs(
        self,
        request: main_models.GetIntegrationVersionForCSRequest,
    ) -> main_models.GetIntegrationVersionForCSResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_integration_version_for_cswith_options(request, headers, runtime)

    async def get_integration_version_for_cs_async(
        self,
        request: main_models.GetIntegrationVersionForCSRequest,
    ) -> main_models.GetIntegrationVersionForCSResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_integration_version_for_cswith_options_async(request, headers, runtime)

    def get_prometheus_instance_with_options(
        self,
        prometheus_instance_id: str,
        request: main_models.GetPrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(prometheus_instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_instance_with_options_async(
        self,
        prometheus_instance_id: str,
        request: main_models.GetPrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(prometheus_instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_instance(
        self,
        prometheus_instance_id: str,
        request: main_models.GetPrometheusInstanceRequest,
    ) -> main_models.GetPrometheusInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_prometheus_instance_with_options(prometheus_instance_id, request, headers, runtime)

    async def get_prometheus_instance_async(
        self,
        prometheus_instance_id: str,
        request: main_models.GetPrometheusInstanceRequest,
    ) -> main_models.GetPrometheusInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_prometheus_instance_with_options_async(prometheus_instance_id, request, headers, runtime)

    def get_prometheus_user_setting_with_options(
        self,
        request: main_models.GetPrometheusUserSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusUserSetting',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-user-setting',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_user_setting_with_options_async(
        self,
        request: main_models.GetPrometheusUserSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusUserSetting',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-user-setting',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_user_setting(
        self,
        request: main_models.GetPrometheusUserSettingRequest,
    ) -> main_models.GetPrometheusUserSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_prometheus_user_setting_with_options(request, headers, runtime)

    async def get_prometheus_user_setting_async(
        self,
        request: main_models.GetPrometheusUserSettingRequest,
    ) -> main_models.GetPrometheusUserSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_prometheus_user_setting_with_options_async(request, headers, runtime)

    def get_prometheus_view_with_options(
        self,
        prometheus_view_id: str,
        request: main_models.GetPrometheusViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusView',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views/{DaraURL.percent_encode(prometheus_view_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_view_with_options_async(
        self,
        prometheus_view_id: str,
        request: main_models.GetPrometheusViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusView',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views/{DaraURL.percent_encode(prometheus_view_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_view(
        self,
        prometheus_view_id: str,
        request: main_models.GetPrometheusViewRequest,
    ) -> main_models.GetPrometheusViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_prometheus_view_with_options(prometheus_view_id, request, headers, runtime)

    async def get_prometheus_view_async(
        self,
        prometheus_view_id: str,
        request: main_models.GetPrometheusViewRequest,
    ) -> main_models.GetPrometheusViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_prometheus_view_with_options_async(prometheus_view_id, request, headers, runtime)

    def get_service_with_options(
        self,
        workspace: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        workspace: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        workspace: str,
        service_id: str,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_with_options(workspace, service_id, headers, runtime)

    async def get_service_async(
        self,
        workspace: str,
        service_id: str,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(workspace, service_id, headers, runtime)

    def get_service_observability_with_options(
        self,
        workspace: str,
        type: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceObservabilityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceObservability',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service-observability/{DaraURL.percent_encode(type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceObservabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_observability_with_options_async(
        self,
        workspace: str,
        type: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceObservabilityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceObservability',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service-observability/{DaraURL.percent_encode(type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceObservabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_observability(
        self,
        workspace: str,
        type: str,
    ) -> main_models.GetServiceObservabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_observability_with_options(workspace, type, headers, runtime)

    async def get_service_observability_async(
        self,
        workspace: str,
        type: str,
    ) -> main_models.GetServiceObservabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_observability_with_options_async(workspace, type, headers, runtime)

    def get_thread_with_options(
        self,
        name: str,
        thread_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetThreadResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetThread',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetThreadResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_thread_with_options_async(
        self,
        name: str,
        thread_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetThreadResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetThread',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetThreadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_thread(
        self,
        name: str,
        thread_id: str,
    ) -> main_models.GetThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_thread_with_options(name, thread_id, headers, runtime)

    async def get_thread_async(
        self,
        name: str,
        thread_id: str,
    ) -> main_models.GetThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_thread_with_options_async(name, thread_id, headers, runtime)

    def get_thread_data_with_options(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetThreadDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetThreadData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}/data',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetThreadDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_thread_data_with_options_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetThreadDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetThreadData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}/data',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetThreadDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_thread_data(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadDataRequest,
    ) -> main_models.GetThreadDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_thread_data_with_options(name, thread_id, request, headers, runtime)

    async def get_thread_data_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadDataRequest,
    ) -> main_models.GetThreadDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_thread_data_with_options_async(name, thread_id, request, headers, runtime)

    def get_umodel_with_options(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUmodelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUmodel',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_umodel_with_options_async(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUmodelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUmodel',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_umodel(
        self,
        workspace: str,
    ) -> main_models.GetUmodelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_umodel_with_options(workspace, headers, runtime)

    async def get_umodel_async(
        self,
        workspace: str,
    ) -> main_models.GetUmodelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_umodel_with_options_async(workspace, headers, runtime)

    def get_umodel_common_schema_ref_with_options(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUmodelCommonSchemaRefResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUmodelCommonSchemaRef',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/common-schema-ref',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUmodelCommonSchemaRefResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_umodel_common_schema_ref_with_options_async(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUmodelCommonSchemaRefResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUmodelCommonSchemaRef',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/common-schema-ref',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUmodelCommonSchemaRefResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_umodel_common_schema_ref(
        self,
        workspace: str,
    ) -> main_models.GetUmodelCommonSchemaRefResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_umodel_common_schema_ref_with_options(workspace, headers, runtime)

    async def get_umodel_common_schema_ref_async(
        self,
        workspace: str,
    ) -> main_models.GetUmodelCommonSchemaRefResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_umodel_common_schema_ref_with_options_async(workspace, headers, runtime)

    def get_umodel_data_with_options(
        self,
        workspace: str,
        request: main_models.GetUmodelDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUmodelDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.method):
            query['method'] = request.method
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUmodelData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/graph',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_umodel_data_with_options_async(
        self,
        workspace: str,
        request: main_models.GetUmodelDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUmodelDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.method):
            query['method'] = request.method
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUmodelData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/graph',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_umodel_data(
        self,
        workspace: str,
        request: main_models.GetUmodelDataRequest,
    ) -> main_models.GetUmodelDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_umodel_data_with_options(workspace, request, headers, runtime)

    async def get_umodel_data_async(
        self,
        workspace: str,
        request: main_models.GetUmodelDataRequest,
    ) -> main_models.GetUmodelDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_umodel_data_with_options_async(workspace, request, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_name: str,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_name, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_name: str,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_name, headers, runtime)

    def list_addon_releases_with_options(
        self,
        policy_id: str,
        request: main_models.ListAddonReleasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonReleasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.parent_addon_release_id):
            query['parentAddonReleaseId'] = request.parent_addon_release_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddonReleases',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addon_releases_with_options_async(
        self,
        policy_id: str,
        request: main_models.ListAddonReleasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonReleasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.parent_addon_release_id):
            query['parentAddonReleaseId'] = request.parent_addon_release_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddonReleases',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonReleasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addon_releases(
        self,
        policy_id: str,
        request: main_models.ListAddonReleasesRequest,
    ) -> main_models.ListAddonReleasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_addon_releases_with_options(policy_id, request, headers, runtime)

    async def list_addon_releases_async(
        self,
        policy_id: str,
        request: main_models.ListAddonReleasesRequest,
    ) -> main_models.ListAddonReleasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_addon_releases_with_options_async(policy_id, request, headers, runtime)

    def list_addons_with_options(
        self,
        request: main_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.category):
            query['category'] = request.category
        if not DaraCore.is_null(request.regexp):
            query['regexp'] = request.regexp
        if not DaraCore.is_null(request.search):
            query['search'] = request.search
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddons',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/addons',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addons_with_options_async(
        self,
        request: main_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.category):
            query['category'] = request.category
        if not DaraCore.is_null(request.regexp):
            query['regexp'] = request.regexp
        if not DaraCore.is_null(request.search):
            query['search'] = request.search
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddons',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/addons',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addons(
        self,
        request: main_models.ListAddonsRequest,
    ) -> main_models.ListAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_addons_with_options(request, headers, runtime)

    async def list_addons_async(
        self,
        request: main_models.ListAddonsRequest,
    ) -> main_models.ListAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_addons_with_options_async(request, headers, runtime)

    def list_agg_task_groups_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.ListAggTaskGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAggTaskGroupsResponse:
        tmp_req.validate()
        request = main_models.ListAggTaskGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_agg_task_group_ids):
            query['filterAggTaskGroupIds'] = request.filter_agg_task_group_ids
        if not DaraCore.is_null(request.filter_agg_task_group_names):
            query['filterAggTaskGroupNames'] = request.filter_agg_task_group_names
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_prometheus_id):
            query['targetPrometheusId'] = request.target_prometheus_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggTaskGroups',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggTaskGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agg_task_groups_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.ListAggTaskGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAggTaskGroupsResponse:
        tmp_req.validate()
        request = main_models.ListAggTaskGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_agg_task_group_ids):
            query['filterAggTaskGroupIds'] = request.filter_agg_task_group_ids
        if not DaraCore.is_null(request.filter_agg_task_group_names):
            query['filterAggTaskGroupNames'] = request.filter_agg_task_group_names
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_prometheus_id):
            query['targetPrometheusId'] = request.target_prometheus_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggTaskGroups',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggTaskGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agg_task_groups(
        self,
        instance_id: str,
        request: main_models.ListAggTaskGroupsRequest,
    ) -> main_models.ListAggTaskGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agg_task_groups_with_options(instance_id, request, headers, runtime)

    async def list_agg_task_groups_async(
        self,
        instance_id: str,
        request: main_models.ListAggTaskGroupsRequest,
    ) -> main_models.ListAggTaskGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agg_task_groups_with_options_async(instance_id, request, headers, runtime)

    def list_alert_actions_with_options(
        self,
        tmp_req: main_models.ListAlertActionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertActionsResponse:
        tmp_req.validate()
        request = main_models.ListAlertActionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alert_action_ids):
            request.alert_action_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_action_ids, 'alertActionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.alert_action_ids_shrink):
            query['alertActionIds'] = request.alert_action_ids_shrink
        if not DaraCore.is_null(request.alert_action_name):
            query['alertActionName'] = request.alert_action_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertActions',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/alertActions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_actions_with_options_async(
        self,
        tmp_req: main_models.ListAlertActionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertActionsResponse:
        tmp_req.validate()
        request = main_models.ListAlertActionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alert_action_ids):
            request.alert_action_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_action_ids, 'alertActionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.alert_action_ids_shrink):
            query['alertActionIds'] = request.alert_action_ids_shrink
        if not DaraCore.is_null(request.alert_action_name):
            query['alertActionName'] = request.alert_action_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertActions',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/alertActions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_actions(
        self,
        request: main_models.ListAlertActionsRequest,
    ) -> main_models.ListAlertActionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_alert_actions_with_options(request, headers, runtime)

    async def list_alert_actions_async(
        self,
        request: main_models.ListAlertActionsRequest,
    ) -> main_models.ListAlertActionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_alert_actions_with_options_async(request, headers, runtime)

    def list_biz_traces_with_options(
        self,
        request: main_models.ListBizTracesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBizTracesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBizTraces',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTraces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBizTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_biz_traces_with_options_async(
        self,
        request: main_models.ListBizTracesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBizTracesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBizTraces',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTraces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBizTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_biz_traces(
        self,
        request: main_models.ListBizTracesRequest,
    ) -> main_models.ListBizTracesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_biz_traces_with_options(request, headers, runtime)

    async def list_biz_traces_async(
        self,
        request: main_models.ListBizTracesRequest,
    ) -> main_models.ListBizTracesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_biz_traces_with_options_async(request, headers, runtime)

    def list_digital_employees_with_options(
        self,
        request: main_models.ListDigitalEmployeesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDigitalEmployeesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDigitalEmployees',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDigitalEmployeesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_digital_employees_with_options_async(
        self,
        request: main_models.ListDigitalEmployeesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDigitalEmployeesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDigitalEmployees',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDigitalEmployeesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_digital_employees(
        self,
        request: main_models.ListDigitalEmployeesRequest,
    ) -> main_models.ListDigitalEmployeesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_digital_employees_with_options(request, headers, runtime)

    async def list_digital_employees_async(
        self,
        request: main_models.ListDigitalEmployeesRequest,
    ) -> main_models.ListDigitalEmployeesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_digital_employees_with_options_async(request, headers, runtime)

    def list_integration_policies_with_options(
        self,
        tmp_req: main_models.ListIntegrationPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPoliciesResponse:
        tmp_req.validate()
        request = main_models.ListIntegrationPoliciesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.bind_resource_id):
            query['bindResourceId'] = request.bind_resource_id
        if not DaraCore.is_null(request.entity_group_ids):
            query['entityGroupIds'] = request.entity_group_ids
        if not DaraCore.is_null(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_id):
            query['policyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            query['policyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['policyType'] = request.policy_type
        if not DaraCore.is_null(request.prometheus_instance_id):
            query['prometheusInstanceId'] = request.prometheus_instance_id
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicies',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policies_with_options_async(
        self,
        tmp_req: main_models.ListIntegrationPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPoliciesResponse:
        tmp_req.validate()
        request = main_models.ListIntegrationPoliciesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.bind_resource_id):
            query['bindResourceId'] = request.bind_resource_id
        if not DaraCore.is_null(request.entity_group_ids):
            query['entityGroupIds'] = request.entity_group_ids
        if not DaraCore.is_null(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_id):
            query['policyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            query['policyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['policyType'] = request.policy_type
        if not DaraCore.is_null(request.prometheus_instance_id):
            query['prometheusInstanceId'] = request.prometheus_instance_id
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicies',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policies(
        self,
        request: main_models.ListIntegrationPoliciesRequest,
    ) -> main_models.ListIntegrationPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_integration_policies_with_options(request, headers, runtime)

    async def list_integration_policies_async(
        self,
        request: main_models.ListIntegrationPoliciesRequest,
    ) -> main_models.ListIntegrationPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_integration_policies_with_options_async(request, headers, runtime)

    def list_integration_policy_addons_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyAddonsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyAddons',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addons',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_addons_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyAddonsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyAddons',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addons',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_addons(
        self,
        policy_id: str,
    ) -> main_models.ListIntegrationPolicyAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_integration_policy_addons_with_options(policy_id, headers, runtime)

    async def list_integration_policy_addons_async(
        self,
        policy_id: str,
    ) -> main_models.ListIntegrationPolicyAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_addons_with_options_async(policy_id, headers, runtime)

    def list_integration_policy_collectors_with_options(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyCollectorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyCollectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.collector_type):
            query['collectorType'] = request.collector_type
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyCollectors',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/collectors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyCollectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_collectors_with_options_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyCollectorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyCollectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.collector_type):
            query['collectorType'] = request.collector_type
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyCollectors',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/collectors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyCollectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_collectors(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyCollectorsRequest,
    ) -> main_models.ListIntegrationPolicyCollectorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_integration_policy_collectors_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_collectors_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyCollectorsRequest,
    ) -> main_models.ListIntegrationPolicyCollectorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_collectors_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_custom_scrape_job_rules_with_options(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyCustomScrapeJobRules',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/custom-scrape-job-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyCustomScrapeJobRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_custom_scrape_job_rules_with_options_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyCustomScrapeJobRules',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/custom-scrape-job-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyCustomScrapeJobRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_custom_scrape_job_rules(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
    ) -> main_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_integration_policy_custom_scrape_job_rules_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_custom_scrape_job_rules_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
    ) -> main_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_custom_scrape_job_rules_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_dashboards_with_options(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyDashboardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyDashboards',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_dashboards_with_options_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyDashboardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyDashboards',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_dashboards(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyDashboardsRequest,
    ) -> main_models.ListIntegrationPolicyDashboardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_integration_policy_dashboards_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_dashboards_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyDashboardsRequest,
    ) -> main_models.ListIntegrationPolicyDashboardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_dashboards_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_pod_monitors_with_options(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyPodMonitorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyPodMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyPodMonitors',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/pod-monitors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyPodMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_pod_monitors_with_options_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyPodMonitorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyPodMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyPodMonitors',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/pod-monitors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyPodMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_pod_monitors(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyPodMonitorsRequest,
    ) -> main_models.ListIntegrationPolicyPodMonitorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_integration_policy_pod_monitors_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_pod_monitors_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyPodMonitorsRequest,
    ) -> main_models.ListIntegrationPolicyPodMonitorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_pod_monitors_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_service_monitors_with_options(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyServiceMonitorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyServiceMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyServiceMonitors',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/service-monitors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyServiceMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_service_monitors_with_options_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyServiceMonitorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyServiceMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyServiceMonitors',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/service-monitors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyServiceMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_service_monitors(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyServiceMonitorsRequest,
    ) -> main_models.ListIntegrationPolicyServiceMonitorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_integration_policy_service_monitors_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_service_monitors_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyServiceMonitorsRequest,
    ) -> main_models.ListIntegrationPolicyServiceMonitorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_service_monitors_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_storage_requirements_with_options(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyStorageRequirementsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyStorageRequirementsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.storage_type):
            query['storageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyStorageRequirements',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/storage-requirements',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyStorageRequirementsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_storage_requirements_with_options_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyStorageRequirementsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationPolicyStorageRequirementsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['addonName'] = request.addon_name
        if not DaraCore.is_null(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not DaraCore.is_null(request.storage_type):
            query['storageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegrationPolicyStorageRequirements',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/storage-requirements',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationPolicyStorageRequirementsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_storage_requirements(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyStorageRequirementsRequest,
    ) -> main_models.ListIntegrationPolicyStorageRequirementsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_integration_policy_storage_requirements_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_storage_requirements_async(
        self,
        policy_id: str,
        request: main_models.ListIntegrationPolicyStorageRequirementsRequest,
    ) -> main_models.ListIntegrationPolicyStorageRequirementsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_storage_requirements_with_options_async(policy_id, request, headers, runtime)

    def list_prometheus_dashboards_with_options(
        self,
        prometheus_instance_id: str,
        request: main_models.ListPrometheusDashboardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusDashboards',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(prometheus_instance_id)}/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_dashboards_with_options_async(
        self,
        prometheus_instance_id: str,
        request: main_models.ListPrometheusDashboardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusDashboards',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(prometheus_instance_id)}/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_dashboards(
        self,
        prometheus_instance_id: str,
        request: main_models.ListPrometheusDashboardsRequest,
    ) -> main_models.ListPrometheusDashboardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_prometheus_dashboards_with_options(prometheus_instance_id, request, headers, runtime)

    async def list_prometheus_dashboards_async(
        self,
        prometheus_instance_id: str,
        request: main_models.ListPrometheusDashboardsRequest,
    ) -> main_models.ListPrometheusDashboardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_prometheus_dashboards_with_options_async(prometheus_instance_id, request, headers, runtime)

    def list_prometheus_instances_with_options(
        self,
        tmp_req: main_models.ListPrometheusInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusInstancesResponse:
        tmp_req.validate()
        request = main_models.ListPrometheusInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prometheus_instance_ids):
            query['prometheusInstanceIds'] = request.prometheus_instance_ids
        if not DaraCore.is_null(request.prometheus_instance_name):
            query['prometheusInstanceName'] = request.prometheus_instance_name
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusInstances',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_instances_with_options_async(
        self,
        tmp_req: main_models.ListPrometheusInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusInstancesResponse:
        tmp_req.validate()
        request = main_models.ListPrometheusInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prometheus_instance_ids):
            query['prometheusInstanceIds'] = request.prometheus_instance_ids
        if not DaraCore.is_null(request.prometheus_instance_name):
            query['prometheusInstanceName'] = request.prometheus_instance_name
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusInstances',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_instances(
        self,
        request: main_models.ListPrometheusInstancesRequest,
    ) -> main_models.ListPrometheusInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_prometheus_instances_with_options(request, headers, runtime)

    async def list_prometheus_instances_async(
        self,
        request: main_models.ListPrometheusInstancesRequest,
    ) -> main_models.ListPrometheusInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_prometheus_instances_with_options_async(request, headers, runtime)

    def list_prometheus_views_with_options(
        self,
        tmp_req: main_models.ListPrometheusViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusViewsResponse:
        tmp_req.validate()
        request = main_models.ListPrometheusViewsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prometheus_view_ids):
            query['prometheusViewIds'] = request.prometheus_view_ids
        if not DaraCore.is_null(request.prometheus_view_name):
            query['prometheusViewName'] = request.prometheus_view_name
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusViews',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_views_with_options_async(
        self,
        tmp_req: main_models.ListPrometheusViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusViewsResponse:
        tmp_req.validate()
        request = main_models.ListPrometheusViewsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prometheus_view_ids):
            query['prometheusViewIds'] = request.prometheus_view_ids
        if not DaraCore.is_null(request.prometheus_view_name):
            query['prometheusViewName'] = request.prometheus_view_name
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusViews',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_views(
        self,
        request: main_models.ListPrometheusViewsRequest,
    ) -> main_models.ListPrometheusViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_prometheus_views_with_options(request, headers, runtime)

    async def list_prometheus_views_async(
        self,
        request: main_models.ListPrometheusViewsRequest,
    ) -> main_models.ListPrometheusViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_prometheus_views_with_options_async(request, headers, runtime)

    def list_prometheus_virtual_instances_with_options(
        self,
        request: main_models.ListPrometheusVirtualInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusVirtualInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusVirtualInstances',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/virtual-instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusVirtualInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_virtual_instances_with_options_async(
        self,
        request: main_models.ListPrometheusVirtualInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusVirtualInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusVirtualInstances',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/virtual-instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusVirtualInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_virtual_instances(
        self,
        request: main_models.ListPrometheusVirtualInstancesRequest,
    ) -> main_models.ListPrometheusVirtualInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_prometheus_virtual_instances_with_options(request, headers, runtime)

    async def list_prometheus_virtual_instances_async(
        self,
        request: main_models.ListPrometheusVirtualInstancesRequest,
    ) -> main_models.ListPrometheusVirtualInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_prometheus_virtual_instances_with_options_async(request, headers, runtime)

    def list_services_with_options(
        self,
        workspace: str,
        tmp_req: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        tmp_req.validate()
        request = main_models.ListServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        workspace: str,
        tmp_req: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        tmp_req.validate()
        request = main_models.ListServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        workspace: str,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_services_with_options(workspace, request, headers, runtime)

    async def list_services_async(
        self,
        workspace: str,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(workspace, request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_threads_with_options(
        self,
        name: str,
        tmp_req: main_models.ListThreadsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListThreadsResponse:
        tmp_req.validate()
        request = main_models.ListThreadsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.thread_id):
            query['threadId'] = request.thread_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListThreads',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/threads',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListThreadsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_threads_with_options_async(
        self,
        name: str,
        tmp_req: main_models.ListThreadsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListThreadsResponse:
        tmp_req.validate()
        request = main_models.ListThreadsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.thread_id):
            query['threadId'] = request.thread_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListThreads',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/threads',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListThreadsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_threads(
        self,
        name: str,
        request: main_models.ListThreadsRequest,
    ) -> main_models.ListThreadsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_threads_with_options(name, request, headers, runtime)

    async def list_threads_async(
        self,
        name: str,
        request: main_models.ListThreadsRequest,
    ) -> main_models.ListThreadsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_threads_with_options_async(name, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        tmp_req.validate()
        request = main_models.ListWorkspacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workspace_name_list):
            request.workspace_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.workspace_name_list, 'workspaceNameList', 'simple')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        if not DaraCore.is_null(request.workspace_name_list_shrink):
            query['workspaceNameList'] = request.workspace_name_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        tmp_req.validate()
        request = main_models.ListWorkspacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workspace_name_list):
            request.workspace_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.workspace_name_list, 'workspaceNameList', 'simple')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        if not DaraCore.is_null(request.workspace_name_list_shrink):
            query['workspaceNameList'] = request.workspace_name_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def put_workspace_with_options(
        self,
        workspace_name: str,
        request: main_models.PutWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutWorkspace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_workspace_with_options_async(
        self,
        workspace_name: str,
        request: main_models.PutWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutWorkspace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_workspace(
        self,
        workspace_name: str,
        request: main_models.PutWorkspaceRequest,
    ) -> main_models.PutWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_workspace_with_options(workspace_name, request, headers, runtime)

    async def put_workspace_async(
        self,
        workspace_name: str,
        request: main_models.PutWorkspaceRequest,
    ) -> main_models.PutWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_workspace_with_options_async(workspace_name, request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'tagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['tagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'tagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['tagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_addon_release_with_options(
        self,
        release_name: str,
        policy_id: str,
        request: main_models.UpdateAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAddonReleaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.addon_version):
            body['addonVersion'] = request.addon_version
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.entity_rules):
            body['entityRules'] = request.entity_rules
        if not DaraCore.is_null(request.values):
            body['values'] = request.values
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAddonRelease',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases/{DaraURL.percent_encode(release_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_addon_release_with_options_async(
        self,
        release_name: str,
        policy_id: str,
        request: main_models.UpdateAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAddonReleaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.addon_version):
            body['addonVersion'] = request.addon_version
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.entity_rules):
            body['entityRules'] = request.entity_rules
        if not DaraCore.is_null(request.values):
            body['values'] = request.values
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAddonRelease',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(policy_id)}/addon-releases/{DaraURL.percent_encode(release_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_addon_release(
        self,
        release_name: str,
        policy_id: str,
        request: main_models.UpdateAddonReleaseRequest,
    ) -> main_models.UpdateAddonReleaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_addon_release_with_options(release_name, policy_id, request, headers, runtime)

    async def update_addon_release_async(
        self,
        release_name: str,
        policy_id: str,
        request: main_models.UpdateAddonReleaseRequest,
    ) -> main_models.UpdateAddonReleaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_addon_release_with_options_async(release_name, policy_id, request, headers, runtime)

    def update_agg_task_group_with_options(
        self,
        instance_id: str,
        group_id: str,
        request: main_models.UpdateAggTaskGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggTaskGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agg_task_group_config):
            body['aggTaskGroupConfig'] = request.agg_task_group_config
        if not DaraCore.is_null(request.agg_task_group_config_type):
            body['aggTaskGroupConfigType'] = request.agg_task_group_config_type
        if not DaraCore.is_null(request.agg_task_group_name):
            body['aggTaskGroupName'] = request.agg_task_group_name
        if not DaraCore.is_null(request.cron_expr):
            body['cronExpr'] = request.cron_expr
        if not DaraCore.is_null(request.delay):
            body['delay'] = request.delay
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.from_time):
            body['fromTime'] = request.from_time
        if not DaraCore.is_null(request.max_retries):
            body['maxRetries'] = request.max_retries
        if not DaraCore.is_null(request.max_run_time_in_seconds):
            body['maxRunTimeInSeconds'] = request.max_run_time_in_seconds
        if not DaraCore.is_null(request.precheck_string):
            body['precheckString'] = request.precheck_string
        if not DaraCore.is_null(request.schedule_mode):
            body['scheduleMode'] = request.schedule_mode
        if not DaraCore.is_null(request.schedule_time_expr):
            body['scheduleTimeExpr'] = request.schedule_time_expr
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.target_prometheus_id):
            body['targetPrometheusId'] = request.target_prometheus_id
        if not DaraCore.is_null(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggTaskGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups/{DaraURL.percent_encode(group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agg_task_group_with_options_async(
        self,
        instance_id: str,
        group_id: str,
        request: main_models.UpdateAggTaskGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggTaskGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agg_task_group_config):
            body['aggTaskGroupConfig'] = request.agg_task_group_config
        if not DaraCore.is_null(request.agg_task_group_config_type):
            body['aggTaskGroupConfigType'] = request.agg_task_group_config_type
        if not DaraCore.is_null(request.agg_task_group_name):
            body['aggTaskGroupName'] = request.agg_task_group_name
        if not DaraCore.is_null(request.cron_expr):
            body['cronExpr'] = request.cron_expr
        if not DaraCore.is_null(request.delay):
            body['delay'] = request.delay
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.from_time):
            body['fromTime'] = request.from_time
        if not DaraCore.is_null(request.max_retries):
            body['maxRetries'] = request.max_retries
        if not DaraCore.is_null(request.max_run_time_in_seconds):
            body['maxRunTimeInSeconds'] = request.max_run_time_in_seconds
        if not DaraCore.is_null(request.precheck_string):
            body['precheckString'] = request.precheck_string
        if not DaraCore.is_null(request.schedule_mode):
            body['scheduleMode'] = request.schedule_mode
        if not DaraCore.is_null(request.schedule_time_expr):
            body['scheduleTimeExpr'] = request.schedule_time_expr
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.target_prometheus_id):
            body['targetPrometheusId'] = request.target_prometheus_id
        if not DaraCore.is_null(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggTaskGroup',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups/{DaraURL.percent_encode(group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agg_task_group(
        self,
        instance_id: str,
        group_id: str,
        request: main_models.UpdateAggTaskGroupRequest,
    ) -> main_models.UpdateAggTaskGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agg_task_group_with_options(instance_id, group_id, request, headers, runtime)

    async def update_agg_task_group_async(
        self,
        instance_id: str,
        group_id: str,
        request: main_models.UpdateAggTaskGroupRequest,
    ) -> main_models.UpdateAggTaskGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agg_task_group_with_options_async(instance_id, group_id, request, headers, runtime)

    def update_agg_task_group_status_with_options(
        self,
        instance_id: str,
        group_id: str,
        request: main_models.UpdateAggTaskGroupStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggTaskGroupStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggTaskGroupStatus',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups/{DaraURL.percent_encode(group_id)}/status',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggTaskGroupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agg_task_group_status_with_options_async(
        self,
        instance_id: str,
        group_id: str,
        request: main_models.UpdateAggTaskGroupStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggTaskGroupStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggTaskGroupStatus',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(instance_id)}/agg-task-groups/{DaraURL.percent_encode(group_id)}/status',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggTaskGroupStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agg_task_group_status(
        self,
        instance_id: str,
        group_id: str,
        request: main_models.UpdateAggTaskGroupStatusRequest,
    ) -> main_models.UpdateAggTaskGroupStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agg_task_group_status_with_options(instance_id, group_id, request, headers, runtime)

    async def update_agg_task_group_status_async(
        self,
        instance_id: str,
        group_id: str,
        request: main_models.UpdateAggTaskGroupStatusRequest,
    ) -> main_models.UpdateAggTaskGroupStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agg_task_group_status_with_options_async(instance_id, group_id, request, headers, runtime)

    def update_biz_trace_with_options(
        self,
        biz_trace_id: str,
        request: main_models.UpdateBizTraceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBizTraceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_config):
            body['advancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.biz_trace_name):
            body['bizTraceName'] = request.biz_trace_name
        if not DaraCore.is_null(request.rule_config):
            body['ruleConfig'] = request.rule_config
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBizTrace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTrace/{DaraURL.percent_encode(biz_trace_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBizTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_trace_with_options_async(
        self,
        biz_trace_id: str,
        request: main_models.UpdateBizTraceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBizTraceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_config):
            body['advancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.biz_trace_name):
            body['bizTraceName'] = request.biz_trace_name
        if not DaraCore.is_null(request.rule_config):
            body['ruleConfig'] = request.rule_config
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBizTrace',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/bizTrace/{DaraURL.percent_encode(biz_trace_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBizTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_trace(
        self,
        biz_trace_id: str,
        request: main_models.UpdateBizTraceRequest,
    ) -> main_models.UpdateBizTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_biz_trace_with_options(biz_trace_id, request, headers, runtime)

    async def update_biz_trace_async(
        self,
        biz_trace_id: str,
        request: main_models.UpdateBizTraceRequest,
    ) -> main_models.UpdateBizTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_biz_trace_with_options_async(biz_trace_id, request, headers, runtime)

    def update_digital_employee_with_options(
        self,
        name: str,
        request: main_models.UpdateDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDigitalEmployeeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_rule):
            body['defaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.knowledges):
            body['knowledges'] = request.knowledges
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDigitalEmployee',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDigitalEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_digital_employee_with_options_async(
        self,
        name: str,
        request: main_models.UpdateDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDigitalEmployeeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_rule):
            body['defaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.knowledges):
            body['knowledges'] = request.knowledges
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDigitalEmployee',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDigitalEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_digital_employee(
        self,
        name: str,
        request: main_models.UpdateDigitalEmployeeRequest,
    ) -> main_models.UpdateDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_digital_employee_with_options(name, request, headers, runtime)

    async def update_digital_employee_async(
        self,
        name: str,
        request: main_models.UpdateDigitalEmployeeRequest,
    ) -> main_models.UpdateDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_digital_employee_with_options_async(name, request, headers, runtime)

    def update_integration_policy_with_options(
        self,
        integration_policy_id: str,
        request: main_models.UpdateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIntegrationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fee_package):
            body['feePackage'] = request.fee_package
        if not DaraCore.is_null(request.policy_name):
            body['policyName'] = request.policy_name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIntegrationPolicy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(integration_policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIntegrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_integration_policy_with_options_async(
        self,
        integration_policy_id: str,
        request: main_models.UpdateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIntegrationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fee_package):
            body['feePackage'] = request.fee_package
        if not DaraCore.is_null(request.policy_name):
            body['policyName'] = request.policy_name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIntegrationPolicy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/integration-policies/{DaraURL.percent_encode(integration_policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIntegrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_integration_policy(
        self,
        integration_policy_id: str,
        request: main_models.UpdateIntegrationPolicyRequest,
    ) -> main_models.UpdateIntegrationPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_integration_policy_with_options(integration_policy_id, request, headers, runtime)

    async def update_integration_policy_async(
        self,
        integration_policy_id: str,
        request: main_models.UpdateIntegrationPolicyRequest,
    ) -> main_models.UpdateIntegrationPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_integration_policy_with_options_async(integration_policy_id, request, headers, runtime)

    def update_notify_strategy_with_options(
        self,
        notify_strategy_id: str,
        request: main_models.UpdateNotifyStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNotifyStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNotifyStrategy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/notifyStrategies/{DaraURL.percent_encode(notify_strategy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNotifyStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_notify_strategy_with_options_async(
        self,
        notify_strategy_id: str,
        request: main_models.UpdateNotifyStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNotifyStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNotifyStrategy',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/notifyStrategies/{DaraURL.percent_encode(notify_strategy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNotifyStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_notify_strategy(
        self,
        notify_strategy_id: str,
        request: main_models.UpdateNotifyStrategyRequest,
    ) -> main_models.UpdateNotifyStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_notify_strategy_with_options(notify_strategy_id, request, headers, runtime)

    async def update_notify_strategy_async(
        self,
        notify_strategy_id: str,
        request: main_models.UpdateNotifyStrategyRequest,
    ) -> main_models.UpdateNotifyStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_notify_strategy_with_options_async(notify_strategy_id, request, headers, runtime)

    def update_prometheus_instance_with_options(
        self,
        prometheus_instance_id: str,
        request: main_models.UpdatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not DaraCore.is_null(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not DaraCore.is_null(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not DaraCore.is_null(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(prometheus_instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_instance_with_options_async(
        self,
        prometheus_instance_id: str,
        request: main_models.UpdatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not DaraCore.is_null(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not DaraCore.is_null(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not DaraCore.is_null(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusInstance',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-instances/{DaraURL.percent_encode(prometheus_instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_instance(
        self,
        prometheus_instance_id: str,
        request: main_models.UpdatePrometheusInstanceRequest,
    ) -> main_models.UpdatePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_prometheus_instance_with_options(prometheus_instance_id, request, headers, runtime)

    async def update_prometheus_instance_async(
        self,
        prometheus_instance_id: str,
        request: main_models.UpdatePrometheusInstanceRequest,
    ) -> main_models.UpdatePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_prometheus_instance_with_options_async(prometheus_instance_id, request, headers, runtime)

    def update_prometheus_user_setting_with_options(
        self,
        setting_key: str,
        request: main_models.UpdatePrometheusUserSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.setting_value):
            query['settingValue'] = request.setting_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusUserSetting',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-user-setting/{DaraURL.percent_encode(setting_key)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_user_setting_with_options_async(
        self,
        setting_key: str,
        request: main_models.UpdatePrometheusUserSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.setting_value):
            query['settingValue'] = request.setting_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusUserSetting',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-user-setting/{DaraURL.percent_encode(setting_key)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_user_setting(
        self,
        setting_key: str,
        request: main_models.UpdatePrometheusUserSettingRequest,
    ) -> main_models.UpdatePrometheusUserSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_prometheus_user_setting_with_options(setting_key, request, headers, runtime)

    async def update_prometheus_user_setting_async(
        self,
        setting_key: str,
        request: main_models.UpdatePrometheusUserSettingRequest,
    ) -> main_models.UpdatePrometheusUserSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_prometheus_user_setting_with_options_async(setting_key, request, headers, runtime)

    def update_prometheus_view_with_options(
        self,
        prometheus_view_id: str,
        request: main_models.UpdatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusViewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.prometheus_instances):
            body['prometheusInstances'] = request.prometheus_instances
        if not DaraCore.is_null(request.prometheus_view_name):
            body['prometheusViewName'] = request.prometheus_view_name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusView',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views/{DaraURL.percent_encode(prometheus_view_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_view_with_options_async(
        self,
        prometheus_view_id: str,
        request: main_models.UpdatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusViewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.prometheus_instances):
            body['prometheusInstances'] = request.prometheus_instances
        if not DaraCore.is_null(request.prometheus_view_name):
            body['prometheusViewName'] = request.prometheus_view_name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusView',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/prometheus-views/{DaraURL.percent_encode(prometheus_view_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_view(
        self,
        prometheus_view_id: str,
        request: main_models.UpdatePrometheusViewRequest,
    ) -> main_models.UpdatePrometheusViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_prometheus_view_with_options(prometheus_view_id, request, headers, runtime)

    async def update_prometheus_view_async(
        self,
        prometheus_view_id: str,
        request: main_models.UpdatePrometheusViewRequest,
    ) -> main_models.UpdatePrometheusViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_prometheus_view_with_options_async(prometheus_view_id, request, headers, runtime)

    def update_service_with_options(
        self,
        workspace: str,
        service_id: str,
        request: main_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.service_status):
            body['serviceStatus'] = request.service_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service/{DaraURL.percent_encode(service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        workspace: str,
        service_id: str,
        request: main_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.service_status):
            body['serviceStatus'] = request.service_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/service/{DaraURL.percent_encode(service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        workspace: str,
        service_id: str,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_with_options(workspace, service_id, request, headers, runtime)

    async def update_service_async(
        self,
        workspace: str,
        service_id: str,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(workspace, service_id, request, headers, runtime)

    def update_subscription_with_options(
        self,
        subscription_id: str,
        request: main_models.UpdateSubscriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubscription',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/subscriptions/{DaraURL.percent_encode(subscription_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscription_with_options_async(
        self,
        subscription_id: str,
        request: main_models.UpdateSubscriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubscription',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/subscriptions/{DaraURL.percent_encode(subscription_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscription(
        self,
        subscription_id: str,
        request: main_models.UpdateSubscriptionRequest,
    ) -> main_models.UpdateSubscriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_subscription_with_options(subscription_id, request, headers, runtime)

    async def update_subscription_async(
        self,
        subscription_id: str,
        request: main_models.UpdateSubscriptionRequest,
    ) -> main_models.UpdateSubscriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_subscription_with_options_async(subscription_id, request, headers, runtime)

    def update_thread_with_options(
        self,
        name: str,
        thread_id: str,
        request: main_models.UpdateThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateThreadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateThread',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateThreadResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_thread_with_options_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.UpdateThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateThreadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateThread',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateThreadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_thread(
        self,
        name: str,
        thread_id: str,
        request: main_models.UpdateThreadRequest,
    ) -> main_models.UpdateThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_thread_with_options(name, thread_id, request, headers, runtime)

    async def update_thread_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.UpdateThreadRequest,
    ) -> main_models.UpdateThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_thread_with_options_async(name, thread_id, request, headers, runtime)

    def update_umodel_with_options(
        self,
        workspace: str,
        request: main_models.UpdateUmodelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUmodelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUmodel',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_umodel_with_options_async(
        self,
        workspace: str,
        request: main_models.UpdateUmodelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUmodelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUmodel',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_umodel(
        self,
        workspace: str,
        request: main_models.UpdateUmodelRequest,
    ) -> main_models.UpdateUmodelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_umodel_with_options(workspace, request, headers, runtime)

    async def update_umodel_async(
        self,
        workspace: str,
        request: main_models.UpdateUmodelRequest,
    ) -> main_models.UpdateUmodelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_umodel_with_options_async(workspace, request, headers, runtime)

    def upsert_umodel_common_schema_ref_with_options(
        self,
        workspace: str,
        request: main_models.UpsertUmodelCommonSchemaRefRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpsertUmodelCommonSchemaRefResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpsertUmodelCommonSchemaRef',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/common-schema-ref',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertUmodelCommonSchemaRefResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_umodel_common_schema_ref_with_options_async(
        self,
        workspace: str,
        request: main_models.UpsertUmodelCommonSchemaRefRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpsertUmodelCommonSchemaRefResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpsertUmodelCommonSchemaRef',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/common-schema-ref',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertUmodelCommonSchemaRefResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_umodel_common_schema_ref(
        self,
        workspace: str,
        request: main_models.UpsertUmodelCommonSchemaRefRequest,
    ) -> main_models.UpsertUmodelCommonSchemaRefResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upsert_umodel_common_schema_ref_with_options(workspace, request, headers, runtime)

    async def upsert_umodel_common_schema_ref_async(
        self,
        workspace: str,
        request: main_models.UpsertUmodelCommonSchemaRefRequest,
    ) -> main_models.UpsertUmodelCommonSchemaRefResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upsert_umodel_common_schema_ref_with_options_async(workspace, request, headers, runtime)

    def upsert_umodel_data_with_options(
        self,
        workspace: str,
        request: main_models.UpsertUmodelDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpsertUmodelDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.method):
            query['method'] = request.method
        body = {}
        if not DaraCore.is_null(request.elements):
            body['elements'] = request.elements
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertUmodelData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/data',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_umodel_data_with_options_async(
        self,
        workspace: str,
        request: main_models.UpsertUmodelDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpsertUmodelDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.method):
            query['method'] = request.method
        body = {}
        if not DaraCore.is_null(request.elements):
            body['elements'] = request.elements
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertUmodelData',
            version = '2024-03-30',
            protocol = 'HTTPS',
            pathname = f'/workspace/{DaraURL.percent_encode(workspace)}/umodel/data',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_umodel_data(
        self,
        workspace: str,
        request: main_models.UpsertUmodelDataRequest,
    ) -> main_models.UpsertUmodelDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upsert_umodel_data_with_options(workspace, request, headers, runtime)

    async def upsert_umodel_data_async(
        self,
        workspace: str,
        request: main_models.UpsertUmodelDataRequest,
    ) -> main_models.UpsertUmodelDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upsert_umodel_data_with_options_async(workspace, request, headers, runtime)
