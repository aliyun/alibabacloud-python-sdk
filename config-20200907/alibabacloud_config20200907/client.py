# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_config20200907 import models as config_20200907_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def active_aggregate_config_rules_with_options(
        self,
        request: config_20200907_models.ActiveAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ActiveAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveAggregateConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ActiveAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.ActiveAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ActiveAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveAggregateConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ActiveAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_aggregate_config_rules(
        self,
        request: config_20200907_models.ActiveAggregateConfigRulesRequest,
    ) -> config_20200907_models.ActiveAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.active_aggregate_config_rules_with_options(request, runtime)

    async def active_aggregate_config_rules_async(
        self,
        request: config_20200907_models.ActiveAggregateConfigRulesRequest,
    ) -> config_20200907_models.ActiveAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.active_aggregate_config_rules_with_options_async(request, runtime)

    def attach_aggregate_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.AttachAggregateConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.AttachAggregateConfigRuleToCompliancePackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAggregateConfigRuleToCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.AttachAggregateConfigRuleToCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_aggregate_config_rule_to_compliance_pack_with_options_async(
        self,
        request: config_20200907_models.AttachAggregateConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.AttachAggregateConfigRuleToCompliancePackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAggregateConfigRuleToCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.AttachAggregateConfigRuleToCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_aggregate_config_rule_to_compliance_pack(
        self,
        request: config_20200907_models.AttachAggregateConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.AttachAggregateConfigRuleToCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_aggregate_config_rule_to_compliance_pack_with_options(request, runtime)

    async def attach_aggregate_config_rule_to_compliance_pack_async(
        self,
        request: config_20200907_models.AttachAggregateConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.AttachAggregateConfigRuleToCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_aggregate_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def attach_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.AttachConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.AttachConfigRuleToCompliancePackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachConfigRuleToCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.AttachConfigRuleToCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_config_rule_to_compliance_pack_with_options_async(
        self,
        request: config_20200907_models.AttachConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.AttachConfigRuleToCompliancePackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachConfigRuleToCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.AttachConfigRuleToCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_config_rule_to_compliance_pack(
        self,
        request: config_20200907_models.AttachConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.AttachConfigRuleToCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_config_rule_to_compliance_pack_with_options(request, runtime)

    async def attach_config_rule_to_compliance_pack_async(
        self,
        request: config_20200907_models.AttachConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.AttachConfigRuleToCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def create_aggregate_compliance_pack_with_options(
        self,
        tmp_req: config_20200907_models.CreateAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateCompliancePackResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateAggregateCompliancePackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_rules):
            request.config_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not UtilClient.is_unset(request.compliance_pack_template_id):
            body['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not UtilClient.is_unset(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggregateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_compliance_pack_with_options_async(
        self,
        tmp_req: config_20200907_models.CreateAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateCompliancePackResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateAggregateCompliancePackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_rules):
            request.config_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not UtilClient.is_unset(request.compliance_pack_template_id):
            body['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not UtilClient.is_unset(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggregateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_compliance_pack(
        self,
        request: config_20200907_models.CreateAggregateCompliancePackRequest,
    ) -> config_20200907_models.CreateAggregateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_compliance_pack_with_options(request, runtime)

    async def create_aggregate_compliance_pack_async(
        self,
        request: config_20200907_models.CreateAggregateCompliancePackRequest,
    ) -> config_20200907_models.CreateAggregateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_compliance_pack_with_options_async(request, runtime)

    def create_aggregate_config_rule_with_options(
        self,
        tmp_req: config_20200907_models.CreateAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateConfigRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateAggregateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not UtilClient.is_unset(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggregateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_config_rule_with_options_async(
        self,
        tmp_req: config_20200907_models.CreateAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateConfigRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateAggregateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not UtilClient.is_unset(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggregateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_config_rule(
        self,
        request: config_20200907_models.CreateAggregateConfigRuleRequest,
    ) -> config_20200907_models.CreateAggregateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_config_rule_with_options(request, runtime)

    async def create_aggregate_config_rule_async(
        self,
        request: config_20200907_models.CreateAggregateConfigRuleRequest,
    ) -> config_20200907_models.CreateAggregateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_config_rule_with_options_async(request, runtime)

    def create_aggregator_with_options(
        self,
        tmp_req: config_20200907_models.CreateAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregatorResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateAggregatorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregator_accounts):
            request.aggregator_accounts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregator_accounts, 'AggregatorAccounts', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_accounts_shrink):
            body['AggregatorAccounts'] = request.aggregator_accounts_shrink
        if not UtilClient.is_unset(request.aggregator_name):
            body['AggregatorName'] = request.aggregator_name
        if not UtilClient.is_unset(request.aggregator_type):
            body['AggregatorType'] = request.aggregator_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggregator',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregator_with_options_async(
        self,
        tmp_req: config_20200907_models.CreateAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregatorResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateAggregatorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregator_accounts):
            request.aggregator_accounts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregator_accounts, 'AggregatorAccounts', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_accounts_shrink):
            body['AggregatorAccounts'] = request.aggregator_accounts_shrink
        if not UtilClient.is_unset(request.aggregator_name):
            body['AggregatorName'] = request.aggregator_name
        if not UtilClient.is_unset(request.aggregator_type):
            body['AggregatorType'] = request.aggregator_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggregator',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregator(
        self,
        request: config_20200907_models.CreateAggregatorRequest,
    ) -> config_20200907_models.CreateAggregatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_aggregator_with_options(request, runtime)

    async def create_aggregator_async(
        self,
        request: config_20200907_models.CreateAggregatorRequest,
    ) -> config_20200907_models.CreateAggregatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregator_with_options_async(request, runtime)

    def create_compliance_pack_with_options(
        self,
        tmp_req: config_20200907_models.CreateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateCompliancePackResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateCompliancePackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_rules):
            request.config_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not UtilClient.is_unset(request.compliance_pack_template_id):
            body['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not UtilClient.is_unset(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compliance_pack_with_options_async(
        self,
        tmp_req: config_20200907_models.CreateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateCompliancePackResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateCompliancePackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_rules):
            request.config_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not UtilClient.is_unset(request.compliance_pack_template_id):
            body['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not UtilClient.is_unset(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compliance_pack(
        self,
        request: config_20200907_models.CreateCompliancePackRequest,
    ) -> config_20200907_models.CreateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_compliance_pack_with_options(request, runtime)

    async def create_compliance_pack_async(
        self,
        request: config_20200907_models.CreateCompliancePackRequest,
    ) -> config_20200907_models.CreateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_compliance_pack_with_options_async(request, runtime)

    def create_config_rule_with_options(
        self,
        tmp_req: config_20200907_models.CreateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateConfigRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not UtilClient.is_unset(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_rule_with_options_async(
        self,
        tmp_req: config_20200907_models.CreateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateConfigRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not UtilClient.is_unset(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.CreateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_rule(
        self,
        request: config_20200907_models.CreateConfigRuleRequest,
    ) -> config_20200907_models.CreateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_config_rule_with_options(request, runtime)

    async def create_config_rule_async(
        self,
        request: config_20200907_models.CreateConfigRuleRequest,
    ) -> config_20200907_models.CreateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_config_rule_with_options_async(request, runtime)

    def deactive_aggregate_config_rules_with_options(
        self,
        request: config_20200907_models.DeactiveAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveAggregateConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeactiveAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactive_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.DeactiveAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveAggregateConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeactiveAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactive_aggregate_config_rules(
        self,
        request: config_20200907_models.DeactiveAggregateConfigRulesRequest,
    ) -> config_20200907_models.DeactiveAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactive_aggregate_config_rules_with_options(request, runtime)

    async def deactive_aggregate_config_rules_async(
        self,
        request: config_20200907_models.DeactiveAggregateConfigRulesRequest,
    ) -> config_20200907_models.DeactiveAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactive_aggregate_config_rules_with_options_async(request, runtime)

    def deactive_config_rules_with_options(
        self,
        request: config_20200907_models.DeactiveConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeactiveConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactive_config_rules_with_options_async(
        self,
        request: config_20200907_models.DeactiveConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeactiveConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactive_config_rules(
        self,
        request: config_20200907_models.DeactiveConfigRulesRequest,
    ) -> config_20200907_models.DeactiveConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactive_config_rules_with_options(request, runtime)

    async def deactive_config_rules_async(
        self,
        request: config_20200907_models.DeactiveConfigRulesRequest,
    ) -> config_20200907_models.DeactiveConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactive_config_rules_with_options_async(request, runtime)

    def delete_aggregate_compliance_packs_with_options(
        self,
        request: config_20200907_models.DeleteAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateCompliancePacksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_ids):
            body['CompliancePackIds'] = request.compliance_pack_ids
        if not UtilClient.is_unset(request.delete_rule):
            body['DeleteRule'] = request.delete_rule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAggregateCompliancePacks',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregate_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateCompliancePacksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_ids):
            body['CompliancePackIds'] = request.compliance_pack_ids
        if not UtilClient.is_unset(request.delete_rule):
            body['DeleteRule'] = request.delete_rule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAggregateCompliancePacks',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregate_compliance_packs(
        self,
        request: config_20200907_models.DeleteAggregateCompliancePacksRequest,
    ) -> config_20200907_models.DeleteAggregateCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregate_compliance_packs_with_options(request, runtime)

    async def delete_aggregate_compliance_packs_async(
        self,
        request: config_20200907_models.DeleteAggregateCompliancePacksRequest,
    ) -> config_20200907_models.DeleteAggregateCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregate_compliance_packs_with_options_async(request, runtime)

    def delete_aggregate_config_rules_with_options(
        self,
        request: config_20200907_models.DeleteAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAggregateConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAggregateConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregate_config_rules(
        self,
        request: config_20200907_models.DeleteAggregateConfigRulesRequest,
    ) -> config_20200907_models.DeleteAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregate_config_rules_with_options(request, runtime)

    async def delete_aggregate_config_rules_async(
        self,
        request: config_20200907_models.DeleteAggregateConfigRulesRequest,
    ) -> config_20200907_models.DeleteAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregate_config_rules_with_options_async(request, runtime)

    def delete_aggregators_with_options(
        self,
        request: config_20200907_models.DeleteAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregatorsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_ids):
            body['AggregatorIds'] = request.aggregator_ids
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAggregators',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregators_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregatorsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_ids):
            body['AggregatorIds'] = request.aggregator_ids
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAggregators',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregators(
        self,
        request: config_20200907_models.DeleteAggregatorsRequest,
    ) -> config_20200907_models.DeleteAggregatorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregators_with_options(request, runtime)

    async def delete_aggregators_async(
        self,
        request: config_20200907_models.DeleteAggregatorsRequest,
    ) -> config_20200907_models.DeleteAggregatorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregators_with_options_async(request, runtime)

    def delete_compliance_packs_with_options(
        self,
        request: config_20200907_models.DeleteCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteCompliancePacksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_ids):
            body['CompliancePackIds'] = request.compliance_pack_ids
        if not UtilClient.is_unset(request.delete_rule):
            body['DeleteRule'] = request.delete_rule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCompliancePacks',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.DeleteCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteCompliancePacksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_ids):
            body['CompliancePackIds'] = request.compliance_pack_ids
        if not UtilClient.is_unset(request.delete_rule):
            body['DeleteRule'] = request.delete_rule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCompliancePacks',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_compliance_packs(
        self,
        request: config_20200907_models.DeleteCompliancePacksRequest,
    ) -> config_20200907_models.DeleteCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_compliance_packs_with_options(request, runtime)

    async def delete_compliance_packs_async(
        self,
        request: config_20200907_models.DeleteCompliancePacksRequest,
    ) -> config_20200907_models.DeleteCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_compliance_packs_with_options_async(request, runtime)

    def detach_aggregate_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.DetachAggregateConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachAggregateConfigRuleToCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_aggregate_config_rule_to_compliance_pack_with_options_async(
        self,
        request: config_20200907_models.DetachAggregateConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachAggregateConfigRuleToCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_aggregate_config_rule_to_compliance_pack(
        self,
        request: config_20200907_models.DetachAggregateConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_aggregate_config_rule_to_compliance_pack_with_options(request, runtime)

    async def detach_aggregate_config_rule_to_compliance_pack_async(
        self,
        request: config_20200907_models.DetachAggregateConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_aggregate_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def detach_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.DetachConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DetachConfigRuleToCompliancePackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachConfigRuleToCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DetachConfigRuleToCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_config_rule_to_compliance_pack_with_options_async(
        self,
        request: config_20200907_models.DetachConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DetachConfigRuleToCompliancePackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachConfigRuleToCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.DetachConfigRuleToCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_config_rule_to_compliance_pack(
        self,
        request: config_20200907_models.DetachConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.DetachConfigRuleToCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_config_rule_to_compliance_pack_with_options(request, runtime)

    async def detach_config_rule_to_compliance_pack_async(
        self,
        request: config_20200907_models.DetachConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.DetachConfigRuleToCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def generate_aggregate_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GenerateAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateAggregateCompliancePackReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateCompliancePackReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_aggregate_compliance_pack_report_with_options_async(
        self,
        request: config_20200907_models.GenerateAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateAggregateCompliancePackReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateCompliancePackReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_aggregate_compliance_pack_report(
        self,
        request: config_20200907_models.GenerateAggregateCompliancePackReportRequest,
    ) -> config_20200907_models.GenerateAggregateCompliancePackReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_aggregate_compliance_pack_report_with_options(request, runtime)

    async def generate_aggregate_compliance_pack_report_async(
        self,
        request: config_20200907_models.GenerateAggregateCompliancePackReportRequest,
    ) -> config_20200907_models.GenerateAggregateCompliancePackReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_aggregate_compliance_pack_report_with_options_async(request, runtime)

    def generate_aggregate_config_rules_report_with_options(
        self,
        request: config_20200907_models.GenerateAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateAggregateConfigRulesReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_aggregate_config_rules_report_with_options_async(
        self,
        request: config_20200907_models.GenerateAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateAggregateConfigRulesReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_aggregate_config_rules_report(
        self,
        request: config_20200907_models.GenerateAggregateConfigRulesReportRequest,
    ) -> config_20200907_models.GenerateAggregateConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_aggregate_config_rules_report_with_options(request, runtime)

    async def generate_aggregate_config_rules_report_async(
        self,
        request: config_20200907_models.GenerateAggregateConfigRulesReportRequest,
    ) -> config_20200907_models.GenerateAggregateConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_aggregate_config_rules_report_with_options_async(request, runtime)

    def generate_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GenerateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCompliancePackReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateCompliancePackReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_compliance_pack_report_with_options_async(
        self,
        request: config_20200907_models.GenerateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCompliancePackReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateCompliancePackReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_compliance_pack_report(
        self,
        request: config_20200907_models.GenerateCompliancePackReportRequest,
    ) -> config_20200907_models.GenerateCompliancePackReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_compliance_pack_report_with_options(request, runtime)

    async def generate_compliance_pack_report_async(
        self,
        request: config_20200907_models.GenerateCompliancePackReportRequest,
    ) -> config_20200907_models.GenerateCompliancePackReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_compliance_pack_report_with_options_async(request, runtime)

    def generate_config_rules_report_with_options(
        self,
        request: config_20200907_models.GenerateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateConfigRulesReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_config_rules_report_with_options_async(
        self,
        request: config_20200907_models.GenerateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateConfigRulesReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_config_rules_report(
        self,
        request: config_20200907_models.GenerateConfigRulesReportRequest,
    ) -> config_20200907_models.GenerateConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_config_rules_report_with_options(request, runtime)

    async def generate_config_rules_report_async(
        self,
        request: config_20200907_models.GenerateConfigRulesReportRequest,
    ) -> config_20200907_models.GenerateConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_config_rules_report_with_options_async(request, runtime)

    def get_aggregate_account_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateAccountComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateAccountComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateAccountComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateAccountComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_account_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetAggregateAccountComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateAccountComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateAccountComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateAccountComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_account_compliance_by_pack(
        self,
        request: config_20200907_models.GetAggregateAccountComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateAccountComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_account_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_account_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetAggregateAccountComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateAccountComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_account_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_compliance_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateCompliancePackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_compliance_pack_with_options_async(
        self,
        request: config_20200907_models.GetAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateCompliancePackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_compliance_pack(
        self,
        request: config_20200907_models.GetAggregateCompliancePackRequest,
    ) -> config_20200907_models.GetAggregateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_compliance_pack_with_options(request, runtime)

    async def get_aggregate_compliance_pack_async(
        self,
        request: config_20200907_models.GetAggregateCompliancePackRequest,
    ) -> config_20200907_models.GetAggregateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_compliance_pack_with_options_async(request, runtime)

    def get_aggregate_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GetAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateCompliancePackReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateCompliancePackReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_compliance_pack_report_with_options_async(
        self,
        request: config_20200907_models.GetAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateCompliancePackReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateCompliancePackReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_compliance_pack_report(
        self,
        request: config_20200907_models.GetAggregateCompliancePackReportRequest,
    ) -> config_20200907_models.GetAggregateCompliancePackReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_compliance_pack_report_with_options(request, runtime)

    async def get_aggregate_compliance_pack_report_async(
        self,
        request: config_20200907_models.GetAggregateCompliancePackReportRequest,
    ) -> config_20200907_models.GetAggregateCompliancePackReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_compliance_pack_report_with_options_async(request, runtime)

    def get_aggregate_config_rule_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['ConfigRuleId'] = request.config_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['ConfigRuleId'] = request.config_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rule(
        self,
        request: config_20200907_models.GetAggregateConfigRuleRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rule_with_options(request, runtime)

    async def get_aggregate_config_rule_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rule_with_options_async(request, runtime)

    def get_aggregate_config_rule_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRuleComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRuleComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rule_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRuleComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rule_compliance_by_pack(
        self,
        request: config_20200907_models.GetAggregateConfigRuleComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rule_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_config_rule_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rule_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_config_rule_summary_by_risk_level_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRuleSummaryByRiskLevel',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rule_summary_by_risk_level_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRuleSummaryByRiskLevel',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rule_summary_by_risk_level(
        self,
        request: config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rule_summary_by_risk_level_with_options(request, runtime)

    async def get_aggregate_config_rule_summary_by_risk_level_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rule_summary_by_risk_level_with_options_async(request, runtime)

    def get_aggregate_config_rules_report_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRulesReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rules_report_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRulesReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rules_report(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rules_report_with_options(request, runtime)

    async def get_aggregate_config_rules_report_async(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rules_report_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_by_config_rule_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceByConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_by_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceByConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_by_config_rule(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_by_config_rule_with_options(request, runtime)

    async def get_aggregate_resource_compliance_by_config_rule_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_by_config_rule_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_by_pack(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_resource_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_timeline_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceTimeline',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_timeline_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceTimeline',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_timeline(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceTimelineRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_timeline_with_options(request, runtime)

    async def get_aggregate_resource_compliance_timeline_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceTimelineRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_timeline_with_options_async(request, runtime)

    def get_aggregate_resource_configuration_timeline_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceConfigurationTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceConfigurationTimeline',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceConfigurationTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_configuration_timeline_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceConfigurationTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceConfigurationTimeline',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceConfigurationTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_configuration_timeline(
        self,
        request: config_20200907_models.GetAggregateResourceConfigurationTimelineRequest,
    ) -> config_20200907_models.GetAggregateResourceConfigurationTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_configuration_timeline_with_options(request, runtime)

    async def get_aggregate_resource_configuration_timeline_async(
        self,
        request: config_20200907_models.GetAggregateResourceConfigurationTimelineRequest,
    ) -> config_20200907_models.GetAggregateResourceConfigurationTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_configuration_timeline_with_options_async(request, runtime)

    def get_aggregate_resource_counts_group_by_region_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceCountsGroupByRegion',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_counts_group_by_region_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceCountsGroupByRegion',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_counts_group_by_region(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_counts_group_by_region_with_options(request, runtime)

    async def get_aggregate_resource_counts_group_by_region_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_counts_group_by_region_with_options_async(request, runtime)

    def get_aggregate_resource_counts_group_by_resource_type_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceCountsGroupByResourceType',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_counts_group_by_resource_type_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceCountsGroupByResourceType',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_counts_group_by_resource_type(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_counts_group_by_resource_type_with_options(request, runtime)

    async def get_aggregate_resource_counts_group_by_resource_type_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_counts_group_by_resource_type_with_options_async(request, runtime)

    def get_aggregator_with_options(
        self,
        request: config_20200907_models.GetAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregatorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregator',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregator_with_options_async(
        self,
        request: config_20200907_models.GetAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregatorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregator',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregator(
        self,
        request: config_20200907_models.GetAggregatorRequest,
    ) -> config_20200907_models.GetAggregatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregator_with_options(request, runtime)

    async def get_aggregator_async(
        self,
        request: config_20200907_models.GetAggregatorRequest,
    ) -> config_20200907_models.GetAggregatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregator_with_options_async(request, runtime)

    def get_compliance_pack_with_options(
        self,
        request: config_20200907_models.GetCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetCompliancePackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compliance_pack_with_options_async(
        self,
        request: config_20200907_models.GetCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetCompliancePackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compliance_pack(
        self,
        request: config_20200907_models.GetCompliancePackRequest,
    ) -> config_20200907_models.GetCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_compliance_pack_with_options(request, runtime)

    async def get_compliance_pack_async(
        self,
        request: config_20200907_models.GetCompliancePackRequest,
    ) -> config_20200907_models.GetCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_compliance_pack_with_options_async(request, runtime)

    def get_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GetCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetCompliancePackReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCompliancePackReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetCompliancePackReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compliance_pack_report_with_options_async(
        self,
        request: config_20200907_models.GetCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetCompliancePackReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCompliancePackReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetCompliancePackReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compliance_pack_report(
        self,
        request: config_20200907_models.GetCompliancePackReportRequest,
    ) -> config_20200907_models.GetCompliancePackReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_compliance_pack_report_with_options(request, runtime)

    async def get_compliance_pack_report_async(
        self,
        request: config_20200907_models.GetCompliancePackReportRequest,
    ) -> config_20200907_models.GetCompliancePackReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_compliance_pack_report_with_options_async(request, runtime)

    def get_config_rule_with_options(
        self,
        request: config_20200907_models.GetConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleId'] = request.config_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleId'] = request.config_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rule(
        self,
        request: config_20200907_models.GetConfigRuleRequest,
    ) -> config_20200907_models.GetConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_with_options(request, runtime)

    async def get_config_rule_async(
        self,
        request: config_20200907_models.GetConfigRuleRequest,
    ) -> config_20200907_models.GetConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_with_options_async(request, runtime)

    def get_config_rule_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetConfigRuleComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigRuleComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rule_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetConfigRuleComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigRuleComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rule_compliance_by_pack(
        self,
        request: config_20200907_models.GetConfigRuleComplianceByPackRequest,
    ) -> config_20200907_models.GetConfigRuleComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_compliance_by_pack_with_options(request, runtime)

    async def get_config_rule_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetConfigRuleComplianceByPackRequest,
    ) -> config_20200907_models.GetConfigRuleComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_compliance_by_pack_with_options_async(request, runtime)

    def get_config_rule_summary_by_risk_level_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetConfigRuleSummaryByRiskLevel',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rule_summary_by_risk_level_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetConfigRuleSummaryByRiskLevel',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rule_summary_by_risk_level(self) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_summary_by_risk_level_with_options(runtime)

    async def get_config_rule_summary_by_risk_level_async(self) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_summary_by_risk_level_with_options_async(runtime)

    def get_config_rules_report_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetConfigRulesReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rules_report_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetConfigRulesReport',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rules_report(self) -> config_20200907_models.GetConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_rules_report_with_options(runtime)

    async def get_config_rules_report_async(self) -> config_20200907_models.GetConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rules_report_with_options_async(runtime)

    def get_discovered_resource_counts_group_by_region_with_options(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCountsGroupByRegion',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_counts_group_by_region_with_options_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCountsGroupByRegion',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource_counts_group_by_region(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_counts_group_by_region_with_options(request, runtime)

    async def get_discovered_resource_counts_group_by_region_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_discovered_resource_counts_group_by_region_with_options_async(request, runtime)

    def get_discovered_resource_counts_group_by_resource_type_with_options(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCountsGroupByResourceType',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_counts_group_by_resource_type_with_options_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCountsGroupByResourceType',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource_counts_group_by_resource_type(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_counts_group_by_resource_type_with_options(request, runtime)

    async def get_discovered_resource_counts_group_by_resource_type_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_discovered_resource_counts_group_by_resource_type_with_options_async(request, runtime)

    def get_resource_compliance_by_config_rule_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceByConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceByConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceByConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_by_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceByConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceByConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceByConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_by_config_rule(
        self,
        request: config_20200907_models.GetResourceComplianceByConfigRuleRequest,
    ) -> config_20200907_models.GetResourceComplianceByConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_by_config_rule_with_options(request, runtime)

    async def get_resource_compliance_by_config_rule_async(
        self,
        request: config_20200907_models.GetResourceComplianceByConfigRuleRequest,
    ) -> config_20200907_models.GetResourceComplianceByConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_by_config_rule_with_options_async(request, runtime)

    def get_resource_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceByPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetResourceComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceByPack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceByPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_by_pack(
        self,
        request: config_20200907_models.GetResourceComplianceByPackRequest,
    ) -> config_20200907_models.GetResourceComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_by_pack_with_options(request, runtime)

    async def get_resource_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetResourceComplianceByPackRequest,
    ) -> config_20200907_models.GetResourceComplianceByPackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_by_pack_with_options_async(request, runtime)

    def get_resource_compliance_timeline_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceTimeline',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_timeline_with_options_async(
        self,
        request: config_20200907_models.GetResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceTimeline',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_timeline(
        self,
        request: config_20200907_models.GetResourceComplianceTimelineRequest,
    ) -> config_20200907_models.GetResourceComplianceTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_timeline_with_options(request, runtime)

    async def get_resource_compliance_timeline_async(
        self,
        request: config_20200907_models.GetResourceComplianceTimelineRequest,
    ) -> config_20200907_models.GetResourceComplianceTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_timeline_with_options_async(request, runtime)

    def get_resource_configuration_timeline_with_options(
        self,
        request: config_20200907_models.GetResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceConfigurationTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceConfigurationTimeline',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceConfigurationTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_configuration_timeline_with_options_async(
        self,
        request: config_20200907_models.GetResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceConfigurationTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceConfigurationTimeline',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceConfigurationTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_configuration_timeline(
        self,
        request: config_20200907_models.GetResourceConfigurationTimelineRequest,
    ) -> config_20200907_models.GetResourceConfigurationTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_configuration_timeline_with_options(request, runtime)

    async def get_resource_configuration_timeline_async(
        self,
        request: config_20200907_models.GetResourceConfigurationTimelineRequest,
    ) -> config_20200907_models.GetResourceConfigurationTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_configuration_timeline_with_options_async(request, runtime)

    def ignore_aggregate_evaluation_results_with_options(
        self,
        tmp_req: config_20200907_models.IgnoreAggregateEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.IgnoreAggregateEvaluationResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.IgnoreAggregateEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IgnoreAggregateEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.IgnoreAggregateEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ignore_aggregate_evaluation_results_with_options_async(
        self,
        tmp_req: config_20200907_models.IgnoreAggregateEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.IgnoreAggregateEvaluationResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.IgnoreAggregateEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IgnoreAggregateEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.IgnoreAggregateEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ignore_aggregate_evaluation_results(
        self,
        request: config_20200907_models.IgnoreAggregateEvaluationResultsRequest,
    ) -> config_20200907_models.IgnoreAggregateEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.ignore_aggregate_evaluation_results_with_options(request, runtime)

    async def ignore_aggregate_evaluation_results_async(
        self,
        request: config_20200907_models.IgnoreAggregateEvaluationResultsRequest,
    ) -> config_20200907_models.IgnoreAggregateEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ignore_aggregate_evaluation_results_with_options_async(request, runtime)

    def ignore_evaluation_results_with_options(
        self,
        tmp_req: config_20200907_models.IgnoreEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.IgnoreEvaluationResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.IgnoreEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IgnoreEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.IgnoreEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ignore_evaluation_results_with_options_async(
        self,
        tmp_req: config_20200907_models.IgnoreEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.IgnoreEvaluationResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.IgnoreEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IgnoreEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.IgnoreEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ignore_evaluation_results(
        self,
        request: config_20200907_models.IgnoreEvaluationResultsRequest,
    ) -> config_20200907_models.IgnoreEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.ignore_evaluation_results_with_options(request, runtime)

    async def ignore_evaluation_results_async(
        self,
        request: config_20200907_models.IgnoreEvaluationResultsRequest,
    ) -> config_20200907_models.IgnoreEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ignore_evaluation_results_with_options_async(request, runtime)

    def list_aggregate_compliance_packs_with_options(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateCompliancePacks',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateCompliancePacks',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_compliance_packs(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_compliance_packs_with_options(request, runtime)

    async def list_aggregate_compliance_packs_async(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_compliance_packs_with_options_async(request, runtime)

    def list_aggregate_config_rule_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRuleEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_rule_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRuleEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_rule_evaluation_results(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_config_rule_evaluation_results_with_options(request, runtime)

    async def list_aggregate_config_rule_evaluation_results_async(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_config_rule_evaluation_results_with_options_async(request, runtime)

    def list_aggregate_config_rules_with_options(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRules',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_rules(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_config_rules_with_options(request, runtime)

    async def list_aggregate_config_rules_async(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_config_rules_with_options_async(request, runtime)

    def list_aggregate_resource_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateResourceEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateResourceEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_resource_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateResourceEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateResourceEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_resource_evaluation_results(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_resource_evaluation_results_with_options(request, runtime)

    async def list_aggregate_resource_evaluation_results_async(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_resource_evaluation_results_with_options_async(request, runtime)

    def list_aggregators_with_options(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregatorsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregators',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregators_with_options_async(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregatorsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregators',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregators(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
    ) -> config_20200907_models.ListAggregatorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aggregators_with_options(request, runtime)

    async def list_aggregators_async(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
    ) -> config_20200907_models.ListAggregatorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregators_with_options_async(request, runtime)

    def list_compliance_pack_templates_with_options(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCompliancePackTemplates',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListCompliancePackTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compliance_pack_templates_with_options_async(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCompliancePackTemplates',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListCompliancePackTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compliance_pack_templates(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_compliance_pack_templates_with_options(request, runtime)

    async def list_compliance_pack_templates_async(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_compliance_pack_templates_with_options_async(request, runtime)

    def list_compliance_packs_with_options(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCompliancePacks',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCompliancePacks',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compliance_packs(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_compliance_packs_with_options(request, runtime)

    async def list_compliance_packs_async(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_compliance_packs_with_options_async(request, runtime)

    def list_config_rule_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRuleEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigRuleEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListConfigRuleEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rule_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRuleEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigRuleEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListConfigRuleEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rule_evaluation_results(
        self,
        request: config_20200907_models.ListConfigRuleEvaluationResultsRequest,
    ) -> config_20200907_models.ListConfigRuleEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_rule_evaluation_results_with_options(request, runtime)

    async def list_config_rule_evaluation_results_async(
        self,
        request: config_20200907_models.ListConfigRuleEvaluationResultsRequest,
    ) -> config_20200907_models.ListConfigRuleEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_rule_evaluation_results_with_options_async(request, runtime)

    def list_resource_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListResourceEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.ListResourceEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_evaluation_results(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_evaluation_results_with_options(request, runtime)

    async def list_resource_evaluation_results_async(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_evaluation_results_with_options_async(request, runtime)

    def revert_aggregate_evaluation_results_with_options(
        self,
        tmp_req: config_20200907_models.RevertAggregateEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.RevertAggregateEvaluationResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.RevertAggregateEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertAggregateEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.RevertAggregateEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_aggregate_evaluation_results_with_options_async(
        self,
        tmp_req: config_20200907_models.RevertAggregateEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.RevertAggregateEvaluationResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.RevertAggregateEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertAggregateEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.RevertAggregateEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_aggregate_evaluation_results(
        self,
        request: config_20200907_models.RevertAggregateEvaluationResultsRequest,
    ) -> config_20200907_models.RevertAggregateEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.revert_aggregate_evaluation_results_with_options(request, runtime)

    async def revert_aggregate_evaluation_results_async(
        self,
        request: config_20200907_models.RevertAggregateEvaluationResultsRequest,
    ) -> config_20200907_models.RevertAggregateEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revert_aggregate_evaluation_results_with_options_async(request, runtime)

    def revert_evaluation_results_with_options(
        self,
        tmp_req: config_20200907_models.RevertEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.RevertEvaluationResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.RevertEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.RevertEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_evaluation_results_with_options_async(
        self,
        tmp_req: config_20200907_models.RevertEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.RevertEvaluationResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.RevertEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.resources_shrink):
            body['Resources'] = request.resources_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertEvaluationResults',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.RevertEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_evaluation_results(
        self,
        request: config_20200907_models.RevertEvaluationResultsRequest,
    ) -> config_20200907_models.RevertEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.revert_evaluation_results_with_options(request, runtime)

    async def revert_evaluation_results_async(
        self,
        request: config_20200907_models.RevertEvaluationResultsRequest,
    ) -> config_20200907_models.RevertEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revert_evaluation_results_with_options_async(request, runtime)

    def start_aggregate_config_rule_evaluation_with_options(
        self,
        request: config_20200907_models.StartAggregateConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateConfigRuleEvaluationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleId'] = request.config_rule_id
        query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAggregateConfigRuleEvaluation',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.StartAggregateConfigRuleEvaluationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aggregate_config_rule_evaluation_with_options_async(
        self,
        request: config_20200907_models.StartAggregateConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateConfigRuleEvaluationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AggregatorId'] = request.aggregator_id
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleId'] = request.config_rule_id
        query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAggregateConfigRuleEvaluation',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.StartAggregateConfigRuleEvaluationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aggregate_config_rule_evaluation(
        self,
        request: config_20200907_models.StartAggregateConfigRuleEvaluationRequest,
    ) -> config_20200907_models.StartAggregateConfigRuleEvaluationResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_aggregate_config_rule_evaluation_with_options(request, runtime)

    async def start_aggregate_config_rule_evaluation_async(
        self,
        request: config_20200907_models.StartAggregateConfigRuleEvaluationRequest,
    ) -> config_20200907_models.StartAggregateConfigRuleEvaluationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_aggregate_config_rule_evaluation_with_options_async(request, runtime)

    def update_aggregate_compliance_pack_with_options(
        self,
        tmp_req: config_20200907_models.UpdateAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateCompliancePackResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateAggregateCompliancePackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_rules):
            request.config_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not UtilClient.is_unset(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggregateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregate_compliance_pack_with_options_async(
        self,
        tmp_req: config_20200907_models.UpdateAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateCompliancePackResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateAggregateCompliancePackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_rules):
            request.config_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not UtilClient.is_unset(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggregateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregate_compliance_pack(
        self,
        request: config_20200907_models.UpdateAggregateCompliancePackRequest,
    ) -> config_20200907_models.UpdateAggregateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_aggregate_compliance_pack_with_options(request, runtime)

    async def update_aggregate_compliance_pack_async(
        self,
        request: config_20200907_models.UpdateAggregateCompliancePackRequest,
    ) -> config_20200907_models.UpdateAggregateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregate_compliance_pack_with_options_async(request, runtime)

    def update_aggregate_config_rule_with_options(
        self,
        tmp_req: config_20200907_models.UpdateAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateConfigRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateAggregateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggregateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregate_config_rule_with_options_async(
        self,
        tmp_req: config_20200907_models.UpdateAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateConfigRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateAggregateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggregateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregate_config_rule(
        self,
        request: config_20200907_models.UpdateAggregateConfigRuleRequest,
    ) -> config_20200907_models.UpdateAggregateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_aggregate_config_rule_with_options(request, runtime)

    async def update_aggregate_config_rule_async(
        self,
        request: config_20200907_models.UpdateAggregateConfigRuleRequest,
    ) -> config_20200907_models.UpdateAggregateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregate_config_rule_with_options_async(request, runtime)

    def update_aggregator_with_options(
        self,
        tmp_req: config_20200907_models.UpdateAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregatorResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateAggregatorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregator_accounts):
            request.aggregator_accounts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregator_accounts, 'AggregatorAccounts', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_accounts_shrink):
            body['AggregatorAccounts'] = request.aggregator_accounts_shrink
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.aggregator_name):
            body['AggregatorName'] = request.aggregator_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggregator',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregator_with_options_async(
        self,
        tmp_req: config_20200907_models.UpdateAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregatorResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateAggregatorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregator_accounts):
            request.aggregator_accounts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregator_accounts, 'AggregatorAccounts', 'json')
        body = {}
        if not UtilClient.is_unset(request.aggregator_accounts_shrink):
            body['AggregatorAccounts'] = request.aggregator_accounts_shrink
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.aggregator_name):
            body['AggregatorName'] = request.aggregator_name
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggregator',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregator(
        self,
        request: config_20200907_models.UpdateAggregatorRequest,
    ) -> config_20200907_models.UpdateAggregatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_aggregator_with_options(request, runtime)

    async def update_aggregator_async(
        self,
        request: config_20200907_models.UpdateAggregatorRequest,
    ) -> config_20200907_models.UpdateAggregatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregator_with_options_async(request, runtime)

    def update_compliance_pack_with_options(
        self,
        tmp_req: config_20200907_models.UpdateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateCompliancePackResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateCompliancePackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_rules):
            request.config_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not UtilClient.is_unset(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateCompliancePackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compliance_pack_with_options_async(
        self,
        tmp_req: config_20200907_models.UpdateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateCompliancePackResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateCompliancePackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_rules):
            request.config_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_rules, 'ConfigRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_pack_id):
            body['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.compliance_pack_name):
            body['CompliancePackName'] = request.compliance_pack_name
        if not UtilClient.is_unset(request.config_rules_shrink):
            body['ConfigRules'] = request.config_rules_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCompliancePack',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateCompliancePackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compliance_pack(
        self,
        request: config_20200907_models.UpdateCompliancePackRequest,
    ) -> config_20200907_models.UpdateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_compliance_pack_with_options(request, runtime)

    async def update_compliance_pack_async(
        self,
        request: config_20200907_models.UpdateCompliancePackRequest,
    ) -> config_20200907_models.UpdateCompliancePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_compliance_pack_with_options_async(request, runtime)

    def update_config_rule_with_options(
        self,
        tmp_req: config_20200907_models.UpdateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateConfigRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_rule_with_options_async(
        self,
        tmp_req: config_20200907_models.UpdateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateConfigRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.config_rule_name):
            body['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_trigger_types):
            body['ConfigRuleTriggerTypes'] = request.config_rule_trigger_types
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigRule',
            version='2020-09-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_rule(
        self,
        request: config_20200907_models.UpdateConfigRuleRequest,
    ) -> config_20200907_models.UpdateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_config_rule_with_options(request, runtime)

    async def update_config_rule_async(
        self,
        request: config_20200907_models.UpdateConfigRuleRequest,
    ) -> config_20200907_models.UpdateConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_config_rule_with_options_async(request, runtime)
