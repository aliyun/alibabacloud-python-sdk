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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.ActiveAggregateConfigRulesResponse(),
            self.do_rpcrequest('ActiveAggregateConfigRules', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def active_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.ActiveAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ActiveAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.ActiveAggregateConfigRulesResponse(),
            await self.do_rpcrequest_async('ActiveAggregateConfigRules', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateCompliancePackResponse(),
            self.do_rpcrequest('CreateAggregateCompliancePack', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateCompliancePackResponse(),
            await self.do_rpcrequest_async('CreateAggregateCompliancePack', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateConfigRuleResponse(),
            self.do_rpcrequest('CreateAggregateConfigRule', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateConfigRuleResponse(),
            await self.do_rpcrequest_async('CreateAggregateConfigRule', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_aggregate_remediation_with_options(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateRemediationResponse(),
            self.do_rpcrequest('CreateAggregateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_aggregate_remediation_with_options_async(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregateRemediationResponse(),
            await self.do_rpcrequest_async('CreateAggregateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_aggregate_remediation(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_remediation_with_options(request, runtime)

    async def create_aggregate_remediation_async(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_remediation_with_options_async(request, runtime)

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregatorResponse(),
            self.do_rpcrequest('CreateAggregator', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateAggregatorResponse(),
            await self.do_rpcrequest_async('CreateAggregator', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateCompliancePackResponse(),
            self.do_rpcrequest('CreateCompliancePack', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateCompliancePackResponse(),
            await self.do_rpcrequest_async('CreateCompliancePack', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateConfigRuleResponse(),
            self.do_rpcrequest('CreateConfigRule', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateConfigRuleResponse(),
            await self.do_rpcrequest_async('CreateConfigRule', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_remediation_with_options(
        self,
        request: config_20200907_models.CreateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateRemediationResponse(),
            self.do_rpcrequest('CreateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_remediation_with_options_async(
        self,
        request: config_20200907_models.CreateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.CreateRemediationResponse(),
            await self.do_rpcrequest_async('CreateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_remediation(
        self,
        request: config_20200907_models.CreateRemediationRequest,
    ) -> config_20200907_models.CreateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_remediation_with_options(request, runtime)

    async def create_remediation_async(
        self,
        request: config_20200907_models.CreateRemediationRequest,
    ) -> config_20200907_models.CreateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_remediation_with_options_async(request, runtime)

    def deactive_aggregate_config_rules_with_options(
        self,
        request: config_20200907_models.DeactiveAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeactiveAggregateConfigRulesResponse(),
            self.do_rpcrequest('DeactiveAggregateConfigRules', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactive_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.DeactiveAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeactiveAggregateConfigRulesResponse(),
            await self.do_rpcrequest_async('DeactiveAggregateConfigRules', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeactiveConfigRulesResponse(),
            self.do_rpcrequest('DeactiveConfigRules', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactive_config_rules_with_options_async(
        self,
        request: config_20200907_models.DeactiveConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveConfigRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeactiveConfigRulesResponse(),
            await self.do_rpcrequest_async('DeactiveConfigRules', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateCompliancePacksResponse(),
            self.do_rpcrequest('DeleteAggregateCompliancePacks', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aggregate_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateCompliancePacksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateCompliancePacksResponse(),
            await self.do_rpcrequest_async('DeleteAggregateCompliancePacks', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateConfigRulesResponse(),
            self.do_rpcrequest('DeleteAggregateConfigRules', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateConfigRulesResponse(),
            await self.do_rpcrequest_async('DeleteAggregateConfigRules', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_aggregate_remediations_with_options(
        self,
        request: config_20200907_models.DeleteAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateRemediationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateRemediationsResponse(),
            self.do_rpcrequest('DeleteAggregateRemediations', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aggregate_remediations_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateRemediationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregateRemediationsResponse(),
            await self.do_rpcrequest_async('DeleteAggregateRemediations', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_aggregate_remediations(
        self,
        request: config_20200907_models.DeleteAggregateRemediationsRequest,
    ) -> config_20200907_models.DeleteAggregateRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregate_remediations_with_options(request, runtime)

    async def delete_aggregate_remediations_async(
        self,
        request: config_20200907_models.DeleteAggregateRemediationsRequest,
    ) -> config_20200907_models.DeleteAggregateRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregate_remediations_with_options_async(request, runtime)

    def delete_aggregators_with_options(
        self,
        request: config_20200907_models.DeleteAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregatorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregatorsResponse(),
            self.do_rpcrequest('DeleteAggregators', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aggregators_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregatorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteAggregatorsResponse(),
            await self.do_rpcrequest_async('DeleteAggregators', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteCompliancePacksResponse(),
            self.do_rpcrequest('DeleteCompliancePacks', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.DeleteCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteCompliancePacksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteCompliancePacksResponse(),
            await self.do_rpcrequest_async('DeleteCompliancePacks', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_remediations_with_options(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteRemediationsResponse(),
            self.do_rpcrequest('DeleteRemediations', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_remediations_with_options_async(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.DeleteRemediationsResponse(),
            await self.do_rpcrequest_async('DeleteRemediations', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_remediations(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_remediations_with_options(request, runtime)

    async def delete_remediations_async(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_remediations_with_options_async(request, runtime)

    def generate_aggregate_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GenerateAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateCompliancePackReportResponse(),
            self.do_rpcrequest('GenerateAggregateCompliancePackReport', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_aggregate_compliance_pack_report_with_options_async(
        self,
        request: config_20200907_models.GenerateAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateCompliancePackReportResponse(),
            await self.do_rpcrequest_async('GenerateAggregateCompliancePackReport', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateConfigRulesReportResponse(),
            self.do_rpcrequest('GenerateAggregateConfigRulesReport', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_aggregate_config_rules_report_with_options_async(
        self,
        request: config_20200907_models.GenerateAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateConfigRulesReportResponse(),
            await self.do_rpcrequest_async('GenerateAggregateConfigRulesReport', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def generate_aggregate_resource_inventory_with_options(
        self,
        request: config_20200907_models.GenerateAggregateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateResourceInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateResourceInventoryResponse(),
            self.do_rpcrequest('GenerateAggregateResourceInventory', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_aggregate_resource_inventory_with_options_async(
        self,
        request: config_20200907_models.GenerateAggregateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateResourceInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateAggregateResourceInventoryResponse(),
            await self.do_rpcrequest_async('GenerateAggregateResourceInventory', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_aggregate_resource_inventory(
        self,
        request: config_20200907_models.GenerateAggregateResourceInventoryRequest,
    ) -> config_20200907_models.GenerateAggregateResourceInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_aggregate_resource_inventory_with_options(request, runtime)

    async def generate_aggregate_resource_inventory_async(
        self,
        request: config_20200907_models.GenerateAggregateResourceInventoryRequest,
    ) -> config_20200907_models.GenerateAggregateResourceInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_aggregate_resource_inventory_with_options_async(request, runtime)

    def generate_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GenerateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateCompliancePackReportResponse(),
            self.do_rpcrequest('GenerateCompliancePackReport', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_compliance_pack_report_with_options_async(
        self,
        request: config_20200907_models.GenerateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateCompliancePackReportResponse(),
            await self.do_rpcrequest_async('GenerateCompliancePackReport', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateConfigRulesReportResponse(),
            self.do_rpcrequest('GenerateConfigRulesReport', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_config_rules_report_with_options_async(
        self,
        request: config_20200907_models.GenerateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateConfigRulesReportResponse(),
            await self.do_rpcrequest_async('GenerateConfigRulesReport', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def generate_resource_inventory_with_options(
        self,
        request: config_20200907_models.GenerateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateResourceInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateResourceInventoryResponse(),
            self.do_rpcrequest('GenerateResourceInventory', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_resource_inventory_with_options_async(
        self,
        request: config_20200907_models.GenerateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateResourceInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GenerateResourceInventoryResponse(),
            await self.do_rpcrequest_async('GenerateResourceInventory', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_resource_inventory(
        self,
        request: config_20200907_models.GenerateResourceInventoryRequest,
    ) -> config_20200907_models.GenerateResourceInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_resource_inventory_with_options(request, runtime)

    async def generate_resource_inventory_async(
        self,
        request: config_20200907_models.GenerateResourceInventoryRequest,
    ) -> config_20200907_models.GenerateResourceInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_resource_inventory_with_options_async(request, runtime)

    def get_aggregate_account_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateAccountComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateAccountComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateAccountComplianceByPackResponse(),
            self.do_rpcrequest('GetAggregateAccountComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_account_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetAggregateAccountComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateAccountComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateAccountComplianceByPackResponse(),
            await self.do_rpcrequest_async('GetAggregateAccountComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateCompliancePackResponse(),
            self.do_rpcrequest('GetAggregateCompliancePack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_compliance_pack_with_options_async(
        self,
        request: config_20200907_models.GetAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateCompliancePackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateCompliancePackResponse(),
            await self.do_rpcrequest_async('GetAggregateCompliancePack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateCompliancePackReportResponse(),
            self.do_rpcrequest('GetAggregateCompliancePackReport', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_compliance_pack_report_with_options_async(
        self,
        request: config_20200907_models.GetAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateCompliancePackReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateCompliancePackReportResponse(),
            await self.do_rpcrequest_async('GetAggregateCompliancePackReport', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleResponse(),
            self.do_rpcrequest('GetAggregateConfigRule', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleResponse(),
            await self.do_rpcrequest_async('GetAggregateConfigRule', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse(),
            self.do_rpcrequest('GetAggregateConfigRuleComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_config_rule_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse(),
            await self.do_rpcrequest_async('GetAggregateConfigRuleComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def get_aggregate_config_rules_report_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRulesReportResponse(),
            self.do_rpcrequest('GetAggregateConfigRulesReport', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_config_rules_report_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRulesReportResponse(),
            await self.do_rpcrequest_async('GetAggregateConfigRulesReport', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def get_aggregate_config_rule_summary_by_risk_level_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse(),
            self.do_rpcrequest('GetAggregateConfigRuleSummaryByRiskLevel', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_config_rule_summary_by_risk_level_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse(),
            await self.do_rpcrequest_async('GetAggregateConfigRuleSummaryByRiskLevel', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def get_aggregate_resource_compliance_by_config_rule_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse(),
            self.do_rpcrequest('GetAggregateResourceComplianceByConfigRule', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_resource_compliance_by_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse(),
            await self.do_rpcrequest_async('GetAggregateResourceComplianceByConfigRule', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceByPackResponse(),
            self.do_rpcrequest('GetAggregateResourceComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_resource_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceByPackResponse(),
            await self.do_rpcrequest_async('GetAggregateResourceComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceTimelineResponse(),
            self.do_rpcrequest('GetAggregateResourceComplianceTimeline', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_resource_compliance_timeline_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceComplianceTimelineResponse(),
            await self.do_rpcrequest_async('GetAggregateResourceComplianceTimeline', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceConfigurationTimelineResponse(),
            self.do_rpcrequest('GetAggregateResourceConfigurationTimeline', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_resource_configuration_timeline_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceConfigurationTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceConfigurationTimelineResponse(),
            await self.do_rpcrequest_async('GetAggregateResourceConfigurationTimeline', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse(),
            self.do_rpcrequest('GetAggregateResourceCountsGroupByRegion', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_resource_counts_group_by_region_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse(),
            await self.do_rpcrequest_async('GetAggregateResourceCountsGroupByRegion', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse(),
            self.do_rpcrequest('GetAggregateResourceCountsGroupByResourceType', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_resource_counts_group_by_resource_type_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse(),
            await self.do_rpcrequest_async('GetAggregateResourceCountsGroupByResourceType', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def get_aggregate_resource_inventory_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceInventoryResponse(),
            self.do_rpcrequest('GetAggregateResourceInventory', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aggregate_resource_inventory_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregateResourceInventoryResponse(),
            await self.do_rpcrequest_async('GetAggregateResourceInventory', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aggregate_resource_inventory(
        self,
        request: config_20200907_models.GetAggregateResourceInventoryRequest,
    ) -> config_20200907_models.GetAggregateResourceInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_inventory_with_options(request, runtime)

    async def get_aggregate_resource_inventory_async(
        self,
        request: config_20200907_models.GetAggregateResourceInventoryRequest,
    ) -> config_20200907_models.GetAggregateResourceInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_inventory_with_options_async(request, runtime)

    def get_aggregator_with_options(
        self,
        request: config_20200907_models.GetAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregatorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregatorResponse(),
            self.do_rpcrequest('GetAggregator', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_aggregator_with_options_async(
        self,
        request: config_20200907_models.GetAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregatorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetAggregatorResponse(),
            await self.do_rpcrequest_async('GetAggregator', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetCompliancePackResponse(),
            self.do_rpcrequest('GetCompliancePack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_compliance_pack_with_options_async(
        self,
        request: config_20200907_models.GetCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetCompliancePackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetCompliancePackResponse(),
            await self.do_rpcrequest_async('GetCompliancePack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetCompliancePackReportResponse(),
            self.do_rpcrequest('GetCompliancePackReport', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_compliance_pack_report_with_options_async(
        self,
        request: config_20200907_models.GetCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetCompliancePackReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetCompliancePackReportResponse(),
            await self.do_rpcrequest_async('GetCompliancePackReport', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleResponse(),
            self.do_rpcrequest('GetConfigRule', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleResponse(),
            await self.do_rpcrequest_async('GetConfigRule', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleComplianceByPackResponse(),
            self.do_rpcrequest('GetConfigRuleComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_config_rule_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetConfigRuleComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleComplianceByPackResponse(),
            await self.do_rpcrequest_async('GetConfigRuleComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def get_config_rules_report_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            config_20200907_models.GetConfigRulesReportResponse(),
            self.do_rpcrequest('GetConfigRulesReport', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_config_rules_report_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            config_20200907_models.GetConfigRulesReportResponse(),
            await self.do_rpcrequest_async('GetConfigRulesReport', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_config_rules_report(self) -> config_20200907_models.GetConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_rules_report_with_options(runtime)

    async def get_config_rules_report_async(self) -> config_20200907_models.GetConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rules_report_with_options_async(runtime)

    def get_config_rule_summary_by_risk_level_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse(),
            self.do_rpcrequest('GetConfigRuleSummaryByRiskLevel', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_config_rule_summary_by_risk_level_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse(),
            await self.do_rpcrequest_async('GetConfigRuleSummaryByRiskLevel', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_config_rule_summary_by_risk_level(self) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_summary_by_risk_level_with_options(runtime)

    async def get_config_rule_summary_by_risk_level_async(self) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_summary_by_risk_level_with_options_async(runtime)

    def get_discovered_resource_counts_group_by_region_with_options(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse(),
            self.do_rpcrequest('GetDiscoveredResourceCountsGroupByRegion', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_discovered_resource_counts_group_by_region_with_options_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse(),
            await self.do_rpcrequest_async('GetDiscoveredResourceCountsGroupByRegion', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse(),
            self.do_rpcrequest('GetDiscoveredResourceCountsGroupByResourceType', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_discovered_resource_counts_group_by_resource_type_with_options_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse(),
            await self.do_rpcrequest_async('GetDiscoveredResourceCountsGroupByResourceType', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceByConfigRuleResponse(),
            self.do_rpcrequest('GetResourceComplianceByConfigRule', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_resource_compliance_by_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceByConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceByConfigRuleResponse(),
            await self.do_rpcrequest_async('GetResourceComplianceByConfigRule', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceByPackResponse(),
            self.do_rpcrequest('GetResourceComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_resource_compliance_by_pack_with_options_async(
        self,
        request: config_20200907_models.GetResourceComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceByPackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceByPackResponse(),
            await self.do_rpcrequest_async('GetResourceComplianceByPack', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceTimelineResponse(),
            self.do_rpcrequest('GetResourceComplianceTimeline', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_resource_compliance_timeline_with_options_async(
        self,
        request: config_20200907_models.GetResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceComplianceTimelineResponse(),
            await self.do_rpcrequest_async('GetResourceComplianceTimeline', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceConfigurationTimelineResponse(),
            self.do_rpcrequest('GetResourceConfigurationTimeline', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_resource_configuration_timeline_with_options_async(
        self,
        request: config_20200907_models.GetResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceConfigurationTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.GetResourceConfigurationTimelineResponse(),
            await self.do_rpcrequest_async('GetResourceConfigurationTimeline', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def get_resource_inventory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceInventoryResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            config_20200907_models.GetResourceInventoryResponse(),
            self.do_rpcrequest('GetResourceInventory', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_resource_inventory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceInventoryResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            config_20200907_models.GetResourceInventoryResponse(),
            await self.do_rpcrequest_async('GetResourceInventory', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_inventory(self) -> config_20200907_models.GetResourceInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_inventory_with_options(runtime)

    async def get_resource_inventory_async(self) -> config_20200907_models.GetResourceInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_inventory_with_options_async(runtime)

    def list_aggregate_compliance_packs_with_options(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateCompliancePacksResponse(),
            self.do_rpcrequest('ListAggregateCompliancePacks', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_aggregate_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateCompliancePacksResponse(),
            await self.do_rpcrequest_async('ListAggregateCompliancePacks', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse(),
            self.do_rpcrequest('ListAggregateConfigRuleEvaluationResults', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_aggregate_config_rule_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse(),
            await self.do_rpcrequest_async('ListAggregateConfigRuleEvaluationResults', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateConfigRulesResponse(),
            self.do_rpcrequest('ListAggregateConfigRules', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateConfigRulesResponse(),
            await self.do_rpcrequest_async('ListAggregateConfigRules', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def list_aggregate_remediations_with_options(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateRemediationsResponse(),
            self.do_rpcrequest('ListAggregateRemediations', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aggregate_remediations_with_options_async(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateRemediationsResponse(),
            await self.do_rpcrequest_async('ListAggregateRemediations', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aggregate_remediations(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_remediations_with_options(request, runtime)

    async def list_aggregate_remediations_async(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_remediations_with_options_async(request, runtime)

    def list_aggregate_resource_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateResourceEvaluationResultsResponse(),
            self.do_rpcrequest('ListAggregateResourceEvaluationResults', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_aggregate_resource_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregateResourceEvaluationResultsResponse(),
            await self.do_rpcrequest_async('ListAggregateResourceEvaluationResults', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregatorsResponse(),
            self.do_rpcrequest('ListAggregators', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_aggregators_with_options_async(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregatorsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListAggregatorsResponse(),
            await self.do_rpcrequest_async('ListAggregators', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def list_compliance_packs_with_options(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListCompliancePacksResponse(),
            self.do_rpcrequest('ListCompliancePacks', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListCompliancePacksResponse(),
            await self.do_rpcrequest_async('ListCompliancePacks', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def list_compliance_pack_templates_with_options(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListCompliancePackTemplatesResponse(),
            self.do_rpcrequest('ListCompliancePackTemplates', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_compliance_pack_templates_with_options_async(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListCompliancePackTemplatesResponse(),
            await self.do_rpcrequest_async('ListCompliancePackTemplates', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def list_config_rule_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRuleEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListConfigRuleEvaluationResultsResponse(),
            self.do_rpcrequest('ListConfigRuleEvaluationResults', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_config_rule_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRuleEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListConfigRuleEvaluationResultsResponse(),
            await self.do_rpcrequest_async('ListConfigRuleEvaluationResults', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def list_remediations_with_options(
        self,
        request: config_20200907_models.ListRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.ListRemediationsResponse(),
            self.do_rpcrequest('ListRemediations', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_remediations_with_options_async(
        self,
        request: config_20200907_models.ListRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.ListRemediationsResponse(),
            await self.do_rpcrequest_async('ListRemediations', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_remediations(
        self,
        request: config_20200907_models.ListRemediationsRequest,
    ) -> config_20200907_models.ListRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_remediations_with_options(request, runtime)

    async def list_remediations_async(
        self,
        request: config_20200907_models.ListRemediationsRequest,
    ) -> config_20200907_models.ListRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_remediations_with_options_async(request, runtime)

    def list_resource_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListResourceEvaluationResultsResponse(),
            self.do_rpcrequest('ListResourceEvaluationResults', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_resource_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            config_20200907_models.ListResourceEvaluationResultsResponse(),
            await self.do_rpcrequest_async('ListResourceEvaluationResults', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def list_resource_owner_in_all_aggregator_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceOwnerInAllAggregatorResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            config_20200907_models.ListResourceOwnerInAllAggregatorResponse(),
            self.do_rpcrequest('ListResourceOwnerInAllAggregator', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_resource_owner_in_all_aggregator_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceOwnerInAllAggregatorResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            config_20200907_models.ListResourceOwnerInAllAggregatorResponse(),
            await self.do_rpcrequest_async('ListResourceOwnerInAllAggregator', '2020-09-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_resource_owner_in_all_aggregator(self) -> config_20200907_models.ListResourceOwnerInAllAggregatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_owner_in_all_aggregator_with_options(runtime)

    async def list_resource_owner_in_all_aggregator_async(self) -> config_20200907_models.ListResourceOwnerInAllAggregatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_owner_in_all_aggregator_with_options_async(runtime)

    def start_aggregate_config_rule_evaluation_with_options(
        self,
        request: config_20200907_models.StartAggregateConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateConfigRuleEvaluationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.StartAggregateConfigRuleEvaluationResponse(),
            self.do_rpcrequest('StartAggregateConfigRuleEvaluation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_aggregate_config_rule_evaluation_with_options_async(
        self,
        request: config_20200907_models.StartAggregateConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateConfigRuleEvaluationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.StartAggregateConfigRuleEvaluationResponse(),
            await self.do_rpcrequest_async('StartAggregateConfigRuleEvaluation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def start_aggregate_remediation_with_options(
        self,
        request: config_20200907_models.StartAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.StartAggregateRemediationResponse(),
            self.do_rpcrequest('StartAggregateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_aggregate_remediation_with_options_async(
        self,
        request: config_20200907_models.StartAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.StartAggregateRemediationResponse(),
            await self.do_rpcrequest_async('StartAggregateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_aggregate_remediation(
        self,
        request: config_20200907_models.StartAggregateRemediationRequest,
    ) -> config_20200907_models.StartAggregateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_aggregate_remediation_with_options(request, runtime)

    async def start_aggregate_remediation_async(
        self,
        request: config_20200907_models.StartAggregateRemediationRequest,
    ) -> config_20200907_models.StartAggregateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_aggregate_remediation_with_options_async(request, runtime)

    def start_remediation_with_options(
        self,
        request: config_20200907_models.StartRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.StartRemediationResponse(),
            self.do_rpcrequest('StartRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_remediation_with_options_async(
        self,
        request: config_20200907_models.StartRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.StartRemediationResponse(),
            await self.do_rpcrequest_async('StartRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_remediation(
        self,
        request: config_20200907_models.StartRemediationRequest,
    ) -> config_20200907_models.StartRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_remediation_with_options(request, runtime)

    async def start_remediation_async(
        self,
        request: config_20200907_models.StartRemediationRequest,
    ) -> config_20200907_models.StartRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_remediation_with_options_async(request, runtime)

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateCompliancePackResponse(),
            self.do_rpcrequest('UpdateAggregateCompliancePack', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateCompliancePackResponse(),
            await self.do_rpcrequest_async('UpdateAggregateCompliancePack', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateConfigRuleResponse(),
            self.do_rpcrequest('UpdateAggregateConfigRule', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateConfigRuleResponse(),
            await self.do_rpcrequest_async('UpdateAggregateConfigRule', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_aggregate_remediation_with_options(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateRemediationResponse(),
            self.do_rpcrequest('UpdateAggregateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_aggregate_remediation_with_options_async(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregateRemediationResponse(),
            await self.do_rpcrequest_async('UpdateAggregateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_aggregate_remediation(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_aggregate_remediation_with_options(request, runtime)

    async def update_aggregate_remediation_async(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregate_remediation_with_options_async(request, runtime)

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregatorResponse(),
            self.do_rpcrequest('UpdateAggregator', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateAggregatorResponse(),
            await self.do_rpcrequest_async('UpdateAggregator', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateCompliancePackResponse(),
            self.do_rpcrequest('UpdateCompliancePack', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateCompliancePackResponse(),
            await self.do_rpcrequest_async('UpdateCompliancePack', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateConfigRuleResponse(),
            self.do_rpcrequest('UpdateConfigRule', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateConfigRuleResponse(),
            await self.do_rpcrequest_async('UpdateConfigRule', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_remediation_with_options(
        self,
        request: config_20200907_models.UpdateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateRemediationResponse(),
            self.do_rpcrequest('UpdateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_remediation_with_options_async(
        self,
        request: config_20200907_models.UpdateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateRemediationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            config_20200907_models.UpdateRemediationResponse(),
            await self.do_rpcrequest_async('UpdateRemediation', '2020-09-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_remediation(
        self,
        request: config_20200907_models.UpdateRemediationRequest,
    ) -> config_20200907_models.UpdateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_remediation_with_options(request, runtime)

    async def update_remediation_async(
        self,
        request: config_20200907_models.UpdateRemediationRequest,
    ) -> config_20200907_models.UpdateRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_remediation_with_options_async(request, runtime)
