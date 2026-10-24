# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_csasedr20241122 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('csasedr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_client_rule_strategy_with_options(
        self,
        tmp_req: main_models.CreateClientRuleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientRuleStrategyResponse:
        tmp_req.validate()
        request = main_models.CreateClientRuleStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_user_name_list):
            request.exclude_user_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_user_name_list, 'ExcludeUserNameList', 'json')
        if not DaraCore.is_null(tmp_req.include_group_id_list):
            request.include_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_group_id_list, 'IncludeGroupIdList', 'json')
        if not DaraCore.is_null(tmp_req.port_on_list):
            request.port_on_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.port_on_list, 'PortOnList', 'json')
        if not DaraCore.is_null(tmp_req.soft_ware_on_list):
            request.soft_ware_on_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.soft_ware_on_list, 'SoftWareOnList', 'json')
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.all_group):
            query['AllGroup'] = request.all_group
        if not DaraCore.is_null(request.approval_id):
            query['ApprovalId'] = request.approval_id
        if not DaraCore.is_null(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.exclude_user_name_list_shrink):
            query['ExcludeUserNameList'] = request.exclude_user_name_list_shrink
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.in_switch):
            query['InSwitch'] = request.in_switch
        if not DaraCore.is_null(request.include_group_id_list_shrink):
            query['IncludeGroupIdList'] = request.include_group_id_list_shrink
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.main_button_text_ch):
            query['MainButtonTextCh'] = request.main_button_text_ch
        if not DaraCore.is_null(request.main_button_text_en):
            query['MainButtonTextEn'] = request.main_button_text_en
        if not DaraCore.is_null(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.match_target_ids):
            query['MatchTargetIds'] = request.match_target_ids
        if not DaraCore.is_null(request.md_5list):
            query['Md5List'] = request.md_5list
        if not DaraCore.is_null(request.minor_button_text_ch):
            query['MinorButtonTextCh'] = request.minor_button_text_ch
        if not DaraCore.is_null(request.minor_button_text_en):
            query['MinorButtonTextEn'] = request.minor_button_text_en
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.new_file_path):
            query['NewFilePath'] = request.new_file_path
        if not DaraCore.is_null(request.out_switch):
            query['OutSwitch'] = request.out_switch
        if not DaraCore.is_null(request.parent_cmdline):
            query['ParentCmdline'] = request.parent_cmdline
        if not DaraCore.is_null(request.parent_proc_path):
            query['ParentProcPath'] = request.parent_proc_path
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.port_on_list_shrink):
            query['PortOnList'] = request.port_on_list_shrink
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.proc_path):
            query['ProcPath'] = request.proc_path
        if not DaraCore.is_null(request.registry_content):
            query['RegistryContent'] = request.registry_content
        if not DaraCore.is_null(request.registry_key):
            query['RegistryKey'] = request.registry_key
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.selection_key):
            query['SelectionKey'] = request.selection_key
        if not DaraCore.is_null(request.soft_ware_on_list_shrink):
            query['SoftWareOnList'] = request.soft_ware_on_list_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strategy_source_type):
            query['StrategySourceType'] = request.strategy_source_type
        if not DaraCore.is_null(request.supports_approval):
            query['SupportsApproval'] = request.supports_approval
        if not DaraCore.is_null(request.us_content):
            query['UsContent'] = request.us_content
        if not DaraCore.is_null(request.us_title):
            query['UsTitle'] = request.us_title
        if not DaraCore.is_null(request.zh_content):
            query['ZhContent'] = request.zh_content
        if not DaraCore.is_null(request.zh_title):
            query['ZhTitle'] = request.zh_title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientRuleStrategy',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientRuleStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_rule_strategy_with_options_async(
        self,
        tmp_req: main_models.CreateClientRuleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientRuleStrategyResponse:
        tmp_req.validate()
        request = main_models.CreateClientRuleStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_user_name_list):
            request.exclude_user_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_user_name_list, 'ExcludeUserNameList', 'json')
        if not DaraCore.is_null(tmp_req.include_group_id_list):
            request.include_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_group_id_list, 'IncludeGroupIdList', 'json')
        if not DaraCore.is_null(tmp_req.port_on_list):
            request.port_on_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.port_on_list, 'PortOnList', 'json')
        if not DaraCore.is_null(tmp_req.soft_ware_on_list):
            request.soft_ware_on_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.soft_ware_on_list, 'SoftWareOnList', 'json')
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.all_group):
            query['AllGroup'] = request.all_group
        if not DaraCore.is_null(request.approval_id):
            query['ApprovalId'] = request.approval_id
        if not DaraCore.is_null(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.exclude_user_name_list_shrink):
            query['ExcludeUserNameList'] = request.exclude_user_name_list_shrink
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.in_switch):
            query['InSwitch'] = request.in_switch
        if not DaraCore.is_null(request.include_group_id_list_shrink):
            query['IncludeGroupIdList'] = request.include_group_id_list_shrink
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.main_button_text_ch):
            query['MainButtonTextCh'] = request.main_button_text_ch
        if not DaraCore.is_null(request.main_button_text_en):
            query['MainButtonTextEn'] = request.main_button_text_en
        if not DaraCore.is_null(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.match_target_ids):
            query['MatchTargetIds'] = request.match_target_ids
        if not DaraCore.is_null(request.md_5list):
            query['Md5List'] = request.md_5list
        if not DaraCore.is_null(request.minor_button_text_ch):
            query['MinorButtonTextCh'] = request.minor_button_text_ch
        if not DaraCore.is_null(request.minor_button_text_en):
            query['MinorButtonTextEn'] = request.minor_button_text_en
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.new_file_path):
            query['NewFilePath'] = request.new_file_path
        if not DaraCore.is_null(request.out_switch):
            query['OutSwitch'] = request.out_switch
        if not DaraCore.is_null(request.parent_cmdline):
            query['ParentCmdline'] = request.parent_cmdline
        if not DaraCore.is_null(request.parent_proc_path):
            query['ParentProcPath'] = request.parent_proc_path
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.port_on_list_shrink):
            query['PortOnList'] = request.port_on_list_shrink
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.proc_path):
            query['ProcPath'] = request.proc_path
        if not DaraCore.is_null(request.registry_content):
            query['RegistryContent'] = request.registry_content
        if not DaraCore.is_null(request.registry_key):
            query['RegistryKey'] = request.registry_key
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.selection_key):
            query['SelectionKey'] = request.selection_key
        if not DaraCore.is_null(request.soft_ware_on_list_shrink):
            query['SoftWareOnList'] = request.soft_ware_on_list_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strategy_source_type):
            query['StrategySourceType'] = request.strategy_source_type
        if not DaraCore.is_null(request.supports_approval):
            query['SupportsApproval'] = request.supports_approval
        if not DaraCore.is_null(request.us_content):
            query['UsContent'] = request.us_content
        if not DaraCore.is_null(request.us_title):
            query['UsTitle'] = request.us_title
        if not DaraCore.is_null(request.zh_content):
            query['ZhContent'] = request.zh_content
        if not DaraCore.is_null(request.zh_title):
            query['ZhTitle'] = request.zh_title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientRuleStrategy',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientRuleStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_rule_strategy(
        self,
        request: main_models.CreateClientRuleStrategyRequest,
    ) -> main_models.CreateClientRuleStrategyResponse:
        runtime = RuntimeOptions()
        return self.create_client_rule_strategy_with_options(request, runtime)

    async def create_client_rule_strategy_async(
        self,
        request: main_models.CreateClientRuleStrategyRequest,
    ) -> main_models.CreateClientRuleStrategyResponse:
        runtime = RuntimeOptions()
        return await self.create_client_rule_strategy_with_options_async(request, runtime)

    def create_selection_config_with_options(
        self,
        request: main_models.CreateSelectionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSelectionConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CreateSelectionConfig',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSelectionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_selection_config_with_options_async(
        self,
        request: main_models.CreateSelectionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSelectionConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CreateSelectionConfig',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSelectionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_selection_config(
        self,
        request: main_models.CreateSelectionConfigRequest,
    ) -> main_models.CreateSelectionConfigResponse:
        runtime = RuntimeOptions()
        return self.create_selection_config_with_options(request, runtime)

    async def create_selection_config_async(
        self,
        request: main_models.CreateSelectionConfigRequest,
    ) -> main_models.CreateSelectionConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_selection_config_with_options_async(request, runtime)

    def create_similar_security_events_query_task_with_options(
        self,
        request: main_models.CreateSimilarSecurityEventsQueryTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimilarSecurityEventsQueryTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not DaraCore.is_null(request.similar_event_scenario_code):
            query['SimilarEventScenarioCode'] = request.similar_event_scenario_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimilarSecurityEventsQueryTask',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimilarSecurityEventsQueryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_similar_security_events_query_task_with_options_async(
        self,
        request: main_models.CreateSimilarSecurityEventsQueryTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimilarSecurityEventsQueryTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not DaraCore.is_null(request.similar_event_scenario_code):
            query['SimilarEventScenarioCode'] = request.similar_event_scenario_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimilarSecurityEventsQueryTask',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimilarSecurityEventsQueryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_similar_security_events_query_task(
        self,
        request: main_models.CreateSimilarSecurityEventsQueryTaskRequest,
    ) -> main_models.CreateSimilarSecurityEventsQueryTaskResponse:
        runtime = RuntimeOptions()
        return self.create_similar_security_events_query_task_with_options(request, runtime)

    async def create_similar_security_events_query_task_async(
        self,
        request: main_models.CreateSimilarSecurityEventsQueryTaskRequest,
    ) -> main_models.CreateSimilarSecurityEventsQueryTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_similar_security_events_query_task_with_options_async(request, runtime)

    def delete_client_rule_strategy_with_options(
        self,
        tmp_req: main_models.DeleteClientRuleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientRuleStrategyResponse:
        tmp_req.validate()
        request = main_models.DeleteClientRuleStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.id_list):
            request.id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.id_list, 'IdList', 'json')
        query = {}
        if not DaraCore.is_null(request.id_list_shrink):
            query['IdList'] = request.id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientRuleStrategy',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientRuleStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_rule_strategy_with_options_async(
        self,
        tmp_req: main_models.DeleteClientRuleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientRuleStrategyResponse:
        tmp_req.validate()
        request = main_models.DeleteClientRuleStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.id_list):
            request.id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.id_list, 'IdList', 'json')
        query = {}
        if not DaraCore.is_null(request.id_list_shrink):
            query['IdList'] = request.id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientRuleStrategy',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientRuleStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_rule_strategy(
        self,
        request: main_models.DeleteClientRuleStrategyRequest,
    ) -> main_models.DeleteClientRuleStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_client_rule_strategy_with_options(request, runtime)

    async def delete_client_rule_strategy_async(
        self,
        request: main_models.DeleteClientRuleStrategyRequest,
    ) -> main_models.DeleteClientRuleStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_client_rule_strategy_with_options_async(request, runtime)

    def delete_security_event_mark_miss_list_with_options(
        self,
        request: main_models.DeleteSecurityEventMarkMissListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityEventMarkMissListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityEventMarkMissList',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityEventMarkMissListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_event_mark_miss_list_with_options_async(
        self,
        request: main_models.DeleteSecurityEventMarkMissListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityEventMarkMissListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityEventMarkMissList',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityEventMarkMissListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_event_mark_miss_list(
        self,
        request: main_models.DeleteSecurityEventMarkMissListRequest,
    ) -> main_models.DeleteSecurityEventMarkMissListResponse:
        runtime = RuntimeOptions()
        return self.delete_security_event_mark_miss_list_with_options(request, runtime)

    async def delete_security_event_mark_miss_list_async(
        self,
        request: main_models.DeleteSecurityEventMarkMissListRequest,
    ) -> main_models.DeleteSecurityEventMarkMissListResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_event_mark_miss_list_with_options_async(request, runtime)

    def describe_asset_scope_with_options(
        self,
        request: main_models.DescribeAssetScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetScope',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_scope_with_options_async(
        self,
        request: main_models.DescribeAssetScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetScope',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_scope(
        self,
        request: main_models.DescribeAssetScopeRequest,
    ) -> main_models.DescribeAssetScopeResponse:
        runtime = RuntimeOptions()
        return self.describe_asset_scope_with_options(request, runtime)

    async def describe_asset_scope_async(
        self,
        request: main_models.DescribeAssetScopeRequest,
    ) -> main_models.DescribeAssetScopeResponse:
        runtime = RuntimeOptions()
        return await self.describe_asset_scope_with_options_async(request, runtime)

    def describe_nsas_susp_event_type_with_options(
        self,
        request: main_models.DescribeNsasSuspEventTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNsasSuspEventTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not DaraCore.is_null(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNsasSuspEventType',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNsasSuspEventTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nsas_susp_event_type_with_options_async(
        self,
        request: main_models.DescribeNsasSuspEventTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNsasSuspEventTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not DaraCore.is_null(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNsasSuspEventType',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNsasSuspEventTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nsas_susp_event_type(
        self,
        request: main_models.DescribeNsasSuspEventTypeRequest,
    ) -> main_models.DescribeNsasSuspEventTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_nsas_susp_event_type_with_options(request, runtime)

    async def describe_nsas_susp_event_type_async(
        self,
        request: main_models.DescribeNsasSuspEventTypeRequest,
    ) -> main_models.DescribeNsasSuspEventTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_nsas_susp_event_type_with_options_async(request, runtime)

    def describe_security_event_mark_miss_list_with_options(
        self,
        request: main_models.DescribeSecurityEventMarkMissListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventMarkMissListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.disposal_way):
            query['DisposalWay'] = request.disposal_way
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventMarkMissList',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventMarkMissListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_mark_miss_list_with_options_async(
        self,
        request: main_models.DescribeSecurityEventMarkMissListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventMarkMissListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.disposal_way):
            query['DisposalWay'] = request.disposal_way
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventMarkMissList',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventMarkMissListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_mark_miss_list(
        self,
        request: main_models.DescribeSecurityEventMarkMissListRequest,
    ) -> main_models.DescribeSecurityEventMarkMissListResponse:
        runtime = RuntimeOptions()
        return self.describe_security_event_mark_miss_list_with_options(request, runtime)

    async def describe_security_event_mark_miss_list_async(
        self,
        request: main_models.DescribeSecurityEventMarkMissListRequest,
    ) -> main_models.DescribeSecurityEventMarkMissListResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_event_mark_miss_list_with_options_async(request, runtime)

    def describe_security_event_operation_status_with_options(
        self,
        request: main_models.DescribeSecurityEventOperationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventOperationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventOperationStatus',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventOperationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_operation_status_with_options_async(
        self,
        request: main_models.DescribeSecurityEventOperationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventOperationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventOperationStatus',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventOperationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_operation_status(
        self,
        request: main_models.DescribeSecurityEventOperationStatusRequest,
    ) -> main_models.DescribeSecurityEventOperationStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_security_event_operation_status_with_options(request, runtime)

    async def describe_security_event_operation_status_async(
        self,
        request: main_models.DescribeSecurityEventOperationStatusRequest,
    ) -> main_models.DescribeSecurityEventOperationStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_event_operation_status_with_options_async(request, runtime)

    def describe_security_event_operations_with_options(
        self,
        request: main_models.DescribeSecurityEventOperationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventOperations',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_operations_with_options_async(
        self,
        request: main_models.DescribeSecurityEventOperationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventOperations',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_operations(
        self,
        request: main_models.DescribeSecurityEventOperationsRequest,
    ) -> main_models.DescribeSecurityEventOperationsResponse:
        runtime = RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    async def describe_security_event_operations_async(
        self,
        request: main_models.DescribeSecurityEventOperationsRequest,
    ) -> main_models.DescribeSecurityEventOperationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_event_operations_with_options_async(request, runtime)

    def describe_similar_event_scenarios_with_options(
        self,
        request: main_models.DescribeSimilarEventScenariosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimilarEventScenariosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimilarEventScenarios',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimilarEventScenariosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_similar_event_scenarios_with_options_async(
        self,
        request: main_models.DescribeSimilarEventScenariosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimilarEventScenariosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimilarEventScenarios',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimilarEventScenariosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_similar_event_scenarios(
        self,
        request: main_models.DescribeSimilarEventScenariosRequest,
    ) -> main_models.DescribeSimilarEventScenariosResponse:
        runtime = RuntimeOptions()
        return self.describe_similar_event_scenarios_with_options(request, runtime)

    async def describe_similar_event_scenarios_async(
        self,
        request: main_models.DescribeSimilarEventScenariosRequest,
    ) -> main_models.DescribeSimilarEventScenariosResponse:
        runtime = RuntimeOptions()
        return await self.describe_similar_event_scenarios_with_options_async(request, runtime)

    def describe_similar_security_events_with_options(
        self,
        request: main_models.DescribeSimilarSecurityEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimilarSecurityEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimilarSecurityEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimilarSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_similar_security_events_with_options_async(
        self,
        request: main_models.DescribeSimilarSecurityEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimilarSecurityEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimilarSecurityEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimilarSecurityEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_similar_security_events(
        self,
        request: main_models.DescribeSimilarSecurityEventsRequest,
    ) -> main_models.DescribeSimilarSecurityEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_similar_security_events_with_options(request, runtime)

    async def describe_similar_security_events_async(
        self,
        request: main_models.DescribeSimilarSecurityEventsRequest,
    ) -> main_models.DescribeSimilarSecurityEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_similar_security_events_with_options_async(request, runtime)

    def describe_susp_events_with_options(
        self,
        request: main_models.DescribeSuspEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSuspEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_event_name):
            query['AlarmEventName'] = request.alarm_event_name
        if not DaraCore.is_null(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not DaraCore.is_null(request.assets_type_list):
            query['AssetsTypeList'] = request.assets_type_list
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not DaraCore.is_null(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dealed):
            query['Dealed'] = request.dealed
        if not DaraCore.is_null(request.department):
            query['Department'] = request.department
        if not DaraCore.is_null(request.event_names):
            query['EventNames'] = request.event_names
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.inner_ip):
            query['InnerIp'] = request.inner_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.levels):
            query['Levels'] = request.levels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not DaraCore.is_null(request.operate_time_end):
            query['OperateTimeEnd'] = request.operate_time_end
        if not DaraCore.is_null(request.operate_time_start):
            query['OperateTimeStart'] = request.operate_time_start
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_event_types):
            query['ParentEventTypes'] = request.parent_event_types
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.sort_column):
            query['SortColumn'] = request.sort_column
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.time_end):
            query['TimeEnd'] = request.time_end
        if not DaraCore.is_null(request.time_start):
            query['TimeStart'] = request.time_start
        if not DaraCore.is_null(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        body = {}
        if not DaraCore.is_null(request.tactic_id):
            body['TacticId'] = request.tactic_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSuspEvents',
            version = '2024-11-22',
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
        request: main_models.DescribeSuspEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSuspEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_event_name):
            query['AlarmEventName'] = request.alarm_event_name
        if not DaraCore.is_null(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not DaraCore.is_null(request.assets_type_list):
            query['AssetsTypeList'] = request.assets_type_list
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not DaraCore.is_null(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dealed):
            query['Dealed'] = request.dealed
        if not DaraCore.is_null(request.department):
            query['Department'] = request.department
        if not DaraCore.is_null(request.event_names):
            query['EventNames'] = request.event_names
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.inner_ip):
            query['InnerIp'] = request.inner_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.levels):
            query['Levels'] = request.levels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not DaraCore.is_null(request.operate_time_end):
            query['OperateTimeEnd'] = request.operate_time_end
        if not DaraCore.is_null(request.operate_time_start):
            query['OperateTimeStart'] = request.operate_time_start
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_event_types):
            query['ParentEventTypes'] = request.parent_event_types
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.sort_column):
            query['SortColumn'] = request.sort_column
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.time_end):
            query['TimeEnd'] = request.time_end
        if not DaraCore.is_null(request.time_start):
            query['TimeStart'] = request.time_start
        if not DaraCore.is_null(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        body = {}
        if not DaraCore.is_null(request.tactic_id):
            body['TacticId'] = request.tactic_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSuspEvents',
            version = '2024-11-22',
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

    def get_client_rule_strategy_detail_with_options(
        self,
        request: main_models.GetClientRuleStrategyDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientRuleStrategyDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientRuleStrategyDetail',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientRuleStrategyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_client_rule_strategy_detail_with_options_async(
        self,
        request: main_models.GetClientRuleStrategyDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientRuleStrategyDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientRuleStrategyDetail',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientRuleStrategyDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_client_rule_strategy_detail(
        self,
        request: main_models.GetClientRuleStrategyDetailRequest,
    ) -> main_models.GetClientRuleStrategyDetailResponse:
        runtime = RuntimeOptions()
        return self.get_client_rule_strategy_detail_with_options(request, runtime)

    async def get_client_rule_strategy_detail_async(
        self,
        request: main_models.GetClientRuleStrategyDetailRequest,
    ) -> main_models.GetClientRuleStrategyDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_client_rule_strategy_detail_with_options_async(request, runtime)

    def get_client_rule_strategy_statistics_with_options(
        self,
        request: main_models.GetClientRuleStrategyStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientRuleStrategyStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientRuleStrategyStatistics',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientRuleStrategyStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_client_rule_strategy_statistics_with_options_async(
        self,
        request: main_models.GetClientRuleStrategyStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientRuleStrategyStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientRuleStrategyStatistics',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientRuleStrategyStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_client_rule_strategy_statistics(
        self,
        request: main_models.GetClientRuleStrategyStatisticsRequest,
    ) -> main_models.GetClientRuleStrategyStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_client_rule_strategy_statistics_with_options(request, runtime)

    async def get_client_rule_strategy_statistics_async(
        self,
        request: main_models.GetClientRuleStrategyStatisticsRequest,
    ) -> main_models.GetClientRuleStrategyStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_client_rule_strategy_statistics_with_options_async(request, runtime)

    def handle_security_events_with_options(
        self,
        request: main_models.HandleSecurityEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleSecurityEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mark_batch):
            query['MarkBatch'] = request.mark_batch
        if not DaraCore.is_null(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not DaraCore.is_null(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not DaraCore.is_null(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleSecurityEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_security_events_with_options_async(
        self,
        request: main_models.HandleSecurityEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleSecurityEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mark_batch):
            query['MarkBatch'] = request.mark_batch
        if not DaraCore.is_null(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not DaraCore.is_null(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not DaraCore.is_null(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleSecurityEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleSecurityEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_security_events(
        self,
        request: main_models.HandleSecurityEventsRequest,
    ) -> main_models.HandleSecurityEventsResponse:
        runtime = RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    async def handle_security_events_async(
        self,
        request: main_models.HandleSecurityEventsRequest,
    ) -> main_models.HandleSecurityEventsResponse:
        runtime = RuntimeOptions()
        return await self.handle_security_events_with_options_async(request, runtime)

    def handle_similar_security_events_with_options(
        self,
        request: main_models.HandleSimilarSecurityEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleSimilarSecurityEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not DaraCore.is_null(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not DaraCore.is_null(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleSimilarSecurityEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleSimilarSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_similar_security_events_with_options_async(
        self,
        request: main_models.HandleSimilarSecurityEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleSimilarSecurityEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not DaraCore.is_null(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not DaraCore.is_null(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleSimilarSecurityEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleSimilarSecurityEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_similar_security_events(
        self,
        request: main_models.HandleSimilarSecurityEventsRequest,
    ) -> main_models.HandleSimilarSecurityEventsResponse:
        runtime = RuntimeOptions()
        return self.handle_similar_security_events_with_options(request, runtime)

    async def handle_similar_security_events_async(
        self,
        request: main_models.HandleSimilarSecurityEventsRequest,
    ) -> main_models.HandleSimilarSecurityEventsResponse:
        runtime = RuntimeOptions()
        return await self.handle_similar_security_events_with_options_async(request, runtime)

    def list_client_rule_strategy_with_options(
        self,
        request: main_models.ListClientRuleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientRuleStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientRuleStrategy',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientRuleStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_rule_strategy_with_options_async(
        self,
        request: main_models.ListClientRuleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientRuleStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientRuleStrategy',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientRuleStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_rule_strategy(
        self,
        request: main_models.ListClientRuleStrategyRequest,
    ) -> main_models.ListClientRuleStrategyResponse:
        runtime = RuntimeOptions()
        return self.list_client_rule_strategy_with_options(request, runtime)

    async def list_client_rule_strategy_async(
        self,
        request: main_models.ListClientRuleStrategyRequest,
    ) -> main_models.ListClientRuleStrategyResponse:
        runtime = RuntimeOptions()
        return await self.list_client_rule_strategy_with_options_async(request, runtime)

    def list_system_config_rules_with_options(
        self,
        tmp_req: main_models.ListSystemConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemConfigRulesResponse:
        tmp_req.validate()
        request = main_models.ListSystemConfigRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aggregation_ids):
            request.aggregation_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.aggregation_ids, 'AggregationIds', 'json')
        if not DaraCore.is_null(tmp_req.rule_types):
            request.rule_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.rule_types, 'RuleTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregation_ids_shrink):
            query['AggregationIds'] = request.aggregation_ids_shrink
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_types_shrink):
            query['RuleTypes'] = request.rule_types_shrink
        if not DaraCore.is_null(request.selection_key):
            query['SelectionKey'] = request.selection_key
        if not DaraCore.is_null(request.system_type):
            query['SystemType'] = request.system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemConfigRules',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_config_rules_with_options_async(
        self,
        tmp_req: main_models.ListSystemConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemConfigRulesResponse:
        tmp_req.validate()
        request = main_models.ListSystemConfigRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aggregation_ids):
            request.aggregation_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.aggregation_ids, 'AggregationIds', 'json')
        if not DaraCore.is_null(tmp_req.rule_types):
            request.rule_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.rule_types, 'RuleTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregation_ids_shrink):
            query['AggregationIds'] = request.aggregation_ids_shrink
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_types_shrink):
            query['RuleTypes'] = request.rule_types_shrink
        if not DaraCore.is_null(request.selection_key):
            query['SelectionKey'] = request.selection_key
        if not DaraCore.is_null(request.system_type):
            query['SystemType'] = request.system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemConfigRules',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_config_rules(
        self,
        request: main_models.ListSystemConfigRulesRequest,
    ) -> main_models.ListSystemConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.list_system_config_rules_with_options(request, runtime)

    async def list_system_config_rules_async(
        self,
        request: main_models.ListSystemConfigRulesRequest,
    ) -> main_models.ListSystemConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_system_config_rules_with_options_async(request, runtime)

    def operate_target_config_with_options(
        self,
        tmp_req: main_models.OperateTargetConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateTargetConfigResponse:
        tmp_req.validate()
        request = main_models.OperateTargetConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.switch_id_list):
            request.switch_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.switch_id_list, 'SwitchIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.selection_key):
            query['SelectionKey'] = request.selection_key
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.switch_id_list_shrink):
            query['SwitchIdList'] = request.switch_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateTargetConfig',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateTargetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_target_config_with_options_async(
        self,
        tmp_req: main_models.OperateTargetConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateTargetConfigResponse:
        tmp_req.validate()
        request = main_models.OperateTargetConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.switch_id_list):
            request.switch_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.switch_id_list, 'SwitchIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.selection_key):
            query['SelectionKey'] = request.selection_key
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.switch_id_list_shrink):
            query['SwitchIdList'] = request.switch_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateTargetConfig',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateTargetConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_target_config(
        self,
        request: main_models.OperateTargetConfigRequest,
    ) -> main_models.OperateTargetConfigResponse:
        runtime = RuntimeOptions()
        return self.operate_target_config_with_options(request, runtime)

    async def operate_target_config_async(
        self,
        request: main_models.OperateTargetConfigRequest,
    ) -> main_models.OperateTargetConfigResponse:
        runtime = RuntimeOptions()
        return await self.operate_target_config_with_options_async(request, runtime)

    def update_asset_scope_with_options(
        self,
        request: main_models.UpdateAssetScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAssetScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.match_target_ids):
            query['MatchTargetIds'] = request.match_target_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAssetScope',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAssetScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asset_scope_with_options_async(
        self,
        request: main_models.UpdateAssetScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAssetScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.match_target_ids):
            query['MatchTargetIds'] = request.match_target_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAssetScope',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAssetScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asset_scope(
        self,
        request: main_models.UpdateAssetScopeRequest,
    ) -> main_models.UpdateAssetScopeResponse:
        runtime = RuntimeOptions()
        return self.update_asset_scope_with_options(request, runtime)

    async def update_asset_scope_async(
        self,
        request: main_models.UpdateAssetScopeRequest,
    ) -> main_models.UpdateAssetScopeResponse:
        runtime = RuntimeOptions()
        return await self.update_asset_scope_with_options_async(request, runtime)

    def update_client_rule_strategy_with_options(
        self,
        tmp_req: main_models.UpdateClientRuleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientRuleStrategyResponse:
        tmp_req.validate()
        request = main_models.UpdateClientRuleStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_user_name_list):
            request.exclude_user_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_user_name_list, 'ExcludeUserNameList', 'json')
        if not DaraCore.is_null(tmp_req.include_group_id_list):
            request.include_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_group_id_list, 'IncludeGroupIdList', 'json')
        if not DaraCore.is_null(tmp_req.port_on_list):
            request.port_on_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.port_on_list, 'PortOnList', 'json')
        if not DaraCore.is_null(tmp_req.soft_ware_on_list):
            request.soft_ware_on_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.soft_ware_on_list, 'SoftWareOnList', 'json')
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.all_group):
            query['AllGroup'] = request.all_group
        if not DaraCore.is_null(request.approval_id):
            query['ApprovalId'] = request.approval_id
        if not DaraCore.is_null(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.exclude_user_name_list_shrink):
            query['ExcludeUserNameList'] = request.exclude_user_name_list_shrink
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.in_switch):
            query['InSwitch'] = request.in_switch
        if not DaraCore.is_null(request.include_group_id_list_shrink):
            query['IncludeGroupIdList'] = request.include_group_id_list_shrink
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.main_button_text_ch):
            query['MainButtonTextCh'] = request.main_button_text_ch
        if not DaraCore.is_null(request.main_button_text_en):
            query['MainButtonTextEn'] = request.main_button_text_en
        if not DaraCore.is_null(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.match_target_ids):
            query['MatchTargetIds'] = request.match_target_ids
        if not DaraCore.is_null(request.md_5list):
            query['Md5List'] = request.md_5list
        if not DaraCore.is_null(request.minor_button_text_ch):
            query['MinorButtonTextCh'] = request.minor_button_text_ch
        if not DaraCore.is_null(request.minor_button_text_en):
            query['MinorButtonTextEn'] = request.minor_button_text_en
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.new_file_path):
            query['NewFilePath'] = request.new_file_path
        if not DaraCore.is_null(request.out_switch):
            query['OutSwitch'] = request.out_switch
        if not DaraCore.is_null(request.parent_cmdline):
            query['ParentCmdline'] = request.parent_cmdline
        if not DaraCore.is_null(request.parent_proc_path):
            query['ParentProcPath'] = request.parent_proc_path
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.port_on_list_shrink):
            query['PortOnList'] = request.port_on_list_shrink
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.proc_path):
            query['ProcPath'] = request.proc_path
        if not DaraCore.is_null(request.registry_content):
            query['RegistryContent'] = request.registry_content
        if not DaraCore.is_null(request.registry_key):
            query['RegistryKey'] = request.registry_key
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.soft_ware_on_list_shrink):
            query['SoftWareOnList'] = request.soft_ware_on_list_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strategy_source_type):
            query['StrategySourceType'] = request.strategy_source_type
        if not DaraCore.is_null(request.supports_approval):
            query['SupportsApproval'] = request.supports_approval
        if not DaraCore.is_null(request.us_content):
            query['UsContent'] = request.us_content
        if not DaraCore.is_null(request.us_title):
            query['UsTitle'] = request.us_title
        if not DaraCore.is_null(request.zh_content):
            query['ZhContent'] = request.zh_content
        if not DaraCore.is_null(request.zh_title):
            query['ZhTitle'] = request.zh_title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientRuleStrategy',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientRuleStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_rule_strategy_with_options_async(
        self,
        tmp_req: main_models.UpdateClientRuleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientRuleStrategyResponse:
        tmp_req.validate()
        request = main_models.UpdateClientRuleStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_user_name_list):
            request.exclude_user_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_user_name_list, 'ExcludeUserNameList', 'json')
        if not DaraCore.is_null(tmp_req.include_group_id_list):
            request.include_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_group_id_list, 'IncludeGroupIdList', 'json')
        if not DaraCore.is_null(tmp_req.port_on_list):
            request.port_on_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.port_on_list, 'PortOnList', 'json')
        if not DaraCore.is_null(tmp_req.soft_ware_on_list):
            request.soft_ware_on_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.soft_ware_on_list, 'SoftWareOnList', 'json')
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.all_group):
            query['AllGroup'] = request.all_group
        if not DaraCore.is_null(request.approval_id):
            query['ApprovalId'] = request.approval_id
        if not DaraCore.is_null(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.exclude_user_name_list_shrink):
            query['ExcludeUserNameList'] = request.exclude_user_name_list_shrink
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.in_switch):
            query['InSwitch'] = request.in_switch
        if not DaraCore.is_null(request.include_group_id_list_shrink):
            query['IncludeGroupIdList'] = request.include_group_id_list_shrink
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.main_button_text_ch):
            query['MainButtonTextCh'] = request.main_button_text_ch
        if not DaraCore.is_null(request.main_button_text_en):
            query['MainButtonTextEn'] = request.main_button_text_en
        if not DaraCore.is_null(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.match_target_ids):
            query['MatchTargetIds'] = request.match_target_ids
        if not DaraCore.is_null(request.md_5list):
            query['Md5List'] = request.md_5list
        if not DaraCore.is_null(request.minor_button_text_ch):
            query['MinorButtonTextCh'] = request.minor_button_text_ch
        if not DaraCore.is_null(request.minor_button_text_en):
            query['MinorButtonTextEn'] = request.minor_button_text_en
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.new_file_path):
            query['NewFilePath'] = request.new_file_path
        if not DaraCore.is_null(request.out_switch):
            query['OutSwitch'] = request.out_switch
        if not DaraCore.is_null(request.parent_cmdline):
            query['ParentCmdline'] = request.parent_cmdline
        if not DaraCore.is_null(request.parent_proc_path):
            query['ParentProcPath'] = request.parent_proc_path
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.port_on_list_shrink):
            query['PortOnList'] = request.port_on_list_shrink
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.proc_path):
            query['ProcPath'] = request.proc_path
        if not DaraCore.is_null(request.registry_content):
            query['RegistryContent'] = request.registry_content
        if not DaraCore.is_null(request.registry_key):
            query['RegistryKey'] = request.registry_key
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.soft_ware_on_list_shrink):
            query['SoftWareOnList'] = request.soft_ware_on_list_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strategy_source_type):
            query['StrategySourceType'] = request.strategy_source_type
        if not DaraCore.is_null(request.supports_approval):
            query['SupportsApproval'] = request.supports_approval
        if not DaraCore.is_null(request.us_content):
            query['UsContent'] = request.us_content
        if not DaraCore.is_null(request.us_title):
            query['UsTitle'] = request.us_title
        if not DaraCore.is_null(request.zh_content):
            query['ZhContent'] = request.zh_content
        if not DaraCore.is_null(request.zh_title):
            query['ZhTitle'] = request.zh_title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientRuleStrategy',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientRuleStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_rule_strategy(
        self,
        request: main_models.UpdateClientRuleStrategyRequest,
    ) -> main_models.UpdateClientRuleStrategyResponse:
        runtime = RuntimeOptions()
        return self.update_client_rule_strategy_with_options(request, runtime)

    async def update_client_rule_strategy_async(
        self,
        request: main_models.UpdateClientRuleStrategyRequest,
    ) -> main_models.UpdateClientRuleStrategyResponse:
        runtime = RuntimeOptions()
        return await self.update_client_rule_strategy_with_options_async(request, runtime)
