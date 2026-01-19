# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_config20200907 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-shanghai': 'config.cn-shanghai.aliyuncs.com',
            'ap-southeast-1': 'config.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('config', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def active_aggregate_config_rules_with_options(
        self,
        request: main_models.ActiveAggregateConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveAggregateConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveAggregateConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_aggregate_config_rules_with_options_async(
        self,
        request: main_models.ActiveAggregateConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveAggregateConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveAggregateConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_aggregate_config_rules(
        self,
        request: main_models.ActiveAggregateConfigRulesRequest,
    ) -> main_models.ActiveAggregateConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.active_aggregate_config_rules_with_options(request, runtime)

    async def active_aggregate_config_rules_async(
        self,
        request: main_models.ActiveAggregateConfigRulesRequest,
    ) -> main_models.ActiveAggregateConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.active_aggregate_config_rules_with_options_async(request, runtime)

    def active_config_rules_with_options(
        self,
        request: main_models.ActiveConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_config_rules_with_options_async(
        self,
        request: main_models.ActiveConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_config_rules(
        self,
        request: main_models.ActiveConfigRulesRequest,
    ) -> main_models.ActiveConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.active_config_rules_with_options(request, runtime)

    async def active_config_rules_async(
        self,
        request: main_models.ActiveConfigRulesRequest,
    ) -> main_models.ActiveConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.active_config_rules_with_options_async(request, runtime)

    def attach_aggregate_config_rule_to_compliance_pack_with_options(
        self,
        request: main_models.AttachAggregateConfigRuleToCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachAggregateConfigRuleToCompliancePackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachAggregateConfigRuleToCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachAggregateConfigRuleToCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_aggregate_config_rule_to_compliance_pack_with_options_async(
        self,
        request: main_models.AttachAggregateConfigRuleToCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachAggregateConfigRuleToCompliancePackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachAggregateConfigRuleToCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachAggregateConfigRuleToCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_aggregate_config_rule_to_compliance_pack(
        self,
        request: main_models.AttachAggregateConfigRuleToCompliancePackRequest,
    ) -> main_models.AttachAggregateConfigRuleToCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.attach_aggregate_config_rule_to_compliance_pack_with_options(request, runtime)

    async def attach_aggregate_config_rule_to_compliance_pack_async(
        self,
        request: main_models.AttachAggregateConfigRuleToCompliancePackRequest,
    ) -> main_models.AttachAggregateConfigRuleToCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.attach_aggregate_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def attach_config_rule_to_compliance_pack_with_options(
        self,
        request: main_models.AttachConfigRuleToCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachConfigRuleToCompliancePackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachConfigRuleToCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachConfigRuleToCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_config_rule_to_compliance_pack_with_options_async(
        self,
        request: main_models.AttachConfigRuleToCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachConfigRuleToCompliancePackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachConfigRuleToCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachConfigRuleToCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_config_rule_to_compliance_pack(
        self,
        request: main_models.AttachConfigRuleToCompliancePackRequest,
    ) -> main_models.AttachConfigRuleToCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.attach_config_rule_to_compliance_pack_with_options(request, runtime)

    async def attach_config_rule_to_compliance_pack_async(
        self,
        request: main_models.AttachConfigRuleToCompliancePackRequest,
    ) -> main_models.AttachConfigRuleToCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.attach_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def copy_compliance_packs_with_options(
        self,
        request: main_models.CopyCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyCompliancePacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.des_aggregator_ids):
            query['DesAggregatorIds'] = request.des_aggregator_ids
        if not DaraCore.is_null(request.src_aggregator_id):
            query['SrcAggregatorId'] = request.src_aggregator_id
        if not DaraCore.is_null(request.src_compliance_pack_ids):
            query['SrcCompliancePackIds'] = request.src_compliance_pack_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_compliance_packs_with_options_async(
        self,
        request: main_models.CopyCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyCompliancePacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.des_aggregator_ids):
            query['DesAggregatorIds'] = request.des_aggregator_ids
        if not DaraCore.is_null(request.src_aggregator_id):
            query['SrcAggregatorId'] = request.src_aggregator_id
        if not DaraCore.is_null(request.src_compliance_pack_ids):
            query['SrcCompliancePackIds'] = request.src_compliance_pack_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_compliance_packs(
        self,
        request: main_models.CopyCompliancePacksRequest,
    ) -> main_models.CopyCompliancePacksResponse:
        runtime = RuntimeOptions()
        return self.copy_compliance_packs_with_options(request, runtime)

    async def copy_compliance_packs_async(
        self,
        request: main_models.CopyCompliancePacksRequest,
    ) -> main_models.CopyCompliancePacksResponse:
        runtime = RuntimeOptions()
        return await self.copy_compliance_packs_with_options_async(request, runtime)

    def copy_config_rules_with_options(
        self,
        request: main_models.CopyConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.des_aggregator_ids):
            query['DesAggregatorIds'] = request.des_aggregator_ids
        if not DaraCore.is_null(request.src_aggregator_id):
            query['SrcAggregatorId'] = request.src_aggregator_id
        if not DaraCore.is_null(request.src_config_rule_ids):
            query['SrcConfigRuleIds'] = request.src_config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_config_rules_with_options_async(
        self,
        request: main_models.CopyConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.des_aggregator_ids):
            query['DesAggregatorIds'] = request.des_aggregator_ids
        if not DaraCore.is_null(request.src_aggregator_id):
            query['SrcAggregatorId'] = request.src_aggregator_id
        if not DaraCore.is_null(request.src_config_rule_ids):
            query['SrcConfigRuleIds'] = request.src_config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_config_rules(
        self,
        request: main_models.CopyConfigRulesRequest,
    ) -> main_models.CopyConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.copy_config_rules_with_options(request, runtime)

    async def copy_config_rules_async(
        self,
        request: main_models.CopyConfigRulesRequest,
    ) -> main_models.CopyConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.copy_config_rules_with_options_async(request, runtime)

    def create_advanced_search_file_with_options(
        self,
        request: main_models.CreateAdvancedSearchFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdvancedSearchFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdvancedSearchFile',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdvancedSearchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_advanced_search_file_with_options_async(
        self,
        request: main_models.CreateAdvancedSearchFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdvancedSearchFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdvancedSearchFile',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdvancedSearchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_advanced_search_file(
        self,
        request: main_models.CreateAdvancedSearchFileRequest,
    ) -> main_models.CreateAdvancedSearchFileResponse:
        runtime = RuntimeOptions()
        return self.create_advanced_search_file_with_options(request, runtime)

    async def create_advanced_search_file_async(
        self,
        request: main_models.CreateAdvancedSearchFileRequest,
    ) -> main_models.CreateAdvancedSearchFileResponse:
        runtime = RuntimeOptions()
        return await self.create_advanced_search_file_with_options_async(request, runtime)

    def create_aggregate_advanced_search_file_with_options(
        self,
        request: main_models.CreateAggregateAdvancedSearchFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateAdvancedSearchFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateAdvancedSearchFile',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateAdvancedSearchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_advanced_search_file_with_options_async(
        self,
        request: main_models.CreateAggregateAdvancedSearchFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateAdvancedSearchFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateAdvancedSearchFile',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateAdvancedSearchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_advanced_search_file(
        self,
        request: main_models.CreateAggregateAdvancedSearchFileRequest,
    ) -> main_models.CreateAggregateAdvancedSearchFileResponse:
        runtime = RuntimeOptions()
        return self.create_aggregate_advanced_search_file_with_options(request, runtime)

    async def create_aggregate_advanced_search_file_async(
        self,
        request: main_models.CreateAggregateAdvancedSearchFileRequest,
    ) -> main_models.CreateAggregateAdvancedSearchFileResponse:
        runtime = RuntimeOptions()
        return await self.create_aggregate_advanced_search_file_with_options_async(request, runtime)

    def create_aggregate_compliance_pack_with_options(
        self,
        tmp_req: main_models.CreateAggregateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.CreateAggregateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_rules):
            request.config_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not DaraCore.is_null(request.compliance_pack_template_id):
            body['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not DaraCore.is_null(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not DaraCore.is_null(request.default_enable):
            body['DefaultEnable'] = request.default_enable
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        if not DaraCore.is_null(request.template_content):
            body['TemplateContent'] = request.template_content
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_compliance_pack_with_options_async(
        self,
        tmp_req: main_models.CreateAggregateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.CreateAggregateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_rules):
            request.config_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not DaraCore.is_null(request.compliance_pack_template_id):
            body['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not DaraCore.is_null(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not DaraCore.is_null(request.default_enable):
            body['DefaultEnable'] = request.default_enable
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        if not DaraCore.is_null(request.template_content):
            body['TemplateContent'] = request.template_content
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_compliance_pack(
        self,
        request: main_models.CreateAggregateCompliancePackRequest,
    ) -> main_models.CreateAggregateCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.create_aggregate_compliance_pack_with_options(request, runtime)

    async def create_aggregate_compliance_pack_async(
        self,
        request: main_models.CreateAggregateCompliancePackRequest,
    ) -> main_models.CreateAggregateCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.create_aggregate_compliance_pack_with_options_async(request, runtime)

    def create_aggregate_config_delivery_channel_with_options(
        self,
        request: main_models.CreateAggregateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not DaraCore.is_null(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not DaraCore.is_null(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not DaraCore.is_null(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not DaraCore.is_null(request.delivery_channel_type):
            query['DeliveryChannelType'] = request.delivery_channel_type
        if not DaraCore.is_null(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not DaraCore.is_null(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_config_delivery_channel_with_options_async(
        self,
        request: main_models.CreateAggregateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not DaraCore.is_null(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not DaraCore.is_null(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not DaraCore.is_null(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not DaraCore.is_null(request.delivery_channel_type):
            query['DeliveryChannelType'] = request.delivery_channel_type
        if not DaraCore.is_null(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not DaraCore.is_null(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_config_delivery_channel(
        self,
        request: main_models.CreateAggregateConfigDeliveryChannelRequest,
    ) -> main_models.CreateAggregateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.create_aggregate_config_delivery_channel_with_options(request, runtime)

    async def create_aggregate_config_delivery_channel_async(
        self,
        request: main_models.CreateAggregateConfigDeliveryChannelRequest,
    ) -> main_models.CreateAggregateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.create_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def create_aggregate_config_rule_with_options(
        self,
        tmp_req: main_models.CreateAggregateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.CreateAggregateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input_parameters):
            request.input_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not DaraCore.is_null(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.resource_name_scope):
            query['ResourceNameScope'] = request.resource_name_scope
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.account_ids_scope):
            body['AccountIdsScope'] = request.account_ids_scope
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not DaraCore.is_null(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.extend_content):
            body['ExtendContent'] = request.extend_content
        if not DaraCore.is_null(request.folder_ids_scope):
            body['FolderIdsScope'] = request.folder_ids_scope
        if not DaraCore.is_null(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not DaraCore.is_null(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not DaraCore.is_null(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not DaraCore.is_null(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_config_rule_with_options_async(
        self,
        tmp_req: main_models.CreateAggregateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.CreateAggregateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input_parameters):
            request.input_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not DaraCore.is_null(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.resource_name_scope):
            query['ResourceNameScope'] = request.resource_name_scope
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.account_ids_scope):
            body['AccountIdsScope'] = request.account_ids_scope
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not DaraCore.is_null(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.extend_content):
            body['ExtendContent'] = request.extend_content
        if not DaraCore.is_null(request.folder_ids_scope):
            body['FolderIdsScope'] = request.folder_ids_scope
        if not DaraCore.is_null(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not DaraCore.is_null(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not DaraCore.is_null(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not DaraCore.is_null(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_config_rule(
        self,
        request: main_models.CreateAggregateConfigRuleRequest,
    ) -> main_models.CreateAggregateConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.create_aggregate_config_rule_with_options(request, runtime)

    async def create_aggregate_config_rule_async(
        self,
        request: main_models.CreateAggregateConfigRuleRequest,
    ) -> main_models.CreateAggregateConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_aggregate_config_rule_with_options_async(request, runtime)

    def create_aggregate_remediation_with_options(
        self,
        request: main_models.CreateAggregateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateRemediationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not DaraCore.is_null(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_remediation_with_options_async(
        self,
        request: main_models.CreateAggregateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregateRemediationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not DaraCore.is_null(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_remediation(
        self,
        request: main_models.CreateAggregateRemediationRequest,
    ) -> main_models.CreateAggregateRemediationResponse:
        runtime = RuntimeOptions()
        return self.create_aggregate_remediation_with_options(request, runtime)

    async def create_aggregate_remediation_async(
        self,
        request: main_models.CreateAggregateRemediationRequest,
    ) -> main_models.CreateAggregateRemediationResponse:
        runtime = RuntimeOptions()
        return await self.create_aggregate_remediation_with_options_async(request, runtime)

    def create_aggregator_with_options(
        self,
        tmp_req: main_models.CreateAggregatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregatorResponse:
        tmp_req.validate()
        request = main_models.CreateAggregatorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aggregator_accounts):
            request.aggregator_accounts_shrink = Utils.array_to_string_with_specified_style(tmp_req.aggregator_accounts, 'AggregatorAccounts', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.aggregator_accounts_shrink):
            body['AggregatorAccounts'] = request.aggregator_accounts_shrink
        if not DaraCore.is_null(request.aggregator_name):
            body['AggregatorName'] = request.aggregator_name
        if not DaraCore.is_null(request.aggregator_type):
            body['AggregatorType'] = request.aggregator_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregator',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregator_with_options_async(
        self,
        tmp_req: main_models.CreateAggregatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAggregatorResponse:
        tmp_req.validate()
        request = main_models.CreateAggregatorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aggregator_accounts):
            request.aggregator_accounts_shrink = Utils.array_to_string_with_specified_style(tmp_req.aggregator_accounts, 'AggregatorAccounts', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.aggregator_accounts_shrink):
            body['AggregatorAccounts'] = request.aggregator_accounts_shrink
        if not DaraCore.is_null(request.aggregator_name):
            body['AggregatorName'] = request.aggregator_name
        if not DaraCore.is_null(request.aggregator_type):
            body['AggregatorType'] = request.aggregator_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAggregator',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAggregatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregator(
        self,
        request: main_models.CreateAggregatorRequest,
    ) -> main_models.CreateAggregatorResponse:
        runtime = RuntimeOptions()
        return self.create_aggregator_with_options(request, runtime)

    async def create_aggregator_async(
        self,
        request: main_models.CreateAggregatorRequest,
    ) -> main_models.CreateAggregatorResponse:
        runtime = RuntimeOptions()
        return await self.create_aggregator_with_options_async(request, runtime)

    def create_compliance_pack_with_options(
        self,
        tmp_req: main_models.CreateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.CreateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_rules):
            request.config_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not DaraCore.is_null(request.compliance_pack_template_id):
            body['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not DaraCore.is_null(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not DaraCore.is_null(request.default_enable):
            body['DefaultEnable'] = request.default_enable
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        if not DaraCore.is_null(request.template_content):
            body['TemplateContent'] = request.template_content
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compliance_pack_with_options_async(
        self,
        tmp_req: main_models.CreateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.CreateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_rules):
            request.config_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not DaraCore.is_null(request.compliance_pack_template_id):
            body['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not DaraCore.is_null(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not DaraCore.is_null(request.default_enable):
            body['DefaultEnable'] = request.default_enable
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        if not DaraCore.is_null(request.template_content):
            body['TemplateContent'] = request.template_content
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compliance_pack(
        self,
        request: main_models.CreateCompliancePackRequest,
    ) -> main_models.CreateCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.create_compliance_pack_with_options(request, runtime)

    async def create_compliance_pack_async(
        self,
        request: main_models.CreateCompliancePackRequest,
    ) -> main_models.CreateCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.create_compliance_pack_with_options_async(request, runtime)

    def create_config_delivery_channel_with_options(
        self,
        request: main_models.CreateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not DaraCore.is_null(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not DaraCore.is_null(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not DaraCore.is_null(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not DaraCore.is_null(request.delivery_channel_type):
            query['DeliveryChannelType'] = request.delivery_channel_type
        if not DaraCore.is_null(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not DaraCore.is_null(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_delivery_channel_with_options_async(
        self,
        request: main_models.CreateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not DaraCore.is_null(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not DaraCore.is_null(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not DaraCore.is_null(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not DaraCore.is_null(request.delivery_channel_type):
            query['DeliveryChannelType'] = request.delivery_channel_type
        if not DaraCore.is_null(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not DaraCore.is_null(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_delivery_channel(
        self,
        request: main_models.CreateConfigDeliveryChannelRequest,
    ) -> main_models.CreateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.create_config_delivery_channel_with_options(request, runtime)

    async def create_config_delivery_channel_async(
        self,
        request: main_models.CreateConfigDeliveryChannelRequest,
    ) -> main_models.CreateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.create_config_delivery_channel_with_options_async(request, runtime)

    def create_config_rule_with_options(
        self,
        tmp_req: main_models.CreateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.CreateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input_parameters):
            request.input_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not DaraCore.is_null(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.extend_content):
            body['ExtendContent'] = request.extend_content
        if not DaraCore.is_null(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not DaraCore.is_null(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_name_scope):
            body['ResourceNameScope'] = request.resource_name_scope
        if not DaraCore.is_null(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not DaraCore.is_null(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not DaraCore.is_null(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_rule_with_options_async(
        self,
        tmp_req: main_models.CreateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.CreateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input_parameters):
            request.input_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not DaraCore.is_null(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.extend_content):
            body['ExtendContent'] = request.extend_content
        if not DaraCore.is_null(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not DaraCore.is_null(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_name_scope):
            body['ResourceNameScope'] = request.resource_name_scope
        if not DaraCore.is_null(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not DaraCore.is_null(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not DaraCore.is_null(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_rule(
        self,
        request: main_models.CreateConfigRuleRequest,
    ) -> main_models.CreateConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.create_config_rule_with_options(request, runtime)

    async def create_config_rule_async(
        self,
        request: main_models.CreateConfigRuleRequest,
    ) -> main_models.CreateConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_config_rule_with_options_async(request, runtime)

    def create_remediation_with_options(
        self,
        request: main_models.CreateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRemediationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not DaraCore.is_null(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_remediation_with_options_async(
        self,
        request: main_models.CreateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRemediationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not DaraCore.is_null(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_remediation(
        self,
        request: main_models.CreateRemediationRequest,
    ) -> main_models.CreateRemediationResponse:
        runtime = RuntimeOptions()
        return self.create_remediation_with_options(request, runtime)

    async def create_remediation_async(
        self,
        request: main_models.CreateRemediationRequest,
    ) -> main_models.CreateRemediationResponse:
        runtime = RuntimeOptions()
        return await self.create_remediation_with_options_async(request, runtime)

    def deactive_aggregate_config_rules_with_options(
        self,
        request: main_models.DeactiveAggregateConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactiveAggregateConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactiveAggregateConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactiveAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactive_aggregate_config_rules_with_options_async(
        self,
        request: main_models.DeactiveAggregateConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactiveAggregateConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactiveAggregateConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactiveAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactive_aggregate_config_rules(
        self,
        request: main_models.DeactiveAggregateConfigRulesRequest,
    ) -> main_models.DeactiveAggregateConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.deactive_aggregate_config_rules_with_options(request, runtime)

    async def deactive_aggregate_config_rules_async(
        self,
        request: main_models.DeactiveAggregateConfigRulesRequest,
    ) -> main_models.DeactiveAggregateConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.deactive_aggregate_config_rules_with_options_async(request, runtime)

    def deactive_config_rules_with_options(
        self,
        request: main_models.DeactiveConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactiveConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactiveConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactiveConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactive_config_rules_with_options_async(
        self,
        request: main_models.DeactiveConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactiveConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactiveConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactiveConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactive_config_rules(
        self,
        request: main_models.DeactiveConfigRulesRequest,
    ) -> main_models.DeactiveConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.deactive_config_rules_with_options(request, runtime)

    async def deactive_config_rules_async(
        self,
        request: main_models.DeactiveConfigRulesRequest,
    ) -> main_models.DeactiveConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.deactive_config_rules_with_options_async(request, runtime)

    def delete_aggregate_compliance_packs_with_options(
        self,
        request: main_models.DeleteAggregateCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregateCompliancePacksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_ids):
            body['CompliancePackIds'] = request.compliance_pack_ids
        if not DaraCore.is_null(request.delete_rule):
            body['DeleteRule'] = request.delete_rule
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregateCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregateCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregate_compliance_packs_with_options_async(
        self,
        request: main_models.DeleteAggregateCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregateCompliancePacksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_ids):
            body['CompliancePackIds'] = request.compliance_pack_ids
        if not DaraCore.is_null(request.delete_rule):
            body['DeleteRule'] = request.delete_rule
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregateCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregateCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregate_compliance_packs(
        self,
        request: main_models.DeleteAggregateCompliancePacksRequest,
    ) -> main_models.DeleteAggregateCompliancePacksResponse:
        runtime = RuntimeOptions()
        return self.delete_aggregate_compliance_packs_with_options(request, runtime)

    async def delete_aggregate_compliance_packs_async(
        self,
        request: main_models.DeleteAggregateCompliancePacksRequest,
    ) -> main_models.DeleteAggregateCompliancePacksResponse:
        runtime = RuntimeOptions()
        return await self.delete_aggregate_compliance_packs_with_options_async(request, runtime)

    def delete_aggregate_config_delivery_channel_with_options(
        self,
        request: main_models.DeleteAggregateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregate_config_delivery_channel_with_options_async(
        self,
        request: main_models.DeleteAggregateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregate_config_delivery_channel(
        self,
        request: main_models.DeleteAggregateConfigDeliveryChannelRequest,
    ) -> main_models.DeleteAggregateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.delete_aggregate_config_delivery_channel_with_options(request, runtime)

    async def delete_aggregate_config_delivery_channel_async(
        self,
        request: main_models.DeleteAggregateConfigDeliveryChannelRequest,
    ) -> main_models.DeleteAggregateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.delete_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def delete_aggregate_config_rules_with_options(
        self,
        request: main_models.DeleteAggregateConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregateConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregateConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregate_config_rules_with_options_async(
        self,
        request: main_models.DeleteAggregateConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregateConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregateConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregate_config_rules(
        self,
        request: main_models.DeleteAggregateConfigRulesRequest,
    ) -> main_models.DeleteAggregateConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_aggregate_config_rules_with_options(request, runtime)

    async def delete_aggregate_config_rules_async(
        self,
        request: main_models.DeleteAggregateConfigRulesRequest,
    ) -> main_models.DeleteAggregateConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_aggregate_config_rules_with_options_async(request, runtime)

    def delete_aggregate_remediations_with_options(
        self,
        request: main_models.DeleteAggregateRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregateRemediationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.remediation_ids):
            body['RemediationIds'] = request.remediation_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregateRemediations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregateRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregate_remediations_with_options_async(
        self,
        request: main_models.DeleteAggregateRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregateRemediationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.remediation_ids):
            body['RemediationIds'] = request.remediation_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregateRemediations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregateRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregate_remediations(
        self,
        request: main_models.DeleteAggregateRemediationsRequest,
    ) -> main_models.DeleteAggregateRemediationsResponse:
        runtime = RuntimeOptions()
        return self.delete_aggregate_remediations_with_options(request, runtime)

    async def delete_aggregate_remediations_async(
        self,
        request: main_models.DeleteAggregateRemediationsRequest,
    ) -> main_models.DeleteAggregateRemediationsResponse:
        runtime = RuntimeOptions()
        return await self.delete_aggregate_remediations_with_options_async(request, runtime)

    def delete_aggregators_with_options(
        self,
        request: main_models.DeleteAggregatorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregatorsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_ids):
            body['AggregatorIds'] = request.aggregator_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregators',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregators_with_options_async(
        self,
        request: main_models.DeleteAggregatorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAggregatorsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_ids):
            body['AggregatorIds'] = request.aggregator_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAggregators',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAggregatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregators(
        self,
        request: main_models.DeleteAggregatorsRequest,
    ) -> main_models.DeleteAggregatorsResponse:
        runtime = RuntimeOptions()
        return self.delete_aggregators_with_options(request, runtime)

    async def delete_aggregators_async(
        self,
        request: main_models.DeleteAggregatorsRequest,
    ) -> main_models.DeleteAggregatorsResponse:
        runtime = RuntimeOptions()
        return await self.delete_aggregators_with_options_async(request, runtime)

    def delete_compliance_packs_with_options(
        self,
        request: main_models.DeleteCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCompliancePacksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_ids):
            body['CompliancePackIds'] = request.compliance_pack_ids
        if not DaraCore.is_null(request.delete_rule):
            body['DeleteRule'] = request.delete_rule
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_compliance_packs_with_options_async(
        self,
        request: main_models.DeleteCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCompliancePacksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_ids):
            body['CompliancePackIds'] = request.compliance_pack_ids
        if not DaraCore.is_null(request.delete_rule):
            body['DeleteRule'] = request.delete_rule
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_compliance_packs(
        self,
        request: main_models.DeleteCompliancePacksRequest,
    ) -> main_models.DeleteCompliancePacksResponse:
        runtime = RuntimeOptions()
        return self.delete_compliance_packs_with_options(request, runtime)

    async def delete_compliance_packs_async(
        self,
        request: main_models.DeleteCompliancePacksRequest,
    ) -> main_models.DeleteCompliancePacksResponse:
        runtime = RuntimeOptions()
        return await self.delete_compliance_packs_with_options_async(request, runtime)

    def delete_config_delivery_channel_with_options(
        self,
        request: main_models.DeleteConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_delivery_channel_with_options_async(
        self,
        request: main_models.DeleteConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_delivery_channel(
        self,
        request: main_models.DeleteConfigDeliveryChannelRequest,
    ) -> main_models.DeleteConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.delete_config_delivery_channel_with_options(request, runtime)

    async def delete_config_delivery_channel_async(
        self,
        request: main_models.DeleteConfigDeliveryChannelRequest,
    ) -> main_models.DeleteConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.delete_config_delivery_channel_with_options_async(request, runtime)

    def delete_config_rules_with_options(
        self,
        request: main_models.DeleteConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_rules_with_options_async(
        self,
        request: main_models.DeleteConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_rules(
        self,
        request: main_models.DeleteConfigRulesRequest,
    ) -> main_models.DeleteConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_config_rules_with_options(request, runtime)

    async def delete_config_rules_async(
        self,
        request: main_models.DeleteConfigRulesRequest,
    ) -> main_models.DeleteConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_config_rules_with_options_async(request, runtime)

    def delete_remediations_with_options(
        self,
        request: main_models.DeleteRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRemediationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.remediation_ids):
            body['RemediationIds'] = request.remediation_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRemediations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_remediations_with_options_async(
        self,
        request: main_models.DeleteRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRemediationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.remediation_ids):
            body['RemediationIds'] = request.remediation_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRemediations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_remediations(
        self,
        request: main_models.DeleteRemediationsRequest,
    ) -> main_models.DeleteRemediationsResponse:
        runtime = RuntimeOptions()
        return self.delete_remediations_with_options(request, runtime)

    async def delete_remediations_async(
        self,
        request: main_models.DeleteRemediationsRequest,
    ) -> main_models.DeleteRemediationsResponse:
        runtime = RuntimeOptions()
        return await self.delete_remediations_with_options_async(request, runtime)

    def delete_report_template_with_options(
        self,
        request: main_models.DeleteReportTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReportTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.report_template_id):
            body['ReportTemplateId'] = request.report_template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReportTemplate',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReportTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_report_template_with_options_async(
        self,
        request: main_models.DeleteReportTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReportTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.report_template_id):
            body['ReportTemplateId'] = request.report_template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReportTemplate',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReportTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_report_template(
        self,
        request: main_models.DeleteReportTemplateRequest,
    ) -> main_models.DeleteReportTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_report_template_with_options(request, runtime)

    async def delete_report_template_async(
        self,
        request: main_models.DeleteReportTemplateRequest,
    ) -> main_models.DeleteReportTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_report_template_with_options_async(request, runtime)

    def describe_discovered_resource_batch_with_options(
        self,
        request: main_models.DescribeDiscoveredResourceBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiscoveredResourceBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiscoveredResourceBatch',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiscoveredResourceBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_discovered_resource_batch_with_options_async(
        self,
        request: main_models.DescribeDiscoveredResourceBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiscoveredResourceBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiscoveredResourceBatch',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiscoveredResourceBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_discovered_resource_batch(
        self,
        request: main_models.DescribeDiscoveredResourceBatchRequest,
    ) -> main_models.DescribeDiscoveredResourceBatchResponse:
        runtime = RuntimeOptions()
        return self.describe_discovered_resource_batch_with_options(request, runtime)

    async def describe_discovered_resource_batch_async(
        self,
        request: main_models.DescribeDiscoveredResourceBatchRequest,
    ) -> main_models.DescribeDiscoveredResourceBatchResponse:
        runtime = RuntimeOptions()
        return await self.describe_discovered_resource_batch_with_options_async(request, runtime)

    def describe_integrated_service_status_with_options(
        self,
        request: main_models.DescribeIntegratedServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIntegratedServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIntegratedServiceStatus',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIntegratedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_integrated_service_status_with_options_async(
        self,
        request: main_models.DescribeIntegratedServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIntegratedServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIntegratedServiceStatus',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIntegratedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_integrated_service_status(
        self,
        request: main_models.DescribeIntegratedServiceStatusRequest,
    ) -> main_models.DescribeIntegratedServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_integrated_service_status_with_options(request, runtime)

    async def describe_integrated_service_status_async(
        self,
        request: main_models.DescribeIntegratedServiceStatusRequest,
    ) -> main_models.DescribeIntegratedServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_integrated_service_status_with_options_async(request, runtime)

    def describe_remediation_with_options(
        self,
        request: main_models.DescribeRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRemediationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_remediation_with_options_async(
        self,
        request: main_models.DescribeRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRemediationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_remediation(
        self,
        request: main_models.DescribeRemediationRequest,
    ) -> main_models.DescribeRemediationResponse:
        runtime = RuntimeOptions()
        return self.describe_remediation_with_options(request, runtime)

    async def describe_remediation_async(
        self,
        request: main_models.DescribeRemediationRequest,
    ) -> main_models.DescribeRemediationResponse:
        runtime = RuntimeOptions()
        return await self.describe_remediation_with_options_async(request, runtime)

    def detach_aggregate_config_rule_to_compliance_pack_with_options(
        self,
        request: main_models.DetachAggregateConfigRuleToCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachAggregateConfigRuleToCompliancePackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachAggregateConfigRuleToCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachAggregateConfigRuleToCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_aggregate_config_rule_to_compliance_pack_with_options_async(
        self,
        request: main_models.DetachAggregateConfigRuleToCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachAggregateConfigRuleToCompliancePackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachAggregateConfigRuleToCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachAggregateConfigRuleToCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_aggregate_config_rule_to_compliance_pack(
        self,
        request: main_models.DetachAggregateConfigRuleToCompliancePackRequest,
    ) -> main_models.DetachAggregateConfigRuleToCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.detach_aggregate_config_rule_to_compliance_pack_with_options(request, runtime)

    async def detach_aggregate_config_rule_to_compliance_pack_async(
        self,
        request: main_models.DetachAggregateConfigRuleToCompliancePackRequest,
    ) -> main_models.DetachAggregateConfigRuleToCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.detach_aggregate_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def detach_config_rule_to_compliance_pack_with_options(
        self,
        request: main_models.DetachConfigRuleToCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachConfigRuleToCompliancePackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachConfigRuleToCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachConfigRuleToCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_config_rule_to_compliance_pack_with_options_async(
        self,
        request: main_models.DetachConfigRuleToCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachConfigRuleToCompliancePackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachConfigRuleToCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachConfigRuleToCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_config_rule_to_compliance_pack(
        self,
        request: main_models.DetachConfigRuleToCompliancePackRequest,
    ) -> main_models.DetachConfigRuleToCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.detach_config_rule_to_compliance_pack_with_options(request, runtime)

    async def detach_config_rule_to_compliance_pack_async(
        self,
        request: main_models.DetachConfigRuleToCompliancePackRequest,
    ) -> main_models.DetachConfigRuleToCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.detach_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def dry_run_config_rule_with_options(
        self,
        request: main_models.DryRunConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DryRunConfigRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configuration_item):
            body['ConfigurationItem'] = request.configuration_item
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DryRunConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DryRunConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def dry_run_config_rule_with_options_async(
        self,
        request: main_models.DryRunConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DryRunConfigRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configuration_item):
            body['ConfigurationItem'] = request.configuration_item
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DryRunConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DryRunConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dry_run_config_rule(
        self,
        request: main_models.DryRunConfigRuleRequest,
    ) -> main_models.DryRunConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.dry_run_config_rule_with_options(request, runtime)

    async def dry_run_config_rule_async(
        self,
        request: main_models.DryRunConfigRuleRequest,
    ) -> main_models.DryRunConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.dry_run_config_rule_with_options_async(request, runtime)

    def evaluate_pre_config_rules_with_options(
        self,
        tmp_req: main_models.EvaluatePreConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EvaluatePreConfigRulesResponse:
        tmp_req.validate()
        request = main_models.EvaluatePreConfigRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_evaluate_items):
            request.resource_evaluate_items_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_evaluate_items, 'ResourceEvaluateItems', 'json')
        body = {}
        if not DaraCore.is_null(request.enable_managed_rules):
            body['EnableManagedRules'] = request.enable_managed_rules
        if not DaraCore.is_null(request.resource_evaluate_items_shrink):
            body['ResourceEvaluateItems'] = request.resource_evaluate_items_shrink
        if not DaraCore.is_null(request.resource_type_format):
            body['ResourceTypeFormat'] = request.resource_type_format
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EvaluatePreConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvaluatePreConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_pre_config_rules_with_options_async(
        self,
        tmp_req: main_models.EvaluatePreConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EvaluatePreConfigRulesResponse:
        tmp_req.validate()
        request = main_models.EvaluatePreConfigRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_evaluate_items):
            request.resource_evaluate_items_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_evaluate_items, 'ResourceEvaluateItems', 'json')
        body = {}
        if not DaraCore.is_null(request.enable_managed_rules):
            body['EnableManagedRules'] = request.enable_managed_rules
        if not DaraCore.is_null(request.resource_evaluate_items_shrink):
            body['ResourceEvaluateItems'] = request.resource_evaluate_items_shrink
        if not DaraCore.is_null(request.resource_type_format):
            body['ResourceTypeFormat'] = request.resource_type_format
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EvaluatePreConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvaluatePreConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_pre_config_rules(
        self,
        request: main_models.EvaluatePreConfigRulesRequest,
    ) -> main_models.EvaluatePreConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.evaluate_pre_config_rules_with_options(request, runtime)

    async def evaluate_pre_config_rules_async(
        self,
        request: main_models.EvaluatePreConfigRulesRequest,
    ) -> main_models.EvaluatePreConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.evaluate_pre_config_rules_with_options_async(request, runtime)

    def generate_aggregate_compliance_pack_report_with_options(
        self,
        request: main_models.GenerateAggregateCompliancePackReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAggregateCompliancePackReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.multi_files):
            body['MultiFiles'] = request.multi_files
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAggregateCompliancePackReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAggregateCompliancePackReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_aggregate_compliance_pack_report_with_options_async(
        self,
        request: main_models.GenerateAggregateCompliancePackReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAggregateCompliancePackReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.multi_files):
            body['MultiFiles'] = request.multi_files
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAggregateCompliancePackReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAggregateCompliancePackReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_aggregate_compliance_pack_report(
        self,
        request: main_models.GenerateAggregateCompliancePackReportRequest,
    ) -> main_models.GenerateAggregateCompliancePackReportResponse:
        runtime = RuntimeOptions()
        return self.generate_aggregate_compliance_pack_report_with_options(request, runtime)

    async def generate_aggregate_compliance_pack_report_async(
        self,
        request: main_models.GenerateAggregateCompliancePackReportRequest,
    ) -> main_models.GenerateAggregateCompliancePackReportResponse:
        runtime = RuntimeOptions()
        return await self.generate_aggregate_compliance_pack_report_with_options_async(request, runtime)

    def generate_aggregate_config_rules_report_with_options(
        self,
        request: main_models.GenerateAggregateConfigRulesReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAggregateConfigRulesReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_ids):
            body['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAggregateConfigRulesReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAggregateConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_aggregate_config_rules_report_with_options_async(
        self,
        request: main_models.GenerateAggregateConfigRulesReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAggregateConfigRulesReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_ids):
            body['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAggregateConfigRulesReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAggregateConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_aggregate_config_rules_report(
        self,
        request: main_models.GenerateAggregateConfigRulesReportRequest,
    ) -> main_models.GenerateAggregateConfigRulesReportResponse:
        runtime = RuntimeOptions()
        return self.generate_aggregate_config_rules_report_with_options(request, runtime)

    async def generate_aggregate_config_rules_report_async(
        self,
        request: main_models.GenerateAggregateConfigRulesReportRequest,
    ) -> main_models.GenerateAggregateConfigRulesReportResponse:
        runtime = RuntimeOptions()
        return await self.generate_aggregate_config_rules_report_with_options_async(request, runtime)

    def generate_aggregate_resource_inventory_with_options(
        self,
        request: main_models.GenerateAggregateResourceInventoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAggregateResourceInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAggregateResourceInventory',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAggregateResourceInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_aggregate_resource_inventory_with_options_async(
        self,
        request: main_models.GenerateAggregateResourceInventoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAggregateResourceInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAggregateResourceInventory',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAggregateResourceInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_aggregate_resource_inventory(
        self,
        request: main_models.GenerateAggregateResourceInventoryRequest,
    ) -> main_models.GenerateAggregateResourceInventoryResponse:
        runtime = RuntimeOptions()
        return self.generate_aggregate_resource_inventory_with_options(request, runtime)

    async def generate_aggregate_resource_inventory_async(
        self,
        request: main_models.GenerateAggregateResourceInventoryRequest,
    ) -> main_models.GenerateAggregateResourceInventoryResponse:
        runtime = RuntimeOptions()
        return await self.generate_aggregate_resource_inventory_with_options_async(request, runtime)

    def generate_compliance_pack_report_with_options(
        self,
        request: main_models.GenerateCompliancePackReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCompliancePackReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCompliancePackReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCompliancePackReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_compliance_pack_report_with_options_async(
        self,
        request: main_models.GenerateCompliancePackReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCompliancePackReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCompliancePackReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCompliancePackReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_compliance_pack_report(
        self,
        request: main_models.GenerateCompliancePackReportRequest,
    ) -> main_models.GenerateCompliancePackReportResponse:
        runtime = RuntimeOptions()
        return self.generate_compliance_pack_report_with_options(request, runtime)

    async def generate_compliance_pack_report_async(
        self,
        request: main_models.GenerateCompliancePackReportRequest,
    ) -> main_models.GenerateCompliancePackReportResponse:
        runtime = RuntimeOptions()
        return await self.generate_compliance_pack_report_with_options_async(request, runtime)

    def generate_config_rules_report_with_options(
        self,
        request: main_models.GenerateConfigRulesReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateConfigRulesReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_ids):
            body['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateConfigRulesReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_config_rules_report_with_options_async(
        self,
        request: main_models.GenerateConfigRulesReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateConfigRulesReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_ids):
            body['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateConfigRulesReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_config_rules_report(
        self,
        request: main_models.GenerateConfigRulesReportRequest,
    ) -> main_models.GenerateConfigRulesReportResponse:
        runtime = RuntimeOptions()
        return self.generate_config_rules_report_with_options(request, runtime)

    async def generate_config_rules_report_async(
        self,
        request: main_models.GenerateConfigRulesReportRequest,
    ) -> main_models.GenerateConfigRulesReportResponse:
        runtime = RuntimeOptions()
        return await self.generate_config_rules_report_with_options_async(request, runtime)

    def generate_report_from_template_with_options(
        self,
        request: main_models.GenerateReportFromTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateReportFromTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.report_template_id):
            body['ReportTemplateId'] = request.report_template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateReportFromTemplate',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateReportFromTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_report_from_template_with_options_async(
        self,
        request: main_models.GenerateReportFromTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateReportFromTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.report_template_id):
            body['ReportTemplateId'] = request.report_template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateReportFromTemplate',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateReportFromTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_report_from_template(
        self,
        request: main_models.GenerateReportFromTemplateRequest,
    ) -> main_models.GenerateReportFromTemplateResponse:
        runtime = RuntimeOptions()
        return self.generate_report_from_template_with_options(request, runtime)

    async def generate_report_from_template_async(
        self,
        request: main_models.GenerateReportFromTemplateRequest,
    ) -> main_models.GenerateReportFromTemplateResponse:
        runtime = RuntimeOptions()
        return await self.generate_report_from_template_with_options_async(request, runtime)

    def generate_resource_inventory_with_options(
        self,
        request: main_models.GenerateResourceInventoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateResourceInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateResourceInventory',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateResourceInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_resource_inventory_with_options_async(
        self,
        request: main_models.GenerateResourceInventoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateResourceInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateResourceInventory',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateResourceInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_resource_inventory(
        self,
        request: main_models.GenerateResourceInventoryRequest,
    ) -> main_models.GenerateResourceInventoryResponse:
        runtime = RuntimeOptions()
        return self.generate_resource_inventory_with_options(request, runtime)

    async def generate_resource_inventory_async(
        self,
        request: main_models.GenerateResourceInventoryRequest,
    ) -> main_models.GenerateResourceInventoryResponse:
        runtime = RuntimeOptions()
        return await self.generate_resource_inventory_with_options_async(request, runtime)

    def get_advanced_search_file_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdvancedSearchFileResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAdvancedSearchFile',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdvancedSearchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_advanced_search_file_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdvancedSearchFileResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAdvancedSearchFile',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdvancedSearchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_advanced_search_file(self) -> main_models.GetAdvancedSearchFileResponse:
        runtime = RuntimeOptions()
        return self.get_advanced_search_file_with_options(runtime)

    async def get_advanced_search_file_async(self) -> main_models.GetAdvancedSearchFileResponse:
        runtime = RuntimeOptions()
        return await self.get_advanced_search_file_with_options_async(runtime)

    def get_aggregate_account_compliance_by_pack_with_options(
        self,
        request: main_models.GetAggregateAccountComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateAccountComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateAccountComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateAccountComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_account_compliance_by_pack_with_options_async(
        self,
        request: main_models.GetAggregateAccountComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateAccountComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateAccountComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateAccountComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_account_compliance_by_pack(
        self,
        request: main_models.GetAggregateAccountComplianceByPackRequest,
    ) -> main_models.GetAggregateAccountComplianceByPackResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_account_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_account_compliance_by_pack_async(
        self,
        request: main_models.GetAggregateAccountComplianceByPackRequest,
    ) -> main_models.GetAggregateAccountComplianceByPackResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_account_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_advanced_search_file_with_options(
        self,
        request: main_models.GetAggregateAdvancedSearchFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateAdvancedSearchFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateAdvancedSearchFile',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateAdvancedSearchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_advanced_search_file_with_options_async(
        self,
        request: main_models.GetAggregateAdvancedSearchFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateAdvancedSearchFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateAdvancedSearchFile',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateAdvancedSearchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_advanced_search_file(
        self,
        request: main_models.GetAggregateAdvancedSearchFileRequest,
    ) -> main_models.GetAggregateAdvancedSearchFileResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_advanced_search_file_with_options(request, runtime)

    async def get_aggregate_advanced_search_file_async(
        self,
        request: main_models.GetAggregateAdvancedSearchFileRequest,
    ) -> main_models.GetAggregateAdvancedSearchFileResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_advanced_search_file_with_options_async(request, runtime)

    def get_aggregate_compliance_pack_with_options(
        self,
        tmp_req: main_models.GetAggregateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.GetAggregateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_compliance_pack_with_options_async(
        self,
        tmp_req: main_models.GetAggregateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.GetAggregateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_compliance_pack(
        self,
        request: main_models.GetAggregateCompliancePackRequest,
    ) -> main_models.GetAggregateCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_compliance_pack_with_options(request, runtime)

    async def get_aggregate_compliance_pack_async(
        self,
        request: main_models.GetAggregateCompliancePackRequest,
    ) -> main_models.GetAggregateCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_compliance_pack_with_options_async(request, runtime)

    def get_aggregate_compliance_pack_report_with_options(
        self,
        request: main_models.GetAggregateCompliancePackReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateCompliancePackReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateCompliancePackReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateCompliancePackReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_compliance_pack_report_with_options_async(
        self,
        request: main_models.GetAggregateCompliancePackReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateCompliancePackReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateCompliancePackReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateCompliancePackReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_compliance_pack_report(
        self,
        request: main_models.GetAggregateCompliancePackReportRequest,
    ) -> main_models.GetAggregateCompliancePackReportResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_compliance_pack_report_with_options(request, runtime)

    async def get_aggregate_compliance_pack_report_async(
        self,
        request: main_models.GetAggregateCompliancePackReportRequest,
    ) -> main_models.GetAggregateCompliancePackReportResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_compliance_pack_report_with_options_async(request, runtime)

    def get_aggregate_compliance_summary_with_options(
        self,
        request: main_models.GetAggregateComplianceSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateComplianceSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateComplianceSummary',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateComplianceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_compliance_summary_with_options_async(
        self,
        request: main_models.GetAggregateComplianceSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateComplianceSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateComplianceSummary',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateComplianceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_compliance_summary(
        self,
        request: main_models.GetAggregateComplianceSummaryRequest,
    ) -> main_models.GetAggregateComplianceSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_compliance_summary_with_options(request, runtime)

    async def get_aggregate_compliance_summary_async(
        self,
        request: main_models.GetAggregateComplianceSummaryRequest,
    ) -> main_models.GetAggregateComplianceSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_compliance_summary_with_options_async(request, runtime)

    def get_aggregate_config_delivery_channel_with_options(
        self,
        request: main_models.GetAggregateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_delivery_channel_with_options_async(
        self,
        request: main_models.GetAggregateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_delivery_channel(
        self,
        request: main_models.GetAggregateConfigDeliveryChannelRequest,
    ) -> main_models.GetAggregateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_config_delivery_channel_with_options(request, runtime)

    async def get_aggregate_config_delivery_channel_async(
        self,
        request: main_models.GetAggregateConfigDeliveryChannelRequest,
    ) -> main_models.GetAggregateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def get_aggregate_config_rule_with_options(
        self,
        tmp_req: main_models.GetAggregateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.GetAggregateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rule_with_options_async(
        self,
        tmp_req: main_models.GetAggregateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.GetAggregateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rule(
        self,
        request: main_models.GetAggregateConfigRuleRequest,
    ) -> main_models.GetAggregateConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_config_rule_with_options(request, runtime)

    async def get_aggregate_config_rule_async(
        self,
        request: main_models.GetAggregateConfigRuleRequest,
    ) -> main_models.GetAggregateConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_config_rule_with_options_async(request, runtime)

    def get_aggregate_config_rule_compliance_by_pack_with_options(
        self,
        request: main_models.GetAggregateConfigRuleComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigRuleComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigRuleComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigRuleComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rule_compliance_by_pack_with_options_async(
        self,
        request: main_models.GetAggregateConfigRuleComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigRuleComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigRuleComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigRuleComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rule_compliance_by_pack(
        self,
        request: main_models.GetAggregateConfigRuleComplianceByPackRequest,
    ) -> main_models.GetAggregateConfigRuleComplianceByPackResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_config_rule_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_config_rule_compliance_by_pack_async(
        self,
        request: main_models.GetAggregateConfigRuleComplianceByPackRequest,
    ) -> main_models.GetAggregateConfigRuleComplianceByPackResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_config_rule_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_config_rule_summary_by_risk_level_with_options(
        self,
        request: main_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigRuleSummaryByRiskLevel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigRuleSummaryByRiskLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rule_summary_by_risk_level_with_options_async(
        self,
        request: main_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigRuleSummaryByRiskLevel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigRuleSummaryByRiskLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rule_summary_by_risk_level(
        self,
        request: main_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
    ) -> main_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_config_rule_summary_by_risk_level_with_options(request, runtime)

    async def get_aggregate_config_rule_summary_by_risk_level_async(
        self,
        request: main_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
    ) -> main_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_config_rule_summary_by_risk_level_with_options_async(request, runtime)

    def get_aggregate_config_rules_report_with_options(
        self,
        request: main_models.GetAggregateConfigRulesReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigRulesReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigRulesReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rules_report_with_options_async(
        self,
        request: main_models.GetAggregateConfigRulesReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateConfigRulesReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateConfigRulesReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rules_report(
        self,
        request: main_models.GetAggregateConfigRulesReportRequest,
    ) -> main_models.GetAggregateConfigRulesReportResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_config_rules_report_with_options(request, runtime)

    async def get_aggregate_config_rules_report_async(
        self,
        request: main_models.GetAggregateConfigRulesReportRequest,
    ) -> main_models.GetAggregateConfigRulesReportResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_config_rules_report_with_options_async(request, runtime)

    def get_aggregate_discovered_resource_with_options(
        self,
        request: main_models.GetAggregateDiscoveredResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateDiscoveredResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_option):
            query['ComplianceOption'] = request.compliance_option
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateDiscoveredResource',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_discovered_resource_with_options_async(
        self,
        request: main_models.GetAggregateDiscoveredResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateDiscoveredResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_option):
            query['ComplianceOption'] = request.compliance_option
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateDiscoveredResource',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_discovered_resource(
        self,
        request: main_models.GetAggregateDiscoveredResourceRequest,
    ) -> main_models.GetAggregateDiscoveredResourceResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_discovered_resource_with_options(request, runtime)

    async def get_aggregate_discovered_resource_async(
        self,
        request: main_models.GetAggregateDiscoveredResourceRequest,
    ) -> main_models.GetAggregateDiscoveredResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_discovered_resource_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_by_config_rule_with_options(
        self,
        request: main_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceByConfigRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceByConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceByConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_by_config_rule_with_options_async(
        self,
        request: main_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceByConfigRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceByConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceByConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_by_config_rule(
        self,
        request: main_models.GetAggregateResourceComplianceByConfigRuleRequest,
    ) -> main_models.GetAggregateResourceComplianceByConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_compliance_by_config_rule_with_options(request, runtime)

    async def get_aggregate_resource_compliance_by_config_rule_async(
        self,
        request: main_models.GetAggregateResourceComplianceByConfigRuleRequest,
    ) -> main_models.GetAggregateResourceComplianceByConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_compliance_by_config_rule_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_by_pack_with_options(
        self,
        request: main_models.GetAggregateResourceComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_by_pack_with_options_async(
        self,
        request: main_models.GetAggregateResourceComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_by_pack(
        self,
        request: main_models.GetAggregateResourceComplianceByPackRequest,
    ) -> main_models.GetAggregateResourceComplianceByPackResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_resource_compliance_by_pack_async(
        self,
        request: main_models.GetAggregateResourceComplianceByPackRequest,
    ) -> main_models.GetAggregateResourceComplianceByPackResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_group_by_region_with_options(
        self,
        request: main_models.GetAggregateResourceComplianceGroupByRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceGroupByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceGroupByRegion',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_group_by_region_with_options_async(
        self,
        request: main_models.GetAggregateResourceComplianceGroupByRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceGroupByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceGroupByRegion',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_group_by_region(
        self,
        request: main_models.GetAggregateResourceComplianceGroupByRegionRequest,
    ) -> main_models.GetAggregateResourceComplianceGroupByRegionResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_compliance_group_by_region_with_options(request, runtime)

    async def get_aggregate_resource_compliance_group_by_region_async(
        self,
        request: main_models.GetAggregateResourceComplianceGroupByRegionRequest,
    ) -> main_models.GetAggregateResourceComplianceGroupByRegionResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_compliance_group_by_region_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_group_by_resource_type_with_options(
        self,
        request: main_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceGroupByResourceType',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_group_by_resource_type_with_options_async(
        self,
        request: main_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceGroupByResourceType',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_group_by_resource_type(
        self,
        request: main_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
    ) -> main_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_compliance_group_by_resource_type_with_options(request, runtime)

    async def get_aggregate_resource_compliance_group_by_resource_type_async(
        self,
        request: main_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
    ) -> main_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_compliance_group_by_resource_type_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_timeline_with_options(
        self,
        request: main_models.GetAggregateResourceComplianceTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceTimelineResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceTimeline',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_timeline_with_options_async(
        self,
        request: main_models.GetAggregateResourceComplianceTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceComplianceTimelineResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceComplianceTimeline',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceComplianceTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_timeline(
        self,
        request: main_models.GetAggregateResourceComplianceTimelineRequest,
    ) -> main_models.GetAggregateResourceComplianceTimelineResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_compliance_timeline_with_options(request, runtime)

    async def get_aggregate_resource_compliance_timeline_async(
        self,
        request: main_models.GetAggregateResourceComplianceTimelineRequest,
    ) -> main_models.GetAggregateResourceComplianceTimelineResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_compliance_timeline_with_options_async(request, runtime)

    def get_aggregate_resource_configuration_timeline_with_options(
        self,
        request: main_models.GetAggregateResourceConfigurationTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceConfigurationTimelineResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceConfigurationTimeline',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceConfigurationTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_configuration_timeline_with_options_async(
        self,
        request: main_models.GetAggregateResourceConfigurationTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceConfigurationTimelineResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceConfigurationTimeline',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceConfigurationTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_configuration_timeline(
        self,
        request: main_models.GetAggregateResourceConfigurationTimelineRequest,
    ) -> main_models.GetAggregateResourceConfigurationTimelineResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_configuration_timeline_with_options(request, runtime)

    async def get_aggregate_resource_configuration_timeline_async(
        self,
        request: main_models.GetAggregateResourceConfigurationTimelineRequest,
    ) -> main_models.GetAggregateResourceConfigurationTimelineResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_configuration_timeline_with_options_async(request, runtime)

    def get_aggregate_resource_counts_group_by_region_with_options(
        self,
        request: main_models.GetAggregateResourceCountsGroupByRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceCountsGroupByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceCountsGroupByRegion',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceCountsGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_counts_group_by_region_with_options_async(
        self,
        request: main_models.GetAggregateResourceCountsGroupByRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceCountsGroupByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceCountsGroupByRegion',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceCountsGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_counts_group_by_region(
        self,
        request: main_models.GetAggregateResourceCountsGroupByRegionRequest,
    ) -> main_models.GetAggregateResourceCountsGroupByRegionResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_counts_group_by_region_with_options(request, runtime)

    async def get_aggregate_resource_counts_group_by_region_async(
        self,
        request: main_models.GetAggregateResourceCountsGroupByRegionRequest,
    ) -> main_models.GetAggregateResourceCountsGroupByRegionResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_counts_group_by_region_with_options_async(request, runtime)

    def get_aggregate_resource_counts_group_by_resource_type_with_options(
        self,
        request: main_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceCountsGroupByResourceType',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceCountsGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_counts_group_by_resource_type_with_options_async(
        self,
        request: main_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceCountsGroupByResourceType',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceCountsGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_counts_group_by_resource_type(
        self,
        request: main_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
    ) -> main_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_counts_group_by_resource_type_with_options(request, runtime)

    async def get_aggregate_resource_counts_group_by_resource_type_async(
        self,
        request: main_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
    ) -> main_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_counts_group_by_resource_type_with_options_async(request, runtime)

    def get_aggregate_resource_inventory_with_options(
        self,
        request: main_models.GetAggregateResourceInventoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceInventory',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_inventory_with_options_async(
        self,
        request: main_models.GetAggregateResourceInventoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregateResourceInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregateResourceInventory',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregateResourceInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_inventory(
        self,
        request: main_models.GetAggregateResourceInventoryRequest,
    ) -> main_models.GetAggregateResourceInventoryResponse:
        runtime = RuntimeOptions()
        return self.get_aggregate_resource_inventory_with_options(request, runtime)

    async def get_aggregate_resource_inventory_async(
        self,
        request: main_models.GetAggregateResourceInventoryRequest,
    ) -> main_models.GetAggregateResourceInventoryResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregate_resource_inventory_with_options_async(request, runtime)

    def get_aggregator_with_options(
        self,
        tmp_req: main_models.GetAggregatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregatorResponse:
        tmp_req.validate()
        request = main_models.GetAggregatorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregator',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregator_with_options_async(
        self,
        tmp_req: main_models.GetAggregatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAggregatorResponse:
        tmp_req.validate()
        request = main_models.GetAggregatorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAggregator',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAggregatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregator(
        self,
        request: main_models.GetAggregatorRequest,
    ) -> main_models.GetAggregatorResponse:
        runtime = RuntimeOptions()
        return self.get_aggregator_with_options(request, runtime)

    async def get_aggregator_async(
        self,
        request: main_models.GetAggregatorRequest,
    ) -> main_models.GetAggregatorResponse:
        runtime = RuntimeOptions()
        return await self.get_aggregator_with_options_async(request, runtime)

    def get_compliance_pack_with_options(
        self,
        tmp_req: main_models.GetCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCompliancePackResponse:
        tmp_req.validate()
        request = main_models.GetCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compliance_pack_with_options_async(
        self,
        tmp_req: main_models.GetCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCompliancePackResponse:
        tmp_req.validate()
        request = main_models.GetCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compliance_pack(
        self,
        request: main_models.GetCompliancePackRequest,
    ) -> main_models.GetCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.get_compliance_pack_with_options(request, runtime)

    async def get_compliance_pack_async(
        self,
        request: main_models.GetCompliancePackRequest,
    ) -> main_models.GetCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.get_compliance_pack_with_options_async(request, runtime)

    def get_compliance_pack_report_with_options(
        self,
        request: main_models.GetCompliancePackReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCompliancePackReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCompliancePackReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCompliancePackReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compliance_pack_report_with_options_async(
        self,
        request: main_models.GetCompliancePackReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCompliancePackReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCompliancePackReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCompliancePackReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compliance_pack_report(
        self,
        request: main_models.GetCompliancePackReportRequest,
    ) -> main_models.GetCompliancePackReportResponse:
        runtime = RuntimeOptions()
        return self.get_compliance_pack_report_with_options(request, runtime)

    async def get_compliance_pack_report_async(
        self,
        request: main_models.GetCompliancePackReportRequest,
    ) -> main_models.GetCompliancePackReportResponse:
        runtime = RuntimeOptions()
        return await self.get_compliance_pack_report_with_options_async(request, runtime)

    def get_compliance_summary_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetComplianceSummaryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetComplianceSummary',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComplianceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compliance_summary_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetComplianceSummaryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetComplianceSummary',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComplianceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compliance_summary(self) -> main_models.GetComplianceSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_compliance_summary_with_options(runtime)

    async def get_compliance_summary_async(self) -> main_models.GetComplianceSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_compliance_summary_with_options_async(runtime)

    def get_config_delivery_channel_with_options(
        self,
        request: main_models.GetConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_delivery_channel_with_options_async(
        self,
        request: main_models.GetConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_delivery_channel(
        self,
        request: main_models.GetConfigDeliveryChannelRequest,
    ) -> main_models.GetConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.get_config_delivery_channel_with_options(request, runtime)

    async def get_config_delivery_channel_async(
        self,
        request: main_models.GetConfigDeliveryChannelRequest,
    ) -> main_models.GetConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.get_config_delivery_channel_with_options_async(request, runtime)

    def get_config_rule_with_options(
        self,
        tmp_req: main_models.GetConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRuleResponse:
        tmp_req.validate()
        request = main_models.GetConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rule_with_options_async(
        self,
        tmp_req: main_models.GetConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRuleResponse:
        tmp_req.validate()
        request = main_models.GetConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rule(
        self,
        request: main_models.GetConfigRuleRequest,
    ) -> main_models.GetConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.get_config_rule_with_options(request, runtime)

    async def get_config_rule_async(
        self,
        request: main_models.GetConfigRuleRequest,
    ) -> main_models.GetConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_config_rule_with_options_async(request, runtime)

    def get_config_rule_compliance_by_pack_with_options(
        self,
        request: main_models.GetConfigRuleComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRuleComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigRuleComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRuleComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rule_compliance_by_pack_with_options_async(
        self,
        request: main_models.GetConfigRuleComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRuleComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigRuleComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRuleComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rule_compliance_by_pack(
        self,
        request: main_models.GetConfigRuleComplianceByPackRequest,
    ) -> main_models.GetConfigRuleComplianceByPackResponse:
        runtime = RuntimeOptions()
        return self.get_config_rule_compliance_by_pack_with_options(request, runtime)

    async def get_config_rule_compliance_by_pack_async(
        self,
        request: main_models.GetConfigRuleComplianceByPackRequest,
    ) -> main_models.GetConfigRuleComplianceByPackResponse:
        runtime = RuntimeOptions()
        return await self.get_config_rule_compliance_by_pack_with_options_async(request, runtime)

    def get_config_rule_summary_by_risk_level_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRuleSummaryByRiskLevelResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetConfigRuleSummaryByRiskLevel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRuleSummaryByRiskLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rule_summary_by_risk_level_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRuleSummaryByRiskLevelResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetConfigRuleSummaryByRiskLevel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRuleSummaryByRiskLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rule_summary_by_risk_level(self) -> main_models.GetConfigRuleSummaryByRiskLevelResponse:
        runtime = RuntimeOptions()
        return self.get_config_rule_summary_by_risk_level_with_options(runtime)

    async def get_config_rule_summary_by_risk_level_async(self) -> main_models.GetConfigRuleSummaryByRiskLevelResponse:
        runtime = RuntimeOptions()
        return await self.get_config_rule_summary_by_risk_level_with_options_async(runtime)

    def get_config_rules_report_with_options(
        self,
        request: main_models.GetConfigRulesReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRulesReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigRulesReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rules_report_with_options_async(
        self,
        request: main_models.GetConfigRulesReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRulesReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigRulesReport',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rules_report(
        self,
        request: main_models.GetConfigRulesReportRequest,
    ) -> main_models.GetConfigRulesReportResponse:
        runtime = RuntimeOptions()
        return self.get_config_rules_report_with_options(request, runtime)

    async def get_config_rules_report_async(
        self,
        request: main_models.GetConfigRulesReportRequest,
    ) -> main_models.GetConfigRulesReportResponse:
        runtime = RuntimeOptions()
        return await self.get_config_rules_report_with_options_async(request, runtime)

    def get_configuration_recorder_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigurationRecorderResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetConfigurationRecorder',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_configuration_recorder_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigurationRecorderResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetConfigurationRecorder',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_configuration_recorder(self) -> main_models.GetConfigurationRecorderResponse:
        runtime = RuntimeOptions()
        return self.get_configuration_recorder_with_options(runtime)

    async def get_configuration_recorder_async(self) -> main_models.GetConfigurationRecorderResponse:
        runtime = RuntimeOptions()
        return await self.get_configuration_recorder_with_options_async(runtime)

    def get_discovered_resource_with_options(
        self,
        request: main_models.GetDiscoveredResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDiscoveredResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_option):
            query['ComplianceOption'] = request.compliance_option
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiscoveredResource',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_with_options_async(
        self,
        request: main_models.GetDiscoveredResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDiscoveredResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_option):
            query['ComplianceOption'] = request.compliance_option
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiscoveredResource',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource(
        self,
        request: main_models.GetDiscoveredResourceRequest,
    ) -> main_models.GetDiscoveredResourceResponse:
        runtime = RuntimeOptions()
        return self.get_discovered_resource_with_options(request, runtime)

    async def get_discovered_resource_async(
        self,
        request: main_models.GetDiscoveredResourceRequest,
    ) -> main_models.GetDiscoveredResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_discovered_resource_with_options_async(request, runtime)

    def get_discovered_resource_counts_group_by_region_with_options(
        self,
        request: main_models.GetDiscoveredResourceCountsGroupByRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiscoveredResourceCountsGroupByRegion',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiscoveredResourceCountsGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_counts_group_by_region_with_options_async(
        self,
        request: main_models.GetDiscoveredResourceCountsGroupByRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiscoveredResourceCountsGroupByRegion',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiscoveredResourceCountsGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource_counts_group_by_region(
        self,
        request: main_models.GetDiscoveredResourceCountsGroupByRegionRequest,
    ) -> main_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        runtime = RuntimeOptions()
        return self.get_discovered_resource_counts_group_by_region_with_options(request, runtime)

    async def get_discovered_resource_counts_group_by_region_async(
        self,
        request: main_models.GetDiscoveredResourceCountsGroupByRegionRequest,
    ) -> main_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        runtime = RuntimeOptions()
        return await self.get_discovered_resource_counts_group_by_region_with_options_async(request, runtime)

    def get_discovered_resource_counts_group_by_resource_type_with_options(
        self,
        request: main_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiscoveredResourceCountsGroupByResourceType',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_counts_group_by_resource_type_with_options_async(
        self,
        request: main_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiscoveredResourceCountsGroupByResourceType',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource_counts_group_by_resource_type(
        self,
        request: main_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
    ) -> main_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.get_discovered_resource_counts_group_by_resource_type_with_options(request, runtime)

    async def get_discovered_resource_counts_group_by_resource_type_async(
        self,
        request: main_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
    ) -> main_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.get_discovered_resource_counts_group_by_resource_type_with_options_async(request, runtime)

    def get_integrated_service_status_with_options(
        self,
        request: main_models.GetIntegratedServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegratedServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIntegratedServiceStatus',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegratedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integrated_service_status_with_options_async(
        self,
        request: main_models.GetIntegratedServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegratedServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIntegratedServiceStatus',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegratedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integrated_service_status(
        self,
        request: main_models.GetIntegratedServiceStatusRequest,
    ) -> main_models.GetIntegratedServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_integrated_service_status_with_options(request, runtime)

    async def get_integrated_service_status_async(
        self,
        request: main_models.GetIntegratedServiceStatusRequest,
    ) -> main_models.GetIntegratedServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_integrated_service_status_with_options_async(request, runtime)

    def get_managed_rule_with_options(
        self,
        request: main_models.GetManagedRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetManagedRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_managed_rule_with_options_async(
        self,
        request: main_models.GetManagedRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetManagedRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_managed_rule(
        self,
        request: main_models.GetManagedRuleRequest,
    ) -> main_models.GetManagedRuleResponse:
        runtime = RuntimeOptions()
        return self.get_managed_rule_with_options(request, runtime)

    async def get_managed_rule_async(
        self,
        request: main_models.GetManagedRuleRequest,
    ) -> main_models.GetManagedRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_managed_rule_with_options_async(request, runtime)

    def get_remediation_template_with_options(
        self,
        request: main_models.GetRemediationTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRemediationTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_identifier):
            query['TemplateIdentifier'] = request.template_identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRemediationTemplate',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRemediationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_remediation_template_with_options_async(
        self,
        request: main_models.GetRemediationTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRemediationTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_identifier):
            query['TemplateIdentifier'] = request.template_identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRemediationTemplate',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRemediationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_remediation_template(
        self,
        request: main_models.GetRemediationTemplateRequest,
    ) -> main_models.GetRemediationTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_remediation_template_with_options(request, runtime)

    async def get_remediation_template_async(
        self,
        request: main_models.GetRemediationTemplateRequest,
    ) -> main_models.GetRemediationTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_remediation_template_with_options_async(request, runtime)

    def get_report_from_template_with_options(
        self,
        request: main_models.GetReportFromTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetReportFromTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_template_id):
            query['ReportTemplateId'] = request.report_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetReportFromTemplate',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReportFromTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_report_from_template_with_options_async(
        self,
        request: main_models.GetReportFromTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetReportFromTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_template_id):
            query['ReportTemplateId'] = request.report_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetReportFromTemplate',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReportFromTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_report_from_template(
        self,
        request: main_models.GetReportFromTemplateRequest,
    ) -> main_models.GetReportFromTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_report_from_template_with_options(request, runtime)

    async def get_report_from_template_async(
        self,
        request: main_models.GetReportFromTemplateRequest,
    ) -> main_models.GetReportFromTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_report_from_template_with_options_async(request, runtime)

    def get_resource_compliance_by_config_rule_with_options(
        self,
        request: main_models.GetResourceComplianceByConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceByConfigRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceByConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceByConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_by_config_rule_with_options_async(
        self,
        request: main_models.GetResourceComplianceByConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceByConfigRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceByConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceByConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_by_config_rule(
        self,
        request: main_models.GetResourceComplianceByConfigRuleRequest,
    ) -> main_models.GetResourceComplianceByConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.get_resource_compliance_by_config_rule_with_options(request, runtime)

    async def get_resource_compliance_by_config_rule_async(
        self,
        request: main_models.GetResourceComplianceByConfigRuleRequest,
    ) -> main_models.GetResourceComplianceByConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_compliance_by_config_rule_with_options_async(request, runtime)

    def get_resource_compliance_by_pack_with_options(
        self,
        request: main_models.GetResourceComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_by_pack_with_options_async(
        self,
        request: main_models.GetResourceComplianceByPackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceByPackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceByPack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_by_pack(
        self,
        request: main_models.GetResourceComplianceByPackRequest,
    ) -> main_models.GetResourceComplianceByPackResponse:
        runtime = RuntimeOptions()
        return self.get_resource_compliance_by_pack_with_options(request, runtime)

    async def get_resource_compliance_by_pack_async(
        self,
        request: main_models.GetResourceComplianceByPackRequest,
    ) -> main_models.GetResourceComplianceByPackResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_compliance_by_pack_with_options_async(request, runtime)

    def get_resource_compliance_group_by_region_with_options(
        self,
        request: main_models.GetResourceComplianceGroupByRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceGroupByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceGroupByRegion',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_group_by_region_with_options_async(
        self,
        request: main_models.GetResourceComplianceGroupByRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceGroupByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceGroupByRegion',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_group_by_region(
        self,
        request: main_models.GetResourceComplianceGroupByRegionRequest,
    ) -> main_models.GetResourceComplianceGroupByRegionResponse:
        runtime = RuntimeOptions()
        return self.get_resource_compliance_group_by_region_with_options(request, runtime)

    async def get_resource_compliance_group_by_region_async(
        self,
        request: main_models.GetResourceComplianceGroupByRegionRequest,
    ) -> main_models.GetResourceComplianceGroupByRegionResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_compliance_group_by_region_with_options_async(request, runtime)

    def get_resource_compliance_group_by_resource_type_with_options(
        self,
        request: main_models.GetResourceComplianceGroupByResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceGroupByResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceGroupByResourceType',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_group_by_resource_type_with_options_async(
        self,
        request: main_models.GetResourceComplianceGroupByResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceGroupByResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceGroupByResourceType',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_group_by_resource_type(
        self,
        request: main_models.GetResourceComplianceGroupByResourceTypeRequest,
    ) -> main_models.GetResourceComplianceGroupByResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.get_resource_compliance_group_by_resource_type_with_options(request, runtime)

    async def get_resource_compliance_group_by_resource_type_async(
        self,
        request: main_models.GetResourceComplianceGroupByResourceTypeRequest,
    ) -> main_models.GetResourceComplianceGroupByResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_compliance_group_by_resource_type_with_options_async(request, runtime)

    def get_resource_compliance_timeline_with_options(
        self,
        request: main_models.GetResourceComplianceTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceTimelineResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceTimeline',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_timeline_with_options_async(
        self,
        request: main_models.GetResourceComplianceTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceComplianceTimelineResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceComplianceTimeline',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceComplianceTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_timeline(
        self,
        request: main_models.GetResourceComplianceTimelineRequest,
    ) -> main_models.GetResourceComplianceTimelineResponse:
        runtime = RuntimeOptions()
        return self.get_resource_compliance_timeline_with_options(request, runtime)

    async def get_resource_compliance_timeline_async(
        self,
        request: main_models.GetResourceComplianceTimelineRequest,
    ) -> main_models.GetResourceComplianceTimelineResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_compliance_timeline_with_options_async(request, runtime)

    def get_resource_configuration_sample_with_options(
        self,
        request: main_models.GetResourceConfigurationSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceConfigurationSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mock_only):
            query['MockOnly'] = request.mock_only
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceConfigurationSample',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceConfigurationSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_configuration_sample_with_options_async(
        self,
        request: main_models.GetResourceConfigurationSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceConfigurationSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mock_only):
            query['MockOnly'] = request.mock_only
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceConfigurationSample',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceConfigurationSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_configuration_sample(
        self,
        request: main_models.GetResourceConfigurationSampleRequest,
    ) -> main_models.GetResourceConfigurationSampleResponse:
        runtime = RuntimeOptions()
        return self.get_resource_configuration_sample_with_options(request, runtime)

    async def get_resource_configuration_sample_async(
        self,
        request: main_models.GetResourceConfigurationSampleRequest,
    ) -> main_models.GetResourceConfigurationSampleResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_configuration_sample_with_options_async(request, runtime)

    def get_resource_configuration_timeline_with_options(
        self,
        request: main_models.GetResourceConfigurationTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceConfigurationTimelineResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceConfigurationTimeline',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceConfigurationTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_configuration_timeline_with_options_async(
        self,
        request: main_models.GetResourceConfigurationTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceConfigurationTimelineResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceConfigurationTimeline',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceConfigurationTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_configuration_timeline(
        self,
        request: main_models.GetResourceConfigurationTimelineRequest,
    ) -> main_models.GetResourceConfigurationTimelineResponse:
        runtime = RuntimeOptions()
        return self.get_resource_configuration_timeline_with_options(request, runtime)

    async def get_resource_configuration_timeline_async(
        self,
        request: main_models.GetResourceConfigurationTimelineRequest,
    ) -> main_models.GetResourceConfigurationTimelineResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_configuration_timeline_with_options_async(request, runtime)

    def get_resource_inventory_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceInventoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceInventory',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_inventory_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceInventoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceInventory',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_inventory(self) -> main_models.GetResourceInventoryResponse:
        runtime = RuntimeOptions()
        return self.get_resource_inventory_with_options(runtime)

    async def get_resource_inventory_async(self) -> main_models.GetResourceInventoryResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_inventory_with_options_async(runtime)

    def get_resource_type_properties_with_options(
        self,
        request: main_models.GetResourceTypePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypePropertiesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceTypeProperties',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_properties_with_options_async(
        self,
        request: main_models.GetResourceTypePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypePropertiesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceTypeProperties',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type_properties(
        self,
        request: main_models.GetResourceTypePropertiesRequest,
    ) -> main_models.GetResourceTypePropertiesResponse:
        runtime = RuntimeOptions()
        return self.get_resource_type_properties_with_options(request, runtime)

    async def get_resource_type_properties_async(
        self,
        request: main_models.GetResourceTypePropertiesRequest,
    ) -> main_models.GetResourceTypePropertiesResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_type_properties_with_options_async(request, runtime)

    def get_supported_resource_relation_config_with_options(
        self,
        request: main_models.GetSupportedResourceRelationConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupportedResourceRelationConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupportedResourceRelationConfig',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupportedResourceRelationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supported_resource_relation_config_with_options_async(
        self,
        request: main_models.GetSupportedResourceRelationConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupportedResourceRelationConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupportedResourceRelationConfig',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupportedResourceRelationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supported_resource_relation_config(
        self,
        request: main_models.GetSupportedResourceRelationConfigRequest,
    ) -> main_models.GetSupportedResourceRelationConfigResponse:
        runtime = RuntimeOptions()
        return self.get_supported_resource_relation_config_with_options(request, runtime)

    async def get_supported_resource_relation_config_async(
        self,
        request: main_models.GetSupportedResourceRelationConfigRequest,
    ) -> main_models.GetSupportedResourceRelationConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_supported_resource_relation_config_with_options_async(request, runtime)

    def ignore_aggregate_evaluation_results_with_options(
        self,
        tmp_req: main_models.IgnoreAggregateEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IgnoreAggregateEvaluationResultsResponse:
        tmp_req.validate()
        request = main_models.IgnoreAggregateEvaluationResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.ignore_date):
            body['IgnoreDate'] = request.ignore_date
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        if not DaraCore.is_null(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'IgnoreAggregateEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IgnoreAggregateEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ignore_aggregate_evaluation_results_with_options_async(
        self,
        tmp_req: main_models.IgnoreAggregateEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IgnoreAggregateEvaluationResultsResponse:
        tmp_req.validate()
        request = main_models.IgnoreAggregateEvaluationResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.ignore_date):
            body['IgnoreDate'] = request.ignore_date
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        if not DaraCore.is_null(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'IgnoreAggregateEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IgnoreAggregateEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ignore_aggregate_evaluation_results(
        self,
        request: main_models.IgnoreAggregateEvaluationResultsRequest,
    ) -> main_models.IgnoreAggregateEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.ignore_aggregate_evaluation_results_with_options(request, runtime)

    async def ignore_aggregate_evaluation_results_async(
        self,
        request: main_models.IgnoreAggregateEvaluationResultsRequest,
    ) -> main_models.IgnoreAggregateEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.ignore_aggregate_evaluation_results_with_options_async(request, runtime)

    def ignore_evaluation_results_with_options(
        self,
        tmp_req: main_models.IgnoreEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IgnoreEvaluationResultsResponse:
        tmp_req.validate()
        request = main_models.IgnoreEvaluationResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.ignore_date):
            body['IgnoreDate'] = request.ignore_date
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        if not DaraCore.is_null(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'IgnoreEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IgnoreEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ignore_evaluation_results_with_options_async(
        self,
        tmp_req: main_models.IgnoreEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IgnoreEvaluationResultsResponse:
        tmp_req.validate()
        request = main_models.IgnoreEvaluationResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.ignore_date):
            body['IgnoreDate'] = request.ignore_date
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        if not DaraCore.is_null(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'IgnoreEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IgnoreEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ignore_evaluation_results(
        self,
        request: main_models.IgnoreEvaluationResultsRequest,
    ) -> main_models.IgnoreEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.ignore_evaluation_results_with_options(request, runtime)

    async def ignore_evaluation_results_async(
        self,
        request: main_models.IgnoreEvaluationResultsRequest,
    ) -> main_models.IgnoreEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.ignore_evaluation_results_with_options_async(request, runtime)

    def list_aggregate_compliance_packs_with_options(
        self,
        tmp_req: main_models.ListAggregateCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateCompliancePacksResponse:
        tmp_req.validate()
        request = main_models.ListAggregateCompliancePacksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_compliance_packs_with_options_async(
        self,
        tmp_req: main_models.ListAggregateCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateCompliancePacksResponse:
        tmp_req.validate()
        request = main_models.ListAggregateCompliancePacksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_compliance_packs(
        self,
        request: main_models.ListAggregateCompliancePacksRequest,
    ) -> main_models.ListAggregateCompliancePacksResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_compliance_packs_with_options(request, runtime)

    async def list_aggregate_compliance_packs_async(
        self,
        request: main_models.ListAggregateCompliancePacksRequest,
    ) -> main_models.ListAggregateCompliancePacksResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_compliance_packs_with_options_async(request, runtime)

    def list_aggregate_config_delivery_channels_with_options(
        self,
        request: main_models.ListAggregateConfigDeliveryChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateConfigDeliveryChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.delivery_channel_ids):
            query['DeliveryChannelIds'] = request.delivery_channel_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateConfigDeliveryChannels',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateConfigDeliveryChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_delivery_channels_with_options_async(
        self,
        request: main_models.ListAggregateConfigDeliveryChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateConfigDeliveryChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.delivery_channel_ids):
            query['DeliveryChannelIds'] = request.delivery_channel_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateConfigDeliveryChannels',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateConfigDeliveryChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_delivery_channels(
        self,
        request: main_models.ListAggregateConfigDeliveryChannelsRequest,
    ) -> main_models.ListAggregateConfigDeliveryChannelsResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_config_delivery_channels_with_options(request, runtime)

    async def list_aggregate_config_delivery_channels_async(
        self,
        request: main_models.ListAggregateConfigDeliveryChannelsRequest,
    ) -> main_models.ListAggregateConfigDeliveryChannelsResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_config_delivery_channels_with_options_async(request, runtime)

    def list_aggregate_config_rule_evaluation_results_with_options(
        self,
        request: main_models.ListAggregateConfigRuleEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateConfigRuleEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateConfigRuleEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateConfigRuleEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_rule_evaluation_results_with_options_async(
        self,
        request: main_models.ListAggregateConfigRuleEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateConfigRuleEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateConfigRuleEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateConfigRuleEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_rule_evaluation_results(
        self,
        request: main_models.ListAggregateConfigRuleEvaluationResultsRequest,
    ) -> main_models.ListAggregateConfigRuleEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_config_rule_evaluation_results_with_options(request, runtime)

    async def list_aggregate_config_rule_evaluation_results_async(
        self,
        request: main_models.ListAggregateConfigRuleEvaluationResultsRequest,
    ) -> main_models.ListAggregateConfigRuleEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_config_rule_evaluation_results_with_options_async(request, runtime)

    def list_aggregate_config_rule_evaluation_statistics_with_options(
        self,
        request: main_models.ListAggregateConfigRuleEvaluationStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateConfigRuleEvaluationStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateConfigRuleEvaluationStatistics',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateConfigRuleEvaluationStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_rule_evaluation_statistics_with_options_async(
        self,
        request: main_models.ListAggregateConfigRuleEvaluationStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateConfigRuleEvaluationStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateConfigRuleEvaluationStatistics',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateConfigRuleEvaluationStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_rule_evaluation_statistics(
        self,
        request: main_models.ListAggregateConfigRuleEvaluationStatisticsRequest,
    ) -> main_models.ListAggregateConfigRuleEvaluationStatisticsResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_config_rule_evaluation_statistics_with_options(request, runtime)

    async def list_aggregate_config_rule_evaluation_statistics_async(
        self,
        request: main_models.ListAggregateConfigRuleEvaluationStatisticsRequest,
    ) -> main_models.ListAggregateConfigRuleEvaluationStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_config_rule_evaluation_statistics_with_options_async(request, runtime)

    def list_aggregate_config_rules_with_options(
        self,
        tmp_req: main_models.ListAggregateConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateConfigRulesResponse:
        tmp_req.validate()
        request = main_models.ListAggregateConfigRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_name):
            query['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_state):
            query['ConfigRuleState'] = request.config_rule_state
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_rules_with_options_async(
        self,
        tmp_req: main_models.ListAggregateConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateConfigRulesResponse:
        tmp_req.validate()
        request = main_models.ListAggregateConfigRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_name):
            query['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_state):
            query['ConfigRuleState'] = request.config_rule_state
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_rules(
        self,
        request: main_models.ListAggregateConfigRulesRequest,
    ) -> main_models.ListAggregateConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_config_rules_with_options(request, runtime)

    async def list_aggregate_config_rules_async(
        self,
        request: main_models.ListAggregateConfigRulesRequest,
    ) -> main_models.ListAggregateConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_config_rules_with_options_async(request, runtime)

    def list_aggregate_discovered_resources_with_options(
        self,
        request: main_models.ListAggregateDiscoveredResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateDiscoveredResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.end_update_timestamp):
            query['EndUpdateTimestamp'] = request.end_update_timestamp
        if not DaraCore.is_null(request.exclude_resource_types):
            query['ExcludeResourceTypes'] = request.exclude_resource_types
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.start_update_timestamp):
            query['StartUpdateTimestamp'] = request.start_update_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateDiscoveredResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateDiscoveredResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_discovered_resources_with_options_async(
        self,
        request: main_models.ListAggregateDiscoveredResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateDiscoveredResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.end_update_timestamp):
            query['EndUpdateTimestamp'] = request.end_update_timestamp
        if not DaraCore.is_null(request.exclude_resource_types):
            query['ExcludeResourceTypes'] = request.exclude_resource_types
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.start_update_timestamp):
            query['StartUpdateTimestamp'] = request.start_update_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateDiscoveredResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateDiscoveredResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_discovered_resources(
        self,
        request: main_models.ListAggregateDiscoveredResourcesRequest,
    ) -> main_models.ListAggregateDiscoveredResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_discovered_resources_with_options(request, runtime)

    async def list_aggregate_discovered_resources_async(
        self,
        request: main_models.ListAggregateDiscoveredResourcesRequest,
    ) -> main_models.ListAggregateDiscoveredResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_discovered_resources_with_options_async(request, runtime)

    def list_aggregate_recommend_managed_rules_with_options(
        self,
        request: main_models.ListAggregateRecommendManagedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateRecommendManagedRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.selected_managed_rule_identifiers):
            query['SelectedManagedRuleIdentifiers'] = request.selected_managed_rule_identifiers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateRecommendManagedRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateRecommendManagedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_recommend_managed_rules_with_options_async(
        self,
        request: main_models.ListAggregateRecommendManagedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateRecommendManagedRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.selected_managed_rule_identifiers):
            query['SelectedManagedRuleIdentifiers'] = request.selected_managed_rule_identifiers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateRecommendManagedRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateRecommendManagedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_recommend_managed_rules(
        self,
        request: main_models.ListAggregateRecommendManagedRulesRequest,
    ) -> main_models.ListAggregateRecommendManagedRulesResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_recommend_managed_rules_with_options(request, runtime)

    async def list_aggregate_recommend_managed_rules_async(
        self,
        request: main_models.ListAggregateRecommendManagedRulesRequest,
    ) -> main_models.ListAggregateRecommendManagedRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_recommend_managed_rules_with_options_async(request, runtime)

    def list_aggregate_remediation_executions_with_options(
        self,
        request: main_models.ListAggregateRemediationExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateRemediationExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateRemediationExecutions',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateRemediationExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_remediation_executions_with_options_async(
        self,
        request: main_models.ListAggregateRemediationExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateRemediationExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateRemediationExecutions',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateRemediationExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_remediation_executions(
        self,
        request: main_models.ListAggregateRemediationExecutionsRequest,
    ) -> main_models.ListAggregateRemediationExecutionsResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_remediation_executions_with_options(request, runtime)

    async def list_aggregate_remediation_executions_async(
        self,
        request: main_models.ListAggregateRemediationExecutionsRequest,
    ) -> main_models.ListAggregateRemediationExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_remediation_executions_with_options_async(request, runtime)

    def list_aggregate_remediations_with_options(
        self,
        request: main_models.ListAggregateRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateRemediationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateRemediations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_remediations_with_options_async(
        self,
        request: main_models.ListAggregateRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateRemediationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateRemediations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_remediations(
        self,
        request: main_models.ListAggregateRemediationsRequest,
    ) -> main_models.ListAggregateRemediationsResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_remediations_with_options(request, runtime)

    async def list_aggregate_remediations_async(
        self,
        request: main_models.ListAggregateRemediationsRequest,
    ) -> main_models.ListAggregateRemediationsResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_remediations_with_options_async(request, runtime)

    def list_aggregate_resource_evaluation_results_with_options(
        self,
        request: main_models.ListAggregateResourceEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateResourceEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateResourceEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateResourceEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_resource_evaluation_results_with_options_async(
        self,
        request: main_models.ListAggregateResourceEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateResourceEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateResourceEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateResourceEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_resource_evaluation_results(
        self,
        request: main_models.ListAggregateResourceEvaluationResultsRequest,
    ) -> main_models.ListAggregateResourceEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_resource_evaluation_results_with_options(request, runtime)

    async def list_aggregate_resource_evaluation_results_async(
        self,
        request: main_models.ListAggregateResourceEvaluationResultsRequest,
    ) -> main_models.ListAggregateResourceEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_resource_evaluation_results_with_options_async(request, runtime)

    def list_aggregate_resource_relations_with_options(
        self,
        request: main_models.ListAggregateResourceRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateResourceRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.target_resource_id):
            query['TargetResourceId'] = request.target_resource_id
        if not DaraCore.is_null(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateResourceRelations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateResourceRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_resource_relations_with_options_async(
        self,
        request: main_models.ListAggregateResourceRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateResourceRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.target_resource_id):
            query['TargetResourceId'] = request.target_resource_id
        if not DaraCore.is_null(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateResourceRelations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateResourceRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_resource_relations(
        self,
        request: main_models.ListAggregateResourceRelationsRequest,
    ) -> main_models.ListAggregateResourceRelationsResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_resource_relations_with_options(request, runtime)

    async def list_aggregate_resource_relations_async(
        self,
        request: main_models.ListAggregateResourceRelationsRequest,
    ) -> main_models.ListAggregateResourceRelationsResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_resource_relations_with_options_async(request, runtime)

    def list_aggregate_resources_by_advanced_search_with_options(
        self,
        request: main_models.ListAggregateResourcesByAdvancedSearchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateResourcesByAdvancedSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateResourcesByAdvancedSearch',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateResourcesByAdvancedSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_resources_by_advanced_search_with_options_async(
        self,
        request: main_models.ListAggregateResourcesByAdvancedSearchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregateResourcesByAdvancedSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregateResourcesByAdvancedSearch',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregateResourcesByAdvancedSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_resources_by_advanced_search(
        self,
        request: main_models.ListAggregateResourcesByAdvancedSearchRequest,
    ) -> main_models.ListAggregateResourcesByAdvancedSearchResponse:
        runtime = RuntimeOptions()
        return self.list_aggregate_resources_by_advanced_search_with_options(request, runtime)

    async def list_aggregate_resources_by_advanced_search_async(
        self,
        request: main_models.ListAggregateResourcesByAdvancedSearchRequest,
    ) -> main_models.ListAggregateResourcesByAdvancedSearchResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregate_resources_by_advanced_search_with_options_async(request, runtime)

    def list_aggregators_with_options(
        self,
        tmp_req: main_models.ListAggregatorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregatorsResponse:
        tmp_req.validate()
        request = main_models.ListAggregatorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregators',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregators_with_options_async(
        self,
        tmp_req: main_models.ListAggregatorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAggregatorsResponse:
        tmp_req.validate()
        request = main_models.ListAggregatorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAggregators',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAggregatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregators(
        self,
        request: main_models.ListAggregatorsRequest,
    ) -> main_models.ListAggregatorsResponse:
        runtime = RuntimeOptions()
        return self.list_aggregators_with_options(request, runtime)

    async def list_aggregators_async(
        self,
        request: main_models.ListAggregatorsRequest,
    ) -> main_models.ListAggregatorsResponse:
        runtime = RuntimeOptions()
        return await self.list_aggregators_with_options_async(request, runtime)

    def list_compliance_pack_templates_with_options(
        self,
        request: main_models.ListCompliancePackTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCompliancePackTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_template_id):
            query['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not DaraCore.is_null(request.filter_type):
            query['FilterType'] = request.filter_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.rule_risk_level):
            query['RuleRiskLevel'] = request.rule_risk_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCompliancePackTemplates',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCompliancePackTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compliance_pack_templates_with_options_async(
        self,
        request: main_models.ListCompliancePackTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCompliancePackTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_template_id):
            query['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not DaraCore.is_null(request.filter_type):
            query['FilterType'] = request.filter_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.rule_risk_level):
            query['RuleRiskLevel'] = request.rule_risk_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCompliancePackTemplates',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCompliancePackTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compliance_pack_templates(
        self,
        request: main_models.ListCompliancePackTemplatesRequest,
    ) -> main_models.ListCompliancePackTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_compliance_pack_templates_with_options(request, runtime)

    async def list_compliance_pack_templates_async(
        self,
        request: main_models.ListCompliancePackTemplatesRequest,
    ) -> main_models.ListCompliancePackTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_compliance_pack_templates_with_options_async(request, runtime)

    def list_compliance_packs_with_options(
        self,
        tmp_req: main_models.ListCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCompliancePacksResponse:
        tmp_req.validate()
        request = main_models.ListCompliancePacksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compliance_packs_with_options_async(
        self,
        tmp_req: main_models.ListCompliancePacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCompliancePacksResponse:
        tmp_req.validate()
        request = main_models.ListCompliancePacksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCompliancePacks',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compliance_packs(
        self,
        request: main_models.ListCompliancePacksRequest,
    ) -> main_models.ListCompliancePacksResponse:
        runtime = RuntimeOptions()
        return self.list_compliance_packs_with_options(request, runtime)

    async def list_compliance_packs_async(
        self,
        request: main_models.ListCompliancePacksRequest,
    ) -> main_models.ListCompliancePacksResponse:
        runtime = RuntimeOptions()
        return await self.list_compliance_packs_with_options_async(request, runtime)

    def list_config_delivery_channels_with_options(
        self,
        request: main_models.ListConfigDeliveryChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigDeliveryChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_ids):
            query['DeliveryChannelIds'] = request.delivery_channel_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigDeliveryChannels',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigDeliveryChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_delivery_channels_with_options_async(
        self,
        request: main_models.ListConfigDeliveryChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigDeliveryChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_ids):
            query['DeliveryChannelIds'] = request.delivery_channel_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigDeliveryChannels',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigDeliveryChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_delivery_channels(
        self,
        request: main_models.ListConfigDeliveryChannelsRequest,
    ) -> main_models.ListConfigDeliveryChannelsResponse:
        runtime = RuntimeOptions()
        return self.list_config_delivery_channels_with_options(request, runtime)

    async def list_config_delivery_channels_async(
        self,
        request: main_models.ListConfigDeliveryChannelsRequest,
    ) -> main_models.ListConfigDeliveryChannelsResponse:
        runtime = RuntimeOptions()
        return await self.list_config_delivery_channels_with_options_async(request, runtime)

    def list_config_rule_evaluation_results_with_options(
        self,
        request: main_models.ListConfigRuleEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRuleEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigRuleEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRuleEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rule_evaluation_results_with_options_async(
        self,
        request: main_models.ListConfigRuleEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRuleEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigRuleEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRuleEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rule_evaluation_results(
        self,
        request: main_models.ListConfigRuleEvaluationResultsRequest,
    ) -> main_models.ListConfigRuleEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.list_config_rule_evaluation_results_with_options(request, runtime)

    async def list_config_rule_evaluation_results_async(
        self,
        request: main_models.ListConfigRuleEvaluationResultsRequest,
    ) -> main_models.ListConfigRuleEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_config_rule_evaluation_results_with_options_async(request, runtime)

    def list_config_rule_evaluation_statistics_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRuleEvaluationStatisticsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListConfigRuleEvaluationStatistics',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRuleEvaluationStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rule_evaluation_statistics_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRuleEvaluationStatisticsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListConfigRuleEvaluationStatistics',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRuleEvaluationStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rule_evaluation_statistics(self) -> main_models.ListConfigRuleEvaluationStatisticsResponse:
        runtime = RuntimeOptions()
        return self.list_config_rule_evaluation_statistics_with_options(runtime)

    async def list_config_rule_evaluation_statistics_async(self) -> main_models.ListConfigRuleEvaluationStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.list_config_rule_evaluation_statistics_with_options_async(runtime)

    def list_config_rule_operators_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRuleOperatorsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListConfigRuleOperators',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRuleOperatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rule_operators_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRuleOperatorsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListConfigRuleOperators',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRuleOperatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rule_operators(self) -> main_models.ListConfigRuleOperatorsResponse:
        runtime = RuntimeOptions()
        return self.list_config_rule_operators_with_options(runtime)

    async def list_config_rule_operators_async(self) -> main_models.ListConfigRuleOperatorsResponse:
        runtime = RuntimeOptions()
        return await self.list_config_rule_operators_with_options_async(runtime)

    def list_config_rules_with_options(
        self,
        tmp_req: main_models.ListConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRulesResponse:
        tmp_req.validate()
        request = main_models.ListConfigRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_name):
            query['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_state):
            query['ConfigRuleState'] = request.config_rule_state
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rules_with_options_async(
        self,
        tmp_req: main_models.ListConfigRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRulesResponse:
        tmp_req.validate()
        request = main_models.ListConfigRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.config_rule_name):
            query['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_state):
            query['ConfigRuleState'] = request.config_rule_state
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rules(
        self,
        request: main_models.ListConfigRulesRequest,
    ) -> main_models.ListConfigRulesResponse:
        runtime = RuntimeOptions()
        return self.list_config_rules_with_options(request, runtime)

    async def list_config_rules_async(
        self,
        request: main_models.ListConfigRulesRequest,
    ) -> main_models.ListConfigRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_config_rules_with_options_async(request, runtime)

    def list_discovered_resources_with_options(
        self,
        request: main_models.ListDiscoveredResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDiscoveredResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_update_timestamp):
            query['EndUpdateTimestamp'] = request.end_update_timestamp
        if not DaraCore.is_null(request.exclude_resource_types):
            query['ExcludeResourceTypes'] = request.exclude_resource_types
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.start_update_timestamp):
            query['StartUpdateTimestamp'] = request.start_update_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiscoveredResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiscoveredResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_discovered_resources_with_options_async(
        self,
        request: main_models.ListDiscoveredResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDiscoveredResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_update_timestamp):
            query['EndUpdateTimestamp'] = request.end_update_timestamp
        if not DaraCore.is_null(request.exclude_resource_types):
            query['ExcludeResourceTypes'] = request.exclude_resource_types
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.start_update_timestamp):
            query['StartUpdateTimestamp'] = request.start_update_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiscoveredResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiscoveredResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_discovered_resources(
        self,
        request: main_models.ListDiscoveredResourcesRequest,
    ) -> main_models.ListDiscoveredResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_discovered_resources_with_options(request, runtime)

    async def list_discovered_resources_async(
        self,
        request: main_models.ListDiscoveredResourcesRequest,
    ) -> main_models.ListDiscoveredResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_discovered_resources_with_options_async(request, runtime)

    def list_integrated_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegratedServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListIntegratedService',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegratedServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integrated_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegratedServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListIntegratedService',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegratedServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integrated_service(self) -> main_models.ListIntegratedServiceResponse:
        runtime = RuntimeOptions()
        return self.list_integrated_service_with_options(runtime)

    async def list_integrated_service_async(self) -> main_models.ListIntegratedServiceResponse:
        runtime = RuntimeOptions()
        return await self.list_integrated_service_with_options_async(runtime)

    def list_managed_rules_with_options(
        self,
        request: main_models.ListManagedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListManagedRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_type):
            query['FilterType'] = request.filter_type
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListManagedRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListManagedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_managed_rules_with_options_async(
        self,
        request: main_models.ListManagedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListManagedRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_type):
            query['FilterType'] = request.filter_type
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListManagedRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListManagedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_managed_rules(
        self,
        request: main_models.ListManagedRulesRequest,
    ) -> main_models.ListManagedRulesResponse:
        runtime = RuntimeOptions()
        return self.list_managed_rules_with_options(request, runtime)

    async def list_managed_rules_async(
        self,
        request: main_models.ListManagedRulesRequest,
    ) -> main_models.ListManagedRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_managed_rules_with_options_async(request, runtime)

    def list_pre_managed_rules_with_options(
        self,
        tmp_req: main_models.ListPreManagedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPreManagedRulesResponse:
        tmp_req.validate()
        request = main_models.ListPreManagedRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_types):
            request.resource_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types, 'ResourceTypes', 'json')
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types_shrink):
            body['ResourceTypes'] = request.resource_types_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPreManagedRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPreManagedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pre_managed_rules_with_options_async(
        self,
        tmp_req: main_models.ListPreManagedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPreManagedRulesResponse:
        tmp_req.validate()
        request = main_models.ListPreManagedRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_types):
            request.resource_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types, 'ResourceTypes', 'json')
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_types_shrink):
            body['ResourceTypes'] = request.resource_types_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPreManagedRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPreManagedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pre_managed_rules(
        self,
        request: main_models.ListPreManagedRulesRequest,
    ) -> main_models.ListPreManagedRulesResponse:
        runtime = RuntimeOptions()
        return self.list_pre_managed_rules_with_options(request, runtime)

    async def list_pre_managed_rules_async(
        self,
        request: main_models.ListPreManagedRulesRequest,
    ) -> main_models.ListPreManagedRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_pre_managed_rules_with_options_async(request, runtime)

    def list_recommend_managed_rules_with_options(
        self,
        request: main_models.ListRecommendManagedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecommendManagedRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.selected_managed_rule_identifiers):
            query['SelectedManagedRuleIdentifiers'] = request.selected_managed_rule_identifiers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecommendManagedRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecommendManagedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recommend_managed_rules_with_options_async(
        self,
        request: main_models.ListRecommendManagedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecommendManagedRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.selected_managed_rule_identifiers):
            query['SelectedManagedRuleIdentifiers'] = request.selected_managed_rule_identifiers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecommendManagedRules',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecommendManagedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recommend_managed_rules(
        self,
        request: main_models.ListRecommendManagedRulesRequest,
    ) -> main_models.ListRecommendManagedRulesResponse:
        runtime = RuntimeOptions()
        return self.list_recommend_managed_rules_with_options(request, runtime)

    async def list_recommend_managed_rules_async(
        self,
        request: main_models.ListRecommendManagedRulesRequest,
    ) -> main_models.ListRecommendManagedRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_recommend_managed_rules_with_options_async(request, runtime)

    def list_remediation_executions_with_options(
        self,
        request: main_models.ListRemediationExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemediationExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRemediationExecutions',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemediationExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_remediation_executions_with_options_async(
        self,
        request: main_models.ListRemediationExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemediationExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRemediationExecutions',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemediationExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_remediation_executions(
        self,
        request: main_models.ListRemediationExecutionsRequest,
    ) -> main_models.ListRemediationExecutionsResponse:
        runtime = RuntimeOptions()
        return self.list_remediation_executions_with_options(request, runtime)

    async def list_remediation_executions_async(
        self,
        request: main_models.ListRemediationExecutionsRequest,
    ) -> main_models.ListRemediationExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_remediation_executions_with_options_async(request, runtime)

    def list_remediation_templates_with_options(
        self,
        request: main_models.ListRemediationTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemediationTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.managed_rule_identifier):
            query['ManagedRuleIdentifier'] = request.managed_rule_identifier
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remediation_type):
            query['RemediationType'] = request.remediation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRemediationTemplates',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemediationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_remediation_templates_with_options_async(
        self,
        request: main_models.ListRemediationTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemediationTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.managed_rule_identifier):
            query['ManagedRuleIdentifier'] = request.managed_rule_identifier
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remediation_type):
            query['RemediationType'] = request.remediation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRemediationTemplates',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemediationTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_remediation_templates(
        self,
        request: main_models.ListRemediationTemplatesRequest,
    ) -> main_models.ListRemediationTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_remediation_templates_with_options(request, runtime)

    async def list_remediation_templates_async(
        self,
        request: main_models.ListRemediationTemplatesRequest,
    ) -> main_models.ListRemediationTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_remediation_templates_with_options_async(request, runtime)

    def list_remediations_with_options(
        self,
        request: main_models.ListRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemediationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRemediations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_remediations_with_options_async(
        self,
        request: main_models.ListRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemediationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRemediations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_remediations(
        self,
        request: main_models.ListRemediationsRequest,
    ) -> main_models.ListRemediationsResponse:
        runtime = RuntimeOptions()
        return self.list_remediations_with_options(request, runtime)

    async def list_remediations_async(
        self,
        request: main_models.ListRemediationsRequest,
    ) -> main_models.ListRemediationsResponse:
        runtime = RuntimeOptions()
        return await self.list_remediations_with_options_async(request, runtime)

    def list_resource_evaluation_results_with_options(
        self,
        request: main_models.ListResourceEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_evaluation_results_with_options_async(
        self,
        request: main_models.ListResourceEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_evaluation_results(
        self,
        request: main_models.ListResourceEvaluationResultsRequest,
    ) -> main_models.ListResourceEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_evaluation_results_with_options(request, runtime)

    async def list_resource_evaluation_results_async(
        self,
        request: main_models.ListResourceEvaluationResultsRequest,
    ) -> main_models.ListResourceEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_evaluation_results_with_options_async(request, runtime)

    def list_resource_relations_with_options(
        self,
        request: main_models.ListResourceRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.target_resource_id):
            query['TargetResourceId'] = request.target_resource_id
        if not DaraCore.is_null(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceRelations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_relations_with_options_async(
        self,
        request: main_models.ListResourceRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.target_resource_id):
            query['TargetResourceId'] = request.target_resource_id
        if not DaraCore.is_null(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceRelations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_relations(
        self,
        request: main_models.ListResourceRelationsRequest,
    ) -> main_models.ListResourceRelationsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_relations_with_options(request, runtime)

    async def list_resource_relations_async(
        self,
        request: main_models.ListResourceRelationsRequest,
    ) -> main_models.ListResourceRelationsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_relations_with_options_async(request, runtime)

    def list_resources_by_advanced_search_with_options(
        self,
        request: main_models.ListResourcesByAdvancedSearchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesByAdvancedSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcesByAdvancedSearch',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesByAdvancedSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_by_advanced_search_with_options_async(
        self,
        request: main_models.ListResourcesByAdvancedSearchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesByAdvancedSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcesByAdvancedSearch',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesByAdvancedSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources_by_advanced_search(
        self,
        request: main_models.ListResourcesByAdvancedSearchRequest,
    ) -> main_models.ListResourcesByAdvancedSearchResponse:
        runtime = RuntimeOptions()
        return self.list_resources_by_advanced_search_with_options(request, runtime)

    async def list_resources_by_advanced_search_async(
        self,
        request: main_models.ListResourcesByAdvancedSearchRequest,
    ) -> main_models.ListResourcesByAdvancedSearchResponse:
        runtime = RuntimeOptions()
        return await self.list_resources_by_advanced_search_with_options_async(request, runtime)

    def list_supported_products_with_options(
        self,
        request: main_models.ListSupportedProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportedProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportedProducts',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_supported_products_with_options_async(
        self,
        request: main_models.ListSupportedProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportedProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportedProducts',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportedProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_supported_products(
        self,
        request: main_models.ListSupportedProductsRequest,
    ) -> main_models.ListSupportedProductsResponse:
        runtime = RuntimeOptions()
        return self.list_supported_products_with_options(request, runtime)

    async def list_supported_products_async(
        self,
        request: main_models.ListSupportedProductsRequest,
    ) -> main_models.ListSupportedProductsResponse:
        runtime = RuntimeOptions()
        return await self.list_supported_products_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def put_evaluations_with_options(
        self,
        request: main_models.PutEvaluationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEvaluationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.delete_mode):
            body['DeleteMode'] = request.delete_mode
        if not DaraCore.is_null(request.evaluations):
            body['Evaluations'] = request.evaluations
        if not DaraCore.is_null(request.result_token):
            body['ResultToken'] = request.result_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutEvaluations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEvaluationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_evaluations_with_options_async(
        self,
        request: main_models.PutEvaluationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEvaluationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.delete_mode):
            body['DeleteMode'] = request.delete_mode
        if not DaraCore.is_null(request.evaluations):
            body['Evaluations'] = request.evaluations
        if not DaraCore.is_null(request.result_token):
            body['ResultToken'] = request.result_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutEvaluations',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEvaluationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_evaluations(
        self,
        request: main_models.PutEvaluationsRequest,
    ) -> main_models.PutEvaluationsResponse:
        runtime = RuntimeOptions()
        return self.put_evaluations_with_options(request, runtime)

    async def put_evaluations_async(
        self,
        request: main_models.PutEvaluationsRequest,
    ) -> main_models.PutEvaluationsResponse:
        runtime = RuntimeOptions()
        return await self.put_evaluations_with_options_async(request, runtime)

    def revert_aggregate_evaluation_results_with_options(
        self,
        tmp_req: main_models.RevertAggregateEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertAggregateEvaluationResultsResponse:
        tmp_req.validate()
        request = main_models.RevertAggregateEvaluationResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevertAggregateEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertAggregateEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_aggregate_evaluation_results_with_options_async(
        self,
        tmp_req: main_models.RevertAggregateEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertAggregateEvaluationResultsResponse:
        tmp_req.validate()
        request = main_models.RevertAggregateEvaluationResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevertAggregateEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertAggregateEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_aggregate_evaluation_results(
        self,
        request: main_models.RevertAggregateEvaluationResultsRequest,
    ) -> main_models.RevertAggregateEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.revert_aggregate_evaluation_results_with_options(request, runtime)

    async def revert_aggregate_evaluation_results_async(
        self,
        request: main_models.RevertAggregateEvaluationResultsRequest,
    ) -> main_models.RevertAggregateEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.revert_aggregate_evaluation_results_with_options_async(request, runtime)

    def revert_evaluation_results_with_options(
        self,
        tmp_req: main_models.RevertEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertEvaluationResultsResponse:
        tmp_req.validate()
        request = main_models.RevertEvaluationResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevertEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_evaluation_results_with_options_async(
        self,
        tmp_req: main_models.RevertEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertEvaluationResultsResponse:
        tmp_req.validate()
        request = main_models.RevertEvaluationResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevertEvaluationResults',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_evaluation_results(
        self,
        request: main_models.RevertEvaluationResultsRequest,
    ) -> main_models.RevertEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.revert_evaluation_results_with_options(request, runtime)

    async def revert_evaluation_results_async(
        self,
        request: main_models.RevertEvaluationResultsRequest,
    ) -> main_models.RevertEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.revert_evaluation_results_with_options_async(request, runtime)

    def start_aggregate_config_rule_evaluation_with_options(
        self,
        request: main_models.StartAggregateConfigRuleEvaluationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAggregateConfigRuleEvaluationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.revert_evaluation):
            query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAggregateConfigRuleEvaluation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAggregateConfigRuleEvaluationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aggregate_config_rule_evaluation_with_options_async(
        self,
        request: main_models.StartAggregateConfigRuleEvaluationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAggregateConfigRuleEvaluationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.revert_evaluation):
            query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAggregateConfigRuleEvaluation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAggregateConfigRuleEvaluationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aggregate_config_rule_evaluation(
        self,
        request: main_models.StartAggregateConfigRuleEvaluationRequest,
    ) -> main_models.StartAggregateConfigRuleEvaluationResponse:
        runtime = RuntimeOptions()
        return self.start_aggregate_config_rule_evaluation_with_options(request, runtime)

    async def start_aggregate_config_rule_evaluation_async(
        self,
        request: main_models.StartAggregateConfigRuleEvaluationRequest,
    ) -> main_models.StartAggregateConfigRuleEvaluationResponse:
        runtime = RuntimeOptions()
        return await self.start_aggregate_config_rule_evaluation_with_options_async(request, runtime)

    def start_aggregate_remediation_with_options(
        self,
        request: main_models.StartAggregateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAggregateRemediationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAggregateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAggregateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aggregate_remediation_with_options_async(
        self,
        request: main_models.StartAggregateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAggregateRemediationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAggregateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAggregateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aggregate_remediation(
        self,
        request: main_models.StartAggregateRemediationRequest,
    ) -> main_models.StartAggregateRemediationResponse:
        runtime = RuntimeOptions()
        return self.start_aggregate_remediation_with_options(request, runtime)

    async def start_aggregate_remediation_async(
        self,
        request: main_models.StartAggregateRemediationRequest,
    ) -> main_models.StartAggregateRemediationResponse:
        runtime = RuntimeOptions()
        return await self.start_aggregate_remediation_with_options_async(request, runtime)

    def start_config_rule_evaluation_with_options(
        self,
        request: main_models.StartConfigRuleEvaluationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartConfigRuleEvaluationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.revert_evaluation):
            query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartConfigRuleEvaluation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartConfigRuleEvaluationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_config_rule_evaluation_with_options_async(
        self,
        request: main_models.StartConfigRuleEvaluationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartConfigRuleEvaluationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.revert_evaluation):
            query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartConfigRuleEvaluation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartConfigRuleEvaluationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_config_rule_evaluation(
        self,
        request: main_models.StartConfigRuleEvaluationRequest,
    ) -> main_models.StartConfigRuleEvaluationResponse:
        runtime = RuntimeOptions()
        return self.start_config_rule_evaluation_with_options(request, runtime)

    async def start_config_rule_evaluation_async(
        self,
        request: main_models.StartConfigRuleEvaluationRequest,
    ) -> main_models.StartConfigRuleEvaluationResponse:
        runtime = RuntimeOptions()
        return await self.start_config_rule_evaluation_with_options_async(request, runtime)

    def start_config_rule_evaluation_by_resource_with_options(
        self,
        request: main_models.StartConfigRuleEvaluationByResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartConfigRuleEvaluationByResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartConfigRuleEvaluationByResource',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartConfigRuleEvaluationByResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_config_rule_evaluation_by_resource_with_options_async(
        self,
        request: main_models.StartConfigRuleEvaluationByResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartConfigRuleEvaluationByResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartConfigRuleEvaluationByResource',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartConfigRuleEvaluationByResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_config_rule_evaluation_by_resource(
        self,
        request: main_models.StartConfigRuleEvaluationByResourceRequest,
    ) -> main_models.StartConfigRuleEvaluationByResourceResponse:
        runtime = RuntimeOptions()
        return self.start_config_rule_evaluation_by_resource_with_options(request, runtime)

    async def start_config_rule_evaluation_by_resource_async(
        self,
        request: main_models.StartConfigRuleEvaluationByResourceRequest,
    ) -> main_models.StartConfigRuleEvaluationByResourceResponse:
        runtime = RuntimeOptions()
        return await self.start_config_rule_evaluation_by_resource_with_options_async(request, runtime)

    def start_configuration_recorder_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.StartConfigurationRecorderResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'StartConfigurationRecorder',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_configuration_recorder_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.StartConfigurationRecorderResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'StartConfigurationRecorder',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_configuration_recorder(self) -> main_models.StartConfigurationRecorderResponse:
        runtime = RuntimeOptions()
        return self.start_configuration_recorder_with_options(runtime)

    async def start_configuration_recorder_async(self) -> main_models.StartConfigurationRecorderResponse:
        runtime = RuntimeOptions()
        return await self.start_configuration_recorder_with_options_async(runtime)

    def start_remediation_with_options(
        self,
        request: main_models.StartRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRemediationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_remediation_with_options_async(
        self,
        request: main_models.StartRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRemediationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_remediation(
        self,
        request: main_models.StartRemediationRequest,
    ) -> main_models.StartRemediationResponse:
        runtime = RuntimeOptions()
        return self.start_remediation_with_options(request, runtime)

    async def start_remediation_async(
        self,
        request: main_models.StartRemediationRequest,
    ) -> main_models.StartRemediationResponse:
        runtime = RuntimeOptions()
        return await self.start_remediation_with_options_async(request, runtime)

    def stop_configuration_recorder_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.StopConfigurationRecorderResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'StopConfigurationRecorder',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_configuration_recorder_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.StopConfigurationRecorderResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'StopConfigurationRecorder',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_configuration_recorder(self) -> main_models.StopConfigurationRecorderResponse:
        runtime = RuntimeOptions()
        return self.stop_configuration_recorder_with_options(runtime)

    async def stop_configuration_recorder_async(self) -> main_models.StopConfigurationRecorderResponse:
        runtime = RuntimeOptions()
        return await self.stop_configuration_recorder_with_options_async(runtime)

    def tag_resources_with_options(
        self,
        tmp_req: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        tmp_req.validate()
        request = main_models.TagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        tmp_req: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        tmp_req.validate()
        request = main_models.TagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def trigger_report_send_with_options(
        self,
        request: main_models.TriggerReportSendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerReportSendResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.report_template_id):
            body['ReportTemplateId'] = request.report_template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerReportSend',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerReportSendResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_report_send_with_options_async(
        self,
        request: main_models.TriggerReportSendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerReportSendResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.report_template_id):
            body['ReportTemplateId'] = request.report_template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerReportSend',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerReportSendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_report_send(
        self,
        request: main_models.TriggerReportSendRequest,
    ) -> main_models.TriggerReportSendResponse:
        runtime = RuntimeOptions()
        return self.trigger_report_send_with_options(request, runtime)

    async def trigger_report_send_async(
        self,
        request: main_models.TriggerReportSendRequest,
    ) -> main_models.TriggerReportSendResponse:
        runtime = RuntimeOptions()
        return await self.trigger_report_send_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_aggregate_compliance_pack_with_options(
        self,
        tmp_req: main_models.UpdateAggregateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.UpdateAggregateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_rules):
            request.config_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not DaraCore.is_null(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregate_compliance_pack_with_options_async(
        self,
        tmp_req: main_models.UpdateAggregateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.UpdateAggregateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_rules):
            request.config_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not DaraCore.is_null(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregate_compliance_pack(
        self,
        request: main_models.UpdateAggregateCompliancePackRequest,
    ) -> main_models.UpdateAggregateCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.update_aggregate_compliance_pack_with_options(request, runtime)

    async def update_aggregate_compliance_pack_async(
        self,
        request: main_models.UpdateAggregateCompliancePackRequest,
    ) -> main_models.UpdateAggregateCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.update_aggregate_compliance_pack_with_options_async(request, runtime)

    def update_aggregate_config_delivery_channel_with_options(
        self,
        request: main_models.UpdateAggregateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not DaraCore.is_null(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not DaraCore.is_null(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not DaraCore.is_null(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not DaraCore.is_null(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not DaraCore.is_null(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregate_config_delivery_channel_with_options_async(
        self,
        request: main_models.UpdateAggregateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not DaraCore.is_null(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not DaraCore.is_null(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not DaraCore.is_null(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not DaraCore.is_null(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not DaraCore.is_null(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregate_config_delivery_channel(
        self,
        request: main_models.UpdateAggregateConfigDeliveryChannelRequest,
    ) -> main_models.UpdateAggregateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.update_aggregate_config_delivery_channel_with_options(request, runtime)

    async def update_aggregate_config_delivery_channel_async(
        self,
        request: main_models.UpdateAggregateConfigDeliveryChannelRequest,
    ) -> main_models.UpdateAggregateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.update_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def update_aggregate_config_rule_with_options(
        self,
        tmp_req: main_models.UpdateAggregateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateAggregateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input_parameters):
            request.input_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not DaraCore.is_null(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.account_ids_scope):
            body['AccountIdsScope'] = request.account_ids_scope
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not DaraCore.is_null(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.folder_ids_scope):
            body['FolderIdsScope'] = request.folder_ids_scope
        if not DaraCore.is_null(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not DaraCore.is_null(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_name_scope):
            body['ResourceNameScope'] = request.resource_name_scope
        if not DaraCore.is_null(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregate_config_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateAggregateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateAggregateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input_parameters):
            request.input_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not DaraCore.is_null(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.account_ids_scope):
            body['AccountIdsScope'] = request.account_ids_scope
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not DaraCore.is_null(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.folder_ids_scope):
            body['FolderIdsScope'] = request.folder_ids_scope
        if not DaraCore.is_null(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not DaraCore.is_null(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_name_scope):
            body['ResourceNameScope'] = request.resource_name_scope
        if not DaraCore.is_null(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregate_config_rule(
        self,
        request: main_models.UpdateAggregateConfigRuleRequest,
    ) -> main_models.UpdateAggregateConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.update_aggregate_config_rule_with_options(request, runtime)

    async def update_aggregate_config_rule_async(
        self,
        request: main_models.UpdateAggregateConfigRuleRequest,
    ) -> main_models.UpdateAggregateConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_aggregate_config_rule_with_options_async(request, runtime)

    def update_aggregate_remediation_with_options(
        self,
        request: main_models.UpdateAggregateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregateRemediationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.remediation_id):
            body['RemediationId'] = request.remediation_id
        if not DaraCore.is_null(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not DaraCore.is_null(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregate_remediation_with_options_async(
        self,
        request: main_models.UpdateAggregateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregateRemediationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.remediation_id):
            body['RemediationId'] = request.remediation_id
        if not DaraCore.is_null(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not DaraCore.is_null(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregate_remediation(
        self,
        request: main_models.UpdateAggregateRemediationRequest,
    ) -> main_models.UpdateAggregateRemediationResponse:
        runtime = RuntimeOptions()
        return self.update_aggregate_remediation_with_options(request, runtime)

    async def update_aggregate_remediation_async(
        self,
        request: main_models.UpdateAggregateRemediationRequest,
    ) -> main_models.UpdateAggregateRemediationResponse:
        runtime = RuntimeOptions()
        return await self.update_aggregate_remediation_with_options_async(request, runtime)

    def update_aggregator_with_options(
        self,
        tmp_req: main_models.UpdateAggregatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregatorResponse:
        tmp_req.validate()
        request = main_models.UpdateAggregatorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aggregator_accounts):
            request.aggregator_accounts_shrink = Utils.array_to_string_with_specified_style(tmp_req.aggregator_accounts, 'AggregatorAccounts', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.aggregator_accounts_shrink):
            body['AggregatorAccounts'] = request.aggregator_accounts_shrink
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.aggregator_name):
            body['AggregatorName'] = request.aggregator_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregator',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregator_with_options_async(
        self,
        tmp_req: main_models.UpdateAggregatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAggregatorResponse:
        tmp_req.validate()
        request = main_models.UpdateAggregatorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aggregator_accounts):
            request.aggregator_accounts_shrink = Utils.array_to_string_with_specified_style(tmp_req.aggregator_accounts, 'AggregatorAccounts', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.aggregator_accounts_shrink):
            body['AggregatorAccounts'] = request.aggregator_accounts_shrink
        if not DaraCore.is_null(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not DaraCore.is_null(request.aggregator_name):
            body['AggregatorName'] = request.aggregator_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAggregator',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAggregatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregator(
        self,
        request: main_models.UpdateAggregatorRequest,
    ) -> main_models.UpdateAggregatorResponse:
        runtime = RuntimeOptions()
        return self.update_aggregator_with_options(request, runtime)

    async def update_aggregator_async(
        self,
        request: main_models.UpdateAggregatorRequest,
    ) -> main_models.UpdateAggregatorResponse:
        runtime = RuntimeOptions()
        return await self.update_aggregator_with_options_async(request, runtime)

    def update_compliance_pack_with_options(
        self,
        tmp_req: main_models.UpdateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.UpdateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_rules):
            request.config_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not DaraCore.is_null(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compliance_pack_with_options_async(
        self,
        tmp_req: main_models.UpdateCompliancePackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCompliancePackResponse:
        tmp_req.validate()
        request = main_models.UpdateCompliancePackShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config_rules):
            request.config_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not DaraCore.is_null(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not DaraCore.is_null(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCompliancePack',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compliance_pack(
        self,
        request: main_models.UpdateCompliancePackRequest,
    ) -> main_models.UpdateCompliancePackResponse:
        runtime = RuntimeOptions()
        return self.update_compliance_pack_with_options(request, runtime)

    async def update_compliance_pack_async(
        self,
        request: main_models.UpdateCompliancePackRequest,
    ) -> main_models.UpdateCompliancePackResponse:
        runtime = RuntimeOptions()
        return await self.update_compliance_pack_with_options_async(request, runtime)

    def update_config_delivery_channel_with_options(
        self,
        request: main_models.UpdateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not DaraCore.is_null(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not DaraCore.is_null(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not DaraCore.is_null(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not DaraCore.is_null(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not DaraCore.is_null(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_delivery_channel_with_options_async(
        self,
        request: main_models.UpdateConfigDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not DaraCore.is_null(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not DaraCore.is_null(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not DaraCore.is_null(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not DaraCore.is_null(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not DaraCore.is_null(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigDeliveryChannel',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_delivery_channel(
        self,
        request: main_models.UpdateConfigDeliveryChannelRequest,
    ) -> main_models.UpdateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.update_config_delivery_channel_with_options(request, runtime)

    async def update_config_delivery_channel_async(
        self,
        request: main_models.UpdateConfigDeliveryChannelRequest,
    ) -> main_models.UpdateConfigDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.update_config_delivery_channel_with_options_async(request, runtime)

    def update_config_rule_with_options(
        self,
        tmp_req: main_models.UpdateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input_parameters):
            request.input_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not DaraCore.is_null(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.extend_content):
            body['ExtendContent'] = request.extend_content
        if not DaraCore.is_null(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not DaraCore.is_null(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_name_scope):
            body['ResourceNameScope'] = request.resource_name_scope
        if not DaraCore.is_null(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateConfigRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateConfigRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input_parameters):
            request.input_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not DaraCore.is_null(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not DaraCore.is_null(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not DaraCore.is_null(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not DaraCore.is_null(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not DaraCore.is_null(request.extend_content):
            body['ExtendContent'] = request.extend_content
        if not DaraCore.is_null(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not DaraCore.is_null(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not DaraCore.is_null(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_name_scope):
            body['ResourceNameScope'] = request.resource_name_scope
        if not DaraCore.is_null(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not DaraCore.is_null(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not DaraCore.is_null(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not DaraCore.is_null(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigRule',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_rule(
        self,
        request: main_models.UpdateConfigRuleRequest,
    ) -> main_models.UpdateConfigRuleResponse:
        runtime = RuntimeOptions()
        return self.update_config_rule_with_options(request, runtime)

    async def update_config_rule_async(
        self,
        request: main_models.UpdateConfigRuleRequest,
    ) -> main_models.UpdateConfigRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_config_rule_with_options_async(request, runtime)

    def update_configuration_recorder_with_options(
        self,
        request: main_models.UpdateConfigurationRecorderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigurationRecorderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_types):
            body['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigurationRecorder',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_configuration_recorder_with_options_async(
        self,
        request: main_models.UpdateConfigurationRecorderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigurationRecorderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_types):
            body['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigurationRecorder',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_configuration_recorder(
        self,
        request: main_models.UpdateConfigurationRecorderRequest,
    ) -> main_models.UpdateConfigurationRecorderResponse:
        runtime = RuntimeOptions()
        return self.update_configuration_recorder_with_options(request, runtime)

    async def update_configuration_recorder_async(
        self,
        request: main_models.UpdateConfigurationRecorderRequest,
    ) -> main_models.UpdateConfigurationRecorderResponse:
        runtime = RuntimeOptions()
        return await self.update_configuration_recorder_with_options_async(request, runtime)

    def update_integrated_service_status_with_options(
        self,
        request: main_models.UpdateIntegratedServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIntegratedServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_delivery_data_type):
            body['AggregatorDeliveryDataType'] = request.aggregator_delivery_data_type
        if not DaraCore.is_null(request.integrated_types):
            body['IntegratedTypes'] = request.integrated_types
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIntegratedServiceStatus',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIntegratedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_integrated_service_status_with_options_async(
        self,
        request: main_models.UpdateIntegratedServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIntegratedServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aggregator_delivery_data_type):
            body['AggregatorDeliveryDataType'] = request.aggregator_delivery_data_type
        if not DaraCore.is_null(request.integrated_types):
            body['IntegratedTypes'] = request.integrated_types
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIntegratedServiceStatus',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIntegratedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_integrated_service_status(
        self,
        request: main_models.UpdateIntegratedServiceStatusRequest,
    ) -> main_models.UpdateIntegratedServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.update_integrated_service_status_with_options(request, runtime)

    async def update_integrated_service_status_async(
        self,
        request: main_models.UpdateIntegratedServiceStatusRequest,
    ) -> main_models.UpdateIntegratedServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_integrated_service_status_with_options_async(request, runtime)

    def update_remediation_with_options(
        self,
        request: main_models.UpdateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRemediationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.remediation_id):
            body['RemediationId'] = request.remediation_id
        if not DaraCore.is_null(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not DaraCore.is_null(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_remediation_with_options_async(
        self,
        request: main_models.UpdateRemediationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRemediationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.remediation_id):
            body['RemediationId'] = request.remediation_id
        if not DaraCore.is_null(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not DaraCore.is_null(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRemediation',
            version = '2020-09-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_remediation(
        self,
        request: main_models.UpdateRemediationRequest,
    ) -> main_models.UpdateRemediationResponse:
        runtime = RuntimeOptions()
        return self.update_remediation_with_options(request, runtime)

    async def update_remediation_async(
        self,
        request: main_models.UpdateRemediationRequest,
    ) -> main_models.UpdateRemediationResponse:
        runtime = RuntimeOptions()
        return await self.update_remediation_with_options_async(request, runtime)
