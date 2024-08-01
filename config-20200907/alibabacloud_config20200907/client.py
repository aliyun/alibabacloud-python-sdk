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
        """
        @summary Enables one or more rules in an account group. After a rule is enabled, the rule continues to automatically evaluate resources based on the trigger mechanism.
        
        @description ### [](#)Prerequisites
        The rule is in the `INACTIVE` state.
        ### [](#)Description
        This topic provides an example on how to enable the `cr-5772ba41209e007b***` rule in the `ca-a4e5626622af0079****` account group.
        
        @param request: ActiveAggregateConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveAggregateConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Enables one or more rules in an account group. After a rule is enabled, the rule continues to automatically evaluate resources based on the trigger mechanism.
        
        @description ### [](#)Prerequisites
        The rule is in the `INACTIVE` state.
        ### [](#)Description
        This topic provides an example on how to enable the `cr-5772ba41209e007b***` rule in the `ca-a4e5626622af0079****` account group.
        
        @param request: ActiveAggregateConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveAggregateConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Enables one or more rules in an account group. After a rule is enabled, the rule continues to automatically evaluate resources based on the trigger mechanism.
        
        @description ### [](#)Prerequisites
        The rule is in the `INACTIVE` state.
        ### [](#)Description
        This topic provides an example on how to enable the `cr-5772ba41209e007b***` rule in the `ca-a4e5626622af0079****` account group.
        
        @param request: ActiveAggregateConfigRulesRequest
        @return: ActiveAggregateConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.active_aggregate_config_rules_with_options(request, runtime)

    async def active_aggregate_config_rules_async(
        self,
        request: config_20200907_models.ActiveAggregateConfigRulesRequest,
    ) -> config_20200907_models.ActiveAggregateConfigRulesResponse:
        """
        @summary Enables one or more rules in an account group. After a rule is enabled, the rule continues to automatically evaluate resources based on the trigger mechanism.
        
        @description ### [](#)Prerequisites
        The rule is in the `INACTIVE` state.
        ### [](#)Description
        This topic provides an example on how to enable the `cr-5772ba41209e007b***` rule in the `ca-a4e5626622af0079****` account group.
        
        @param request: ActiveAggregateConfigRulesRequest
        @return: ActiveAggregateConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.active_aggregate_config_rules_with_options_async(request, runtime)

    def active_config_rules_with_options(
        self,
        request: config_20200907_models.ActiveConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ActiveConfigRulesResponse:
        """
        @summary Enables a rule in Cloud Config. After a rule is enabled, Cloud Config automatically evaluates the compliance of a resource based on the trigger mechanism of the rule.
        
        @description ### [](#)Prerequisites
        The rule is in the `INACTIVE` state.
        
        @param request: ActiveConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveConfigRules',
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
            config_20200907_models.ActiveConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_config_rules_with_options_async(
        self,
        request: config_20200907_models.ActiveConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ActiveConfigRulesResponse:
        """
        @summary Enables a rule in Cloud Config. After a rule is enabled, Cloud Config automatically evaluates the compliance of a resource based on the trigger mechanism of the rule.
        
        @description ### [](#)Prerequisites
        The rule is in the `INACTIVE` state.
        
        @param request: ActiveConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActiveConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveConfigRules',
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
            config_20200907_models.ActiveConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_config_rules(
        self,
        request: config_20200907_models.ActiveConfigRulesRequest,
    ) -> config_20200907_models.ActiveConfigRulesResponse:
        """
        @summary Enables a rule in Cloud Config. After a rule is enabled, Cloud Config automatically evaluates the compliance of a resource based on the trigger mechanism of the rule.
        
        @description ### [](#)Prerequisites
        The rule is in the `INACTIVE` state.
        
        @param request: ActiveConfigRulesRequest
        @return: ActiveConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.active_config_rules_with_options(request, runtime)

    async def active_config_rules_async(
        self,
        request: config_20200907_models.ActiveConfigRulesRequest,
    ) -> config_20200907_models.ActiveConfigRulesResponse:
        """
        @summary Enables a rule in Cloud Config. After a rule is enabled, Cloud Config automatically evaluates the compliance of a resource based on the trigger mechanism of the rule.
        
        @description ### [](#)Prerequisites
        The rule is in the `INACTIVE` state.
        
        @param request: ActiveConfigRulesRequest
        @return: ActiveConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.active_config_rules_with_options_async(request, runtime)

    def attach_aggregate_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.AttachAggregateConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.AttachAggregateConfigRuleToCompliancePackResponse:
        """
        @summary Adds one or more rules in an account group to a compliance package.
        
        @description The sample request in this topic shows you how to add the `cr-6cc4626622af00e7***` rule in the `ca-75b4626622af00c3****` account group to the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: AttachAggregateConfigRuleToCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachAggregateConfigRuleToCompliancePackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Adds one or more rules in an account group to a compliance package.
        
        @description The sample request in this topic shows you how to add the `cr-6cc4626622af00e7***` rule in the `ca-75b4626622af00c3****` account group to the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: AttachAggregateConfigRuleToCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachAggregateConfigRuleToCompliancePackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Adds one or more rules in an account group to a compliance package.
        
        @description The sample request in this topic shows you how to add the `cr-6cc4626622af00e7***` rule in the `ca-75b4626622af00c3****` account group to the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: AttachAggregateConfigRuleToCompliancePackRequest
        @return: AttachAggregateConfigRuleToCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_aggregate_config_rule_to_compliance_pack_with_options(request, runtime)

    async def attach_aggregate_config_rule_to_compliance_pack_async(
        self,
        request: config_20200907_models.AttachAggregateConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.AttachAggregateConfigRuleToCompliancePackResponse:
        """
        @summary Adds one or more rules in an account group to a compliance package.
        
        @description The sample request in this topic shows you how to add the `cr-6cc4626622af00e7***` rule in the `ca-75b4626622af00c3****` account group to the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: AttachAggregateConfigRuleToCompliancePackRequest
        @return: AttachAggregateConfigRuleToCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_aggregate_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def attach_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.AttachConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.AttachConfigRuleToCompliancePackResponse:
        """
        @summary Adds one or more rules to a compliance package.
        
        @description This topic provides an example on how to add the `cr-6cc4626622af00e7***` rule to the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: AttachConfigRuleToCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachConfigRuleToCompliancePackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Adds one or more rules to a compliance package.
        
        @description This topic provides an example on how to add the `cr-6cc4626622af00e7***` rule to the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: AttachConfigRuleToCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachConfigRuleToCompliancePackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Adds one or more rules to a compliance package.
        
        @description This topic provides an example on how to add the `cr-6cc4626622af00e7***` rule to the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: AttachConfigRuleToCompliancePackRequest
        @return: AttachConfigRuleToCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_config_rule_to_compliance_pack_with_options(request, runtime)

    async def attach_config_rule_to_compliance_pack_async(
        self,
        request: config_20200907_models.AttachConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.AttachConfigRuleToCompliancePackResponse:
        """
        @summary Adds one or more rules to a compliance package.
        
        @description This topic provides an example on how to add the `cr-6cc4626622af00e7***` rule to the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: AttachConfigRuleToCompliancePackRequest
        @return: AttachConfigRuleToCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def copy_compliance_packs_with_options(
        self,
        request: config_20200907_models.CopyCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CopyCompliancePacksResponse:
        """
        @summary Replicates compliance packages.
        
        @param request: CopyCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyCompliancePacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.des_aggregator_ids):
            query['DesAggregatorIds'] = request.des_aggregator_ids
        if not UtilClient.is_unset(request.src_aggregator_id):
            query['SrcAggregatorId'] = request.src_aggregator_id
        if not UtilClient.is_unset(request.src_compliance_pack_ids):
            query['SrcCompliancePackIds'] = request.src_compliance_pack_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCompliancePacks',
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
            config_20200907_models.CopyCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.CopyCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CopyCompliancePacksResponse:
        """
        @summary Replicates compliance packages.
        
        @param request: CopyCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyCompliancePacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.des_aggregator_ids):
            query['DesAggregatorIds'] = request.des_aggregator_ids
        if not UtilClient.is_unset(request.src_aggregator_id):
            query['SrcAggregatorId'] = request.src_aggregator_id
        if not UtilClient.is_unset(request.src_compliance_pack_ids):
            query['SrcCompliancePackIds'] = request.src_compliance_pack_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCompliancePacks',
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
            config_20200907_models.CopyCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_compliance_packs(
        self,
        request: config_20200907_models.CopyCompliancePacksRequest,
    ) -> config_20200907_models.CopyCompliancePacksResponse:
        """
        @summary Replicates compliance packages.
        
        @param request: CopyCompliancePacksRequest
        @return: CopyCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_compliance_packs_with_options(request, runtime)

    async def copy_compliance_packs_async(
        self,
        request: config_20200907_models.CopyCompliancePacksRequest,
    ) -> config_20200907_models.CopyCompliancePacksResponse:
        """
        @summary Replicates compliance packages.
        
        @param request: CopyCompliancePacksRequest
        @return: CopyCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_compliance_packs_with_options_async(request, runtime)

    def copy_config_rules_with_options(
        self,
        request: config_20200907_models.CopyConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CopyConfigRulesResponse:
        """
        @summary Replicates rules.
        
        @param request: CopyConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.des_aggregator_ids):
            query['DesAggregatorIds'] = request.des_aggregator_ids
        if not UtilClient.is_unset(request.src_aggregator_id):
            query['SrcAggregatorId'] = request.src_aggregator_id
        if not UtilClient.is_unset(request.src_config_rule_ids):
            query['SrcConfigRuleIds'] = request.src_config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyConfigRules',
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
            config_20200907_models.CopyConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_config_rules_with_options_async(
        self,
        request: config_20200907_models.CopyConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CopyConfigRulesResponse:
        """
        @summary Replicates rules.
        
        @param request: CopyConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.des_aggregator_ids):
            query['DesAggregatorIds'] = request.des_aggregator_ids
        if not UtilClient.is_unset(request.src_aggregator_id):
            query['SrcAggregatorId'] = request.src_aggregator_id
        if not UtilClient.is_unset(request.src_config_rule_ids):
            query['SrcConfigRuleIds'] = request.src_config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyConfigRules',
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
            config_20200907_models.CopyConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_config_rules(
        self,
        request: config_20200907_models.CopyConfigRulesRequest,
    ) -> config_20200907_models.CopyConfigRulesResponse:
        """
        @summary Replicates rules.
        
        @param request: CopyConfigRulesRequest
        @return: CopyConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_config_rules_with_options(request, runtime)

    async def copy_config_rules_async(
        self,
        request: config_20200907_models.CopyConfigRulesRequest,
    ) -> config_20200907_models.CopyConfigRulesResponse:
        """
        @summary Replicates rules.
        
        @param request: CopyConfigRulesRequest
        @return: CopyConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_config_rules_with_options_async(request, runtime)

    def create_advanced_search_file_with_options(
        self,
        request: config_20200907_models.CreateAdvancedSearchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAdvancedSearchFileResponse:
        """
        @summary Creates a downloadable resource file for the current Alibaba Cloud account.
        
        @param request: CreateAdvancedSearchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdvancedSearchFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdvancedSearchFile',
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
            config_20200907_models.CreateAdvancedSearchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_advanced_search_file_with_options_async(
        self,
        request: config_20200907_models.CreateAdvancedSearchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAdvancedSearchFileResponse:
        """
        @summary Creates a downloadable resource file for the current Alibaba Cloud account.
        
        @param request: CreateAdvancedSearchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdvancedSearchFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdvancedSearchFile',
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
            config_20200907_models.CreateAdvancedSearchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_advanced_search_file(
        self,
        request: config_20200907_models.CreateAdvancedSearchFileRequest,
    ) -> config_20200907_models.CreateAdvancedSearchFileResponse:
        """
        @summary Creates a downloadable resource file for the current Alibaba Cloud account.
        
        @param request: CreateAdvancedSearchFileRequest
        @return: CreateAdvancedSearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_advanced_search_file_with_options(request, runtime)

    async def create_advanced_search_file_async(
        self,
        request: config_20200907_models.CreateAdvancedSearchFileRequest,
    ) -> config_20200907_models.CreateAdvancedSearchFileResponse:
        """
        @summary Creates a downloadable resource file for the current Alibaba Cloud account.
        
        @param request: CreateAdvancedSearchFileRequest
        @return: CreateAdvancedSearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_advanced_search_file_with_options_async(request, runtime)

    def create_aggregate_advanced_search_file_with_options(
        self,
        request: config_20200907_models.CreateAggregateAdvancedSearchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateAdvancedSearchFileResponse:
        """
        @summary Creates a downloadable resource file for an account group.
        
        @description This topic provides an example on how to create a downloadable resource file for an account group whose ID is `ca-edd3626622af00b3***`. The resource file includes all the ECS instances in the account group.
        
        @param request: CreateAggregateAdvancedSearchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateAdvancedSearchFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAggregateAdvancedSearchFile',
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
            config_20200907_models.CreateAggregateAdvancedSearchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_advanced_search_file_with_options_async(
        self,
        request: config_20200907_models.CreateAggregateAdvancedSearchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateAdvancedSearchFileResponse:
        """
        @summary Creates a downloadable resource file for an account group.
        
        @description This topic provides an example on how to create a downloadable resource file for an account group whose ID is `ca-edd3626622af00b3***`. The resource file includes all the ECS instances in the account group.
        
        @param request: CreateAggregateAdvancedSearchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateAdvancedSearchFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAggregateAdvancedSearchFile',
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
            config_20200907_models.CreateAggregateAdvancedSearchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_advanced_search_file(
        self,
        request: config_20200907_models.CreateAggregateAdvancedSearchFileRequest,
    ) -> config_20200907_models.CreateAggregateAdvancedSearchFileResponse:
        """
        @summary Creates a downloadable resource file for an account group.
        
        @description This topic provides an example on how to create a downloadable resource file for an account group whose ID is `ca-edd3626622af00b3***`. The resource file includes all the ECS instances in the account group.
        
        @param request: CreateAggregateAdvancedSearchFileRequest
        @return: CreateAggregateAdvancedSearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_advanced_search_file_with_options(request, runtime)

    async def create_aggregate_advanced_search_file_async(
        self,
        request: config_20200907_models.CreateAggregateAdvancedSearchFileRequest,
    ) -> config_20200907_models.CreateAggregateAdvancedSearchFileResponse:
        """
        @summary Creates a downloadable resource file for an account group.
        
        @description This topic provides an example on how to create a downloadable resource file for an account group whose ID is `ca-edd3626622af00b3***`. The resource file includes all the ECS instances in the account group.
        
        @param request: CreateAggregateAdvancedSearchFileRequest
        @return: CreateAggregateAdvancedSearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_advanced_search_file_with_options_async(request, runtime)

    def create_aggregate_compliance_pack_with_options(
        self,
        tmp_req: config_20200907_models.CreateAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateCompliancePackResponse:
        """
        @summary Creates a compliance package for an account group.
        
        @description This topic provides an example on how to create a compliance package for the account group `ca-f632626622af0079***` by using the compliance package template `ClassifiedProtectionPreCheck`.
        
        @param tmp_req: CreateAggregateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateCompliancePackResponse
        """
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
        if not UtilClient.is_unset(request.default_enable):
            body['DefaultEnable'] = request.default_enable
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        if not UtilClient.is_unset(request.template_content):
            body['TemplateContent'] = request.template_content
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Creates a compliance package for an account group.
        
        @description This topic provides an example on how to create a compliance package for the account group `ca-f632626622af0079***` by using the compliance package template `ClassifiedProtectionPreCheck`.
        
        @param tmp_req: CreateAggregateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateCompliancePackResponse
        """
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
        if not UtilClient.is_unset(request.default_enable):
            body['DefaultEnable'] = request.default_enable
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        if not UtilClient.is_unset(request.template_content):
            body['TemplateContent'] = request.template_content
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Creates a compliance package for an account group.
        
        @description This topic provides an example on how to create a compliance package for the account group `ca-f632626622af0079***` by using the compliance package template `ClassifiedProtectionPreCheck`.
        
        @param request: CreateAggregateCompliancePackRequest
        @return: CreateAggregateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_compliance_pack_with_options(request, runtime)

    async def create_aggregate_compliance_pack_async(
        self,
        request: config_20200907_models.CreateAggregateCompliancePackRequest,
    ) -> config_20200907_models.CreateAggregateCompliancePackResponse:
        """
        @summary Creates a compliance package for an account group.
        
        @description This topic provides an example on how to create a compliance package for the account group `ca-f632626622af0079***` by using the compliance package template `ClassifiedProtectionPreCheck`.
        
        @param request: CreateAggregateCompliancePackRequest
        @return: CreateAggregateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_compliance_pack_with_options_async(request, runtime)

    def create_aggregate_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.CreateAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateConfigDeliveryChannelResponse:
        """
        @summary Creates a delivery channel for an account group.
        
        @description In this example, a delivery channel is created for an account group. The ID of the account group is `ca-a4e5626622af0079***`. The type of the delivery channel is `OSS` and the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542****:new-bucket`. The result indicates that the delivery channel is created. The ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateAggregateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_channel_type):
            query['DeliveryChannelType'] = request.delivery_channel_type
        if not UtilClient.is_unset(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAggregateConfigDeliveryChannel',
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
            config_20200907_models.CreateAggregateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_config_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.CreateAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateConfigDeliveryChannelResponse:
        """
        @summary Creates a delivery channel for an account group.
        
        @description In this example, a delivery channel is created for an account group. The ID of the account group is `ca-a4e5626622af0079***`. The type of the delivery channel is `OSS` and the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542****:new-bucket`. The result indicates that the delivery channel is created. The ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateAggregateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_channel_type):
            query['DeliveryChannelType'] = request.delivery_channel_type
        if not UtilClient.is_unset(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAggregateConfigDeliveryChannel',
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
            config_20200907_models.CreateAggregateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_config_delivery_channel(
        self,
        request: config_20200907_models.CreateAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.CreateAggregateConfigDeliveryChannelResponse:
        """
        @summary Creates a delivery channel for an account group.
        
        @description In this example, a delivery channel is created for an account group. The ID of the account group is `ca-a4e5626622af0079***`. The type of the delivery channel is `OSS` and the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542****:new-bucket`. The result indicates that the delivery channel is created. The ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateAggregateConfigDeliveryChannelRequest
        @return: CreateAggregateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_config_delivery_channel_with_options(request, runtime)

    async def create_aggregate_config_delivery_channel_async(
        self,
        request: config_20200907_models.CreateAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.CreateAggregateConfigDeliveryChannelResponse:
        """
        @summary Creates a delivery channel for an account group.
        
        @description In this example, a delivery channel is created for an account group. The ID of the account group is `ca-a4e5626622af0079***`. The type of the delivery channel is `OSS` and the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542****:new-bucket`. The result indicates that the delivery channel is created. The ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateAggregateConfigDeliveryChannelRequest
        @return: CreateAggregateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def create_aggregate_config_rule_with_options(
        self,
        tmp_req: config_20200907_models.CreateAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateConfigRuleResponse:
        """
        @summary Creates a rule for an account group.
        
        @description ### Limits
        You can create up to 200 rules for each management account.
        ### Usage notes
        This topic provides an example on how to create a rule based on the required-tags managed rule in the `ca-a4e5626622af0079***` account group. The returned result shows that the rule is created and its ID is `cr-4e3d626622af0080****`.
        
        @param tmp_req: CreateAggregateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateConfigRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateAggregateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.account_ids_scope):
            body['AccountIdsScope'] = request.account_ids_scope
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
        if not UtilClient.is_unset(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not UtilClient.is_unset(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.folder_ids_scope):
            body['FolderIdsScope'] = request.folder_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not UtilClient.is_unset(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Creates a rule for an account group.
        
        @description ### Limits
        You can create up to 200 rules for each management account.
        ### Usage notes
        This topic provides an example on how to create a rule based on the required-tags managed rule in the `ca-a4e5626622af0079***` account group. The returned result shows that the rule is created and its ID is `cr-4e3d626622af0080****`.
        
        @param tmp_req: CreateAggregateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateConfigRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.CreateAggregateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.account_ids_scope):
            body['AccountIdsScope'] = request.account_ids_scope
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
        if not UtilClient.is_unset(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not UtilClient.is_unset(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.folder_ids_scope):
            body['FolderIdsScope'] = request.folder_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not UtilClient.is_unset(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Creates a rule for an account group.
        
        @description ### Limits
        You can create up to 200 rules for each management account.
        ### Usage notes
        This topic provides an example on how to create a rule based on the required-tags managed rule in the `ca-a4e5626622af0079***` account group. The returned result shows that the rule is created and its ID is `cr-4e3d626622af0080****`.
        
        @param request: CreateAggregateConfigRuleRequest
        @return: CreateAggregateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_config_rule_with_options(request, runtime)

    async def create_aggregate_config_rule_async(
        self,
        request: config_20200907_models.CreateAggregateConfigRuleRequest,
    ) -> config_20200907_models.CreateAggregateConfigRuleResponse:
        """
        @summary Creates a rule for an account group.
        
        @description ### Limits
        You can create up to 200 rules for each management account.
        ### Usage notes
        This topic provides an example on how to create a rule based on the required-tags managed rule in the `ca-a4e5626622af0079***` account group. The returned result shows that the rule is created and its ID is `cr-4e3d626622af0080****`.
        
        @param request: CreateAggregateConfigRuleRequest
        @return: CreateAggregateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_config_rule_with_options_async(request, runtime)

    def create_aggregate_remediation_with_options(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
        """
        @summary Creates a remediation template for a rule in an account group.
        
        @description This topic provides an example on how to create a remediation template for the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`. The returned result shows that a remediation template is created and the ID of the remediation template is `crr-909ba2d4716700eb****`.
        
        @param request: CreateAggregateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateRemediationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not UtilClient.is_unset(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggregateRemediation',
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
            config_20200907_models.CreateAggregateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aggregate_remediation_with_options_async(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
        """
        @summary Creates a remediation template for a rule in an account group.
        
        @description This topic provides an example on how to create a remediation template for the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`. The returned result shows that a remediation template is created and the ID of the remediation template is `crr-909ba2d4716700eb****`.
        
        @param request: CreateAggregateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregateRemediationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not UtilClient.is_unset(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggregateRemediation',
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
            config_20200907_models.CreateAggregateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aggregate_remediation(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
        """
        @summary Creates a remediation template for a rule in an account group.
        
        @description This topic provides an example on how to create a remediation template for the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`. The returned result shows that a remediation template is created and the ID of the remediation template is `crr-909ba2d4716700eb****`.
        
        @param request: CreateAggregateRemediationRequest
        @return: CreateAggregateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_remediation_with_options(request, runtime)

    async def create_aggregate_remediation_async(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
        """
        @summary Creates a remediation template for a rule in an account group.
        
        @description This topic provides an example on how to create a remediation template for the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`. The returned result shows that a remediation template is created and the ID of the remediation template is `crr-909ba2d4716700eb****`.
        
        @param request: CreateAggregateRemediationRequest
        @return: CreateAggregateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_remediation_with_options_async(request, runtime)

    def create_aggregator_with_options(
        self,
        tmp_req: config_20200907_models.CreateAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregatorResponse:
        """
        @summary Creates an account group.
        
        @description Each management account can create a maximum of five account groups. Each account group can contain a maximum of 200 member accounts.
        Cloud Config supports the following types of account groups:
        Global account group: The global account group contains all the member accounts that are added to the resource directory. A management account can create only one global account group.
        Custom account group: If you create a custom account group, you must manually add all or specific member accounts from the resource directory to the custom account group.
        This topic provides an example on how to create an account group of the `CUSTOM` type. The custom account group is named `Test_Group`, and its description is `Test account group`. The custom account group contains the following two member accounts:
        Member account ID: `171322098523****`. Member account name: `Alice`.
        Member account ID: `100532098349****`. Member account name: `Tom`.
        
        @param tmp_req: CreateAggregatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregatorResponse
        """
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
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
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
        """
        @summary Creates an account group.
        
        @description Each management account can create a maximum of five account groups. Each account group can contain a maximum of 200 member accounts.
        Cloud Config supports the following types of account groups:
        Global account group: The global account group contains all the member accounts that are added to the resource directory. A management account can create only one global account group.
        Custom account group: If you create a custom account group, you must manually add all or specific member accounts from the resource directory to the custom account group.
        This topic provides an example on how to create an account group of the `CUSTOM` type. The custom account group is named `Test_Group`, and its description is `Test account group`. The custom account group contains the following two member accounts:
        Member account ID: `171322098523****`. Member account name: `Alice`.
        Member account ID: `100532098349****`. Member account name: `Tom`.
        
        @param tmp_req: CreateAggregatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggregatorResponse
        """
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
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
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
        """
        @summary Creates an account group.
        
        @description Each management account can create a maximum of five account groups. Each account group can contain a maximum of 200 member accounts.
        Cloud Config supports the following types of account groups:
        Global account group: The global account group contains all the member accounts that are added to the resource directory. A management account can create only one global account group.
        Custom account group: If you create a custom account group, you must manually add all or specific member accounts from the resource directory to the custom account group.
        This topic provides an example on how to create an account group of the `CUSTOM` type. The custom account group is named `Test_Group`, and its description is `Test account group`. The custom account group contains the following two member accounts:
        Member account ID: `171322098523****`. Member account name: `Alice`.
        Member account ID: `100532098349****`. Member account name: `Tom`.
        
        @param request: CreateAggregatorRequest
        @return: CreateAggregatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_aggregator_with_options(request, runtime)

    async def create_aggregator_async(
        self,
        request: config_20200907_models.CreateAggregatorRequest,
    ) -> config_20200907_models.CreateAggregatorResponse:
        """
        @summary Creates an account group.
        
        @description Each management account can create a maximum of five account groups. Each account group can contain a maximum of 200 member accounts.
        Cloud Config supports the following types of account groups:
        Global account group: The global account group contains all the member accounts that are added to the resource directory. A management account can create only one global account group.
        Custom account group: If you create a custom account group, you must manually add all or specific member accounts from the resource directory to the custom account group.
        This topic provides an example on how to create an account group of the `CUSTOM` type. The custom account group is named `Test_Group`, and its description is `Test account group`. The custom account group contains the following two member accounts:
        Member account ID: `171322098523****`. Member account name: `Alice`.
        Member account ID: `100532098349****`. Member account name: `Tom`.
        
        @param request: CreateAggregatorRequest
        @return: CreateAggregatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregator_with_options_async(request, runtime)

    def create_compliance_pack_with_options(
        self,
        tmp_req: config_20200907_models.CreateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateCompliancePackResponse:
        """
        @summary Creates a compliance package for the current account.
        
        @description Each ordinary account can create up to five compliance packages.
        This topic provides an example on how to create a compliance package named ClassifiedProtectionPreCheck. The compliance package contains a managed rule named `eip-bandwidth-limit`.
        
        @param tmp_req: CreateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCompliancePackResponse
        """
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
        if not UtilClient.is_unset(request.default_enable):
            body['DefaultEnable'] = request.default_enable
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        if not UtilClient.is_unset(request.template_content):
            body['TemplateContent'] = request.template_content
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Creates a compliance package for the current account.
        
        @description Each ordinary account can create up to five compliance packages.
        This topic provides an example on how to create a compliance package named ClassifiedProtectionPreCheck. The compliance package contains a managed rule named `eip-bandwidth-limit`.
        
        @param tmp_req: CreateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCompliancePackResponse
        """
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
        if not UtilClient.is_unset(request.default_enable):
            body['DefaultEnable'] = request.default_enable
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        if not UtilClient.is_unset(request.template_content):
            body['TemplateContent'] = request.template_content
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Creates a compliance package for the current account.
        
        @description Each ordinary account can create up to five compliance packages.
        This topic provides an example on how to create a compliance package named ClassifiedProtectionPreCheck. The compliance package contains a managed rule named `eip-bandwidth-limit`.
        
        @param request: CreateCompliancePackRequest
        @return: CreateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_compliance_pack_with_options(request, runtime)

    async def create_compliance_pack_async(
        self,
        request: config_20200907_models.CreateCompliancePackRequest,
    ) -> config_20200907_models.CreateCompliancePackResponse:
        """
        @summary Creates a compliance package for the current account.
        
        @description Each ordinary account can create up to five compliance packages.
        This topic provides an example on how to create a compliance package named ClassifiedProtectionPreCheck. The compliance package contains a managed rule named `eip-bandwidth-limit`.
        
        @param request: CreateCompliancePackRequest
        @return: CreateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_compliance_pack_with_options_async(request, runtime)

    def create_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.CreateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateConfigDeliveryChannelResponse:
        """
        @summary Creates a delivery channel.
        
        @description In this example, a delivery channel is created. The type of the delivery channel is `OSS` and the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542***:new-bucket`. The result indicates that the delivery channel is created, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_channel_type):
            query['DeliveryChannelType'] = request.delivery_channel_type
        if not UtilClient.is_unset(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConfigDeliveryChannel',
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
            config_20200907_models.CreateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.CreateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateConfigDeliveryChannelResponse:
        """
        @summary Creates a delivery channel.
        
        @description In this example, a delivery channel is created. The type of the delivery channel is `OSS` and the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542***:new-bucket`. The result indicates that the delivery channel is created, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_channel_type):
            query['DeliveryChannelType'] = request.delivery_channel_type
        if not UtilClient.is_unset(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConfigDeliveryChannel',
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
            config_20200907_models.CreateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_delivery_channel(
        self,
        request: config_20200907_models.CreateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.CreateConfigDeliveryChannelResponse:
        """
        @summary Creates a delivery channel.
        
        @description In this example, a delivery channel is created. The type of the delivery channel is `OSS` and the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542***:new-bucket`. The result indicates that the delivery channel is created, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateConfigDeliveryChannelRequest
        @return: CreateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_config_delivery_channel_with_options(request, runtime)

    async def create_config_delivery_channel_async(
        self,
        request: config_20200907_models.CreateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.CreateConfigDeliveryChannelResponse:
        """
        @summary Creates a delivery channel.
        
        @description In this example, a delivery channel is created. The type of the delivery channel is `OSS` and the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542***:new-bucket`. The result indicates that the delivery channel is created, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateConfigDeliveryChannelRequest
        @return: CreateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_config_delivery_channel_with_options_async(request, runtime)

    def create_config_rule_with_options(
        self,
        tmp_req: config_20200907_models.CreateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateConfigRuleResponse:
        """
        @summary Creates a rule for the current account.
        
        @description ## Limits
        You can use a common account to create up to 200 rules.
        
        @param tmp_req: CreateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigRuleResponse
        """
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
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not UtilClient.is_unset(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Creates a rule for the current account.
        
        @description ## Limits
        You can use a common account to create up to 200 rules.
        
        @param tmp_req: CreateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigRuleResponse
        """
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
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_identifier):
            body['SourceIdentifier'] = request.source_identifier
        if not UtilClient.is_unset(request.source_owner):
            body['SourceOwner'] = request.source_owner
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Creates a rule for the current account.
        
        @description ## Limits
        You can use a common account to create up to 200 rules.
        
        @param request: CreateConfigRuleRequest
        @return: CreateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_config_rule_with_options(request, runtime)

    async def create_config_rule_async(
        self,
        request: config_20200907_models.CreateConfigRuleRequest,
    ) -> config_20200907_models.CreateConfigRuleResponse:
        """
        @summary Creates a rule for the current account.
        
        @description ## Limits
        You can use a common account to create up to 200 rules.
        
        @param request: CreateConfigRuleRequest
        @return: CreateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_config_rule_with_options_async(request, runtime)

    def create_delivery_channel_with_options(
        self,
        request: config_20200907_models.CreateDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateDeliveryChannelResponse:
        """
        @deprecated OpenAPI CreateDeliveryChannel is deprecated, please use Config::2020-09-07::CreateConfigDeliveryChannel,Config::2020-09-07::CreateAggregateConfigDeliveryChannel instead.
        
        @summary Creates a delivery channel.
        
        @description In this example, a delivery channel is created. The type of the delivery channel is `OSS`, the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542***:new-bucket`, and the ARN of the role that is assigned to the delivery channel is `acs:ram::100931896542****:role/aliyunserviceroleforconfig`. The returned result shows that the delivery channel is created, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeliveryChannelResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            body['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            body['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_assume_role_arn):
            body['DeliveryChannelAssumeRoleArn'] = request.delivery_channel_assume_role_arn
        if not UtilClient.is_unset(request.delivery_channel_condition):
            body['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_name):
            body['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            body['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_channel_type):
            body['DeliveryChannelType'] = request.delivery_channel_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            body['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            body['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeliveryChannel',
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
            config_20200907_models.CreateDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.CreateDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateDeliveryChannelResponse:
        """
        @deprecated OpenAPI CreateDeliveryChannel is deprecated, please use Config::2020-09-07::CreateConfigDeliveryChannel,Config::2020-09-07::CreateAggregateConfigDeliveryChannel instead.
        
        @summary Creates a delivery channel.
        
        @description In this example, a delivery channel is created. The type of the delivery channel is `OSS`, the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542***:new-bucket`, and the ARN of the role that is assigned to the delivery channel is `acs:ram::100931896542****:role/aliyunserviceroleforconfig`. The returned result shows that the delivery channel is created, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeliveryChannelResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            body['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            body['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_assume_role_arn):
            body['DeliveryChannelAssumeRoleArn'] = request.delivery_channel_assume_role_arn
        if not UtilClient.is_unset(request.delivery_channel_condition):
            body['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_name):
            body['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            body['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_channel_type):
            body['DeliveryChannelType'] = request.delivery_channel_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            body['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            body['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeliveryChannel',
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
            config_20200907_models.CreateDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_delivery_channel(
        self,
        request: config_20200907_models.CreateDeliveryChannelRequest,
    ) -> config_20200907_models.CreateDeliveryChannelResponse:
        """
        @deprecated OpenAPI CreateDeliveryChannel is deprecated, please use Config::2020-09-07::CreateConfigDeliveryChannel,Config::2020-09-07::CreateAggregateConfigDeliveryChannel instead.
        
        @summary Creates a delivery channel.
        
        @description In this example, a delivery channel is created. The type of the delivery channel is `OSS`, the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542***:new-bucket`, and the ARN of the role that is assigned to the delivery channel is `acs:ram::100931896542****:role/aliyunserviceroleforconfig`. The returned result shows that the delivery channel is created, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateDeliveryChannelRequest
        @return: CreateDeliveryChannelResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_delivery_channel_with_options(request, runtime)

    async def create_delivery_channel_async(
        self,
        request: config_20200907_models.CreateDeliveryChannelRequest,
    ) -> config_20200907_models.CreateDeliveryChannelResponse:
        """
        @deprecated OpenAPI CreateDeliveryChannel is deprecated, please use Config::2020-09-07::CreateConfigDeliveryChannel,Config::2020-09-07::CreateAggregateConfigDeliveryChannel instead.
        
        @summary Creates a delivery channel.
        
        @description In this example, a delivery channel is created. The type of the delivery channel is `OSS`, the Alibaba Cloud Resource Name (ARN) of the delivery destination is `acs:oss:cn-shanghai:100931896542***:new-bucket`, and the ARN of the role that is assigned to the delivery channel is `acs:ram::100931896542****:role/aliyunserviceroleforconfig`. The returned result shows that the delivery channel is created, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`.
        
        @param request: CreateDeliveryChannelRequest
        @return: CreateDeliveryChannelResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_delivery_channel_with_options_async(request, runtime)

    def create_remediation_with_options(
        self,
        request: config_20200907_models.CreateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateRemediationResponse:
        """
        @summary Creates a remediation template for a rule.
        
        @description This topic provides an example on how to create a remediation template for the rule `cr-8a973ac2e2be00a2***`. The returned result shows that a remediation template is created and the ID of the remediation template is `crr-909ba2d4716700eb****`.
        
        @param request: CreateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRemediationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not UtilClient.is_unset(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRemediation',
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
            config_20200907_models.CreateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_remediation_with_options_async(
        self,
        request: config_20200907_models.CreateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateRemediationResponse:
        """
        @summary Creates a remediation template for a rule.
        
        @description This topic provides an example on how to create a remediation template for the rule `cr-8a973ac2e2be00a2***`. The returned result shows that a remediation template is created and the ID of the remediation template is `crr-909ba2d4716700eb****`.
        
        @param request: CreateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRemediationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not UtilClient.is_unset(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRemediation',
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
            config_20200907_models.CreateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_remediation(
        self,
        request: config_20200907_models.CreateRemediationRequest,
    ) -> config_20200907_models.CreateRemediationResponse:
        """
        @summary Creates a remediation template for a rule.
        
        @description This topic provides an example on how to create a remediation template for the rule `cr-8a973ac2e2be00a2***`. The returned result shows that a remediation template is created and the ID of the remediation template is `crr-909ba2d4716700eb****`.
        
        @param request: CreateRemediationRequest
        @return: CreateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_remediation_with_options(request, runtime)

    async def create_remediation_async(
        self,
        request: config_20200907_models.CreateRemediationRequest,
    ) -> config_20200907_models.CreateRemediationResponse:
        """
        @summary Creates a remediation template for a rule.
        
        @description This topic provides an example on how to create a remediation template for the rule `cr-8a973ac2e2be00a2***`. The returned result shows that a remediation template is created and the ID of the remediation template is `crr-909ba2d4716700eb****`.
        
        @param request: CreateRemediationRequest
        @return: CreateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_remediation_with_options_async(request, runtime)

    def deactive_aggregate_config_rules_with_options(
        self,
        request: config_20200907_models.DeactiveAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveAggregateConfigRulesResponse:
        """
        @summary Disables one or more rules in an account group. After a rule is disabled, the resource in the rule is no longer evaluated. The compliance evaluation results before the rule is disabled are still displayed.
        
        @description ### [](#)Prerequisites
        The status of the rule is `ACTIVE`.
        ### [](#)Description
        This topic provides an example on how to disable the `cr-5772ba41209e007b***` rule in the `ca-04b3fd170e340007****` account group.
        
        @param request: DeactiveAggregateConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeactiveAggregateConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Disables one or more rules in an account group. After a rule is disabled, the resource in the rule is no longer evaluated. The compliance evaluation results before the rule is disabled are still displayed.
        
        @description ### [](#)Prerequisites
        The status of the rule is `ACTIVE`.
        ### [](#)Description
        This topic provides an example on how to disable the `cr-5772ba41209e007b***` rule in the `ca-04b3fd170e340007****` account group.
        
        @param request: DeactiveAggregateConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeactiveAggregateConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Disables one or more rules in an account group. After a rule is disabled, the resource in the rule is no longer evaluated. The compliance evaluation results before the rule is disabled are still displayed.
        
        @description ### [](#)Prerequisites
        The status of the rule is `ACTIVE`.
        ### [](#)Description
        This topic provides an example on how to disable the `cr-5772ba41209e007b***` rule in the `ca-04b3fd170e340007****` account group.
        
        @param request: DeactiveAggregateConfigRulesRequest
        @return: DeactiveAggregateConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deactive_aggregate_config_rules_with_options(request, runtime)

    async def deactive_aggregate_config_rules_async(
        self,
        request: config_20200907_models.DeactiveAggregateConfigRulesRequest,
    ) -> config_20200907_models.DeactiveAggregateConfigRulesResponse:
        """
        @summary Disables one or more rules in an account group. After a rule is disabled, the resource in the rule is no longer evaluated. The compliance evaluation results before the rule is disabled are still displayed.
        
        @description ### [](#)Prerequisites
        The status of the rule is `ACTIVE`.
        ### [](#)Description
        This topic provides an example on how to disable the `cr-5772ba41209e007b***` rule in the `ca-04b3fd170e340007****` account group.
        
        @param request: DeactiveAggregateConfigRulesRequest
        @return: DeactiveAggregateConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deactive_aggregate_config_rules_with_options_async(request, runtime)

    def deactive_config_rules_with_options(
        self,
        request: config_20200907_models.DeactiveConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeactiveConfigRulesResponse:
        """
        @summary Disables a rule. After a rule is disabled, the resource in the rule is no longer evaluated. The compliance evaluation results before the rule is disabled are still displayed.
        
        @description ### [](#)Prerequisites
        The status of the rule is `ACTIVE`.
        ### [](#)Description
        This topic provides an example on how to disable the `cr-19a56457e0d90058***` rule.
        
        @param request: DeactiveConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeactiveConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Disables a rule. After a rule is disabled, the resource in the rule is no longer evaluated. The compliance evaluation results before the rule is disabled are still displayed.
        
        @description ### [](#)Prerequisites
        The status of the rule is `ACTIVE`.
        ### [](#)Description
        This topic provides an example on how to disable the `cr-19a56457e0d90058***` rule.
        
        @param request: DeactiveConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeactiveConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Disables a rule. After a rule is disabled, the resource in the rule is no longer evaluated. The compliance evaluation results before the rule is disabled are still displayed.
        
        @description ### [](#)Prerequisites
        The status of the rule is `ACTIVE`.
        ### [](#)Description
        This topic provides an example on how to disable the `cr-19a56457e0d90058***` rule.
        
        @param request: DeactiveConfigRulesRequest
        @return: DeactiveConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deactive_config_rules_with_options(request, runtime)

    async def deactive_config_rules_async(
        self,
        request: config_20200907_models.DeactiveConfigRulesRequest,
    ) -> config_20200907_models.DeactiveConfigRulesResponse:
        """
        @summary Disables a rule. After a rule is disabled, the resource in the rule is no longer evaluated. The compliance evaluation results before the rule is disabled are still displayed.
        
        @description ### [](#)Prerequisites
        The status of the rule is `ACTIVE`.
        ### [](#)Description
        This topic provides an example on how to disable the `cr-19a56457e0d90058***` rule.
        
        @param request: DeactiveConfigRulesRequest
        @return: DeactiveConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deactive_config_rules_with_options_async(request, runtime)

    def delete_aggregate_compliance_packs_with_options(
        self,
        request: config_20200907_models.DeleteAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateCompliancePacksResponse:
        """
        @summary Deletes the compliance packages of an account group.
        
        @description This topic provides an example on how to delete the `cp-541e626622af0087***` compliance package from the `ca-04b3fd170e340007****` account group.
        
        @param request: DeleteAggregateCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregateCompliancePacksResponse
        """
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
        """
        @summary Deletes the compliance packages of an account group.
        
        @description This topic provides an example on how to delete the `cp-541e626622af0087***` compliance package from the `ca-04b3fd170e340007****` account group.
        
        @param request: DeleteAggregateCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregateCompliancePacksResponse
        """
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
        """
        @summary Deletes the compliance packages of an account group.
        
        @description This topic provides an example on how to delete the `cp-541e626622af0087***` compliance package from the `ca-04b3fd170e340007****` account group.
        
        @param request: DeleteAggregateCompliancePacksRequest
        @return: DeleteAggregateCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregate_compliance_packs_with_options(request, runtime)

    async def delete_aggregate_compliance_packs_async(
        self,
        request: config_20200907_models.DeleteAggregateCompliancePacksRequest,
    ) -> config_20200907_models.DeleteAggregateCompliancePacksResponse:
        """
        @summary Deletes the compliance packages of an account group.
        
        @description This topic provides an example on how to delete the `cp-541e626622af0087***` compliance package from the `ca-04b3fd170e340007****` account group.
        
        @param request: DeleteAggregateCompliancePacksRequest
        @return: DeleteAggregateCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregate_compliance_packs_with_options_async(request, runtime)

    def delete_aggregate_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.DeleteAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateConfigDeliveryChannelResponse:
        """
        @summary Deletes a delivery channel from an account group.
        
        @description This topic provides an example on how to delete the `cdc-38c3013b46c9002c***` delivery channel from the `ca-23c6626622af0041****` account group. The returned result shows that the `cdc-38c3013b46c9002c****` delivery channel is deleted.
        
        @param request: DeleteAggregateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAggregateConfigDeliveryChannel',
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
            config_20200907_models.DeleteAggregateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregate_config_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateConfigDeliveryChannelResponse:
        """
        @summary Deletes a delivery channel from an account group.
        
        @description This topic provides an example on how to delete the `cdc-38c3013b46c9002c***` delivery channel from the `ca-23c6626622af0041****` account group. The returned result shows that the `cdc-38c3013b46c9002c****` delivery channel is deleted.
        
        @param request: DeleteAggregateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAggregateConfigDeliveryChannel',
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
            config_20200907_models.DeleteAggregateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregate_config_delivery_channel(
        self,
        request: config_20200907_models.DeleteAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.DeleteAggregateConfigDeliveryChannelResponse:
        """
        @summary Deletes a delivery channel from an account group.
        
        @description This topic provides an example on how to delete the `cdc-38c3013b46c9002c***` delivery channel from the `ca-23c6626622af0041****` account group. The returned result shows that the `cdc-38c3013b46c9002c****` delivery channel is deleted.
        
        @param request: DeleteAggregateConfigDeliveryChannelRequest
        @return: DeleteAggregateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregate_config_delivery_channel_with_options(request, runtime)

    async def delete_aggregate_config_delivery_channel_async(
        self,
        request: config_20200907_models.DeleteAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.DeleteAggregateConfigDeliveryChannelResponse:
        """
        @summary Deletes a delivery channel from an account group.
        
        @description This topic provides an example on how to delete the `cdc-38c3013b46c9002c***` delivery channel from the `ca-23c6626622af0041****` account group. The returned result shows that the `cdc-38c3013b46c9002c****` delivery channel is deleted.
        
        @param request: DeleteAggregateConfigDeliveryChannelRequest
        @return: DeleteAggregateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def delete_aggregate_config_rules_with_options(
        self,
        request: config_20200907_models.DeleteAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateConfigRulesResponse:
        """
        @summary Deletes one or more rules from an account group. You can delete a rule in the Cloud Config console. After you delete the rule, the configurations of the rule are deleted.
        
        @description This topic provides an example on how to delete the `cr-4e3d626622af0080***` rule from the `ca-a4e5626622af0079****` account group.
        
        @param request: DeleteAggregateConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregateConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Deletes one or more rules from an account group. You can delete a rule in the Cloud Config console. After you delete the rule, the configurations of the rule are deleted.
        
        @description This topic provides an example on how to delete the `cr-4e3d626622af0080***` rule from the `ca-a4e5626622af0079****` account group.
        
        @param request: DeleteAggregateConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregateConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Deletes one or more rules from an account group. You can delete a rule in the Cloud Config console. After you delete the rule, the configurations of the rule are deleted.
        
        @description This topic provides an example on how to delete the `cr-4e3d626622af0080***` rule from the `ca-a4e5626622af0079****` account group.
        
        @param request: DeleteAggregateConfigRulesRequest
        @return: DeleteAggregateConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregate_config_rules_with_options(request, runtime)

    async def delete_aggregate_config_rules_async(
        self,
        request: config_20200907_models.DeleteAggregateConfigRulesRequest,
    ) -> config_20200907_models.DeleteAggregateConfigRulesResponse:
        """
        @summary Deletes one or more rules from an account group. You can delete a rule in the Cloud Config console. After you delete the rule, the configurations of the rule are deleted.
        
        @description This topic provides an example on how to delete the `cr-4e3d626622af0080***` rule from the `ca-a4e5626622af0079****` account group.
        
        @param request: DeleteAggregateConfigRulesRequest
        @return: DeleteAggregateConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregate_config_rules_with_options_async(request, runtime)

    def delete_aggregate_remediations_with_options(
        self,
        request: config_20200907_models.DeleteAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateRemediationsResponse:
        """
        @summary Deletes one or more remediation templates from a rule in an account group.
        
        @description This topic provides an example on how to delete the remediation template whose ID is `crr-909ba2d4716700eb***` from the account group whose ID is `ca-6b4a626622af0012****`. The returned result shows that the remediation template whose ID is `crr-909ba2d4716700eb****` is deleted.
        
        @param request: DeleteAggregateRemediationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregateRemediationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.remediation_ids):
            body['RemediationIds'] = request.remediation_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAggregateRemediations',
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
            config_20200907_models.DeleteAggregateRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aggregate_remediations_with_options_async(
        self,
        request: config_20200907_models.DeleteAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregateRemediationsResponse:
        """
        @summary Deletes one or more remediation templates from a rule in an account group.
        
        @description This topic provides an example on how to delete the remediation template whose ID is `crr-909ba2d4716700eb***` from the account group whose ID is `ca-6b4a626622af0012****`. The returned result shows that the remediation template whose ID is `crr-909ba2d4716700eb****` is deleted.
        
        @param request: DeleteAggregateRemediationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregateRemediationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.remediation_ids):
            body['RemediationIds'] = request.remediation_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAggregateRemediations',
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
            config_20200907_models.DeleteAggregateRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aggregate_remediations(
        self,
        request: config_20200907_models.DeleteAggregateRemediationsRequest,
    ) -> config_20200907_models.DeleteAggregateRemediationsResponse:
        """
        @summary Deletes one or more remediation templates from a rule in an account group.
        
        @description This topic provides an example on how to delete the remediation template whose ID is `crr-909ba2d4716700eb***` from the account group whose ID is `ca-6b4a626622af0012****`. The returned result shows that the remediation template whose ID is `crr-909ba2d4716700eb****` is deleted.
        
        @param request: DeleteAggregateRemediationsRequest
        @return: DeleteAggregateRemediationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregate_remediations_with_options(request, runtime)

    async def delete_aggregate_remediations_async(
        self,
        request: config_20200907_models.DeleteAggregateRemediationsRequest,
    ) -> config_20200907_models.DeleteAggregateRemediationsResponse:
        """
        @summary Deletes one or more remediation templates from a rule in an account group.
        
        @description This topic provides an example on how to delete the remediation template whose ID is `crr-909ba2d4716700eb***` from the account group whose ID is `ca-6b4a626622af0012****`. The returned result shows that the remediation template whose ID is `crr-909ba2d4716700eb****` is deleted.
        
        @param request: DeleteAggregateRemediationsRequest
        @return: DeleteAggregateRemediationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregate_remediations_with_options_async(request, runtime)

    def delete_aggregators_with_options(
        self,
        request: config_20200907_models.DeleteAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteAggregatorsResponse:
        """
        @summary The management account or delegated administrator account of a resource directory can delete an account group.
        
        @description ### [](#)Background information
        After you delete an account group, the following changes occur to Cloud Config:
        The rules and compliance packages of the account group are deleted and cannot be recovered.
        All compliance results generated in the account group are automatically deleted and cannot be recovered.
        Service-linked roles for Cloud Config of member accounts in the account group are retained.
        If the account groups to which a member belongs are all deleted, the member account uses Cloud Config as an independent Alibaba Cloud account.
        ### [](#)Description
        This topic provides an example on how to delete the account group whose ID is `ca-9190626622af00a9***`.
        
        @param request: DeleteAggregatorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregatorsResponse
        """
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
        """
        @summary The management account or delegated administrator account of a resource directory can delete an account group.
        
        @description ### [](#)Background information
        After you delete an account group, the following changes occur to Cloud Config:
        The rules and compliance packages of the account group are deleted and cannot be recovered.
        All compliance results generated in the account group are automatically deleted and cannot be recovered.
        Service-linked roles for Cloud Config of member accounts in the account group are retained.
        If the account groups to which a member belongs are all deleted, the member account uses Cloud Config as an independent Alibaba Cloud account.
        ### [](#)Description
        This topic provides an example on how to delete the account group whose ID is `ca-9190626622af00a9***`.
        
        @param request: DeleteAggregatorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggregatorsResponse
        """
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
        """
        @summary The management account or delegated administrator account of a resource directory can delete an account group.
        
        @description ### [](#)Background information
        After you delete an account group, the following changes occur to Cloud Config:
        The rules and compliance packages of the account group are deleted and cannot be recovered.
        All compliance results generated in the account group are automatically deleted and cannot be recovered.
        Service-linked roles for Cloud Config of member accounts in the account group are retained.
        If the account groups to which a member belongs are all deleted, the member account uses Cloud Config as an independent Alibaba Cloud account.
        ### [](#)Description
        This topic provides an example on how to delete the account group whose ID is `ca-9190626622af00a9***`.
        
        @param request: DeleteAggregatorsRequest
        @return: DeleteAggregatorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aggregators_with_options(request, runtime)

    async def delete_aggregators_async(
        self,
        request: config_20200907_models.DeleteAggregatorsRequest,
    ) -> config_20200907_models.DeleteAggregatorsResponse:
        """
        @summary The management account or delegated administrator account of a resource directory can delete an account group.
        
        @description ### [](#)Background information
        After you delete an account group, the following changes occur to Cloud Config:
        The rules and compliance packages of the account group are deleted and cannot be recovered.
        All compliance results generated in the account group are automatically deleted and cannot be recovered.
        Service-linked roles for Cloud Config of member accounts in the account group are retained.
        If the account groups to which a member belongs are all deleted, the member account uses Cloud Config as an independent Alibaba Cloud account.
        ### [](#)Description
        This topic provides an example on how to delete the account group whose ID is `ca-9190626622af00a9***`.
        
        @param request: DeleteAggregatorsRequest
        @return: DeleteAggregatorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_aggregators_with_options_async(request, runtime)

    def delete_compliance_packs_with_options(
        self,
        request: config_20200907_models.DeleteCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteCompliancePacksResponse:
        """
        @summary Deletes one or more compliance packages.
        
        @description This topic provides an example on how to delete the `cp-541e626622af0087***` compliance package.
        
        @param request: DeleteCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCompliancePacksResponse
        """
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
        """
        @summary Deletes one or more compliance packages.
        
        @description This topic provides an example on how to delete the `cp-541e626622af0087***` compliance package.
        
        @param request: DeleteCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCompliancePacksResponse
        """
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
        """
        @summary Deletes one or more compliance packages.
        
        @description This topic provides an example on how to delete the `cp-541e626622af0087***` compliance package.
        
        @param request: DeleteCompliancePacksRequest
        @return: DeleteCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_compliance_packs_with_options(request, runtime)

    async def delete_compliance_packs_async(
        self,
        request: config_20200907_models.DeleteCompliancePacksRequest,
    ) -> config_20200907_models.DeleteCompliancePacksResponse:
        """
        @summary Deletes one or more compliance packages.
        
        @description This topic provides an example on how to delete the `cp-541e626622af0087***` compliance package.
        
        @param request: DeleteCompliancePacksRequest
        @return: DeleteCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_compliance_packs_with_options_async(request, runtime)

    def delete_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.DeleteConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteConfigDeliveryChannelResponse:
        """
        @summary Deletes a delivery channel.
        
        @description This topic provides an example on how to delete the `cdc-38c3013b46c9002c***` delivery channel. The returned result shows that the `cdc-38c3013b46c9002c****` delivery channel is deleted.
        
        @param request: DeleteConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigDeliveryChannel',
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
            config_20200907_models.DeleteConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.DeleteConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteConfigDeliveryChannelResponse:
        """
        @summary Deletes a delivery channel.
        
        @description This topic provides an example on how to delete the `cdc-38c3013b46c9002c***` delivery channel. The returned result shows that the `cdc-38c3013b46c9002c****` delivery channel is deleted.
        
        @param request: DeleteConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigDeliveryChannel',
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
            config_20200907_models.DeleteConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_delivery_channel(
        self,
        request: config_20200907_models.DeleteConfigDeliveryChannelRequest,
    ) -> config_20200907_models.DeleteConfigDeliveryChannelResponse:
        """
        @summary Deletes a delivery channel.
        
        @description This topic provides an example on how to delete the `cdc-38c3013b46c9002c***` delivery channel. The returned result shows that the `cdc-38c3013b46c9002c****` delivery channel is deleted.
        
        @param request: DeleteConfigDeliveryChannelRequest
        @return: DeleteConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_config_delivery_channel_with_options(request, runtime)

    async def delete_config_delivery_channel_async(
        self,
        request: config_20200907_models.DeleteConfigDeliveryChannelRequest,
    ) -> config_20200907_models.DeleteConfigDeliveryChannelResponse:
        """
        @summary Deletes a delivery channel.
        
        @description This topic provides an example on how to delete the `cdc-38c3013b46c9002c***` delivery channel. The returned result shows that the `cdc-38c3013b46c9002c****` delivery channel is deleted.
        
        @param request: DeleteConfigDeliveryChannelRequest
        @return: DeleteConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_config_delivery_channel_with_options_async(request, runtime)

    def delete_config_rules_with_options(
        self,
        request: config_20200907_models.DeleteConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteConfigRulesResponse:
        """
        @summary Deletes rules.
        
        @description In this example, the rule whose ID is cr-9908626622af0035\\\\*\\*\\* is deleted.
        
        @param request: DeleteConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigRules',
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
            config_20200907_models.DeleteConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_rules_with_options_async(
        self,
        request: config_20200907_models.DeleteConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteConfigRulesResponse:
        """
        @summary Deletes rules.
        
        @description In this example, the rule whose ID is cr-9908626622af0035\\\\*\\*\\* is deleted.
        
        @param request: DeleteConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigRules',
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
            config_20200907_models.DeleteConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_rules(
        self,
        request: config_20200907_models.DeleteConfigRulesRequest,
    ) -> config_20200907_models.DeleteConfigRulesResponse:
        """
        @summary Deletes rules.
        
        @description In this example, the rule whose ID is cr-9908626622af0035\\\\*\\*\\* is deleted.
        
        @param request: DeleteConfigRulesRequest
        @return: DeleteConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_config_rules_with_options(request, runtime)

    async def delete_config_rules_async(
        self,
        request: config_20200907_models.DeleteConfigRulesRequest,
    ) -> config_20200907_models.DeleteConfigRulesResponse:
        """
        @summary Deletes rules.
        
        @description In this example, the rule whose ID is cr-9908626622af0035\\\\*\\*\\* is deleted.
        
        @param request: DeleteConfigRulesRequest
        @return: DeleteConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_config_rules_with_options_async(request, runtime)

    def delete_remediations_with_options(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        """
        @summary Deletes one or more configured remediation templates that are associated with a rule.
        
        @description This topic provides an example on how to delete the remediation template `crr-909ba2d4716700eb***`. The returned result shows that the remediation template whose ID is `crr-909ba2d4716700eb****` is deleted.
        
        @param request: DeleteRemediationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRemediationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.remediation_ids):
            body['RemediationIds'] = request.remediation_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRemediations',
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
            config_20200907_models.DeleteRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_remediations_with_options_async(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        """
        @summary Deletes one or more configured remediation templates that are associated with a rule.
        
        @description This topic provides an example on how to delete the remediation template `crr-909ba2d4716700eb***`. The returned result shows that the remediation template whose ID is `crr-909ba2d4716700eb****` is deleted.
        
        @param request: DeleteRemediationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRemediationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.remediation_ids):
            body['RemediationIds'] = request.remediation_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRemediations',
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
            config_20200907_models.DeleteRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_remediations(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        """
        @summary Deletes one or more configured remediation templates that are associated with a rule.
        
        @description This topic provides an example on how to delete the remediation template `crr-909ba2d4716700eb***`. The returned result shows that the remediation template whose ID is `crr-909ba2d4716700eb****` is deleted.
        
        @param request: DeleteRemediationsRequest
        @return: DeleteRemediationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_remediations_with_options(request, runtime)

    async def delete_remediations_async(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        """
        @summary Deletes one or more configured remediation templates that are associated with a rule.
        
        @description This topic provides an example on how to delete the remediation template `crr-909ba2d4716700eb***`. The returned result shows that the remediation template whose ID is `crr-909ba2d4716700eb****` is deleted.
        
        @param request: DeleteRemediationsRequest
        @return: DeleteRemediationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_remediations_with_options_async(request, runtime)

    def describe_remediation_with_options(
        self,
        request: config_20200907_models.DescribeRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DescribeRemediationResponse:
        """
        @summary This topic provides an example on how to query the details of a remediation configuration whose ID is crr-f381cf0c1c2f004e\\\\*\\*\\*.
        
        @param request: DescribeRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRemediationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRemediation',
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
            config_20200907_models.DescribeRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_remediation_with_options_async(
        self,
        request: config_20200907_models.DescribeRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DescribeRemediationResponse:
        """
        @summary This topic provides an example on how to query the details of a remediation configuration whose ID is crr-f381cf0c1c2f004e\\\\*\\*\\*.
        
        @param request: DescribeRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRemediationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRemediation',
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
            config_20200907_models.DescribeRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_remediation(
        self,
        request: config_20200907_models.DescribeRemediationRequest,
    ) -> config_20200907_models.DescribeRemediationResponse:
        """
        @summary This topic provides an example on how to query the details of a remediation configuration whose ID is crr-f381cf0c1c2f004e\\\\*\\*\\*.
        
        @param request: DescribeRemediationRequest
        @return: DescribeRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_remediation_with_options(request, runtime)

    async def describe_remediation_async(
        self,
        request: config_20200907_models.DescribeRemediationRequest,
    ) -> config_20200907_models.DescribeRemediationResponse:
        """
        @summary This topic provides an example on how to query the details of a remediation configuration whose ID is crr-f381cf0c1c2f004e\\\\*\\*\\*.
        
        @param request: DescribeRemediationRequest
        @return: DescribeRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_remediation_with_options_async(request, runtime)

    def detach_aggregate_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.DetachAggregateConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse:
        """
        @summary Removes one or more rules in an account group from a compliance package.
        
        @description ### Prerequisites
        One or more rules are added to a compliance package.
        ### Usage notes
        The sample request in this topic shows you how to remove the `cr-6cc4626622af00e7***` rule in the `ca-75b4626622af00c3****` account group from the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: DetachAggregateConfigRuleToCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachAggregateConfigRuleToCompliancePackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Removes one or more rules in an account group from a compliance package.
        
        @description ### Prerequisites
        One or more rules are added to a compliance package.
        ### Usage notes
        The sample request in this topic shows you how to remove the `cr-6cc4626622af00e7***` rule in the `ca-75b4626622af00c3****` account group from the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: DetachAggregateConfigRuleToCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachAggregateConfigRuleToCompliancePackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Removes one or more rules in an account group from a compliance package.
        
        @description ### Prerequisites
        One or more rules are added to a compliance package.
        ### Usage notes
        The sample request in this topic shows you how to remove the `cr-6cc4626622af00e7***` rule in the `ca-75b4626622af00c3****` account group from the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: DetachAggregateConfigRuleToCompliancePackRequest
        @return: DetachAggregateConfigRuleToCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_aggregate_config_rule_to_compliance_pack_with_options(request, runtime)

    async def detach_aggregate_config_rule_to_compliance_pack_async(
        self,
        request: config_20200907_models.DetachAggregateConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse:
        """
        @summary Removes one or more rules in an account group from a compliance package.
        
        @description ### Prerequisites
        One or more rules are added to a compliance package.
        ### Usage notes
        The sample request in this topic shows you how to remove the `cr-6cc4626622af00e7***` rule in the `ca-75b4626622af00c3****` account group from the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: DetachAggregateConfigRuleToCompliancePackRequest
        @return: DetachAggregateConfigRuleToCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_aggregate_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def detach_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.DetachConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DetachConfigRuleToCompliancePackResponse:
        """
        @summary Removes one or more rules from a compliance package.
        
        @description ### Prerequisites
        One or more rules are added to a compliance package.
        ### Usage notes
        This topic provides an example on how to remove the `cr-6cc4626622af00e7***` rule from the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: DetachConfigRuleToCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachConfigRuleToCompliancePackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Removes one or more rules from a compliance package.
        
        @description ### Prerequisites
        One or more rules are added to a compliance package.
        ### Usage notes
        This topic provides an example on how to remove the `cr-6cc4626622af00e7***` rule from the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: DetachConfigRuleToCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachConfigRuleToCompliancePackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_ids):
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
        """
        @summary Removes one or more rules from a compliance package.
        
        @description ### Prerequisites
        One or more rules are added to a compliance package.
        ### Usage notes
        This topic provides an example on how to remove the `cr-6cc4626622af00e7***` rule from the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: DetachConfigRuleToCompliancePackRequest
        @return: DetachConfigRuleToCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_config_rule_to_compliance_pack_with_options(request, runtime)

    async def detach_config_rule_to_compliance_pack_async(
        self,
        request: config_20200907_models.DetachConfigRuleToCompliancePackRequest,
    ) -> config_20200907_models.DetachConfigRuleToCompliancePackResponse:
        """
        @summary Removes one or more rules from a compliance package.
        
        @description ### Prerequisites
        One or more rules are added to a compliance package.
        ### Usage notes
        This topic provides an example on how to remove the `cr-6cc4626622af00e7***` rule from the `cp-5bb1626622af00bd****` compliance package.
        
        @param request: DetachConfigRuleToCompliancePackRequest
        @return: DetachConfigRuleToCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_config_rule_to_compliance_pack_with_options_async(request, runtime)

    def evaluate_pre_config_rules_with_options(
        self,
        tmp_req: config_20200907_models.EvaluatePreConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.EvaluatePreConfigRulesResponse:
        """
        @summary Executes evaluation rules to evaluate resources.
        
        @param tmp_req: EvaluatePreConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvaluatePreConfigRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.EvaluatePreConfigRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_evaluate_items):
            request.resource_evaluate_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_evaluate_items, 'ResourceEvaluateItems', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_managed_rules):
            body['EnableManagedRules'] = request.enable_managed_rules
        if not UtilClient.is_unset(request.resource_evaluate_items_shrink):
            body['ResourceEvaluateItems'] = request.resource_evaluate_items_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EvaluatePreConfigRules',
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
            config_20200907_models.EvaluatePreConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_pre_config_rules_with_options_async(
        self,
        tmp_req: config_20200907_models.EvaluatePreConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.EvaluatePreConfigRulesResponse:
        """
        @summary Executes evaluation rules to evaluate resources.
        
        @param tmp_req: EvaluatePreConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvaluatePreConfigRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.EvaluatePreConfigRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_evaluate_items):
            request.resource_evaluate_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_evaluate_items, 'ResourceEvaluateItems', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_managed_rules):
            body['EnableManagedRules'] = request.enable_managed_rules
        if not UtilClient.is_unset(request.resource_evaluate_items_shrink):
            body['ResourceEvaluateItems'] = request.resource_evaluate_items_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EvaluatePreConfigRules',
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
            config_20200907_models.EvaluatePreConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_pre_config_rules(
        self,
        request: config_20200907_models.EvaluatePreConfigRulesRequest,
    ) -> config_20200907_models.EvaluatePreConfigRulesResponse:
        """
        @summary Executes evaluation rules to evaluate resources.
        
        @param request: EvaluatePreConfigRulesRequest
        @return: EvaluatePreConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.evaluate_pre_config_rules_with_options(request, runtime)

    async def evaluate_pre_config_rules_async(
        self,
        request: config_20200907_models.EvaluatePreConfigRulesRequest,
    ) -> config_20200907_models.EvaluatePreConfigRulesResponse:
        """
        @summary Executes evaluation rules to evaluate resources.
        
        @param request: EvaluatePreConfigRulesRequest
        @return: EvaluatePreConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.evaluate_pre_config_rules_with_options_async(request, runtime)

    def generate_aggregate_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GenerateAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateCompliancePackReportResponse:
        """
        @summary Generates a compliance evaluation report based on a compliance package in an account group.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetAggregateConfigRulesReport operation. For more information, see [GetAggregateCompliancePackReport](https://help.aliyun.com/document_detail/262699.html).
        This topic provides an example on how to generate a compliance evaluation report based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****` account group.
        
        @param request: GenerateAggregateCompliancePackReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAggregateCompliancePackReportResponse
        """
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
        """
        @summary Generates a compliance evaluation report based on a compliance package in an account group.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetAggregateConfigRulesReport operation. For more information, see [GetAggregateCompliancePackReport](https://help.aliyun.com/document_detail/262699.html).
        This topic provides an example on how to generate a compliance evaluation report based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****` account group.
        
        @param request: GenerateAggregateCompliancePackReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAggregateCompliancePackReportResponse
        """
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
        """
        @summary Generates a compliance evaluation report based on a compliance package in an account group.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetAggregateConfigRulesReport operation. For more information, see [GetAggregateCompliancePackReport](https://help.aliyun.com/document_detail/262699.html).
        This topic provides an example on how to generate a compliance evaluation report based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****` account group.
        
        @param request: GenerateAggregateCompliancePackReportRequest
        @return: GenerateAggregateCompliancePackReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_aggregate_compliance_pack_report_with_options(request, runtime)

    async def generate_aggregate_compliance_pack_report_async(
        self,
        request: config_20200907_models.GenerateAggregateCompliancePackReportRequest,
    ) -> config_20200907_models.GenerateAggregateCompliancePackReportResponse:
        """
        @summary Generates a compliance evaluation report based on a compliance package in an account group.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetAggregateConfigRulesReport operation. For more information, see [GetAggregateCompliancePackReport](https://help.aliyun.com/document_detail/262699.html).
        This topic provides an example on how to generate a compliance evaluation report based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****` account group.
        
        @param request: GenerateAggregateCompliancePackReportRequest
        @return: GenerateAggregateCompliancePackReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_aggregate_compliance_pack_report_with_options_async(request, runtime)

    def generate_aggregate_config_rules_report_with_options(
        self,
        request: config_20200907_models.GenerateAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateConfigRulesReportResponse:
        """
        @summary Generates a compliance evaluation report for the rules in a specified account group.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetAggregateConfigRulesReport operation. For more information, see [GetAggregateConfigRulesReport](https://help.aliyun.com/document_detail/262706.html).
        The topic provides an example on how to generate a compliance evaluation report based on all rules in the `ca-f632626622af0079***` account group.
        
        @param request: GenerateAggregateConfigRulesReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAggregateConfigRulesReportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_ids):
            body['ConfigRuleIds'] = request.config_rule_ids
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
        """
        @summary Generates a compliance evaluation report for the rules in a specified account group.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetAggregateConfigRulesReport operation. For more information, see [GetAggregateConfigRulesReport](https://help.aliyun.com/document_detail/262706.html).
        The topic provides an example on how to generate a compliance evaluation report based on all rules in the `ca-f632626622af0079***` account group.
        
        @param request: GenerateAggregateConfigRulesReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAggregateConfigRulesReportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_ids):
            body['ConfigRuleIds'] = request.config_rule_ids
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
        """
        @summary Generates a compliance evaluation report for the rules in a specified account group.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetAggregateConfigRulesReport operation. For more information, see [GetAggregateConfigRulesReport](https://help.aliyun.com/document_detail/262706.html).
        The topic provides an example on how to generate a compliance evaluation report based on all rules in the `ca-f632626622af0079***` account group.
        
        @param request: GenerateAggregateConfigRulesReportRequest
        @return: GenerateAggregateConfigRulesReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_aggregate_config_rules_report_with_options(request, runtime)

    async def generate_aggregate_config_rules_report_async(
        self,
        request: config_20200907_models.GenerateAggregateConfigRulesReportRequest,
    ) -> config_20200907_models.GenerateAggregateConfigRulesReportResponse:
        """
        @summary Generates a compliance evaluation report for the rules in a specified account group.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetAggregateConfigRulesReport operation. For more information, see [GetAggregateConfigRulesReport](https://help.aliyun.com/document_detail/262706.html).
        The topic provides an example on how to generate a compliance evaluation report based on all rules in the `ca-f632626622af0079***` account group.
        
        @param request: GenerateAggregateConfigRulesReportRequest
        @return: GenerateAggregateConfigRulesReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_aggregate_config_rules_report_with_options_async(request, runtime)

    def generate_aggregate_resource_inventory_with_options(
        self,
        request: config_20200907_models.GenerateAggregateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateResourceInventoryResponse:
        """
        @summary Generates a downloadable inventory for global resources in an account group.
        
        @description This topic provides an example to show how to generate a downloadable inventory for global resources in the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GenerateAggregateResourceInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAggregateResourceInventoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAggregateResourceInventory',
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
            config_20200907_models.GenerateAggregateResourceInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_aggregate_resource_inventory_with_options_async(
        self,
        request: config_20200907_models.GenerateAggregateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateAggregateResourceInventoryResponse:
        """
        @summary Generates a downloadable inventory for global resources in an account group.
        
        @description This topic provides an example to show how to generate a downloadable inventory for global resources in the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GenerateAggregateResourceInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAggregateResourceInventoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAggregateResourceInventory',
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
            config_20200907_models.GenerateAggregateResourceInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_aggregate_resource_inventory(
        self,
        request: config_20200907_models.GenerateAggregateResourceInventoryRequest,
    ) -> config_20200907_models.GenerateAggregateResourceInventoryResponse:
        """
        @summary Generates a downloadable inventory for global resources in an account group.
        
        @description This topic provides an example to show how to generate a downloadable inventory for global resources in the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GenerateAggregateResourceInventoryRequest
        @return: GenerateAggregateResourceInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_aggregate_resource_inventory_with_options(request, runtime)

    async def generate_aggregate_resource_inventory_async(
        self,
        request: config_20200907_models.GenerateAggregateResourceInventoryRequest,
    ) -> config_20200907_models.GenerateAggregateResourceInventoryResponse:
        """
        @summary Generates a downloadable inventory for global resources in an account group.
        
        @description This topic provides an example to show how to generate a downloadable inventory for global resources in the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GenerateAggregateResourceInventoryRequest
        @return: GenerateAggregateResourceInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_aggregate_resource_inventory_with_options_async(request, runtime)

    def generate_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GenerateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateCompliancePackReportResponse:
        """
        @summary Generates a compliance evaluation report based on a compliance package.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetCompliancePackReport operation. For more information, see [GetCompliancePackReport](https://help.aliyun.com/document_detail/263347.html).
        This topic provides an example on how to generate a compliance evaluation report based on the `cp-a8a8626622af0082***` compliance package.
        
        @param request: GenerateCompliancePackReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCompliancePackReportResponse
        """
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
        """
        @summary Generates a compliance evaluation report based on a compliance package.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetCompliancePackReport operation. For more information, see [GetCompliancePackReport](https://help.aliyun.com/document_detail/263347.html).
        This topic provides an example on how to generate a compliance evaluation report based on the `cp-a8a8626622af0082***` compliance package.
        
        @param request: GenerateCompliancePackReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCompliancePackReportResponse
        """
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
        """
        @summary Generates a compliance evaluation report based on a compliance package.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetCompliancePackReport operation. For more information, see [GetCompliancePackReport](https://help.aliyun.com/document_detail/263347.html).
        This topic provides an example on how to generate a compliance evaluation report based on the `cp-a8a8626622af0082***` compliance package.
        
        @param request: GenerateCompliancePackReportRequest
        @return: GenerateCompliancePackReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_compliance_pack_report_with_options(request, runtime)

    async def generate_compliance_pack_report_async(
        self,
        request: config_20200907_models.GenerateCompliancePackReportRequest,
    ) -> config_20200907_models.GenerateCompliancePackReportResponse:
        """
        @summary Generates a compliance evaluation report based on a compliance package.
        
        @description > You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetCompliancePackReport operation. For more information, see [GetCompliancePackReport](https://help.aliyun.com/document_detail/263347.html).
        This topic provides an example on how to generate a compliance evaluation report based on the `cp-a8a8626622af0082***` compliance package.
        
        @param request: GenerateCompliancePackReportRequest
        @return: GenerateCompliancePackReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_compliance_pack_report_with_options_async(request, runtime)

    def generate_config_rules_report_with_options(
        self,
        request: config_20200907_models.GenerateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateConfigRulesReportResponse:
        """
        @summary Generates a compliance evaluation report for a rule.
        
        @description >  You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetConfigRulesReport operation. For more information, see [GetConfigRulesReport](https://help.aliyun.com/document_detail/263608.html).
        This topic provides an example of how to generate a compliance evaluation report based on all existing rules.
        
        @param request: GenerateConfigRulesReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateConfigRulesReportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_ids):
            body['ConfigRuleIds'] = request.config_rule_ids
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
        """
        @summary Generates a compliance evaluation report for a rule.
        
        @description >  You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetConfigRulesReport operation. For more information, see [GetConfigRulesReport](https://help.aliyun.com/document_detail/263608.html).
        This topic provides an example of how to generate a compliance evaluation report based on all existing rules.
        
        @param request: GenerateConfigRulesReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateConfigRulesReportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_rule_ids):
            body['ConfigRuleIds'] = request.config_rule_ids
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
        """
        @summary Generates a compliance evaluation report for a rule.
        
        @description >  You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetConfigRulesReport operation. For more information, see [GetConfigRulesReport](https://help.aliyun.com/document_detail/263608.html).
        This topic provides an example of how to generate a compliance evaluation report based on all existing rules.
        
        @param request: GenerateConfigRulesReportRequest
        @return: GenerateConfigRulesReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_config_rules_report_with_options(request, runtime)

    async def generate_config_rules_report_async(
        self,
        request: config_20200907_models.GenerateConfigRulesReportRequest,
    ) -> config_20200907_models.GenerateConfigRulesReportResponse:
        """
        @summary Generates a compliance evaluation report for a rule.
        
        @description >  You can call this operation to generate the latest compliance evaluation report. To download the report, call the GetConfigRulesReport operation. For more information, see [GetConfigRulesReport](https://help.aliyun.com/document_detail/263608.html).
        This topic provides an example of how to generate a compliance evaluation report based on all existing rules.
        
        @param request: GenerateConfigRulesReportRequest
        @return: GenerateConfigRulesReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_config_rules_report_with_options_async(request, runtime)

    def generate_resource_inventory_with_options(
        self,
        request: config_20200907_models.GenerateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateResourceInventoryResponse:
        """
        @summary Generates a resource inventory for global resources.
        
        @description This topic provides an example on how to generate a resource inventory for global resources of the current account.
        
        @param request: GenerateResourceInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateResourceInventoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateResourceInventory',
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
            config_20200907_models.GenerateResourceInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_resource_inventory_with_options_async(
        self,
        request: config_20200907_models.GenerateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GenerateResourceInventoryResponse:
        """
        @summary Generates a resource inventory for global resources.
        
        @description This topic provides an example on how to generate a resource inventory for global resources of the current account.
        
        @param request: GenerateResourceInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateResourceInventoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateResourceInventory',
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
            config_20200907_models.GenerateResourceInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_resource_inventory(
        self,
        request: config_20200907_models.GenerateResourceInventoryRequest,
    ) -> config_20200907_models.GenerateResourceInventoryResponse:
        """
        @summary Generates a resource inventory for global resources.
        
        @description This topic provides an example on how to generate a resource inventory for global resources of the current account.
        
        @param request: GenerateResourceInventoryRequest
        @return: GenerateResourceInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_resource_inventory_with_options(request, runtime)

    async def generate_resource_inventory_async(
        self,
        request: config_20200907_models.GenerateResourceInventoryRequest,
    ) -> config_20200907_models.GenerateResourceInventoryResponse:
        """
        @summary Generates a resource inventory for global resources.
        
        @description This topic provides an example on how to generate a resource inventory for global resources of the current account.
        
        @param request: GenerateResourceInventoryRequest
        @return: GenerateResourceInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_resource_inventory_with_options_async(request, runtime)

    def get_advanced_search_file_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAdvancedSearchFileResponse:
        """
        @summary Obtains the last resource advanced search file that is generated within the current account. You can call this operation to obtain the URL of the resource advanced search file.
        
        @description ### [](#)Prerequisites
        You must call the [CreateAdvancedSearchFile](https://help.aliyun.com/document_detail/2511967.html) operation to create a resource advanced search file. Then, you can call this operation to obtain the URL of the resource advanced search file.
        
        @param request: GetAdvancedSearchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdvancedSearchFileResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAdvancedSearchFile',
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
            config_20200907_models.GetAdvancedSearchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_advanced_search_file_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAdvancedSearchFileResponse:
        """
        @summary Obtains the last resource advanced search file that is generated within the current account. You can call this operation to obtain the URL of the resource advanced search file.
        
        @description ### [](#)Prerequisites
        You must call the [CreateAdvancedSearchFile](https://help.aliyun.com/document_detail/2511967.html) operation to create a resource advanced search file. Then, you can call this operation to obtain the URL of the resource advanced search file.
        
        @param request: GetAdvancedSearchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdvancedSearchFileResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAdvancedSearchFile',
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
            config_20200907_models.GetAdvancedSearchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_advanced_search_file(self) -> config_20200907_models.GetAdvancedSearchFileResponse:
        """
        @summary Obtains the last resource advanced search file that is generated within the current account. You can call this operation to obtain the URL of the resource advanced search file.
        
        @description ### [](#)Prerequisites
        You must call the [CreateAdvancedSearchFile](https://help.aliyun.com/document_detail/2511967.html) operation to create a resource advanced search file. Then, you can call this operation to obtain the URL of the resource advanced search file.
        
        @return: GetAdvancedSearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_advanced_search_file_with_options(runtime)

    async def get_advanced_search_file_async(self) -> config_20200907_models.GetAdvancedSearchFileResponse:
        """
        @summary Obtains the last resource advanced search file that is generated within the current account. You can call this operation to obtain the URL of the resource advanced search file.
        
        @description ### [](#)Prerequisites
        You must call the [CreateAdvancedSearchFile](https://help.aliyun.com/document_detail/2511967.html) operation to create a resource advanced search file. Then, you can call this operation to obtain the URL of the resource advanced search file.
        
        @return: GetAdvancedSearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_advanced_search_file_with_options_async(runtime)

    def get_aggregate_account_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateAccountComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateAccountComplianceByPackResponse:
        """
        @summary Queries the compliance evaluation results of member accounts for which a compliance package takes effect in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of member accounts for which the `cp-541e626622af0087***` compliance package takes effect in the `ca-04b3fd170e340007****` account group. The returned result shows that two member accounts are monitored by the compliance package and they are both evaluated as compliant.
        
        @param request: GetAggregateAccountComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateAccountComplianceByPackResponse
        """
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
        """
        @summary Queries the compliance evaluation results of member accounts for which a compliance package takes effect in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of member accounts for which the `cp-541e626622af0087***` compliance package takes effect in the `ca-04b3fd170e340007****` account group. The returned result shows that two member accounts are monitored by the compliance package and they are both evaluated as compliant.
        
        @param request: GetAggregateAccountComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateAccountComplianceByPackResponse
        """
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
        """
        @summary Queries the compliance evaluation results of member accounts for which a compliance package takes effect in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of member accounts for which the `cp-541e626622af0087***` compliance package takes effect in the `ca-04b3fd170e340007****` account group. The returned result shows that two member accounts are monitored by the compliance package and they are both evaluated as compliant.
        
        @param request: GetAggregateAccountComplianceByPackRequest
        @return: GetAggregateAccountComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_account_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_account_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetAggregateAccountComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateAccountComplianceByPackResponse:
        """
        @summary Queries the compliance evaluation results of member accounts for which a compliance package takes effect in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of member accounts for which the `cp-541e626622af0087***` compliance package takes effect in the `ca-04b3fd170e340007****` account group. The returned result shows that two member accounts are monitored by the compliance package and they are both evaluated as compliant.
        
        @param request: GetAggregateAccountComplianceByPackRequest
        @return: GetAggregateAccountComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_account_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_advanced_search_file_with_options(
        self,
        request: config_20200907_models.GetAggregateAdvancedSearchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateAdvancedSearchFileResponse:
        """
        @summary Queries the most recently generated resource file of an account group.
        
        @param request: GetAggregateAdvancedSearchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateAdvancedSearchFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateAdvancedSearchFile',
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
            config_20200907_models.GetAggregateAdvancedSearchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_advanced_search_file_with_options_async(
        self,
        request: config_20200907_models.GetAggregateAdvancedSearchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateAdvancedSearchFileResponse:
        """
        @summary Queries the most recently generated resource file of an account group.
        
        @param request: GetAggregateAdvancedSearchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateAdvancedSearchFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateAdvancedSearchFile',
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
            config_20200907_models.GetAggregateAdvancedSearchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_advanced_search_file(
        self,
        request: config_20200907_models.GetAggregateAdvancedSearchFileRequest,
    ) -> config_20200907_models.GetAggregateAdvancedSearchFileResponse:
        """
        @summary Queries the most recently generated resource file of an account group.
        
        @param request: GetAggregateAdvancedSearchFileRequest
        @return: GetAggregateAdvancedSearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_advanced_search_file_with_options(request, runtime)

    async def get_aggregate_advanced_search_file_async(
        self,
        request: config_20200907_models.GetAggregateAdvancedSearchFileRequest,
    ) -> config_20200907_models.GetAggregateAdvancedSearchFileResponse:
        """
        @summary Queries the most recently generated resource file of an account group.
        
        @param request: GetAggregateAdvancedSearchFileRequest
        @return: GetAggregateAdvancedSearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_advanced_search_file_with_options_async(request, runtime)

    def get_aggregate_compliance_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateCompliancePackResponse:
        """
        @summary Queries the details of a compliance package in an account group.
        
        @description The topic provides an example on how to query the details of a compliance package whose ID is `cp-fdc8626622af00f9***` in an account group whose ID is `ca-f632626622af0079****`.
        
        @param request: GetAggregateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateCompliancePackResponse
        """
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
        """
        @summary Queries the details of a compliance package in an account group.
        
        @description The topic provides an example on how to query the details of a compliance package whose ID is `cp-fdc8626622af00f9***` in an account group whose ID is `ca-f632626622af0079****`.
        
        @param request: GetAggregateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateCompliancePackResponse
        """
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
        """
        @summary Queries the details of a compliance package in an account group.
        
        @description The topic provides an example on how to query the details of a compliance package whose ID is `cp-fdc8626622af00f9***` in an account group whose ID is `ca-f632626622af0079****`.
        
        @param request: GetAggregateCompliancePackRequest
        @return: GetAggregateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_compliance_pack_with_options(request, runtime)

    async def get_aggregate_compliance_pack_async(
        self,
        request: config_20200907_models.GetAggregateCompliancePackRequest,
    ) -> config_20200907_models.GetAggregateCompliancePackResponse:
        """
        @summary Queries the details of a compliance package in an account group.
        
        @description The topic provides an example on how to query the details of a compliance package whose ID is `cp-fdc8626622af00f9***` in an account group whose ID is `ca-f632626622af0079****`.
        
        @param request: GetAggregateCompliancePackRequest
        @return: GetAggregateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_compliance_pack_with_options_async(request, runtime)

    def get_aggregate_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GetAggregateCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateCompliancePackReportResponse:
        """
        @summary Queries the compliance evaluation report that is generated based on a compliance package of an account group.
        
        @description > Before you call this operation, you must call the GenerateAggregateCompliancePackReport operation to generate the latest compliance evaluation report based on a compliance package. For more information, see [GenerateAggregateCompliancePackReport](https://help.aliyun.com/document_detail/262687.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****` account group.
        
        @param request: GetAggregateCompliancePackReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateCompliancePackReportResponse
        """
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
        """
        @summary Queries the compliance evaluation report that is generated based on a compliance package of an account group.
        
        @description > Before you call this operation, you must call the GenerateAggregateCompliancePackReport operation to generate the latest compliance evaluation report based on a compliance package. For more information, see [GenerateAggregateCompliancePackReport](https://help.aliyun.com/document_detail/262687.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****` account group.
        
        @param request: GetAggregateCompliancePackReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateCompliancePackReportResponse
        """
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
        """
        @summary Queries the compliance evaluation report that is generated based on a compliance package of an account group.
        
        @description > Before you call this operation, you must call the GenerateAggregateCompliancePackReport operation to generate the latest compliance evaluation report based on a compliance package. For more information, see [GenerateAggregateCompliancePackReport](https://help.aliyun.com/document_detail/262687.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****` account group.
        
        @param request: GetAggregateCompliancePackReportRequest
        @return: GetAggregateCompliancePackReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_compliance_pack_report_with_options(request, runtime)

    async def get_aggregate_compliance_pack_report_async(
        self,
        request: config_20200907_models.GetAggregateCompliancePackReportRequest,
    ) -> config_20200907_models.GetAggregateCompliancePackReportResponse:
        """
        @summary Queries the compliance evaluation report that is generated based on a compliance package of an account group.
        
        @description > Before you call this operation, you must call the GenerateAggregateCompliancePackReport operation to generate the latest compliance evaluation report based on a compliance package. For more information, see [GenerateAggregateCompliancePackReport](https://help.aliyun.com/document_detail/262687.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****` account group.
        
        @param request: GetAggregateCompliancePackReportRequest
        @return: GetAggregateCompliancePackReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_compliance_pack_report_with_options_async(request, runtime)

    def get_aggregate_compliance_summary_with_options(
        self,
        request: config_20200907_models.GetAggregateComplianceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateComplianceSummaryResponse:
        """
        @summary Queries the compliance statistics of an account group.
        
        @description This topic provides an example on how to query the compliance statistics of resources and rules in the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GetAggregateComplianceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateComplianceSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateComplianceSummary',
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
            config_20200907_models.GetAggregateComplianceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_compliance_summary_with_options_async(
        self,
        request: config_20200907_models.GetAggregateComplianceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateComplianceSummaryResponse:
        """
        @summary Queries the compliance statistics of an account group.
        
        @description This topic provides an example on how to query the compliance statistics of resources and rules in the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GetAggregateComplianceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateComplianceSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateComplianceSummary',
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
            config_20200907_models.GetAggregateComplianceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_compliance_summary(
        self,
        request: config_20200907_models.GetAggregateComplianceSummaryRequest,
    ) -> config_20200907_models.GetAggregateComplianceSummaryResponse:
        """
        @summary Queries the compliance statistics of an account group.
        
        @description This topic provides an example on how to query the compliance statistics of resources and rules in the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GetAggregateComplianceSummaryRequest
        @return: GetAggregateComplianceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_compliance_summary_with_options(request, runtime)

    async def get_aggregate_compliance_summary_async(
        self,
        request: config_20200907_models.GetAggregateComplianceSummaryRequest,
    ) -> config_20200907_models.GetAggregateComplianceSummaryResponse:
        """
        @summary Queries the compliance statistics of an account group.
        
        @description This topic provides an example on how to query the compliance statistics of resources and rules in the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GetAggregateComplianceSummaryRequest
        @return: GetAggregateComplianceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_compliance_summary_with_options_async(request, runtime)

    def get_aggregate_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigDeliveryChannelResponse:
        """
        @summary Queries the information about a delivery channel in an account group.
        
        @param request: GetAggregateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigDeliveryChannel',
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
            config_20200907_models.GetAggregateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigDeliveryChannelResponse:
        """
        @summary Queries the information about a delivery channel in an account group.
        
        @param request: GetAggregateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigDeliveryChannel',
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
            config_20200907_models.GetAggregateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_delivery_channel(
        self,
        request: config_20200907_models.GetAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.GetAggregateConfigDeliveryChannelResponse:
        """
        @summary Queries the information about a delivery channel in an account group.
        
        @param request: GetAggregateConfigDeliveryChannelRequest
        @return: GetAggregateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_delivery_channel_with_options(request, runtime)

    async def get_aggregate_config_delivery_channel_async(
        self,
        request: config_20200907_models.GetAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.GetAggregateConfigDeliveryChannelResponse:
        """
        @summary Queries the information about a delivery channel in an account group.
        
        @param request: GetAggregateConfigDeliveryChannelRequest
        @return: GetAggregateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def get_aggregate_config_rule_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleResponse:
        """
        @summary 获取账号组规则详情
        
        @description This example shows how to query the details of the `cr-7f7d626622af0041***` rule in the `ca-7f00626622af0041****` account group.
        
        @param request: GetAggregateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
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
        """
        @summary 获取账号组规则详情
        
        @description This example shows how to query the details of the `cr-7f7d626622af0041***` rule in the `ca-7f00626622af0041****` account group.
        
        @param request: GetAggregateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
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
        """
        @summary 获取账号组规则详情
        
        @description This example shows how to query the details of the `cr-7f7d626622af0041***` rule in the `ca-7f00626622af0041****` account group.
        
        @param request: GetAggregateConfigRuleRequest
        @return: GetAggregateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rule_with_options(request, runtime)

    async def get_aggregate_config_rule_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleResponse:
        """
        @summary 获取账号组规则详情
        
        @description This example shows how to query the details of the `cr-7f7d626622af0041***` rule in the `ca-7f00626622af0041****` account group.
        
        @param request: GetAggregateConfigRuleRequest
        @return: GetAggregateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rule_with_options_async(request, runtime)

    def get_aggregate_config_rule_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRuleComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse:
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package in an account group.
        
        @description The sample request in this topic shows you how to query the compliance evaluation results based on rules in the `cp-541e626622af0087***` compliance package that is created for the `ca-04b3fd170e340007****` account group. The return result shows a total of `one` rule. `No resources` are evaluated as non-compliant based on the rule.
        
        @param request: GetAggregateConfigRuleComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigRuleComplianceByPackResponse
        """
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
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package in an account group.
        
        @description The sample request in this topic shows you how to query the compliance evaluation results based on rules in the `cp-541e626622af0087***` compliance package that is created for the `ca-04b3fd170e340007****` account group. The return result shows a total of `one` rule. `No resources` are evaluated as non-compliant based on the rule.
        
        @param request: GetAggregateConfigRuleComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigRuleComplianceByPackResponse
        """
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
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package in an account group.
        
        @description The sample request in this topic shows you how to query the compliance evaluation results based on rules in the `cp-541e626622af0087***` compliance package that is created for the `ca-04b3fd170e340007****` account group. The return result shows a total of `one` rule. `No resources` are evaluated as non-compliant based on the rule.
        
        @param request: GetAggregateConfigRuleComplianceByPackRequest
        @return: GetAggregateConfigRuleComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rule_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_config_rule_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleComplianceByPackResponse:
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package in an account group.
        
        @description The sample request in this topic shows you how to query the compliance evaluation results based on rules in the `cp-541e626622af0087***` compliance package that is created for the `ca-04b3fd170e340007****` account group. The return result shows a total of `one` rule. `No resources` are evaluated as non-compliant based on the rule.
        
        @param request: GetAggregateConfigRuleComplianceByPackRequest
        @return: GetAggregateConfigRuleComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rule_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_config_rule_summary_by_risk_level_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        """
        @summary Queries the summary of compliance evaluation results by rule risk level in an account group.
        
        @description This topic provides an example on how to query the summary of compliance evaluation results by rule risk level in the `ca-3a58626622af0005***` account group. The returned result shows four rules that are specified with the high risk level. One of the rules detects non-compliant resources, and the resources evaluated by the remaining three are compliant.
        
        @param request: GetAggregateConfigRuleSummaryByRiskLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigRuleSummaryByRiskLevelResponse
        """
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
        """
        @summary Queries the summary of compliance evaluation results by rule risk level in an account group.
        
        @description This topic provides an example on how to query the summary of compliance evaluation results by rule risk level in the `ca-3a58626622af0005***` account group. The returned result shows four rules that are specified with the high risk level. One of the rules detects non-compliant resources, and the resources evaluated by the remaining three are compliant.
        
        @param request: GetAggregateConfigRuleSummaryByRiskLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigRuleSummaryByRiskLevelResponse
        """
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
        """
        @summary Queries the summary of compliance evaluation results by rule risk level in an account group.
        
        @description This topic provides an example on how to query the summary of compliance evaluation results by rule risk level in the `ca-3a58626622af0005***` account group. The returned result shows four rules that are specified with the high risk level. One of the rules detects non-compliant resources, and the resources evaluated by the remaining three are compliant.
        
        @param request: GetAggregateConfigRuleSummaryByRiskLevelRequest
        @return: GetAggregateConfigRuleSummaryByRiskLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rule_summary_by_risk_level_with_options(request, runtime)

    async def get_aggregate_config_rule_summary_by_risk_level_async(
        self,
        request: config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelRequest,
    ) -> config_20200907_models.GetAggregateConfigRuleSummaryByRiskLevelResponse:
        """
        @summary Queries the summary of compliance evaluation results by rule risk level in an account group.
        
        @description This topic provides an example on how to query the summary of compliance evaluation results by rule risk level in the `ca-3a58626622af0005***` account group. The returned result shows four rules that are specified with the high risk level. One of the rules detects non-compliant resources, and the resources evaluated by the remaining three are compliant.
        
        @param request: GetAggregateConfigRuleSummaryByRiskLevelRequest
        @return: GetAggregateConfigRuleSummaryByRiskLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rule_summary_by_risk_level_with_options_async(request, runtime)

    def get_aggregate_config_rules_report_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        """
        @summary Downloads the compliance evaluation report in the Excel format to your on-premises machine. This allows you to assign tasks and modify incompliant resource configurations.
        
        @description > Before you call this operation, you must call the GenerateAggregateConfigRulesReport operation to generate the latest compliance evaluation report based on all rules in an account group. For more information, see [GenerateAggregateConfigRulesReport](https://help.aliyun.com/document_detail/262701.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on all rules in the `ca-f632626622af0079***` account group.
        
        @param request: GetAggregateConfigRulesReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigRulesReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRulesReport',
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
            config_20200907_models.GetAggregateConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_config_rules_report_with_options_async(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        """
        @summary Downloads the compliance evaluation report in the Excel format to your on-premises machine. This allows you to assign tasks and modify incompliant resource configurations.
        
        @description > Before you call this operation, you must call the GenerateAggregateConfigRulesReport operation to generate the latest compliance evaluation report based on all rules in an account group. For more information, see [GenerateAggregateConfigRulesReport](https://help.aliyun.com/document_detail/262701.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on all rules in the `ca-f632626622af0079***` account group.
        
        @param request: GetAggregateConfigRulesReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateConfigRulesReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateConfigRulesReport',
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
            config_20200907_models.GetAggregateConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_config_rules_report(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        """
        @summary Downloads the compliance evaluation report in the Excel format to your on-premises machine. This allows you to assign tasks and modify incompliant resource configurations.
        
        @description > Before you call this operation, you must call the GenerateAggregateConfigRulesReport operation to generate the latest compliance evaluation report based on all rules in an account group. For more information, see [GenerateAggregateConfigRulesReport](https://help.aliyun.com/document_detail/262701.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on all rules in the `ca-f632626622af0079***` account group.
        
        @param request: GetAggregateConfigRulesReportRequest
        @return: GetAggregateConfigRulesReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rules_report_with_options(request, runtime)

    async def get_aggregate_config_rules_report_async(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        """
        @summary Downloads the compliance evaluation report in the Excel format to your on-premises machine. This allows you to assign tasks and modify incompliant resource configurations.
        
        @description > Before you call this operation, you must call the GenerateAggregateConfigRulesReport operation to generate the latest compliance evaluation report based on all rules in an account group. For more information, see [GenerateAggregateConfigRulesReport](https://help.aliyun.com/document_detail/262701.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on all rules in the `ca-f632626622af0079***` account group.
        
        @param request: GetAggregateConfigRulesReportRequest
        @return: GetAggregateConfigRulesReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rules_report_with_options_async(request, runtime)

    def get_aggregate_discovered_resource_with_options(
        self,
        request: config_20200907_models.GetAggregateDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateDiscoveredResourceResponse:
        """
        @summary Queries the details of a specific resource in an account group.
        
        @description This topic provides an example on how to query the details of an Elastic Compute Service (ECS) instance `i-bp12g4xbl4i0brkn***` that resides in the China (Hangzhou) region in the account group `ca-5885626622af0008****`.
        
        @param request: GetAggregateDiscoveredResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateDiscoveredResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_option):
            query['ComplianceOption'] = request.compliance_option
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateDiscoveredResource',
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
            config_20200907_models.GetAggregateDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_discovered_resource_with_options_async(
        self,
        request: config_20200907_models.GetAggregateDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateDiscoveredResourceResponse:
        """
        @summary Queries the details of a specific resource in an account group.
        
        @description This topic provides an example on how to query the details of an Elastic Compute Service (ECS) instance `i-bp12g4xbl4i0brkn***` that resides in the China (Hangzhou) region in the account group `ca-5885626622af0008****`.
        
        @param request: GetAggregateDiscoveredResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateDiscoveredResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_option):
            query['ComplianceOption'] = request.compliance_option
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateDiscoveredResource',
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
            config_20200907_models.GetAggregateDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_discovered_resource(
        self,
        request: config_20200907_models.GetAggregateDiscoveredResourceRequest,
    ) -> config_20200907_models.GetAggregateDiscoveredResourceResponse:
        """
        @summary Queries the details of a specific resource in an account group.
        
        @description This topic provides an example on how to query the details of an Elastic Compute Service (ECS) instance `i-bp12g4xbl4i0brkn***` that resides in the China (Hangzhou) region in the account group `ca-5885626622af0008****`.
        
        @param request: GetAggregateDiscoveredResourceRequest
        @return: GetAggregateDiscoveredResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_discovered_resource_with_options(request, runtime)

    async def get_aggregate_discovered_resource_async(
        self,
        request: config_20200907_models.GetAggregateDiscoveredResourceRequest,
    ) -> config_20200907_models.GetAggregateDiscoveredResourceResponse:
        """
        @summary Queries the details of a specific resource in an account group.
        
        @description This topic provides an example on how to query the details of an Elastic Compute Service (ECS) instance `i-bp12g4xbl4i0brkn***` that resides in the China (Hangzhou) region in the account group `ca-5885626622af0008****`.
        
        @param request: GetAggregateDiscoveredResourceRequest
        @return: GetAggregateDiscoveredResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_discovered_resource_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_by_config_rule_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results based on the `cr-d369626622af008e***` rule in the `ca-a4e5626622af0079****` account group. The returned result shows that a total of 10 resources are evaluated by the rule and five of them are evaluated as compliant.
        
        @param request: GetAggregateResourceComplianceByConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceByConfigRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceByConfigRule',
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
            config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_by_config_rule_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results based on the `cr-d369626622af008e***` rule in the `ca-a4e5626622af0079****` account group. The returned result shows that a total of 10 resources are evaluated by the rule and five of them are evaluated as compliant.
        
        @param request: GetAggregateResourceComplianceByConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceByConfigRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceByConfigRule',
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
            config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_by_config_rule(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results based on the `cr-d369626622af008e***` rule in the `ca-a4e5626622af0079****` account group. The returned result shows that a total of 10 resources are evaluated by the rule and five of them are evaluated as compliant.
        
        @param request: GetAggregateResourceComplianceByConfigRuleRequest
        @return: GetAggregateResourceComplianceByConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_by_config_rule_with_options(request, runtime)

    async def get_aggregate_resource_compliance_by_config_rule_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results based on the `cr-d369626622af008e***` rule in the `ca-a4e5626622af0079****` account group. The returned result shows that a total of 10 resources are evaluated by the rule and five of them are evaluated as compliant.
        
        @param request: GetAggregateResourceComplianceByConfigRuleRequest
        @return: GetAggregateResourceComplianceByConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_by_config_rule_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByPackResponse:
        """
        @summary Queries the compliance evaluation results of resources evaluated based on a compliance package of an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources monitored based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****`account group. The returned result shows that the total number of monitored resources is `10` and the number of non-compliant resources is `7`.
        
        @param request: GetAggregateResourceComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceByPackResponse
        """
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
        """
        @summary Queries the compliance evaluation results of resources evaluated based on a compliance package of an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources monitored based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****`account group. The returned result shows that the total number of monitored resources is `10` and the number of non-compliant resources is `7`.
        
        @param request: GetAggregateResourceComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceByPackResponse
        """
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
        """
        @summary Queries the compliance evaluation results of resources evaluated based on a compliance package of an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources monitored based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****`account group. The returned result shows that the total number of monitored resources is `10` and the number of non-compliant resources is `7`.
        
        @param request: GetAggregateResourceComplianceByPackRequest
        @return: GetAggregateResourceComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_by_pack_with_options(request, runtime)

    async def get_aggregate_resource_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByPackRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceByPackResponse:
        """
        @summary Queries the compliance evaluation results of resources evaluated based on a compliance package of an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources monitored based on the `cp-fdc8626622af00f9***` compliance package in the `ca-f632626622af0079****`account group. The returned result shows that the total number of monitored resources is `10` and the number of non-compliant resources is `7`.
        
        @param request: GetAggregateResourceComplianceByPackRequest
        @return: GetAggregateResourceComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_by_pack_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_group_by_region_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByRegionResponse:
        """
        @summary Queries the evaluation results grouped by resource type for an account group rule.
        
        @param request: GetAggregateResourceComplianceGroupByRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceGroupByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceGroupByRegion',
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
            config_20200907_models.GetAggregateResourceComplianceGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_group_by_region_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByRegionResponse:
        """
        @summary Queries the evaluation results grouped by resource type for an account group rule.
        
        @param request: GetAggregateResourceComplianceGroupByRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceGroupByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceGroupByRegion',
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
            config_20200907_models.GetAggregateResourceComplianceGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_group_by_region(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByRegionRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByRegionResponse:
        """
        @summary Queries the evaluation results grouped by resource type for an account group rule.
        
        @param request: GetAggregateResourceComplianceGroupByRegionRequest
        @return: GetAggregateResourceComplianceGroupByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_group_by_region_with_options(request, runtime)

    async def get_aggregate_resource_compliance_group_by_region_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByRegionRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByRegionResponse:
        """
        @summary Queries the evaluation results grouped by resource type for an account group rule.
        
        @param request: GetAggregateResourceComplianceGroupByRegionRequest
        @return: GetAggregateResourceComplianceGroupByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_group_by_region_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_group_by_resource_type_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        """
        @summary Queries the evaluation results grouped by resource type for an account group rule.
        
        @param request: GetAggregateResourceComplianceGroupByResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceGroupByResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceGroupByResourceType',
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
            config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_compliance_group_by_resource_type_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        """
        @summary Queries the evaluation results grouped by resource type for an account group rule.
        
        @param request: GetAggregateResourceComplianceGroupByResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceGroupByResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceComplianceGroupByResourceType',
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
            config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_compliance_group_by_resource_type(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        """
        @summary Queries the evaluation results grouped by resource type for an account group rule.
        
        @param request: GetAggregateResourceComplianceGroupByResourceTypeRequest
        @return: GetAggregateResourceComplianceGroupByResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_group_by_resource_type_with_options(request, runtime)

    async def get_aggregate_resource_compliance_group_by_resource_type_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        """
        @summary Queries the evaluation results grouped by resource type for an account group rule.
        
        @param request: GetAggregateResourceComplianceGroupByResourceTypeRequest
        @return: GetAggregateResourceComplianceGroupByResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_group_by_resource_type_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_timeline_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceTimelineResponse:
        """
        @summary Queries the compliance timeline of a resource in an account group.
        
        @description The sample request in this topic shows you how to query the compliance timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region within the `100931896542***` member account of the `ca-5885626622af0008****` account group. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows the following two timestamps on the compliance timeline: `1625200295276` and `1625200228510`. The first timestamp indicates 12:31:35 on July 2, 2021 (UTC+8), and the second timestamp indicates 12:30:28 on July 2, 2021 (UTC+8).
        
        @param request: GetAggregateResourceComplianceTimelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceTimelineResponse
        """
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
        """
        @summary Queries the compliance timeline of a resource in an account group.
        
        @description The sample request in this topic shows you how to query the compliance timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region within the `100931896542***` member account of the `ca-5885626622af0008****` account group. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows the following two timestamps on the compliance timeline: `1625200295276` and `1625200228510`. The first timestamp indicates 12:31:35 on July 2, 2021 (UTC+8), and the second timestamp indicates 12:30:28 on July 2, 2021 (UTC+8).
        
        @param request: GetAggregateResourceComplianceTimelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceComplianceTimelineResponse
        """
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
        """
        @summary Queries the compliance timeline of a resource in an account group.
        
        @description The sample request in this topic shows you how to query the compliance timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region within the `100931896542***` member account of the `ca-5885626622af0008****` account group. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows the following two timestamps on the compliance timeline: `1625200295276` and `1625200228510`. The first timestamp indicates 12:31:35 on July 2, 2021 (UTC+8), and the second timestamp indicates 12:30:28 on July 2, 2021 (UTC+8).
        
        @param request: GetAggregateResourceComplianceTimelineRequest
        @return: GetAggregateResourceComplianceTimelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_timeline_with_options(request, runtime)

    async def get_aggregate_resource_compliance_timeline_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceTimelineRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceTimelineResponse:
        """
        @summary Queries the compliance timeline of a resource in an account group.
        
        @description The sample request in this topic shows you how to query the compliance timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region within the `100931896542***` member account of the `ca-5885626622af0008****` account group. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows the following two timestamps on the compliance timeline: `1625200295276` and `1625200228510`. The first timestamp indicates 12:31:35 on July 2, 2021 (UTC+8), and the second timestamp indicates 12:30:28 on July 2, 2021 (UTC+8).
        
        @param request: GetAggregateResourceComplianceTimelineRequest
        @return: GetAggregateResourceComplianceTimelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_timeline_with_options_async(request, runtime)

    def get_aggregate_resource_configuration_timeline_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceConfigurationTimelineResponse:
        """
        @summary Queries the configuration timeline of a resource in an account group.
        
        @description The sample request in this topic shows you how to query the configuration timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region within the `100931896542***` member account of the `ca-5885626622af0008****` account group. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows that the timestamp when the resource configuration changes is `1624961112000`. The timestamp indicates 18:05:12 on June 29, 2021 (UTC+8).
        
        @param request: GetAggregateResourceConfigurationTimelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceConfigurationTimelineResponse
        """
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
        """
        @summary Queries the configuration timeline of a resource in an account group.
        
        @description The sample request in this topic shows you how to query the configuration timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region within the `100931896542***` member account of the `ca-5885626622af0008****` account group. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows that the timestamp when the resource configuration changes is `1624961112000`. The timestamp indicates 18:05:12 on June 29, 2021 (UTC+8).
        
        @param request: GetAggregateResourceConfigurationTimelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceConfigurationTimelineResponse
        """
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
        """
        @summary Queries the configuration timeline of a resource in an account group.
        
        @description The sample request in this topic shows you how to query the configuration timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region within the `100931896542***` member account of the `ca-5885626622af0008****` account group. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows that the timestamp when the resource configuration changes is `1624961112000`. The timestamp indicates 18:05:12 on June 29, 2021 (UTC+8).
        
        @param request: GetAggregateResourceConfigurationTimelineRequest
        @return: GetAggregateResourceConfigurationTimelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_configuration_timeline_with_options(request, runtime)

    async def get_aggregate_resource_configuration_timeline_async(
        self,
        request: config_20200907_models.GetAggregateResourceConfigurationTimelineRequest,
    ) -> config_20200907_models.GetAggregateResourceConfigurationTimelineResponse:
        """
        @summary Queries the configuration timeline of a resource in an account group.
        
        @description The sample request in this topic shows you how to query the configuration timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region within the `100931896542***` member account of the `ca-5885626622af0008****` account group. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows that the timestamp when the resource configuration changes is `1624961112000`. The timestamp indicates 18:05:12 on June 29, 2021 (UTC+8).
        
        @param request: GetAggregateResourceConfigurationTimelineRequest
        @return: GetAggregateResourceConfigurationTimelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_configuration_timeline_with_options_async(request, runtime)

    def get_aggregate_resource_counts_group_by_region_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        """
        @summary Queries the statistics on the resources in an account group by region.
        
        @description This topic provides an example on how to query the statistics on the resources in an account group named `ca-a260626622af0005***` by region. The returned result shows that a total of `10` resources exist in the `cn-hangzhou` region.
        
        @param request: GetAggregateResourceCountsGroupByRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceCountsGroupByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceCountsGroupByRegion',
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
            config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_counts_group_by_region_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        """
        @summary Queries the statistics on the resources in an account group by region.
        
        @description This topic provides an example on how to query the statistics on the resources in an account group named `ca-a260626622af0005***` by region. The returned result shows that a total of `10` resources exist in the `cn-hangzhou` region.
        
        @param request: GetAggregateResourceCountsGroupByRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceCountsGroupByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceCountsGroupByRegion',
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
            config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_counts_group_by_region(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        """
        @summary Queries the statistics on the resources in an account group by region.
        
        @description This topic provides an example on how to query the statistics on the resources in an account group named `ca-a260626622af0005***` by region. The returned result shows that a total of `10` resources exist in the `cn-hangzhou` region.
        
        @param request: GetAggregateResourceCountsGroupByRegionRequest
        @return: GetAggregateResourceCountsGroupByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_counts_group_by_region_with_options(request, runtime)

    async def get_aggregate_resource_counts_group_by_region_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByRegionRequest,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByRegionResponse:
        """
        @summary Queries the statistics on the resources in an account group by region.
        
        @description This topic provides an example on how to query the statistics on the resources in an account group named `ca-a260626622af0005***` by region. The returned result shows that a total of `10` resources exist in the `cn-hangzhou` region.
        
        @param request: GetAggregateResourceCountsGroupByRegionRequest
        @return: GetAggregateResourceCountsGroupByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_counts_group_by_region_with_options_async(request, runtime)

    def get_aggregate_resource_counts_group_by_resource_type_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        """
        @summary Queries the statistics on the resources in an account group by resource type.
        
        @description This topic provides an example on how to query the statistics on the resources in an account group whose ID is `ca-a260626622af0005***` by resource type. The returned result shows that the account group has a total of `seven` resources of the `ACS::RAM::Role` resource type.
        
        @param request: GetAggregateResourceCountsGroupByResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceCountsGroupByResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceCountsGroupByResourceType',
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
            config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_counts_group_by_resource_type_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        """
        @summary Queries the statistics on the resources in an account group by resource type.
        
        @description This topic provides an example on how to query the statistics on the resources in an account group whose ID is `ca-a260626622af0005***` by resource type. The returned result shows that the account group has a total of `seven` resources of the `ACS::RAM::Role` resource type.
        
        @param request: GetAggregateResourceCountsGroupByResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceCountsGroupByResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceCountsGroupByResourceType',
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
            config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_counts_group_by_resource_type(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        """
        @summary Queries the statistics on the resources in an account group by resource type.
        
        @description This topic provides an example on how to query the statistics on the resources in an account group whose ID is `ca-a260626622af0005***` by resource type. The returned result shows that the account group has a total of `seven` resources of the `ACS::RAM::Role` resource type.
        
        @param request: GetAggregateResourceCountsGroupByResourceTypeRequest
        @return: GetAggregateResourceCountsGroupByResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_counts_group_by_resource_type_with_options(request, runtime)

    async def get_aggregate_resource_counts_group_by_resource_type_async(
        self,
        request: config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetAggregateResourceCountsGroupByResourceTypeResponse:
        """
        @summary Queries the statistics on the resources in an account group by resource type.
        
        @description This topic provides an example on how to query the statistics on the resources in an account group whose ID is `ca-a260626622af0005***` by resource type. The returned result shows that the account group has a total of `seven` resources of the `ACS::RAM::Role` resource type.
        
        @param request: GetAggregateResourceCountsGroupByResourceTypeRequest
        @return: GetAggregateResourceCountsGroupByResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_counts_group_by_resource_type_with_options_async(request, runtime)

    def get_aggregate_resource_inventory_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceInventoryResponse:
        """
        @summary Obtains the last resource inventory that is generated on the Global Resources page within the current account group.
        
        @description ### [](#)Prerequisites
        The [GenerateAggregateResourceInventory](https://help.aliyun.com/document_detail/2398353.html) operation is called to generate a resource inventory. Then, this operation is called to obtain the URL of the resource inventory.
        ### [](#)Description
        This topic provides an example on how to obtain the last resource inventory that is generated within the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GetAggregateResourceInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceInventoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceInventory',
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
            config_20200907_models.GetAggregateResourceInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_resource_inventory_with_options_async(
        self,
        request: config_20200907_models.GetAggregateResourceInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceInventoryResponse:
        """
        @summary Obtains the last resource inventory that is generated on the Global Resources page within the current account group.
        
        @description ### [](#)Prerequisites
        The [GenerateAggregateResourceInventory](https://help.aliyun.com/document_detail/2398353.html) operation is called to generate a resource inventory. Then, this operation is called to obtain the URL of the resource inventory.
        ### [](#)Description
        This topic provides an example on how to obtain the last resource inventory that is generated within the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GetAggregateResourceInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregateResourceInventoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateResourceInventory',
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
            config_20200907_models.GetAggregateResourceInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_resource_inventory(
        self,
        request: config_20200907_models.GetAggregateResourceInventoryRequest,
    ) -> config_20200907_models.GetAggregateResourceInventoryResponse:
        """
        @summary Obtains the last resource inventory that is generated on the Global Resources page within the current account group.
        
        @description ### [](#)Prerequisites
        The [GenerateAggregateResourceInventory](https://help.aliyun.com/document_detail/2398353.html) operation is called to generate a resource inventory. Then, this operation is called to obtain the URL of the resource inventory.
        ### [](#)Description
        This topic provides an example on how to obtain the last resource inventory that is generated within the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GetAggregateResourceInventoryRequest
        @return: GetAggregateResourceInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_inventory_with_options(request, runtime)

    async def get_aggregate_resource_inventory_async(
        self,
        request: config_20200907_models.GetAggregateResourceInventoryRequest,
    ) -> config_20200907_models.GetAggregateResourceInventoryResponse:
        """
        @summary Obtains the last resource inventory that is generated on the Global Resources page within the current account group.
        
        @description ### [](#)Prerequisites
        The [GenerateAggregateResourceInventory](https://help.aliyun.com/document_detail/2398353.html) operation is called to generate a resource inventory. Then, this operation is called to obtain the URL of the resource inventory.
        ### [](#)Description
        This topic provides an example on how to obtain the last resource inventory that is generated within the account group ca-a91d626622af0035\\\\*\\*\\*.
        
        @param request: GetAggregateResourceInventoryRequest
        @return: GetAggregateResourceInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_inventory_with_options_async(request, runtime)

    def get_aggregator_with_options(
        self,
        request: config_20200907_models.GetAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregatorResponse:
        """
        @summary Queries the details of an account group. You can query the name, creation time, member, and type of an account group.
        
        @description The sample request in this topic shows you how to query the details of the `ca-88ea626622af0055***` account group. The return result shows that the account group is named `Test_Group`, its description is `Test account group`, and it is of the `CUSTOM` type. The account group is in the `1` state, which indicates that it is created.
        
        @param request: GetAggregatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregator',
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
            config_20200907_models.GetAggregatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregator_with_options_async(
        self,
        request: config_20200907_models.GetAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregatorResponse:
        """
        @summary Queries the details of an account group. You can query the name, creation time, member, and type of an account group.
        
        @description The sample request in this topic shows you how to query the details of the `ca-88ea626622af0055***` account group. The return result shows that the account group is named `Test_Group`, its description is `Test account group`, and it is of the `CUSTOM` type. The account group is in the `1` state, which indicates that it is created.
        
        @param request: GetAggregatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggregatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregator',
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
            config_20200907_models.GetAggregatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregator(
        self,
        request: config_20200907_models.GetAggregatorRequest,
    ) -> config_20200907_models.GetAggregatorResponse:
        """
        @summary Queries the details of an account group. You can query the name, creation time, member, and type of an account group.
        
        @description The sample request in this topic shows you how to query the details of the `ca-88ea626622af0055***` account group. The return result shows that the account group is named `Test_Group`, its description is `Test account group`, and it is of the `CUSTOM` type. The account group is in the `1` state, which indicates that it is created.
        
        @param request: GetAggregatorRequest
        @return: GetAggregatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aggregator_with_options(request, runtime)

    async def get_aggregator_async(
        self,
        request: config_20200907_models.GetAggregatorRequest,
    ) -> config_20200907_models.GetAggregatorResponse:
        """
        @summary Queries the details of an account group. You can query the name, creation time, member, and type of an account group.
        
        @description The sample request in this topic shows you how to query the details of the `ca-88ea626622af0055***` account group. The return result shows that the account group is named `Test_Group`, its description is `Test account group`, and it is of the `CUSTOM` type. The account group is in the `1` state, which indicates that it is created.
        
        @param request: GetAggregatorRequest
        @return: GetAggregatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregator_with_options_async(request, runtime)

    def get_compliance_pack_with_options(
        self,
        request: config_20200907_models.GetCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetCompliancePackResponse:
        """
        @summary Queries the details of a compliance package.
        
        @description This topic provides an example on how to query the details of a compliance package whose ID is `cp-fdc8626622af00f9***`. The returned result shows that the name of the compliance package is `ClassifiedProtectionPreCheck`, the compliance package is in the `ACTIVE` state, and the risk level of the rules in the compliance package is `1`, which indicates high risk level.
        
        @param request: GetCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCompliancePackResponse
        """
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
        """
        @summary Queries the details of a compliance package.
        
        @description This topic provides an example on how to query the details of a compliance package whose ID is `cp-fdc8626622af00f9***`. The returned result shows that the name of the compliance package is `ClassifiedProtectionPreCheck`, the compliance package is in the `ACTIVE` state, and the risk level of the rules in the compliance package is `1`, which indicates high risk level.
        
        @param request: GetCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCompliancePackResponse
        """
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
        """
        @summary Queries the details of a compliance package.
        
        @description This topic provides an example on how to query the details of a compliance package whose ID is `cp-fdc8626622af00f9***`. The returned result shows that the name of the compliance package is `ClassifiedProtectionPreCheck`, the compliance package is in the `ACTIVE` state, and the risk level of the rules in the compliance package is `1`, which indicates high risk level.
        
        @param request: GetCompliancePackRequest
        @return: GetCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_compliance_pack_with_options(request, runtime)

    async def get_compliance_pack_async(
        self,
        request: config_20200907_models.GetCompliancePackRequest,
    ) -> config_20200907_models.GetCompliancePackResponse:
        """
        @summary Queries the details of a compliance package.
        
        @description This topic provides an example on how to query the details of a compliance package whose ID is `cp-fdc8626622af00f9***`. The returned result shows that the name of the compliance package is `ClassifiedProtectionPreCheck`, the compliance package is in the `ACTIVE` state, and the risk level of the rules in the compliance package is `1`, which indicates high risk level.
        
        @param request: GetCompliancePackRequest
        @return: GetCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_compliance_pack_with_options_async(request, runtime)

    def get_compliance_pack_report_with_options(
        self,
        request: config_20200907_models.GetCompliancePackReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetCompliancePackReportResponse:
        """
        @summary Queries the compliance evaluation report that is generated based on a compliance package.
        
        @description > Before you call this operation, you must call the GenerateCompliancePackReport operation to generate the latest compliance evaluation report based on a compliance package. For more information, see [GenerateCompliancePackReport](https://help.aliyun.com/document_detail/263525.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on the `cp-fdc8626622af00f9***` compliance package.
        
        @param request: GetCompliancePackReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCompliancePackReportResponse
        """
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
        """
        @summary Queries the compliance evaluation report that is generated based on a compliance package.
        
        @description > Before you call this operation, you must call the GenerateCompliancePackReport operation to generate the latest compliance evaluation report based on a compliance package. For more information, see [GenerateCompliancePackReport](https://help.aliyun.com/document_detail/263525.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on the `cp-fdc8626622af00f9***` compliance package.
        
        @param request: GetCompliancePackReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCompliancePackReportResponse
        """
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
        """
        @summary Queries the compliance evaluation report that is generated based on a compliance package.
        
        @description > Before you call this operation, you must call the GenerateCompliancePackReport operation to generate the latest compliance evaluation report based on a compliance package. For more information, see [GenerateCompliancePackReport](https://help.aliyun.com/document_detail/263525.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on the `cp-fdc8626622af00f9***` compliance package.
        
        @param request: GetCompliancePackReportRequest
        @return: GetCompliancePackReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_compliance_pack_report_with_options(request, runtime)

    async def get_compliance_pack_report_async(
        self,
        request: config_20200907_models.GetCompliancePackReportRequest,
    ) -> config_20200907_models.GetCompliancePackReportResponse:
        """
        @summary Queries the compliance evaluation report that is generated based on a compliance package.
        
        @description > Before you call this operation, you must call the GenerateCompliancePackReport operation to generate the latest compliance evaluation report based on a compliance package. For more information, see [GenerateCompliancePackReport](https://help.aliyun.com/document_detail/263525.html).
        This topic provides an example on how to query the compliance evaluation report that is generated based on the `cp-fdc8626622af00f9***` compliance package.
        
        @param request: GetCompliancePackReportRequest
        @return: GetCompliancePackReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_compliance_pack_report_with_options_async(request, runtime)

    def get_compliance_summary_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetComplianceSummaryResponse:
        """
        @summary Queries the summary of compliance statistics within the current account.
        
        @description This topic provides an example on how to query the compliance statistics of resources and rules in the current account group.
        
        @param request: GetComplianceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetComplianceSummaryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetComplianceSummary',
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
            config_20200907_models.GetComplianceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compliance_summary_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetComplianceSummaryResponse:
        """
        @summary Queries the summary of compliance statistics within the current account.
        
        @description This topic provides an example on how to query the compliance statistics of resources and rules in the current account group.
        
        @param request: GetComplianceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetComplianceSummaryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetComplianceSummary',
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
            config_20200907_models.GetComplianceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compliance_summary(self) -> config_20200907_models.GetComplianceSummaryResponse:
        """
        @summary Queries the summary of compliance statistics within the current account.
        
        @description This topic provides an example on how to query the compliance statistics of resources and rules in the current account group.
        
        @return: GetComplianceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_compliance_summary_with_options(runtime)

    async def get_compliance_summary_async(self) -> config_20200907_models.GetComplianceSummaryResponse:
        """
        @summary Queries the summary of compliance statistics within the current account.
        
        @description This topic provides an example on how to query the compliance statistics of resources and rules in the current account group.
        
        @return: GetComplianceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_compliance_summary_with_options_async(runtime)

    def get_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.GetConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigDeliveryChannelResponse:
        """
        @summary Queries the information about a delivery channel.
        
        @param request: GetConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigDeliveryChannel',
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
            config_20200907_models.GetConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.GetConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigDeliveryChannelResponse:
        """
        @summary Queries the information about a delivery channel.
        
        @param request: GetConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigDeliveryChannel',
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
            config_20200907_models.GetConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_delivery_channel(
        self,
        request: config_20200907_models.GetConfigDeliveryChannelRequest,
    ) -> config_20200907_models.GetConfigDeliveryChannelResponse:
        """
        @summary Queries the information about a delivery channel.
        
        @param request: GetConfigDeliveryChannelRequest
        @return: GetConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_config_delivery_channel_with_options(request, runtime)

    async def get_config_delivery_channel_async(
        self,
        request: config_20200907_models.GetConfigDeliveryChannelRequest,
    ) -> config_20200907_models.GetConfigDeliveryChannelResponse:
        """
        @summary Queries the information about a delivery channel.
        
        @param request: GetConfigDeliveryChannelRequest
        @return: GetConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_config_delivery_channel_with_options_async(request, runtime)

    def get_config_rule_with_options(
        self,
        request: config_20200907_models.GetConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleResponse:
        """
        @summary Queries the details of a rule.
        
        @description This topic provides an example on how to query the details of the `cr-7f7d626622af0041***` rule.
        
        @param request: GetConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_id):
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
        """
        @summary Queries the details of a rule.
        
        @description This topic provides an example on how to query the details of the `cr-7f7d626622af0041***` rule.
        
        @param request: GetConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_id):
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
        """
        @summary Queries the details of a rule.
        
        @description This topic provides an example on how to query the details of the `cr-7f7d626622af0041***` rule.
        
        @param request: GetConfigRuleRequest
        @return: GetConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_with_options(request, runtime)

    async def get_config_rule_async(
        self,
        request: config_20200907_models.GetConfigRuleRequest,
    ) -> config_20200907_models.GetConfigRuleResponse:
        """
        @summary Queries the details of a rule.
        
        @description This topic provides an example on how to query the details of the `cr-7f7d626622af0041***` rule.
        
        @param request: GetConfigRuleRequest
        @return: GetConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_with_options_async(request, runtime)

    def get_config_rule_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetConfigRuleComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleComplianceByPackResponse:
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package.
        
        @description In this topic, the `cp-541e626622af0087***` compliance package is used as an example. The return result shows a total of one rule against which specific resources are evaluated as compliant.
        
        @param request: GetConfigRuleComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRuleComplianceByPackResponse
        """
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
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package.
        
        @description In this topic, the `cp-541e626622af0087***` compliance package is used as an example. The return result shows a total of one rule against which specific resources are evaluated as compliant.
        
        @param request: GetConfigRuleComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRuleComplianceByPackResponse
        """
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
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package.
        
        @description In this topic, the `cp-541e626622af0087***` compliance package is used as an example. The return result shows a total of one rule against which specific resources are evaluated as compliant.
        
        @param request: GetConfigRuleComplianceByPackRequest
        @return: GetConfigRuleComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_compliance_by_pack_with_options(request, runtime)

    async def get_config_rule_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetConfigRuleComplianceByPackRequest,
    ) -> config_20200907_models.GetConfigRuleComplianceByPackResponse:
        """
        @summary Queries compliance evaluation results based on the rules in a compliance package.
        
        @description In this topic, the `cp-541e626622af0087***` compliance package is used as an example. The return result shows a total of one rule against which specific resources are evaluated as compliant.
        
        @param request: GetConfigRuleComplianceByPackRequest
        @return: GetConfigRuleComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_compliance_by_pack_with_options_async(request, runtime)

    def get_config_rule_summary_by_risk_level_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        """
        @summary Queries the compliance summary based on the risk level of a rule.
        
        @description This topic provides an example of how to query the summary of compliance evaluation results by rule risk level. The return result shows four rules that are specified with the high risk level. One of them detects non-compliant resources, and the resources evaluated by the remaining three are all compliant.
        
        @param request: GetConfigRuleSummaryByRiskLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRuleSummaryByRiskLevelResponse
        """
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
        """
        @summary Queries the compliance summary based on the risk level of a rule.
        
        @description This topic provides an example of how to query the summary of compliance evaluation results by rule risk level. The return result shows four rules that are specified with the high risk level. One of them detects non-compliant resources, and the resources evaluated by the remaining three are all compliant.
        
        @param request: GetConfigRuleSummaryByRiskLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRuleSummaryByRiskLevelResponse
        """
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
        """
        @summary Queries the compliance summary based on the risk level of a rule.
        
        @description This topic provides an example of how to query the summary of compliance evaluation results by rule risk level. The return result shows four rules that are specified with the high risk level. One of them detects non-compliant resources, and the resources evaluated by the remaining three are all compliant.
        
        @return: GetConfigRuleSummaryByRiskLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_config_rule_summary_by_risk_level_with_options(runtime)

    async def get_config_rule_summary_by_risk_level_async(self) -> config_20200907_models.GetConfigRuleSummaryByRiskLevelResponse:
        """
        @summary Queries the compliance summary based on the risk level of a rule.
        
        @description This topic provides an example of how to query the summary of compliance evaluation results by rule risk level. The return result shows four rules that are specified with the high risk level. One of them detects non-compliant resources, and the resources evaluated by the remaining three are all compliant.
        
        @return: GetConfigRuleSummaryByRiskLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rule_summary_by_risk_level_with_options_async(runtime)

    def get_config_rules_report_with_options(
        self,
        request: config_20200907_models.GetConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        """
        @summary Downloads the compliance evaluation report in the Excel format to your on-premises machine. This allows you to assign tasks and modify incompliant resource configurations.
        
        @description >  Before you call this operation, you must call the GenerateConfigRulesReport operation to generate the latest compliance evaluation report based on all existing rules. For more information, see [GenerateConfigRulesReport](https://help.aliyun.com/document_detail/263601.html).
        This topic provides an example of how to query the compliance evaluation report that is generated based on all existing rules.
        
        @param request: GetConfigRulesReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRulesReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigRulesReport',
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
            config_20200907_models.GetConfigRulesReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rules_report_with_options_async(
        self,
        request: config_20200907_models.GetConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        """
        @summary Downloads the compliance evaluation report in the Excel format to your on-premises machine. This allows you to assign tasks and modify incompliant resource configurations.
        
        @description >  Before you call this operation, you must call the GenerateConfigRulesReport operation to generate the latest compliance evaluation report based on all existing rules. For more information, see [GenerateConfigRulesReport](https://help.aliyun.com/document_detail/263601.html).
        This topic provides an example of how to query the compliance evaluation report that is generated based on all existing rules.
        
        @param request: GetConfigRulesReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigRulesReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigRulesReport',
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
            config_20200907_models.GetConfigRulesReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rules_report(
        self,
        request: config_20200907_models.GetConfigRulesReportRequest,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        """
        @summary Downloads the compliance evaluation report in the Excel format to your on-premises machine. This allows you to assign tasks and modify incompliant resource configurations.
        
        @description >  Before you call this operation, you must call the GenerateConfigRulesReport operation to generate the latest compliance evaluation report based on all existing rules. For more information, see [GenerateConfigRulesReport](https://help.aliyun.com/document_detail/263601.html).
        This topic provides an example of how to query the compliance evaluation report that is generated based on all existing rules.
        
        @param request: GetConfigRulesReportRequest
        @return: GetConfigRulesReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_config_rules_report_with_options(request, runtime)

    async def get_config_rules_report_async(
        self,
        request: config_20200907_models.GetConfigRulesReportRequest,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        """
        @summary Downloads the compliance evaluation report in the Excel format to your on-premises machine. This allows you to assign tasks and modify incompliant resource configurations.
        
        @description >  Before you call this operation, you must call the GenerateConfigRulesReport operation to generate the latest compliance evaluation report based on all existing rules. For more information, see [GenerateConfigRulesReport](https://help.aliyun.com/document_detail/263601.html).
        This topic provides an example of how to query the compliance evaluation report that is generated based on all existing rules.
        
        @param request: GetConfigRulesReportRequest
        @return: GetConfigRulesReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rules_report_with_options_async(request, runtime)

    def get_configuration_recorder_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigurationRecorderResponse:
        """
        @summary Queries the activation status and resource monitoring scope of Cloud Config for the current account.
        
        @description This topic provides an example on how to query the activation status and resource monitoring scope of Cloud Config for the current account.
        
        @param request: GetConfigurationRecorderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigurationRecorderResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetConfigurationRecorder',
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
            config_20200907_models.GetConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_configuration_recorder_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigurationRecorderResponse:
        """
        @summary Queries the activation status and resource monitoring scope of Cloud Config for the current account.
        
        @description This topic provides an example on how to query the activation status and resource monitoring scope of Cloud Config for the current account.
        
        @param request: GetConfigurationRecorderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigurationRecorderResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetConfigurationRecorder',
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
            config_20200907_models.GetConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_configuration_recorder(self) -> config_20200907_models.GetConfigurationRecorderResponse:
        """
        @summary Queries the activation status and resource monitoring scope of Cloud Config for the current account.
        
        @description This topic provides an example on how to query the activation status and resource monitoring scope of Cloud Config for the current account.
        
        @return: GetConfigurationRecorderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_configuration_recorder_with_options(runtime)

    async def get_configuration_recorder_async(self) -> config_20200907_models.GetConfigurationRecorderResponse:
        """
        @summary Queries the activation status and resource monitoring scope of Cloud Config for the current account.
        
        @description This topic provides an example on how to query the activation status and resource monitoring scope of Cloud Config for the current account.
        
        @return: GetConfigurationRecorderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_configuration_recorder_with_options_async(runtime)

    def get_discovered_resource_with_options(
        self,
        request: config_20200907_models.GetDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceResponse:
        """
        @summary Queries the details of a specific resource.
        
        @description This topic provides an example on how to query the details of the Elastic Compute Service (ECS) instance `i-bp12g4xbl4i0brkn***` that resides in the China (Hangzhou) region.
        
        @param request: GetDiscoveredResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiscoveredResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_option):
            query['ComplianceOption'] = request.compliance_option
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResource',
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
            config_20200907_models.GetDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_with_options_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceResponse:
        """
        @summary Queries the details of a specific resource.
        
        @description This topic provides an example on how to query the details of the Elastic Compute Service (ECS) instance `i-bp12g4xbl4i0brkn***` that resides in the China (Hangzhou) region.
        
        @param request: GetDiscoveredResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiscoveredResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_option):
            query['ComplianceOption'] = request.compliance_option
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResource',
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
            config_20200907_models.GetDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource(
        self,
        request: config_20200907_models.GetDiscoveredResourceRequest,
    ) -> config_20200907_models.GetDiscoveredResourceResponse:
        """
        @summary Queries the details of a specific resource.
        
        @description This topic provides an example on how to query the details of the Elastic Compute Service (ECS) instance `i-bp12g4xbl4i0brkn***` that resides in the China (Hangzhou) region.
        
        @param request: GetDiscoveredResourceRequest
        @return: GetDiscoveredResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_with_options(request, runtime)

    async def get_discovered_resource_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceRequest,
    ) -> config_20200907_models.GetDiscoveredResourceResponse:
        """
        @summary Queries the details of a specific resource.
        
        @description This topic provides an example on how to query the details of the Elastic Compute Service (ECS) instance `i-bp12g4xbl4i0brkn***` that resides in the China (Hangzhou) region.
        
        @param request: GetDiscoveredResourceRequest
        @return: GetDiscoveredResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_discovered_resource_with_options_async(request, runtime)

    def get_discovered_resource_counts_group_by_region_with_options(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        """
        @summary Queries the statistics on resources by region.
        
        @description This topic provides an example to demonstrate how to query the statistics on resources by region. The returned result shows that a total of 10 resources exist in the `cn-hangzhou` region.
        
        @param request: GetDiscoveredResourceCountsGroupByRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiscoveredResourceCountsGroupByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCountsGroupByRegion',
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
            config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_counts_group_by_region_with_options_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        """
        @summary Queries the statistics on resources by region.
        
        @description This topic provides an example to demonstrate how to query the statistics on resources by region. The returned result shows that a total of 10 resources exist in the `cn-hangzhou` region.
        
        @param request: GetDiscoveredResourceCountsGroupByRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiscoveredResourceCountsGroupByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCountsGroupByRegion',
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
            config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource_counts_group_by_region(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        """
        @summary Queries the statistics on resources by region.
        
        @description This topic provides an example to demonstrate how to query the statistics on resources by region. The returned result shows that a total of 10 resources exist in the `cn-hangzhou` region.
        
        @param request: GetDiscoveredResourceCountsGroupByRegionRequest
        @return: GetDiscoveredResourceCountsGroupByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_counts_group_by_region_with_options(request, runtime)

    async def get_discovered_resource_counts_group_by_region_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByRegionRequest,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByRegionResponse:
        """
        @summary Queries the statistics on resources by region.
        
        @description This topic provides an example to demonstrate how to query the statistics on resources by region. The returned result shows that a total of 10 resources exist in the `cn-hangzhou` region.
        
        @param request: GetDiscoveredResourceCountsGroupByRegionRequest
        @return: GetDiscoveredResourceCountsGroupByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_discovered_resource_counts_group_by_region_with_options_async(request, runtime)

    def get_discovered_resource_counts_group_by_resource_type_with_options(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        """
        @summary Queries the statistics on resources by resource type.
        
        @description This topic describes how to query the statistics on resources by resource type. The returned result shows that a total of 10 resources of the `ACS::ECS::Instance` resource type exist.
        
        @param request: GetDiscoveredResourceCountsGroupByResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiscoveredResourceCountsGroupByResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCountsGroupByResourceType',
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
            config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_counts_group_by_resource_type_with_options_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        """
        @summary Queries the statistics on resources by resource type.
        
        @description This topic describes how to query the statistics on resources by resource type. The returned result shows that a total of 10 resources of the `ACS::ECS::Instance` resource type exist.
        
        @param request: GetDiscoveredResourceCountsGroupByResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiscoveredResourceCountsGroupByResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCountsGroupByResourceType',
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
            config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource_counts_group_by_resource_type(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        """
        @summary Queries the statistics on resources by resource type.
        
        @description This topic describes how to query the statistics on resources by resource type. The returned result shows that a total of 10 resources of the `ACS::ECS::Instance` resource type exist.
        
        @param request: GetDiscoveredResourceCountsGroupByResourceTypeRequest
        @return: GetDiscoveredResourceCountsGroupByResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_counts_group_by_resource_type_with_options(request, runtime)

    async def get_discovered_resource_counts_group_by_resource_type_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetDiscoveredResourceCountsGroupByResourceTypeResponse:
        """
        @summary Queries the statistics on resources by resource type.
        
        @description This topic describes how to query the statistics on resources by resource type. The returned result shows that a total of 10 resources of the `ACS::ECS::Instance` resource type exist.
        
        @param request: GetDiscoveredResourceCountsGroupByResourceTypeRequest
        @return: GetDiscoveredResourceCountsGroupByResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_discovered_resource_counts_group_by_resource_type_with_options_async(request, runtime)

    def get_integrated_service_status_with_options(
        self,
        request: config_20200907_models.GetIntegratedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetIntegratedServiceStatusResponse:
        """
        @summary Queries the integration status of a specific cloud service.
        
        @param request: GetIntegratedServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIntegratedServiceStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIntegratedServiceStatus',
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
            config_20200907_models.GetIntegratedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integrated_service_status_with_options_async(
        self,
        request: config_20200907_models.GetIntegratedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetIntegratedServiceStatusResponse:
        """
        @summary Queries the integration status of a specific cloud service.
        
        @param request: GetIntegratedServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIntegratedServiceStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIntegratedServiceStatus',
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
            config_20200907_models.GetIntegratedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integrated_service_status(
        self,
        request: config_20200907_models.GetIntegratedServiceStatusRequest,
    ) -> config_20200907_models.GetIntegratedServiceStatusResponse:
        """
        @summary Queries the integration status of a specific cloud service.
        
        @param request: GetIntegratedServiceStatusRequest
        @return: GetIntegratedServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_integrated_service_status_with_options(request, runtime)

    async def get_integrated_service_status_async(
        self,
        request: config_20200907_models.GetIntegratedServiceStatusRequest,
    ) -> config_20200907_models.GetIntegratedServiceStatusResponse:
        """
        @summary Queries the integration status of a specific cloud service.
        
        @param request: GetIntegratedServiceStatusRequest
        @return: GetIntegratedServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_integrated_service_status_with_options_async(request, runtime)

    def get_managed_rule_with_options(
        self,
        request: config_20200907_models.GetManagedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetManagedRuleResponse:
        """
        @summary Queries the details of a specific managed rule.
        
        @description This topic provides an example on how to query the details of the managed rule `cdn-domain-https-enabled`.
        
        @param request: GetManagedRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetManagedRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetManagedRule',
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
            config_20200907_models.GetManagedRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_managed_rule_with_options_async(
        self,
        request: config_20200907_models.GetManagedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetManagedRuleResponse:
        """
        @summary Queries the details of a specific managed rule.
        
        @description This topic provides an example on how to query the details of the managed rule `cdn-domain-https-enabled`.
        
        @param request: GetManagedRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetManagedRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetManagedRule',
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
            config_20200907_models.GetManagedRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_managed_rule(
        self,
        request: config_20200907_models.GetManagedRuleRequest,
    ) -> config_20200907_models.GetManagedRuleResponse:
        """
        @summary Queries the details of a specific managed rule.
        
        @description This topic provides an example on how to query the details of the managed rule `cdn-domain-https-enabled`.
        
        @param request: GetManagedRuleRequest
        @return: GetManagedRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_managed_rule_with_options(request, runtime)

    async def get_managed_rule_async(
        self,
        request: config_20200907_models.GetManagedRuleRequest,
    ) -> config_20200907_models.GetManagedRuleResponse:
        """
        @summary Queries the details of a specific managed rule.
        
        @description This topic provides an example on how to query the details of the managed rule `cdn-domain-https-enabled`.
        
        @param request: GetManagedRuleRequest
        @return: GetManagedRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_managed_rule_with_options_async(request, runtime)

    def get_remediation_template_with_options(
        self,
        request: config_20200907_models.GetRemediationTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetRemediationTemplateResponse:
        """
        @summary Queries the details of an automatic remediation template.
        
        @description This topic provides an example on how to query the details of the automatic remediation template ACS-ALB-BulkyEnableDeletionProtection.
        
        @param request: GetRemediationTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRemediationTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_identifier):
            query['TemplateIdentifier'] = request.template_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRemediationTemplate',
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
            config_20200907_models.GetRemediationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_remediation_template_with_options_async(
        self,
        request: config_20200907_models.GetRemediationTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetRemediationTemplateResponse:
        """
        @summary Queries the details of an automatic remediation template.
        
        @description This topic provides an example on how to query the details of the automatic remediation template ACS-ALB-BulkyEnableDeletionProtection.
        
        @param request: GetRemediationTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRemediationTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_identifier):
            query['TemplateIdentifier'] = request.template_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRemediationTemplate',
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
            config_20200907_models.GetRemediationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_remediation_template(
        self,
        request: config_20200907_models.GetRemediationTemplateRequest,
    ) -> config_20200907_models.GetRemediationTemplateResponse:
        """
        @summary Queries the details of an automatic remediation template.
        
        @description This topic provides an example on how to query the details of the automatic remediation template ACS-ALB-BulkyEnableDeletionProtection.
        
        @param request: GetRemediationTemplateRequest
        @return: GetRemediationTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_remediation_template_with_options(request, runtime)

    async def get_remediation_template_async(
        self,
        request: config_20200907_models.GetRemediationTemplateRequest,
    ) -> config_20200907_models.GetRemediationTemplateResponse:
        """
        @summary Queries the details of an automatic remediation template.
        
        @description This topic provides an example on how to query the details of the automatic remediation template ACS-ALB-BulkyEnableDeletionProtection.
        
        @param request: GetRemediationTemplateRequest
        @return: GetRemediationTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_remediation_template_with_options_async(request, runtime)

    def get_resource_compliance_by_config_rule_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceByConfigRuleResponse:
        """
        @summary Queries the compliance summary based on the compliance evaluation result of a rule.
        
        @description In this topic, the `cr-d369626622af008e***` rule is used as an example. The return result shows that a total of 10 resources are evaluated by the rule and `five` of them are evaluated as compliant.
        
        @param request: GetResourceComplianceByConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceByConfigRuleResponse
        """
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
        """
        @summary Queries the compliance summary based on the compliance evaluation result of a rule.
        
        @description In this topic, the `cr-d369626622af008e***` rule is used as an example. The return result shows that a total of 10 resources are evaluated by the rule and `five` of them are evaluated as compliant.
        
        @param request: GetResourceComplianceByConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceByConfigRuleResponse
        """
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
        """
        @summary Queries the compliance summary based on the compliance evaluation result of a rule.
        
        @description In this topic, the `cr-d369626622af008e***` rule is used as an example. The return result shows that a total of 10 resources are evaluated by the rule and `five` of them are evaluated as compliant.
        
        @param request: GetResourceComplianceByConfigRuleRequest
        @return: GetResourceComplianceByConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_by_config_rule_with_options(request, runtime)

    async def get_resource_compliance_by_config_rule_async(
        self,
        request: config_20200907_models.GetResourceComplianceByConfigRuleRequest,
    ) -> config_20200907_models.GetResourceComplianceByConfigRuleResponse:
        """
        @summary Queries the compliance summary based on the compliance evaluation result of a rule.
        
        @description In this topic, the `cr-d369626622af008e***` rule is used as an example. The return result shows that a total of 10 resources are evaluated by the rule and `five` of them are evaluated as compliant.
        
        @param request: GetResourceComplianceByConfigRuleRequest
        @return: GetResourceComplianceByConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_by_config_rule_with_options_async(request, runtime)

    def get_resource_compliance_by_pack_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceByPackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceByPackResponse:
        """
        @summary Queries the compliance evaluation results of resources evaluated based on a compliance package.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources monitored by using the `cp-541e626622af0087***` compliance package. The returned result shows a total of 10 resources and seven of them are evaluated as non-compliant.
        
        @param request: GetResourceComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceByPackResponse
        """
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
        """
        @summary Queries the compliance evaluation results of resources evaluated based on a compliance package.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources monitored by using the `cp-541e626622af0087***` compliance package. The returned result shows a total of 10 resources and seven of them are evaluated as non-compliant.
        
        @param request: GetResourceComplianceByPackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceByPackResponse
        """
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
        """
        @summary Queries the compliance evaluation results of resources evaluated based on a compliance package.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources monitored by using the `cp-541e626622af0087***` compliance package. The returned result shows a total of 10 resources and seven of them are evaluated as non-compliant.
        
        @param request: GetResourceComplianceByPackRequest
        @return: GetResourceComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_by_pack_with_options(request, runtime)

    async def get_resource_compliance_by_pack_async(
        self,
        request: config_20200907_models.GetResourceComplianceByPackRequest,
    ) -> config_20200907_models.GetResourceComplianceByPackResponse:
        """
        @summary Queries the compliance evaluation results of resources evaluated based on a compliance package.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources monitored by using the `cp-541e626622af0087***` compliance package. The returned result shows a total of 10 resources and seven of them are evaluated as non-compliant.
        
        @param request: GetResourceComplianceByPackRequest
        @return: GetResourceComplianceByPackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_by_pack_with_options_async(request, runtime)

    def get_resource_compliance_group_by_region_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceGroupByRegionResponse:
        """
        @summary Queries the evaluation results grouped by region for a rule.
        
        @param request: GetResourceComplianceGroupByRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceGroupByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceGroupByRegion',
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
            config_20200907_models.GetResourceComplianceGroupByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_group_by_region_with_options_async(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceGroupByRegionResponse:
        """
        @summary Queries the evaluation results grouped by region for a rule.
        
        @param request: GetResourceComplianceGroupByRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceGroupByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceGroupByRegion',
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
            config_20200907_models.GetResourceComplianceGroupByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_group_by_region(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByRegionRequest,
    ) -> config_20200907_models.GetResourceComplianceGroupByRegionResponse:
        """
        @summary Queries the evaluation results grouped by region for a rule.
        
        @param request: GetResourceComplianceGroupByRegionRequest
        @return: GetResourceComplianceGroupByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_group_by_region_with_options(request, runtime)

    async def get_resource_compliance_group_by_region_async(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByRegionRequest,
    ) -> config_20200907_models.GetResourceComplianceGroupByRegionResponse:
        """
        @summary Queries the evaluation results grouped by region for a rule.
        
        @param request: GetResourceComplianceGroupByRegionRequest
        @return: GetResourceComplianceGroupByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_group_by_region_with_options_async(request, runtime)

    def get_resource_compliance_group_by_resource_type_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceGroupByResourceTypeResponse:
        """
        @summary Queries the evaluation results grouped by resource type for a rule.
        
        @param request: GetResourceComplianceGroupByResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceGroupByResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceGroupByResourceType',
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
            config_20200907_models.GetResourceComplianceGroupByResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_group_by_resource_type_with_options_async(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceGroupByResourceTypeResponse:
        """
        @summary Queries the evaluation results grouped by resource type for a rule.
        
        @param request: GetResourceComplianceGroupByResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceGroupByResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceGroupByResourceType',
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
            config_20200907_models.GetResourceComplianceGroupByResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_group_by_resource_type(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetResourceComplianceGroupByResourceTypeResponse:
        """
        @summary Queries the evaluation results grouped by resource type for a rule.
        
        @param request: GetResourceComplianceGroupByResourceTypeRequest
        @return: GetResourceComplianceGroupByResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_group_by_resource_type_with_options(request, runtime)

    async def get_resource_compliance_group_by_resource_type_async(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetResourceComplianceGroupByResourceTypeResponse:
        """
        @summary Queries the evaluation results grouped by resource type for a rule.
        
        @param request: GetResourceComplianceGroupByResourceTypeRequest
        @return: GetResourceComplianceGroupByResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_group_by_resource_type_with_options_async(request, runtime)

    def get_resource_compliance_timeline_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceTimelineResponse:
        """
        @summary Queries the compliance timeline of a resource. The compliance timeline of a resource indicates the compliance evaluation record of the resource. A compliance timeline includes points and the content on the compliance timeline.
        
        @description In Cloud Config, each resource has a compliance timeline. Cloud Config generates a compliance evaluation record for a resource each time the resource is evaluated based on a rule. The compliance evaluation records of a resource are displayed in a compliance timeline. You can configure Cloud Config to execute a rule to evaluate a resource on a regular basis or each time you change the resource configuration. You can also manually execute a rule to evaluate a resource.
        This topic provides an example on how to query the compliance timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region. The resource is an Object Storage Service (OSS) bucket. The returned result shows the following two timestamps on the compliance timeline: `1625200295276` and `1625200228510`. The first timestamp indicates 12:31:35 on July 2, 2021 (UTC+8) and the second timestamp indicates 12:30:28 on July 2, 2021 (UTC+8).
        
        @param request: GetResourceComplianceTimelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceTimelineResponse
        """
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
        """
        @summary Queries the compliance timeline of a resource. The compliance timeline of a resource indicates the compliance evaluation record of the resource. A compliance timeline includes points and the content on the compliance timeline.
        
        @description In Cloud Config, each resource has a compliance timeline. Cloud Config generates a compliance evaluation record for a resource each time the resource is evaluated based on a rule. The compliance evaluation records of a resource are displayed in a compliance timeline. You can configure Cloud Config to execute a rule to evaluate a resource on a regular basis or each time you change the resource configuration. You can also manually execute a rule to evaluate a resource.
        This topic provides an example on how to query the compliance timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region. The resource is an Object Storage Service (OSS) bucket. The returned result shows the following two timestamps on the compliance timeline: `1625200295276` and `1625200228510`. The first timestamp indicates 12:31:35 on July 2, 2021 (UTC+8) and the second timestamp indicates 12:30:28 on July 2, 2021 (UTC+8).
        
        @param request: GetResourceComplianceTimelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceComplianceTimelineResponse
        """
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
        """
        @summary Queries the compliance timeline of a resource. The compliance timeline of a resource indicates the compliance evaluation record of the resource. A compliance timeline includes points and the content on the compliance timeline.
        
        @description In Cloud Config, each resource has a compliance timeline. Cloud Config generates a compliance evaluation record for a resource each time the resource is evaluated based on a rule. The compliance evaluation records of a resource are displayed in a compliance timeline. You can configure Cloud Config to execute a rule to evaluate a resource on a regular basis or each time you change the resource configuration. You can also manually execute a rule to evaluate a resource.
        This topic provides an example on how to query the compliance timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region. The resource is an Object Storage Service (OSS) bucket. The returned result shows the following two timestamps on the compliance timeline: `1625200295276` and `1625200228510`. The first timestamp indicates 12:31:35 on July 2, 2021 (UTC+8) and the second timestamp indicates 12:30:28 on July 2, 2021 (UTC+8).
        
        @param request: GetResourceComplianceTimelineRequest
        @return: GetResourceComplianceTimelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_timeline_with_options(request, runtime)

    async def get_resource_compliance_timeline_async(
        self,
        request: config_20200907_models.GetResourceComplianceTimelineRequest,
    ) -> config_20200907_models.GetResourceComplianceTimelineResponse:
        """
        @summary Queries the compliance timeline of a resource. The compliance timeline of a resource indicates the compliance evaluation record of the resource. A compliance timeline includes points and the content on the compliance timeline.
        
        @description In Cloud Config, each resource has a compliance timeline. Cloud Config generates a compliance evaluation record for a resource each time the resource is evaluated based on a rule. The compliance evaluation records of a resource are displayed in a compliance timeline. You can configure Cloud Config to execute a rule to evaluate a resource on a regular basis or each time you change the resource configuration. You can also manually execute a rule to evaluate a resource.
        This topic provides an example on how to query the compliance timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region. The resource is an Object Storage Service (OSS) bucket. The returned result shows the following two timestamps on the compliance timeline: `1625200295276` and `1625200228510`. The first timestamp indicates 12:31:35 on July 2, 2021 (UTC+8) and the second timestamp indicates 12:30:28 on July 2, 2021 (UTC+8).
        
        @param request: GetResourceComplianceTimelineRequest
        @return: GetResourceComplianceTimelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_timeline_with_options_async(request, runtime)

    def get_resource_configuration_timeline_with_options(
        self,
        request: config_20200907_models.GetResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceConfigurationTimelineResponse:
        """
        @summary Queries the configuration timeline of a resource.
        
        @description The sample request in this topic shows you how to query the configuration timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows that the timestamp when the resource configuration changes is `1624961112000`. The timestamp indicates 18:05:12 on June 29, 2021 (UTC+8).
        
        @param request: GetResourceConfigurationTimelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceConfigurationTimelineResponse
        """
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
        """
        @summary Queries the configuration timeline of a resource.
        
        @description The sample request in this topic shows you how to query the configuration timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows that the timestamp when the resource configuration changes is `1624961112000`. The timestamp indicates 18:05:12 on June 29, 2021 (UTC+8).
        
        @param request: GetResourceConfigurationTimelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceConfigurationTimelineResponse
        """
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
        """
        @summary Queries the configuration timeline of a resource.
        
        @description The sample request in this topic shows you how to query the configuration timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows that the timestamp when the resource configuration changes is `1624961112000`. The timestamp indicates 18:05:12 on June 29, 2021 (UTC+8).
        
        @param request: GetResourceConfigurationTimelineRequest
        @return: GetResourceConfigurationTimelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_configuration_timeline_with_options(request, runtime)

    async def get_resource_configuration_timeline_async(
        self,
        request: config_20200907_models.GetResourceConfigurationTimelineRequest,
    ) -> config_20200907_models.GetResourceConfigurationTimelineResponse:
        """
        @summary Queries the configuration timeline of a resource.
        
        @description The sample request in this topic shows you how to query the configuration timeline of the `new-bucket` resource that resides in the `cn-hangzhou` region. The new-bucket resource is an Object Storage Service (OSS) bucket. The return result shows that the timestamp when the resource configuration changes is `1624961112000`. The timestamp indicates 18:05:12 on June 29, 2021 (UTC+8).
        
        @param request: GetResourceConfigurationTimelineRequest
        @return: GetResourceConfigurationTimelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_configuration_timeline_with_options_async(request, runtime)

    def get_resource_inventory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceInventoryResponse:
        """
        @summary Obtains the last resource inventory that is generated within the current Alibaba Cloud account.
        
        @description ### [](#)Prerequisites
        You can call the [GenerateResourceInventory](https://help.aliyun.com/document_detail/2398354.html) operation to generate a resource inventory. Then, you can call the GetResourceInventory operation to obtain the URL of the resource inventory.
        ### [](#)Description
        This topic provides an example on how to obtain the last resource inventory that is generated within the current Alibaba Cloud account.
        
        @param request: GetResourceInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceInventoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceInventory',
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
            config_20200907_models.GetResourceInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_inventory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceInventoryResponse:
        """
        @summary Obtains the last resource inventory that is generated within the current Alibaba Cloud account.
        
        @description ### [](#)Prerequisites
        You can call the [GenerateResourceInventory](https://help.aliyun.com/document_detail/2398354.html) operation to generate a resource inventory. Then, you can call the GetResourceInventory operation to obtain the URL of the resource inventory.
        ### [](#)Description
        This topic provides an example on how to obtain the last resource inventory that is generated within the current Alibaba Cloud account.
        
        @param request: GetResourceInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceInventoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceInventory',
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
            config_20200907_models.GetResourceInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_inventory(self) -> config_20200907_models.GetResourceInventoryResponse:
        """
        @summary Obtains the last resource inventory that is generated within the current Alibaba Cloud account.
        
        @description ### [](#)Prerequisites
        You can call the [GenerateResourceInventory](https://help.aliyun.com/document_detail/2398354.html) operation to generate a resource inventory. Then, you can call the GetResourceInventory operation to obtain the URL of the resource inventory.
        ### [](#)Description
        This topic provides an example on how to obtain the last resource inventory that is generated within the current Alibaba Cloud account.
        
        @return: GetResourceInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_inventory_with_options(runtime)

    async def get_resource_inventory_async(self) -> config_20200907_models.GetResourceInventoryResponse:
        """
        @summary Obtains the last resource inventory that is generated within the current Alibaba Cloud account.
        
        @description ### [](#)Prerequisites
        You can call the [GenerateResourceInventory](https://help.aliyun.com/document_detail/2398354.html) operation to generate a resource inventory. Then, you can call the GetResourceInventory operation to obtain the URL of the resource inventory.
        ### [](#)Description
        This topic provides an example on how to obtain the last resource inventory that is generated within the current Alibaba Cloud account.
        
        @return: GetResourceInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_inventory_with_options_async(runtime)

    def get_supported_resource_relation_config_with_options(
        self,
        request: config_20200907_models.GetSupportedResourceRelationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetSupportedResourceRelationConfigResponse:
        """
        @summary Queries the resource relationships supported by a resource type.
        
        @description This topic provides an example to show how to query the resource relationships that are supported by the ACS::ECS::Instance resource type.
        
        @param request: GetSupportedResourceRelationConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSupportedResourceRelationConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSupportedResourceRelationConfig',
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
            config_20200907_models.GetSupportedResourceRelationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supported_resource_relation_config_with_options_async(
        self,
        request: config_20200907_models.GetSupportedResourceRelationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetSupportedResourceRelationConfigResponse:
        """
        @summary Queries the resource relationships supported by a resource type.
        
        @description This topic provides an example to show how to query the resource relationships that are supported by the ACS::ECS::Instance resource type.
        
        @param request: GetSupportedResourceRelationConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSupportedResourceRelationConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSupportedResourceRelationConfig',
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
            config_20200907_models.GetSupportedResourceRelationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supported_resource_relation_config(
        self,
        request: config_20200907_models.GetSupportedResourceRelationConfigRequest,
    ) -> config_20200907_models.GetSupportedResourceRelationConfigResponse:
        """
        @summary Queries the resource relationships supported by a resource type.
        
        @description This topic provides an example to show how to query the resource relationships that are supported by the ACS::ECS::Instance resource type.
        
        @param request: GetSupportedResourceRelationConfigRequest
        @return: GetSupportedResourceRelationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_supported_resource_relation_config_with_options(request, runtime)

    async def get_supported_resource_relation_config_async(
        self,
        request: config_20200907_models.GetSupportedResourceRelationConfigRequest,
    ) -> config_20200907_models.GetSupportedResourceRelationConfigResponse:
        """
        @summary Queries the resource relationships supported by a resource type.
        
        @description This topic provides an example to show how to query the resource relationships that are supported by the ACS::ECS::Instance resource type.
        
        @param request: GetSupportedResourceRelationConfigRequest
        @return: GetSupportedResourceRelationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_supported_resource_relation_config_with_options_async(request, runtime)

    def ignore_aggregate_evaluation_results_with_options(
        self,
        tmp_req: config_20200907_models.IgnoreAggregateEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.IgnoreAggregateEvaluationResultsResponse:
        """
        @summary Ignores the compliance evaluation results of one or more non-compliant resources that are evaluated based on a rule in an account group.
        
        @description After you ignore a resource that is evaluated as incompliant by using a rule, the resource is still evaluated by using the rule, but the compliance result is Ignored.
        This example shows how to ignore the `lb-hp3a3b4ztyfm2plgm***` incompliant resource that is evaluated by using the `cr-7e72626622af0051***` rule in the `120886317861****` member account of the `ca-5b6c626622af008f****` account group. The ID of the region where the resource resides is `cn-beijing`, and the type of the resource is `ACS::SLB::LoadBalancer`.
        
        @param tmp_req: IgnoreAggregateEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IgnoreAggregateEvaluationResultsResponse
        """
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
        if not UtilClient.is_unset(request.ignore_date):
            body['IgnoreDate'] = request.ignore_date
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
        """
        @summary Ignores the compliance evaluation results of one or more non-compliant resources that are evaluated based on a rule in an account group.
        
        @description After you ignore a resource that is evaluated as incompliant by using a rule, the resource is still evaluated by using the rule, but the compliance result is Ignored.
        This example shows how to ignore the `lb-hp3a3b4ztyfm2plgm***` incompliant resource that is evaluated by using the `cr-7e72626622af0051***` rule in the `120886317861****` member account of the `ca-5b6c626622af008f****` account group. The ID of the region where the resource resides is `cn-beijing`, and the type of the resource is `ACS::SLB::LoadBalancer`.
        
        @param tmp_req: IgnoreAggregateEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IgnoreAggregateEvaluationResultsResponse
        """
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
        if not UtilClient.is_unset(request.ignore_date):
            body['IgnoreDate'] = request.ignore_date
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
        """
        @summary Ignores the compliance evaluation results of one or more non-compliant resources that are evaluated based on a rule in an account group.
        
        @description After you ignore a resource that is evaluated as incompliant by using a rule, the resource is still evaluated by using the rule, but the compliance result is Ignored.
        This example shows how to ignore the `lb-hp3a3b4ztyfm2plgm***` incompliant resource that is evaluated by using the `cr-7e72626622af0051***` rule in the `120886317861****` member account of the `ca-5b6c626622af008f****` account group. The ID of the region where the resource resides is `cn-beijing`, and the type of the resource is `ACS::SLB::LoadBalancer`.
        
        @param request: IgnoreAggregateEvaluationResultsRequest
        @return: IgnoreAggregateEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ignore_aggregate_evaluation_results_with_options(request, runtime)

    async def ignore_aggregate_evaluation_results_async(
        self,
        request: config_20200907_models.IgnoreAggregateEvaluationResultsRequest,
    ) -> config_20200907_models.IgnoreAggregateEvaluationResultsResponse:
        """
        @summary Ignores the compliance evaluation results of one or more non-compliant resources that are evaluated based on a rule in an account group.
        
        @description After you ignore a resource that is evaluated as incompliant by using a rule, the resource is still evaluated by using the rule, but the compliance result is Ignored.
        This example shows how to ignore the `lb-hp3a3b4ztyfm2plgm***` incompliant resource that is evaluated by using the `cr-7e72626622af0051***` rule in the `120886317861****` member account of the `ca-5b6c626622af008f****` account group. The ID of the region where the resource resides is `cn-beijing`, and the type of the resource is `ACS::SLB::LoadBalancer`.
        
        @param request: IgnoreAggregateEvaluationResultsRequest
        @return: IgnoreAggregateEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ignore_aggregate_evaluation_results_with_options_async(request, runtime)

    def ignore_evaluation_results_with_options(
        self,
        tmp_req: config_20200907_models.IgnoreEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.IgnoreEvaluationResultsResponse:
        """
        @summary Ignores one or more resources that are evaluated as non-compliant by using a rule.
        
        @description After you ignore a resource that is evaluated as incompliant by using a rule, the resource is still evaluated by using the rule, but the compliance result is Ignored.
        This example shows how to ignore the `lb-hp3a3b4ztyfm2plgm***` resource that is evaluated as incompliant by using the `cr-7e72626622af0051****` rule in the `100931896542****` account. The ID of the region in which the resource resides is `cn-beijing`, and the type of the resource is `ACS::SLB::LoadBalancer`.
        
        @param tmp_req: IgnoreEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IgnoreEvaluationResultsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.IgnoreEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.ignore_date):
            body['IgnoreDate'] = request.ignore_date
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
        """
        @summary Ignores one or more resources that are evaluated as non-compliant by using a rule.
        
        @description After you ignore a resource that is evaluated as incompliant by using a rule, the resource is still evaluated by using the rule, but the compliance result is Ignored.
        This example shows how to ignore the `lb-hp3a3b4ztyfm2plgm***` resource that is evaluated as incompliant by using the `cr-7e72626622af0051****` rule in the `100931896542****` account. The ID of the region in which the resource resides is `cn-beijing`, and the type of the resource is `ACS::SLB::LoadBalancer`.
        
        @param tmp_req: IgnoreEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IgnoreEvaluationResultsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.IgnoreEvaluationResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        body = {}
        if not UtilClient.is_unset(request.config_rule_id):
            body['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.ignore_date):
            body['IgnoreDate'] = request.ignore_date
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
        """
        @summary Ignores one or more resources that are evaluated as non-compliant by using a rule.
        
        @description After you ignore a resource that is evaluated as incompliant by using a rule, the resource is still evaluated by using the rule, but the compliance result is Ignored.
        This example shows how to ignore the `lb-hp3a3b4ztyfm2plgm***` resource that is evaluated as incompliant by using the `cr-7e72626622af0051****` rule in the `100931896542****` account. The ID of the region in which the resource resides is `cn-beijing`, and the type of the resource is `ACS::SLB::LoadBalancer`.
        
        @param request: IgnoreEvaluationResultsRequest
        @return: IgnoreEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ignore_evaluation_results_with_options(request, runtime)

    async def ignore_evaluation_results_async(
        self,
        request: config_20200907_models.IgnoreEvaluationResultsRequest,
    ) -> config_20200907_models.IgnoreEvaluationResultsResponse:
        """
        @summary Ignores one or more resources that are evaluated as non-compliant by using a rule.
        
        @description After you ignore a resource that is evaluated as incompliant by using a rule, the resource is still evaluated by using the rule, but the compliance result is Ignored.
        This example shows how to ignore the `lb-hp3a3b4ztyfm2plgm***` resource that is evaluated as incompliant by using the `cr-7e72626622af0051****` rule in the `100931896542****` account. The ID of the region in which the resource resides is `cn-beijing`, and the type of the resource is `ACS::SLB::LoadBalancer`.
        
        @param request: IgnoreEvaluationResultsRequest
        @return: IgnoreEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ignore_evaluation_results_with_options_async(request, runtime)

    def list_aggregate_compliance_packs_with_options(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        """
        @summary Queries a list of compliance packages in an account group.
        
        @description In this topic, the `ca-f632626622af0079***` account group is used as an example. The return result shows one compliance package whose ID is `cp-fdc8626622af00f9****`.
        
        @param request: ListAggregateCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateCompliancePacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateCompliancePacks',
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
            config_20200907_models.ListAggregateCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        """
        @summary Queries a list of compliance packages in an account group.
        
        @description In this topic, the `ca-f632626622af0079***` account group is used as an example. The return result shows one compliance package whose ID is `cp-fdc8626622af00f9****`.
        
        @param request: ListAggregateCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateCompliancePacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateCompliancePacks',
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
            config_20200907_models.ListAggregateCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_compliance_packs(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        """
        @summary Queries a list of compliance packages in an account group.
        
        @description In this topic, the `ca-f632626622af0079***` account group is used as an example. The return result shows one compliance package whose ID is `cp-fdc8626622af00f9****`.
        
        @param request: ListAggregateCompliancePacksRequest
        @return: ListAggregateCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_compliance_packs_with_options(request, runtime)

    async def list_aggregate_compliance_packs_async(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        """
        @summary Queries a list of compliance packages in an account group.
        
        @description In this topic, the `ca-f632626622af0079***` account group is used as an example. The return result shows one compliance package whose ID is `cp-fdc8626622af00f9****`.
        
        @param request: ListAggregateCompliancePacksRequest
        @return: ListAggregateCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_compliance_packs_with_options_async(request, runtime)

    def list_aggregate_config_delivery_channels_with_options(
        self,
        request: config_20200907_models.ListAggregateConfigDeliveryChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigDeliveryChannelsResponse:
        """
        @summary Queries the information about all delivery channels in an account group.
        
        @param request: ListAggregateConfigDeliveryChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateConfigDeliveryChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.delivery_channel_ids):
            query['DeliveryChannelIds'] = request.delivery_channel_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigDeliveryChannels',
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
            config_20200907_models.ListAggregateConfigDeliveryChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_delivery_channels_with_options_async(
        self,
        request: config_20200907_models.ListAggregateConfigDeliveryChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigDeliveryChannelsResponse:
        """
        @summary Queries the information about all delivery channels in an account group.
        
        @param request: ListAggregateConfigDeliveryChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateConfigDeliveryChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.delivery_channel_ids):
            query['DeliveryChannelIds'] = request.delivery_channel_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigDeliveryChannels',
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
            config_20200907_models.ListAggregateConfigDeliveryChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_delivery_channels(
        self,
        request: config_20200907_models.ListAggregateConfigDeliveryChannelsRequest,
    ) -> config_20200907_models.ListAggregateConfigDeliveryChannelsResponse:
        """
        @summary Queries the information about all delivery channels in an account group.
        
        @param request: ListAggregateConfigDeliveryChannelsRequest
        @return: ListAggregateConfigDeliveryChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_config_delivery_channels_with_options(request, runtime)

    async def list_aggregate_config_delivery_channels_async(
        self,
        request: config_20200907_models.ListAggregateConfigDeliveryChannelsRequest,
    ) -> config_20200907_models.ListAggregateConfigDeliveryChannelsResponse:
        """
        @summary Queries the information about all delivery channels in an account group.
        
        @param request: ListAggregateConfigDeliveryChannelsRequest
        @return: ListAggregateConfigDeliveryChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_config_delivery_channels_with_options_async(request, runtime)

    def list_aggregate_config_rule_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources based on a rule in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources based on the `cr-888f626622af00ae***` rule in the `ca-d1e3326622af00cb****` account group. The returned result indicates that the `Bucket-test` resource is evaluated as `NON_COMPLIANT` by using the rule. The resource is an Object Storage Service (OSS) bucket.
        
        @param request: ListAggregateConfigRuleEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateConfigRuleEvaluationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRuleEvaluationResults',
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
            config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_rule_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources based on a rule in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources based on the `cr-888f626622af00ae***` rule in the `ca-d1e3326622af00cb****` account group. The returned result indicates that the `Bucket-test` resource is evaluated as `NON_COMPLIANT` by using the rule. The resource is an Object Storage Service (OSS) bucket.
        
        @param request: ListAggregateConfigRuleEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateConfigRuleEvaluationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRuleEvaluationResults',
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
            config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_rule_evaluation_results(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources based on a rule in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources based on the `cr-888f626622af00ae***` rule in the `ca-d1e3326622af00cb****` account group. The returned result indicates that the `Bucket-test` resource is evaluated as `NON_COMPLIANT` by using the rule. The resource is an Object Storage Service (OSS) bucket.
        
        @param request: ListAggregateConfigRuleEvaluationResultsRequest
        @return: ListAggregateConfigRuleEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_config_rule_evaluation_results_with_options(request, runtime)

    async def list_aggregate_config_rule_evaluation_results_async(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationResultsRequest,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources based on a rule in an account group.
        
        @description This topic provides an example on how to query the compliance evaluation results of resources based on the `cr-888f626622af00ae***` rule in the `ca-d1e3326622af00cb****` account group. The returned result indicates that the `Bucket-test` resource is evaluated as `NON_COMPLIANT` by using the rule. The resource is an Object Storage Service (OSS) bucket.
        
        @param request: ListAggregateConfigRuleEvaluationResultsRequest
        @return: ListAggregateConfigRuleEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_config_rule_evaluation_results_with_options_async(request, runtime)

    def list_aggregate_config_rule_evaluation_statistics_with_options(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsResponse:
        """
        @summary Queries the statistics of compliance evaluation results of an account group.
        
        @description This topic provides an example on how to query the statistics of compliance evaluation results of an account group whose ID is ca-edd3626622af00b3\\\\*\\*\\*.
        
        @param request: ListAggregateConfigRuleEvaluationStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateConfigRuleEvaluationStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRuleEvaluationStatistics',
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
            config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_rule_evaluation_statistics_with_options_async(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsResponse:
        """
        @summary Queries the statistics of compliance evaluation results of an account group.
        
        @description This topic provides an example on how to query the statistics of compliance evaluation results of an account group whose ID is ca-edd3626622af00b3\\\\*\\*\\*.
        
        @param request: ListAggregateConfigRuleEvaluationStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateConfigRuleEvaluationStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRuleEvaluationStatistics',
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
            config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_rule_evaluation_statistics(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsRequest,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsResponse:
        """
        @summary Queries the statistics of compliance evaluation results of an account group.
        
        @description This topic provides an example on how to query the statistics of compliance evaluation results of an account group whose ID is ca-edd3626622af00b3\\\\*\\*\\*.
        
        @param request: ListAggregateConfigRuleEvaluationStatisticsRequest
        @return: ListAggregateConfigRuleEvaluationStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_config_rule_evaluation_statistics_with_options(request, runtime)

    async def list_aggregate_config_rule_evaluation_statistics_async(
        self,
        request: config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsRequest,
    ) -> config_20200907_models.ListAggregateConfigRuleEvaluationStatisticsResponse:
        """
        @summary Queries the statistics of compliance evaluation results of an account group.
        
        @description This topic provides an example on how to query the statistics of compliance evaluation results of an account group whose ID is ca-edd3626622af00b3\\\\*\\*\\*.
        
        @param request: ListAggregateConfigRuleEvaluationStatisticsRequest
        @return: ListAggregateConfigRuleEvaluationStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_config_rule_evaluation_statistics_with_options_async(request, runtime)

    def list_aggregate_config_rules_with_options(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        """
        @summary Queries a list of rules in an account group.
        
        @description This topic provides an example on how to query the rules in an account group whose ID is `ca-f632626622af0079***`. The returned result shows a total of one rule and two evaluated resources. The resources are both evaluated as `COMPLIANT`.
        
        @param request: ListAggregateConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_name):
            query['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_state):
            query['ConfigRuleState'] = request.config_rule_state
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRules',
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
            config_20200907_models.ListAggregateConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_config_rules_with_options_async(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        """
        @summary Queries a list of rules in an account group.
        
        @description This topic provides an example on how to query the rules in an account group whose ID is `ca-f632626622af0079***`. The returned result shows a total of one rule and two evaluated resources. The resources are both evaluated as `COMPLIANT`.
        
        @param request: ListAggregateConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_name):
            query['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_state):
            query['ConfigRuleState'] = request.config_rule_state
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateConfigRules',
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
            config_20200907_models.ListAggregateConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_config_rules(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        """
        @summary Queries a list of rules in an account group.
        
        @description This topic provides an example on how to query the rules in an account group whose ID is `ca-f632626622af0079***`. The returned result shows a total of one rule and two evaluated resources. The resources are both evaluated as `COMPLIANT`.
        
        @param request: ListAggregateConfigRulesRequest
        @return: ListAggregateConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_config_rules_with_options(request, runtime)

    async def list_aggregate_config_rules_async(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        """
        @summary Queries a list of rules in an account group.
        
        @description This topic provides an example on how to query the rules in an account group whose ID is `ca-f632626622af0079***`. The returned result shows a total of one rule and two evaluated resources. The resources are both evaluated as `COMPLIANT`.
        
        @param request: ListAggregateConfigRulesRequest
        @return: ListAggregateConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_config_rules_with_options_async(request, runtime)

    def list_aggregate_discovered_resources_with_options(
        self,
        request: config_20200907_models.ListAggregateDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateDiscoveredResourcesResponse:
        """
        @summary Obtains a list of resources aggregated across regions within all member accounts of a specific account group.
        
        @description This topic provides an example on how to query the resources within the member account `100931896542***` of the account group `ca-c560626622af0005****`. The result indicates that eight resources are queried.
        
        @param request: ListAggregateDiscoveredResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateDiscoveredResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateDiscoveredResources',
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
            config_20200907_models.ListAggregateDiscoveredResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_discovered_resources_with_options_async(
        self,
        request: config_20200907_models.ListAggregateDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateDiscoveredResourcesResponse:
        """
        @summary Obtains a list of resources aggregated across regions within all member accounts of a specific account group.
        
        @description This topic provides an example on how to query the resources within the member account `100931896542***` of the account group `ca-c560626622af0005****`. The result indicates that eight resources are queried.
        
        @param request: ListAggregateDiscoveredResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateDiscoveredResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateDiscoveredResources',
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
            config_20200907_models.ListAggregateDiscoveredResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_discovered_resources(
        self,
        request: config_20200907_models.ListAggregateDiscoveredResourcesRequest,
    ) -> config_20200907_models.ListAggregateDiscoveredResourcesResponse:
        """
        @summary Obtains a list of resources aggregated across regions within all member accounts of a specific account group.
        
        @description This topic provides an example on how to query the resources within the member account `100931896542***` of the account group `ca-c560626622af0005****`. The result indicates that eight resources are queried.
        
        @param request: ListAggregateDiscoveredResourcesRequest
        @return: ListAggregateDiscoveredResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_discovered_resources_with_options(request, runtime)

    async def list_aggregate_discovered_resources_async(
        self,
        request: config_20200907_models.ListAggregateDiscoveredResourcesRequest,
    ) -> config_20200907_models.ListAggregateDiscoveredResourcesResponse:
        """
        @summary Obtains a list of resources aggregated across regions within all member accounts of a specific account group.
        
        @description This topic provides an example on how to query the resources within the member account `100931896542***` of the account group `ca-c560626622af0005****`. The result indicates that eight resources are queried.
        
        @param request: ListAggregateDiscoveredResourcesRequest
        @return: ListAggregateDiscoveredResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_discovered_resources_with_options_async(request, runtime)

    def list_aggregate_remediation_executions_with_options(
        self,
        request: config_20200907_models.ListAggregateRemediationExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateRemediationExecutionsResponse:
        """
        @summary Queries the remediation records of a rule in an account group.
        
        @description This topic provides an example on how to query the remediation records of the `cr-d04a626622af00af***` rule in the `ca-edd3626622af00b3****` account group.
        
        @param request: ListAggregateRemediationExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateRemediationExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateRemediationExecutions',
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
            config_20200907_models.ListAggregateRemediationExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_remediation_executions_with_options_async(
        self,
        request: config_20200907_models.ListAggregateRemediationExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateRemediationExecutionsResponse:
        """
        @summary Queries the remediation records of a rule in an account group.
        
        @description This topic provides an example on how to query the remediation records of the `cr-d04a626622af00af***` rule in the `ca-edd3626622af00b3****` account group.
        
        @param request: ListAggregateRemediationExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateRemediationExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateRemediationExecutions',
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
            config_20200907_models.ListAggregateRemediationExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_remediation_executions(
        self,
        request: config_20200907_models.ListAggregateRemediationExecutionsRequest,
    ) -> config_20200907_models.ListAggregateRemediationExecutionsResponse:
        """
        @summary Queries the remediation records of a rule in an account group.
        
        @description This topic provides an example on how to query the remediation records of the `cr-d04a626622af00af***` rule in the `ca-edd3626622af00b3****` account group.
        
        @param request: ListAggregateRemediationExecutionsRequest
        @return: ListAggregateRemediationExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_remediation_executions_with_options(request, runtime)

    async def list_aggregate_remediation_executions_async(
        self,
        request: config_20200907_models.ListAggregateRemediationExecutionsRequest,
    ) -> config_20200907_models.ListAggregateRemediationExecutionsResponse:
        """
        @summary Queries the remediation records of a rule in an account group.
        
        @description This topic provides an example on how to query the remediation records of the `cr-d04a626622af00af***` rule in the `ca-edd3626622af00b3****` account group.
        
        @param request: ListAggregateRemediationExecutionsRequest
        @return: ListAggregateRemediationExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_remediation_executions_with_options_async(request, runtime)

    def list_aggregate_remediations_with_options(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
        """
        @summary Queries a list of remediation templates for a rule in an account group.
        
        @description This topic provides an example on how to query the remediation templates of the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`.
        
        @param request: ListAggregateRemediationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateRemediationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateRemediations',
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
            config_20200907_models.ListAggregateRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_remediations_with_options_async(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
        """
        @summary Queries a list of remediation templates for a rule in an account group.
        
        @description This topic provides an example on how to query the remediation templates of the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`.
        
        @param request: ListAggregateRemediationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateRemediationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateRemediations',
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
            config_20200907_models.ListAggregateRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_remediations(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
        """
        @summary Queries a list of remediation templates for a rule in an account group.
        
        @description This topic provides an example on how to query the remediation templates of the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`.
        
        @param request: ListAggregateRemediationsRequest
        @return: ListAggregateRemediationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_remediations_with_options(request, runtime)

    async def list_aggregate_remediations_async(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
        """
        @summary Queries a list of remediation templates for a rule in an account group.
        
        @description This topic provides an example on how to query the remediation templates of the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`.
        
        @param request: ListAggregateRemediationsRequest
        @return: ListAggregateRemediationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_remediations_with_options_async(request, runtime)

    def list_aggregate_resource_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources in an account group.
        
        @description This example shows how to query the compliance evaluation result of the `23642660635396***` resource in the `ca-7f00626622af0041****` account group. The resource is a RAM user. The returned result indicates that the resource is evaluated as `NON_COMPLIANT` by using the `cr-7f7d626622af0041****` rule.
        
        @param request: ListAggregateResourceEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateResourceEvaluationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateResourceEvaluationResults',
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
            config_20200907_models.ListAggregateResourceEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_resource_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources in an account group.
        
        @description This example shows how to query the compliance evaluation result of the `23642660635396***` resource in the `ca-7f00626622af0041****` account group. The resource is a RAM user. The returned result indicates that the resource is evaluated as `NON_COMPLIANT` by using the `cr-7f7d626622af0041****` rule.
        
        @param request: ListAggregateResourceEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateResourceEvaluationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateResourceEvaluationResults',
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
            config_20200907_models.ListAggregateResourceEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_resource_evaluation_results(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources in an account group.
        
        @description This example shows how to query the compliance evaluation result of the `23642660635396***` resource in the `ca-7f00626622af0041****` account group. The resource is a RAM user. The returned result indicates that the resource is evaluated as `NON_COMPLIANT` by using the `cr-7f7d626622af0041****` rule.
        
        @param request: ListAggregateResourceEvaluationResultsRequest
        @return: ListAggregateResourceEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_resource_evaluation_results_with_options(request, runtime)

    async def list_aggregate_resource_evaluation_results_async(
        self,
        request: config_20200907_models.ListAggregateResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListAggregateResourceEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources in an account group.
        
        @description This example shows how to query the compliance evaluation result of the `23642660635396***` resource in the `ca-7f00626622af0041****` account group. The resource is a RAM user. The returned result indicates that the resource is evaluated as `NON_COMPLIANT` by using the `cr-7f7d626622af0041****` rule.
        
        @param request: ListAggregateResourceEvaluationResultsRequest
        @return: ListAggregateResourceEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_resource_evaluation_results_with_options_async(request, runtime)

    def list_aggregate_resource_relations_with_options(
        self,
        request: config_20200907_models.ListAggregateResourceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourceRelationsResponse:
        """
        @summary Queries a list of the resources of a specific resource in an account group.
        
        @description This topic provides an example on how to query the disks that are associated with an Elastic Compute Service (ECS) instance in an account group.
        
        @param request: ListAggregateResourceRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateResourceRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target_resource_id):
            query['TargetResourceId'] = request.target_resource_id
        if not UtilClient.is_unset(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateResourceRelations',
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
            config_20200907_models.ListAggregateResourceRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_resource_relations_with_options_async(
        self,
        request: config_20200907_models.ListAggregateResourceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourceRelationsResponse:
        """
        @summary Queries a list of the resources of a specific resource in an account group.
        
        @description This topic provides an example on how to query the disks that are associated with an Elastic Compute Service (ECS) instance in an account group.
        
        @param request: ListAggregateResourceRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateResourceRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target_resource_id):
            query['TargetResourceId'] = request.target_resource_id
        if not UtilClient.is_unset(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateResourceRelations',
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
            config_20200907_models.ListAggregateResourceRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_resource_relations(
        self,
        request: config_20200907_models.ListAggregateResourceRelationsRequest,
    ) -> config_20200907_models.ListAggregateResourceRelationsResponse:
        """
        @summary Queries a list of the resources of a specific resource in an account group.
        
        @description This topic provides an example on how to query the disks that are associated with an Elastic Compute Service (ECS) instance in an account group.
        
        @param request: ListAggregateResourceRelationsRequest
        @return: ListAggregateResourceRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_resource_relations_with_options(request, runtime)

    async def list_aggregate_resource_relations_async(
        self,
        request: config_20200907_models.ListAggregateResourceRelationsRequest,
    ) -> config_20200907_models.ListAggregateResourceRelationsResponse:
        """
        @summary Queries a list of the resources of a specific resource in an account group.
        
        @description This topic provides an example on how to query the disks that are associated with an Elastic Compute Service (ECS) instance in an account group.
        
        @param request: ListAggregateResourceRelationsRequest
        @return: ListAggregateResourceRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_resource_relations_with_options_async(request, runtime)

    def list_aggregate_resources_by_advanced_search_with_options(
        self,
        request: config_20200907_models.ListAggregateResourcesByAdvancedSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourcesByAdvancedSearchResponse:
        """
        @summary Obtains resources in a specific account group based on the fields in the resource properties by using a SELECT statement.
        
        @description When you write a `SELECT` statement, you must obtain the fields and the data types of the fields from the property file of the resource type. For more information about property files, see [Alibaba Cloud Config Resource Schema](javascript:void\\(0\\))
        >
        Each resource type supported by Cloud Config has a property file. Property files are named based on the related resource types. For example, the property file of the `ACS::ECS::Instance` resource type is named `ACS_ECS_Instance.properties.json`. Property files of different resource types are placed under the `config/properties/resource-types` path.
        For more information about the examples and limits on SQL query statements, see [Examples of SQL query statements](https://help.aliyun.com/document_detail/398718.html) and [Limits on SQL query statements](https://help.aliyun.com/document_detail/398750.html).
        This topic provides an example on how to obtain all resources whose tag key is `business` and whose tag value is `online` in the account group `ca-4b05626622af000c***` by using the advanced search feature.
        
        @param request: ListAggregateResourcesByAdvancedSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateResourcesByAdvancedSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateResourcesByAdvancedSearch',
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
            config_20200907_models.ListAggregateResourcesByAdvancedSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_resources_by_advanced_search_with_options_async(
        self,
        request: config_20200907_models.ListAggregateResourcesByAdvancedSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateResourcesByAdvancedSearchResponse:
        """
        @summary Obtains resources in a specific account group based on the fields in the resource properties by using a SELECT statement.
        
        @description When you write a `SELECT` statement, you must obtain the fields and the data types of the fields from the property file of the resource type. For more information about property files, see [Alibaba Cloud Config Resource Schema](javascript:void\\(0\\))
        >
        Each resource type supported by Cloud Config has a property file. Property files are named based on the related resource types. For example, the property file of the `ACS::ECS::Instance` resource type is named `ACS_ECS_Instance.properties.json`. Property files of different resource types are placed under the `config/properties/resource-types` path.
        For more information about the examples and limits on SQL query statements, see [Examples of SQL query statements](https://help.aliyun.com/document_detail/398718.html) and [Limits on SQL query statements](https://help.aliyun.com/document_detail/398750.html).
        This topic provides an example on how to obtain all resources whose tag key is `business` and whose tag value is `online` in the account group `ca-4b05626622af000c***` by using the advanced search feature.
        
        @param request: ListAggregateResourcesByAdvancedSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregateResourcesByAdvancedSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateResourcesByAdvancedSearch',
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
            config_20200907_models.ListAggregateResourcesByAdvancedSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_resources_by_advanced_search(
        self,
        request: config_20200907_models.ListAggregateResourcesByAdvancedSearchRequest,
    ) -> config_20200907_models.ListAggregateResourcesByAdvancedSearchResponse:
        """
        @summary Obtains resources in a specific account group based on the fields in the resource properties by using a SELECT statement.
        
        @description When you write a `SELECT` statement, you must obtain the fields and the data types of the fields from the property file of the resource type. For more information about property files, see [Alibaba Cloud Config Resource Schema](javascript:void\\(0\\))
        >
        Each resource type supported by Cloud Config has a property file. Property files are named based on the related resource types. For example, the property file of the `ACS::ECS::Instance` resource type is named `ACS_ECS_Instance.properties.json`. Property files of different resource types are placed under the `config/properties/resource-types` path.
        For more information about the examples and limits on SQL query statements, see [Examples of SQL query statements](https://help.aliyun.com/document_detail/398718.html) and [Limits on SQL query statements](https://help.aliyun.com/document_detail/398750.html).
        This topic provides an example on how to obtain all resources whose tag key is `business` and whose tag value is `online` in the account group `ca-4b05626622af000c***` by using the advanced search feature.
        
        @param request: ListAggregateResourcesByAdvancedSearchRequest
        @return: ListAggregateResourcesByAdvancedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_resources_by_advanced_search_with_options(request, runtime)

    async def list_aggregate_resources_by_advanced_search_async(
        self,
        request: config_20200907_models.ListAggregateResourcesByAdvancedSearchRequest,
    ) -> config_20200907_models.ListAggregateResourcesByAdvancedSearchResponse:
        """
        @summary Obtains resources in a specific account group based on the fields in the resource properties by using a SELECT statement.
        
        @description When you write a `SELECT` statement, you must obtain the fields and the data types of the fields from the property file of the resource type. For more information about property files, see [Alibaba Cloud Config Resource Schema](javascript:void\\(0\\))
        >
        Each resource type supported by Cloud Config has a property file. Property files are named based on the related resource types. For example, the property file of the `ACS::ECS::Instance` resource type is named `ACS_ECS_Instance.properties.json`. Property files of different resource types are placed under the `config/properties/resource-types` path.
        For more information about the examples and limits on SQL query statements, see [Examples of SQL query statements](https://help.aliyun.com/document_detail/398718.html) and [Limits on SQL query statements](https://help.aliyun.com/document_detail/398750.html).
        This topic provides an example on how to obtain all resources whose tag key is `business` and whose tag value is `online` in the account group `ca-4b05626622af000c***` by using the advanced search feature.
        
        @param request: ListAggregateResourcesByAdvancedSearchRequest
        @return: ListAggregateResourcesByAdvancedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_resources_by_advanced_search_with_options_async(request, runtime)

    def list_aggregators_with_options(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregatorsResponse:
        """
        @summary Queries a list of account groups that the current account manages or to which the current account belongs.
        
        @description The sample request in this topic shows you how to query account groups. A maximum of 10 entries can be returned for the request. As shown in the responses, the account group returned is named as `Test_Group`, its description is `Test account group`, and it is of the `CUSTOM` type, which indicates a custom account group. The account group contains two member accounts.
        
        @param request: ListAggregatorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregatorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregators',
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
            config_20200907_models.ListAggregatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregators_with_options_async(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregatorsResponse:
        """
        @summary Queries a list of account groups that the current account manages or to which the current account belongs.
        
        @description The sample request in this topic shows you how to query account groups. A maximum of 10 entries can be returned for the request. As shown in the responses, the account group returned is named as `Test_Group`, its description is `Test account group`, and it is of the `CUSTOM` type, which indicates a custom account group. The account group contains two member accounts.
        
        @param request: ListAggregatorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggregatorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregators',
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
            config_20200907_models.ListAggregatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregators(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
    ) -> config_20200907_models.ListAggregatorsResponse:
        """
        @summary Queries a list of account groups that the current account manages or to which the current account belongs.
        
        @description The sample request in this topic shows you how to query account groups. A maximum of 10 entries can be returned for the request. As shown in the responses, the account group returned is named as `Test_Group`, its description is `Test account group`, and it is of the `CUSTOM` type, which indicates a custom account group. The account group contains two member accounts.
        
        @param request: ListAggregatorsRequest
        @return: ListAggregatorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aggregators_with_options(request, runtime)

    async def list_aggregators_async(
        self,
        request: config_20200907_models.ListAggregatorsRequest,
    ) -> config_20200907_models.ListAggregatorsResponse:
        """
        @summary Queries a list of account groups that the current account manages or to which the current account belongs.
        
        @description The sample request in this topic shows you how to query account groups. A maximum of 10 entries can be returned for the request. As shown in the responses, the account group returned is named as `Test_Group`, its description is `Test account group`, and it is of the `CUSTOM` type, which indicates a custom account group. The account group contains two member accounts.
        
        @param request: ListAggregatorsRequest
        @return: ListAggregatorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregators_with_options_async(request, runtime)

    def list_compliance_pack_templates_with_options(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        """
        @summary Queries all compliance package templates provided by Cloud Config and the details of the compliance package templates.
        
        @description This topic provides an example on how to query the details of a compliance package template whose ID is `ct-d254ff4e06a300cf***`. The returned result indicates that the template name is `BestPracticesForNetwork`, the template ID is `ct-d254ff4e06a300cf****`, and the ID of the managed rule of the template is `slb-servercertificate-expired-check`.
        
        @param request: ListCompliancePackTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCompliancePackTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_pack_template_id):
            query['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCompliancePackTemplates',
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
            config_20200907_models.ListCompliancePackTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compliance_pack_templates_with_options_async(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        """
        @summary Queries all compliance package templates provided by Cloud Config and the details of the compliance package templates.
        
        @description This topic provides an example on how to query the details of a compliance package template whose ID is `ct-d254ff4e06a300cf***`. The returned result indicates that the template name is `BestPracticesForNetwork`, the template ID is `ct-d254ff4e06a300cf****`, and the ID of the managed rule of the template is `slb-servercertificate-expired-check`.
        
        @param request: ListCompliancePackTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCompliancePackTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_pack_template_id):
            query['CompliancePackTemplateId'] = request.compliance_pack_template_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCompliancePackTemplates',
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
            config_20200907_models.ListCompliancePackTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compliance_pack_templates(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        """
        @summary Queries all compliance package templates provided by Cloud Config and the details of the compliance package templates.
        
        @description This topic provides an example on how to query the details of a compliance package template whose ID is `ct-d254ff4e06a300cf***`. The returned result indicates that the template name is `BestPracticesForNetwork`, the template ID is `ct-d254ff4e06a300cf****`, and the ID of the managed rule of the template is `slb-servercertificate-expired-check`.
        
        @param request: ListCompliancePackTemplatesRequest
        @return: ListCompliancePackTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_compliance_pack_templates_with_options(request, runtime)

    async def list_compliance_pack_templates_async(
        self,
        request: config_20200907_models.ListCompliancePackTemplatesRequest,
    ) -> config_20200907_models.ListCompliancePackTemplatesResponse:
        """
        @summary Queries all compliance package templates provided by Cloud Config and the details of the compliance package templates.
        
        @description This topic provides an example on how to query the details of a compliance package template whose ID is `ct-d254ff4e06a300cf***`. The returned result indicates that the template name is `BestPracticesForNetwork`, the template ID is `ct-d254ff4e06a300cf****`, and the ID of the managed rule of the template is `slb-servercertificate-expired-check`.
        
        @param request: ListCompliancePackTemplatesRequest
        @return: ListCompliancePackTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_compliance_pack_templates_with_options_async(request, runtime)

    def list_compliance_packs_with_options(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        """
        @summary Queries a list of compliance packages.
        
        @description This topic provides an example of how to query compliance packages. The return result shows the details of the `cp-fdc8626622af00f9***` compliance package.
        
        @param request: ListCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCompliancePacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCompliancePacks',
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
            config_20200907_models.ListCompliancePacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compliance_packs_with_options_async(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        """
        @summary Queries a list of compliance packages.
        
        @description This topic provides an example of how to query compliance packages. The return result shows the details of the `cp-fdc8626622af00f9***` compliance package.
        
        @param request: ListCompliancePacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCompliancePacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCompliancePacks',
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
            config_20200907_models.ListCompliancePacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compliance_packs(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        """
        @summary Queries a list of compliance packages.
        
        @description This topic provides an example of how to query compliance packages. The return result shows the details of the `cp-fdc8626622af00f9***` compliance package.
        
        @param request: ListCompliancePacksRequest
        @return: ListCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_compliance_packs_with_options(request, runtime)

    async def list_compliance_packs_async(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        """
        @summary Queries a list of compliance packages.
        
        @description This topic provides an example of how to query compliance packages. The return result shows the details of the `cp-fdc8626622af00f9***` compliance package.
        
        @param request: ListCompliancePacksRequest
        @return: ListCompliancePacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_compliance_packs_with_options_async(request, runtime)

    def list_config_delivery_channels_with_options(
        self,
        request: config_20200907_models.ListConfigDeliveryChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigDeliveryChannelsResponse:
        """
        @summary Queries a list of delivery channels.
        
        @param request: ListConfigDeliveryChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigDeliveryChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_channel_ids):
            query['DeliveryChannelIds'] = request.delivery_channel_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigDeliveryChannels',
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
            config_20200907_models.ListConfigDeliveryChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_delivery_channels_with_options_async(
        self,
        request: config_20200907_models.ListConfigDeliveryChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigDeliveryChannelsResponse:
        """
        @summary Queries a list of delivery channels.
        
        @param request: ListConfigDeliveryChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigDeliveryChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_channel_ids):
            query['DeliveryChannelIds'] = request.delivery_channel_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigDeliveryChannels',
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
            config_20200907_models.ListConfigDeliveryChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_delivery_channels(
        self,
        request: config_20200907_models.ListConfigDeliveryChannelsRequest,
    ) -> config_20200907_models.ListConfigDeliveryChannelsResponse:
        """
        @summary Queries a list of delivery channels.
        
        @param request: ListConfigDeliveryChannelsRequest
        @return: ListConfigDeliveryChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_config_delivery_channels_with_options(request, runtime)

    async def list_config_delivery_channels_async(
        self,
        request: config_20200907_models.ListConfigDeliveryChannelsRequest,
    ) -> config_20200907_models.ListConfigDeliveryChannelsResponse:
        """
        @summary Queries a list of delivery channels.
        
        @param request: ListConfigDeliveryChannelsRequest
        @return: ListConfigDeliveryChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_config_delivery_channels_with_options_async(request, runtime)

    def list_config_rule_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListConfigRuleEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRuleEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources based on a rule.
        
        @description This topic provides an example on how to query the compliance evaluation result of resources based on a rule whose ID is `cr-cac56457e0d900d3***`. The returned result indicates that the `i-hp3e4kvhzqn2s11t****` resource is evaluated as `NON_COMPLIANT` by using the rule. The resource is an Elastic Compute Service (ECS) instance.
        
        @param request: ListConfigRuleEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigRuleEvaluationResultsResponse
        """
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
        """
        @summary Queries the compliance evaluation results of resources based on a rule.
        
        @description This topic provides an example on how to query the compliance evaluation result of resources based on a rule whose ID is `cr-cac56457e0d900d3***`. The returned result indicates that the `i-hp3e4kvhzqn2s11t****` resource is evaluated as `NON_COMPLIANT` by using the rule. The resource is an Elastic Compute Service (ECS) instance.
        
        @param request: ListConfigRuleEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigRuleEvaluationResultsResponse
        """
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
        """
        @summary Queries the compliance evaluation results of resources based on a rule.
        
        @description This topic provides an example on how to query the compliance evaluation result of resources based on a rule whose ID is `cr-cac56457e0d900d3***`. The returned result indicates that the `i-hp3e4kvhzqn2s11t****` resource is evaluated as `NON_COMPLIANT` by using the rule. The resource is an Elastic Compute Service (ECS) instance.
        
        @param request: ListConfigRuleEvaluationResultsRequest
        @return: ListConfigRuleEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_config_rule_evaluation_results_with_options(request, runtime)

    async def list_config_rule_evaluation_results_async(
        self,
        request: config_20200907_models.ListConfigRuleEvaluationResultsRequest,
    ) -> config_20200907_models.ListConfigRuleEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources based on a rule.
        
        @description This topic provides an example on how to query the compliance evaluation result of resources based on a rule whose ID is `cr-cac56457e0d900d3***`. The returned result indicates that the `i-hp3e4kvhzqn2s11t****` resource is evaluated as `NON_COMPLIANT` by using the rule. The resource is an Elastic Compute Service (ECS) instance.
        
        @param request: ListConfigRuleEvaluationResultsRequest
        @return: ListConfigRuleEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_config_rule_evaluation_results_with_options_async(request, runtime)

    def list_config_rule_evaluation_statistics_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRuleEvaluationStatisticsResponse:
        """
        @summary Queries the statistics of compliance evaluation results of the current Alibaba Cloud account.
        
        @param request: ListConfigRuleEvaluationStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigRuleEvaluationStatisticsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListConfigRuleEvaluationStatistics',
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
            config_20200907_models.ListConfigRuleEvaluationStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rule_evaluation_statistics_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRuleEvaluationStatisticsResponse:
        """
        @summary Queries the statistics of compliance evaluation results of the current Alibaba Cloud account.
        
        @param request: ListConfigRuleEvaluationStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigRuleEvaluationStatisticsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListConfigRuleEvaluationStatistics',
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
            config_20200907_models.ListConfigRuleEvaluationStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rule_evaluation_statistics(self) -> config_20200907_models.ListConfigRuleEvaluationStatisticsResponse:
        """
        @summary Queries the statistics of compliance evaluation results of the current Alibaba Cloud account.
        
        @return: ListConfigRuleEvaluationStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_config_rule_evaluation_statistics_with_options(runtime)

    async def list_config_rule_evaluation_statistics_async(self) -> config_20200907_models.ListConfigRuleEvaluationStatisticsResponse:
        """
        @summary Queries the statistics of compliance evaluation results of the current Alibaba Cloud account.
        
        @return: ListConfigRuleEvaluationStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_config_rule_evaluation_statistics_with_options_async(runtime)

    def list_config_rules_with_options(
        self,
        request: config_20200907_models.ListConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRulesResponse:
        """
        @summary Queries the rules of the current account.
        
        @description This topic provides an example on how to query the rules of the current account. The response shows that the current account has a total of one rule and three evaluated resources. The resources are evaluated as compliant.
        
        @param request: ListConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_name):
            query['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_state):
            query['ConfigRuleState'] = request.config_rule_state
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigRules',
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
            config_20200907_models.ListConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rules_with_options_async(
        self,
        request: config_20200907_models.ListConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigRulesResponse:
        """
        @summary Queries the rules of the current account.
        
        @description This topic provides an example on how to query the rules of the current account. The response shows that the current account has a total of one rule and three evaluated resources. The resources are evaluated as compliant.
        
        @param request: ListConfigRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_name):
            query['ConfigRuleName'] = request.config_rule_name
        if not UtilClient.is_unset(request.config_rule_state):
            query['ConfigRuleState'] = request.config_rule_state
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigRules',
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
            config_20200907_models.ListConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rules(
        self,
        request: config_20200907_models.ListConfigRulesRequest,
    ) -> config_20200907_models.ListConfigRulesResponse:
        """
        @summary Queries the rules of the current account.
        
        @description This topic provides an example on how to query the rules of the current account. The response shows that the current account has a total of one rule and three evaluated resources. The resources are evaluated as compliant.
        
        @param request: ListConfigRulesRequest
        @return: ListConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_config_rules_with_options(request, runtime)

    async def list_config_rules_async(
        self,
        request: config_20200907_models.ListConfigRulesRequest,
    ) -> config_20200907_models.ListConfigRulesResponse:
        """
        @summary Queries the rules of the current account.
        
        @description This topic provides an example on how to query the rules of the current account. The response shows that the current account has a total of one rule and three evaluated resources. The resources are evaluated as compliant.
        
        @param request: ListConfigRulesRequest
        @return: ListConfigRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_config_rules_with_options_async(request, runtime)

    def list_discovered_resources_with_options(
        self,
        request: config_20200907_models.ListDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListDiscoveredResourcesResponse:
        """
        @summary Obtains a list of resources aggregated across regions within an Alibaba Cloud account.
        
        @description This topic provides an example on how to call the ListDiscoveredResources operation to query the resources in the current Alibaba Cloud account. The returned result indicates that a total of eight resources exist in the account.
        
        @param request: ListDiscoveredResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDiscoveredResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiscoveredResources',
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
            config_20200907_models.ListDiscoveredResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_discovered_resources_with_options_async(
        self,
        request: config_20200907_models.ListDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListDiscoveredResourcesResponse:
        """
        @summary Obtains a list of resources aggregated across regions within an Alibaba Cloud account.
        
        @description This topic provides an example on how to call the ListDiscoveredResources operation to query the resources in the current Alibaba Cloud account. The returned result indicates that a total of eight resources exist in the account.
        
        @param request: ListDiscoveredResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDiscoveredResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_deleted):
            query['ResourceDeleted'] = request.resource_deleted
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiscoveredResources',
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
            config_20200907_models.ListDiscoveredResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_discovered_resources(
        self,
        request: config_20200907_models.ListDiscoveredResourcesRequest,
    ) -> config_20200907_models.ListDiscoveredResourcesResponse:
        """
        @summary Obtains a list of resources aggregated across regions within an Alibaba Cloud account.
        
        @description This topic provides an example on how to call the ListDiscoveredResources operation to query the resources in the current Alibaba Cloud account. The returned result indicates that a total of eight resources exist in the account.
        
        @param request: ListDiscoveredResourcesRequest
        @return: ListDiscoveredResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_discovered_resources_with_options(request, runtime)

    async def list_discovered_resources_async(
        self,
        request: config_20200907_models.ListDiscoveredResourcesRequest,
    ) -> config_20200907_models.ListDiscoveredResourcesResponse:
        """
        @summary Obtains a list of resources aggregated across regions within an Alibaba Cloud account.
        
        @description This topic provides an example on how to call the ListDiscoveredResources operation to query the resources in the current Alibaba Cloud account. The returned result indicates that a total of eight resources exist in the account.
        
        @param request: ListDiscoveredResourcesRequest
        @return: ListDiscoveredResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_discovered_resources_with_options_async(request, runtime)

    def list_integrated_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListIntegratedServiceResponse:
        """
        @summary Queries a list of cloud services that are integrated with Cloud Config and the status of each cloud service.
        
        @description This topic provides an example on how to query the cloud services that can be integrated by the current Alibaba Cloud account.
        
        @param request: ListIntegratedServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegratedServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListIntegratedService',
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
            config_20200907_models.ListIntegratedServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integrated_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListIntegratedServiceResponse:
        """
        @summary Queries a list of cloud services that are integrated with Cloud Config and the status of each cloud service.
        
        @description This topic provides an example on how to query the cloud services that can be integrated by the current Alibaba Cloud account.
        
        @param request: ListIntegratedServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegratedServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListIntegratedService',
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
            config_20200907_models.ListIntegratedServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integrated_service(self) -> config_20200907_models.ListIntegratedServiceResponse:
        """
        @summary Queries a list of cloud services that are integrated with Cloud Config and the status of each cloud service.
        
        @description This topic provides an example on how to query the cloud services that can be integrated by the current Alibaba Cloud account.
        
        @return: ListIntegratedServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_integrated_service_with_options(runtime)

    async def list_integrated_service_async(self) -> config_20200907_models.ListIntegratedServiceResponse:
        """
        @summary Queries a list of cloud services that are integrated with Cloud Config and the status of each cloud service.
        
        @description This topic provides an example on how to query the cloud services that can be integrated by the current Alibaba Cloud account.
        
        @return: ListIntegratedServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_integrated_service_with_options_async(runtime)

    def list_managed_rules_with_options(
        self,
        request: config_20200907_models.ListManagedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListManagedRulesResponse:
        """
        @summary Queries a list of managed rules supported by Cloud Config.
        
        @description ### [](#)Background information
        For more information about how to define, execute, and integrate an evaluation rule, see [Definition and execution of evaluation rules](https://help.aliyun.com/document_detail/470802.html).
        ### [](#)Usage notes
        This topic provides an example on how to query all managed rules whose keyword is `CDN`. The response shows that 21 managed rules exist.
        
        @param request: ListManagedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListManagedRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManagedRules',
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
            config_20200907_models.ListManagedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_managed_rules_with_options_async(
        self,
        request: config_20200907_models.ListManagedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListManagedRulesResponse:
        """
        @summary Queries a list of managed rules supported by Cloud Config.
        
        @description ### [](#)Background information
        For more information about how to define, execute, and integrate an evaluation rule, see [Definition and execution of evaluation rules](https://help.aliyun.com/document_detail/470802.html).
        ### [](#)Usage notes
        This topic provides an example on how to query all managed rules whose keyword is `CDN`. The response shows that 21 managed rules exist.
        
        @param request: ListManagedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListManagedRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManagedRules',
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
            config_20200907_models.ListManagedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_managed_rules(
        self,
        request: config_20200907_models.ListManagedRulesRequest,
    ) -> config_20200907_models.ListManagedRulesResponse:
        """
        @summary Queries a list of managed rules supported by Cloud Config.
        
        @description ### [](#)Background information
        For more information about how to define, execute, and integrate an evaluation rule, see [Definition and execution of evaluation rules](https://help.aliyun.com/document_detail/470802.html).
        ### [](#)Usage notes
        This topic provides an example on how to query all managed rules whose keyword is `CDN`. The response shows that 21 managed rules exist.
        
        @param request: ListManagedRulesRequest
        @return: ListManagedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_managed_rules_with_options(request, runtime)

    async def list_managed_rules_async(
        self,
        request: config_20200907_models.ListManagedRulesRequest,
    ) -> config_20200907_models.ListManagedRulesResponse:
        """
        @summary Queries a list of managed rules supported by Cloud Config.
        
        @description ### [](#)Background information
        For more information about how to define, execute, and integrate an evaluation rule, see [Definition and execution of evaluation rules](https://help.aliyun.com/document_detail/470802.html).
        ### [](#)Usage notes
        This topic provides an example on how to query all managed rules whose keyword is `CDN`. The response shows that 21 managed rules exist.
        
        @param request: ListManagedRulesRequest
        @return: ListManagedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_managed_rules_with_options_async(request, runtime)

    def list_pre_managed_rules_with_options(
        self,
        tmp_req: config_20200907_models.ListPreManagedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListPreManagedRulesResponse:
        """
        @summary Queries a list of evaluation rules supported by Cloud Config.
        
        @description For more information about how to define, execute, and integrate an evaluation rule, see [Definition and execution of evaluation rules](https://help.aliyun.com/document_detail/470802.html).
        After you create an evaluation rule, a managed rule that has the same settings as the evaluation rule is created. After you create a resource, the managed rule can be used to continuously check the compliance of the resource.
        
        @param tmp_req: ListPreManagedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPreManagedRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.ListPreManagedRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_types):
            request.resource_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types, 'ResourceTypes', 'json')
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types_shrink):
            body['ResourceTypes'] = request.resource_types_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPreManagedRules',
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
            config_20200907_models.ListPreManagedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pre_managed_rules_with_options_async(
        self,
        tmp_req: config_20200907_models.ListPreManagedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListPreManagedRulesResponse:
        """
        @summary Queries a list of evaluation rules supported by Cloud Config.
        
        @description For more information about how to define, execute, and integrate an evaluation rule, see [Definition and execution of evaluation rules](https://help.aliyun.com/document_detail/470802.html).
        After you create an evaluation rule, a managed rule that has the same settings as the evaluation rule is created. After you create a resource, the managed rule can be used to continuously check the compliance of the resource.
        
        @param tmp_req: ListPreManagedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPreManagedRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.ListPreManagedRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_types):
            request.resource_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types, 'ResourceTypes', 'json')
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_types_shrink):
            body['ResourceTypes'] = request.resource_types_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPreManagedRules',
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
            config_20200907_models.ListPreManagedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pre_managed_rules(
        self,
        request: config_20200907_models.ListPreManagedRulesRequest,
    ) -> config_20200907_models.ListPreManagedRulesResponse:
        """
        @summary Queries a list of evaluation rules supported by Cloud Config.
        
        @description For more information about how to define, execute, and integrate an evaluation rule, see [Definition and execution of evaluation rules](https://help.aliyun.com/document_detail/470802.html).
        After you create an evaluation rule, a managed rule that has the same settings as the evaluation rule is created. After you create a resource, the managed rule can be used to continuously check the compliance of the resource.
        
        @param request: ListPreManagedRulesRequest
        @return: ListPreManagedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_pre_managed_rules_with_options(request, runtime)

    async def list_pre_managed_rules_async(
        self,
        request: config_20200907_models.ListPreManagedRulesRequest,
    ) -> config_20200907_models.ListPreManagedRulesResponse:
        """
        @summary Queries a list of evaluation rules supported by Cloud Config.
        
        @description For more information about how to define, execute, and integrate an evaluation rule, see [Definition and execution of evaluation rules](https://help.aliyun.com/document_detail/470802.html).
        After you create an evaluation rule, a managed rule that has the same settings as the evaluation rule is created. After you create a resource, the managed rule can be used to continuously check the compliance of the resource.
        
        @param request: ListPreManagedRulesRequest
        @return: ListPreManagedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_pre_managed_rules_with_options_async(request, runtime)

    def list_remediation_executions_with_options(
        self,
        request: config_20200907_models.ListRemediationExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationExecutionsResponse:
        """
        @summary Queries the remediation records of a rule.
        
        @description This topic provides an example on how to query the remediation records of the rule cr-5392626622af0000\\\\*\\*\\*.
        
        @param request: ListRemediationExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRemediationExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRemediationExecutions',
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
            config_20200907_models.ListRemediationExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_remediation_executions_with_options_async(
        self,
        request: config_20200907_models.ListRemediationExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationExecutionsResponse:
        """
        @summary Queries the remediation records of a rule.
        
        @description This topic provides an example on how to query the remediation records of the rule cr-5392626622af0000\\\\*\\*\\*.
        
        @param request: ListRemediationExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRemediationExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRemediationExecutions',
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
            config_20200907_models.ListRemediationExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_remediation_executions(
        self,
        request: config_20200907_models.ListRemediationExecutionsRequest,
    ) -> config_20200907_models.ListRemediationExecutionsResponse:
        """
        @summary Queries the remediation records of a rule.
        
        @description This topic provides an example on how to query the remediation records of the rule cr-5392626622af0000\\\\*\\*\\*.
        
        @param request: ListRemediationExecutionsRequest
        @return: ListRemediationExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_remediation_executions_with_options(request, runtime)

    async def list_remediation_executions_async(
        self,
        request: config_20200907_models.ListRemediationExecutionsRequest,
    ) -> config_20200907_models.ListRemediationExecutionsResponse:
        """
        @summary Queries the remediation records of a rule.
        
        @description This topic provides an example on how to query the remediation records of the rule cr-5392626622af0000\\\\*\\*\\*.
        
        @param request: ListRemediationExecutionsRequest
        @return: ListRemediationExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_remediation_executions_with_options_async(request, runtime)

    def list_remediation_templates_with_options(
        self,
        request: config_20200907_models.ListRemediationTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationTemplatesResponse:
        """
        @summary Queries a list of remediation templates for a managed rule.
        
        @description In this topic, the `oss-bucket-public-write-prohibited` managed rule is used as an example. The return result shows the details of the remediation template of the `OOS` type for the managed rule. OOS represents Operation Orchestration Service.
        
        @param request: ListRemediationTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRemediationTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.managed_rule_identifier):
            query['ManagedRuleIdentifier'] = request.managed_rule_identifier
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remediation_type):
            query['RemediationType'] = request.remediation_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRemediationTemplates',
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
            config_20200907_models.ListRemediationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_remediation_templates_with_options_async(
        self,
        request: config_20200907_models.ListRemediationTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationTemplatesResponse:
        """
        @summary Queries a list of remediation templates for a managed rule.
        
        @description In this topic, the `oss-bucket-public-write-prohibited` managed rule is used as an example. The return result shows the details of the remediation template of the `OOS` type for the managed rule. OOS represents Operation Orchestration Service.
        
        @param request: ListRemediationTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRemediationTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.managed_rule_identifier):
            query['ManagedRuleIdentifier'] = request.managed_rule_identifier
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remediation_type):
            query['RemediationType'] = request.remediation_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRemediationTemplates',
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
            config_20200907_models.ListRemediationTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_remediation_templates(
        self,
        request: config_20200907_models.ListRemediationTemplatesRequest,
    ) -> config_20200907_models.ListRemediationTemplatesResponse:
        """
        @summary Queries a list of remediation templates for a managed rule.
        
        @description In this topic, the `oss-bucket-public-write-prohibited` managed rule is used as an example. The return result shows the details of the remediation template of the `OOS` type for the managed rule. OOS represents Operation Orchestration Service.
        
        @param request: ListRemediationTemplatesRequest
        @return: ListRemediationTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_remediation_templates_with_options(request, runtime)

    async def list_remediation_templates_async(
        self,
        request: config_20200907_models.ListRemediationTemplatesRequest,
    ) -> config_20200907_models.ListRemediationTemplatesResponse:
        """
        @summary Queries a list of remediation templates for a managed rule.
        
        @description In this topic, the `oss-bucket-public-write-prohibited` managed rule is used as an example. The return result shows the details of the remediation template of the `OOS` type for the managed rule. OOS represents Operation Orchestration Service.
        
        @param request: ListRemediationTemplatesRequest
        @return: ListRemediationTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_remediation_templates_with_options_async(request, runtime)

    def list_remediations_with_options(
        self,
        request: config_20200907_models.ListRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationsResponse:
        """
        @summary Queries the information about the execution of remediation templates.
        
        @description This topic provides an example on how to query the remediation templates for the rule whose ID is `cr-6b7c626622af00b4***`.
        
        @param request: ListRemediationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRemediationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRemediations',
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
            config_20200907_models.ListRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_remediations_with_options_async(
        self,
        request: config_20200907_models.ListRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationsResponse:
        """
        @summary Queries the information about the execution of remediation templates.
        
        @description This topic provides an example on how to query the remediation templates for the rule whose ID is `cr-6b7c626622af00b4***`.
        
        @param request: ListRemediationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRemediationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRemediations',
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
            config_20200907_models.ListRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_remediations(
        self,
        request: config_20200907_models.ListRemediationsRequest,
    ) -> config_20200907_models.ListRemediationsResponse:
        """
        @summary Queries the information about the execution of remediation templates.
        
        @description This topic provides an example on how to query the remediation templates for the rule whose ID is `cr-6b7c626622af00b4***`.
        
        @param request: ListRemediationsRequest
        @return: ListRemediationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_remediations_with_options(request, runtime)

    async def list_remediations_async(
        self,
        request: config_20200907_models.ListRemediationsRequest,
    ) -> config_20200907_models.ListRemediationsResponse:
        """
        @summary Queries the information about the execution of remediation templates.
        
        @description This topic provides an example on how to query the remediation templates for the rule whose ID is `cr-6b7c626622af00b4***`.
        
        @param request: ListRemediationsRequest
        @return: ListRemediationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_remediations_with_options_async(request, runtime)

    def list_resource_evaluation_results_with_options(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources.
        
        @description In this example, the compliance evaluation result of the `23642660635396***` resource is queried and the resource is a RAM user. The returned result indicates that the resource is evaluated as `NON_COMPLIANT` by using the `cr-7f7d626622af0041****` rule.
        
        @param request: ListResourceEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceEvaluationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceEvaluationResults',
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
            config_20200907_models.ListResourceEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_evaluation_results_with_options_async(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources.
        
        @description In this example, the compliance evaluation result of the `23642660635396***` resource is queried and the resource is a RAM user. The returned result indicates that the resource is evaluated as `NON_COMPLIANT` by using the `cr-7f7d626622af0041****` rule.
        
        @param request: ListResourceEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceEvaluationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceEvaluationResults',
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
            config_20200907_models.ListResourceEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_evaluation_results(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources.
        
        @description In this example, the compliance evaluation result of the `23642660635396***` resource is queried and the resource is a RAM user. The returned result indicates that the resource is evaluated as `NON_COMPLIANT` by using the `cr-7f7d626622af0041****` rule.
        
        @param request: ListResourceEvaluationResultsRequest
        @return: ListResourceEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_evaluation_results_with_options(request, runtime)

    async def list_resource_evaluation_results_async(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        """
        @summary Queries the compliance evaluation results of resources.
        
        @description In this example, the compliance evaluation result of the `23642660635396***` resource is queried and the resource is a RAM user. The returned result indicates that the resource is evaluated as `NON_COMPLIANT` by using the `cr-7f7d626622af0041****` rule.
        
        @param request: ListResourceEvaluationResultsRequest
        @return: ListResourceEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_evaluation_results_with_options_async(request, runtime)

    def list_resource_relations_with_options(
        self,
        request: config_20200907_models.ListResourceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceRelationsResponse:
        """
        @summary Queries a list of resources that associate with a specific resource.
        
        @description This topic provides an example on how to query the disks that are associated with an Elastic Compute Service (ECS) instance within the current Alibaba Cloud account.
        
        @param request: ListResourceRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target_resource_id):
            query['TargetResourceId'] = request.target_resource_id
        if not UtilClient.is_unset(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceRelations',
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
            config_20200907_models.ListResourceRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_relations_with_options_async(
        self,
        request: config_20200907_models.ListResourceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourceRelationsResponse:
        """
        @summary Queries a list of resources that associate with a specific resource.
        
        @description This topic provides an example on how to query the disks that are associated with an Elastic Compute Service (ECS) instance within the current Alibaba Cloud account.
        
        @param request: ListResourceRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target_resource_id):
            query['TargetResourceId'] = request.target_resource_id
        if not UtilClient.is_unset(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceRelations',
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
            config_20200907_models.ListResourceRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_relations(
        self,
        request: config_20200907_models.ListResourceRelationsRequest,
    ) -> config_20200907_models.ListResourceRelationsResponse:
        """
        @summary Queries a list of resources that associate with a specific resource.
        
        @description This topic provides an example on how to query the disks that are associated with an Elastic Compute Service (ECS) instance within the current Alibaba Cloud account.
        
        @param request: ListResourceRelationsRequest
        @return: ListResourceRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_relations_with_options(request, runtime)

    async def list_resource_relations_async(
        self,
        request: config_20200907_models.ListResourceRelationsRequest,
    ) -> config_20200907_models.ListResourceRelationsResponse:
        """
        @summary Queries a list of resources that associate with a specific resource.
        
        @description This topic provides an example on how to query the disks that are associated with an Elastic Compute Service (ECS) instance within the current Alibaba Cloud account.
        
        @param request: ListResourceRelationsRequest
        @return: ListResourceRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_relations_with_options_async(request, runtime)

    def list_resources_by_advanced_search_with_options(
        self,
        request: config_20200907_models.ListResourcesByAdvancedSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourcesByAdvancedSearchResponse:
        """
        @summary Obtains resources based on the fields in the resource properties by using a SELECT statement.
        
        @description When you write a `SELECT` statement, you must obtain the fields and the data types of the fields from the property file of the resource type. For more information about property files, see [Alibaba Cloud Config Resource Schema](javascript:void\\(0\\)).
        >
        Each resource type supported by Cloud Config has a property file. Property files are named based on the related resource types. For example, the property file of the `ACS::ECS::Instance` resource type is named `ACS_ECS_Instance.properties.json`. Property files of different resource types are placed under the `config/properties/resource-types` path.
        For more information about the examples and limits on SQL query statements, see [Examples of SQL query statements](https://help.aliyun.com/document_detail/398718.html) and [Limits on SQL query statements](https://help.aliyun.com/document_detail/398750.html).
        This topic provides an example on how to obtain all resources whose tag key is `business` and whose tag value is `online` within the current account by using the advanced search feature.
        
        @param request: ListResourcesByAdvancedSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesByAdvancedSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByAdvancedSearch',
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
            config_20200907_models.ListResourcesByAdvancedSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_by_advanced_search_with_options_async(
        self,
        request: config_20200907_models.ListResourcesByAdvancedSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListResourcesByAdvancedSearchResponse:
        """
        @summary Obtains resources based on the fields in the resource properties by using a SELECT statement.
        
        @description When you write a `SELECT` statement, you must obtain the fields and the data types of the fields from the property file of the resource type. For more information about property files, see [Alibaba Cloud Config Resource Schema](javascript:void\\(0\\)).
        >
        Each resource type supported by Cloud Config has a property file. Property files are named based on the related resource types. For example, the property file of the `ACS::ECS::Instance` resource type is named `ACS_ECS_Instance.properties.json`. Property files of different resource types are placed under the `config/properties/resource-types` path.
        For more information about the examples and limits on SQL query statements, see [Examples of SQL query statements](https://help.aliyun.com/document_detail/398718.html) and [Limits on SQL query statements](https://help.aliyun.com/document_detail/398750.html).
        This topic provides an example on how to obtain all resources whose tag key is `business` and whose tag value is `online` within the current account by using the advanced search feature.
        
        @param request: ListResourcesByAdvancedSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesByAdvancedSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByAdvancedSearch',
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
            config_20200907_models.ListResourcesByAdvancedSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources_by_advanced_search(
        self,
        request: config_20200907_models.ListResourcesByAdvancedSearchRequest,
    ) -> config_20200907_models.ListResourcesByAdvancedSearchResponse:
        """
        @summary Obtains resources based on the fields in the resource properties by using a SELECT statement.
        
        @description When you write a `SELECT` statement, you must obtain the fields and the data types of the fields from the property file of the resource type. For more information about property files, see [Alibaba Cloud Config Resource Schema](javascript:void\\(0\\)).
        >
        Each resource type supported by Cloud Config has a property file. Property files are named based on the related resource types. For example, the property file of the `ACS::ECS::Instance` resource type is named `ACS_ECS_Instance.properties.json`. Property files of different resource types are placed under the `config/properties/resource-types` path.
        For more information about the examples and limits on SQL query statements, see [Examples of SQL query statements](https://help.aliyun.com/document_detail/398718.html) and [Limits on SQL query statements](https://help.aliyun.com/document_detail/398750.html).
        This topic provides an example on how to obtain all resources whose tag key is `business` and whose tag value is `online` within the current account by using the advanced search feature.
        
        @param request: ListResourcesByAdvancedSearchRequest
        @return: ListResourcesByAdvancedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resources_by_advanced_search_with_options(request, runtime)

    async def list_resources_by_advanced_search_async(
        self,
        request: config_20200907_models.ListResourcesByAdvancedSearchRequest,
    ) -> config_20200907_models.ListResourcesByAdvancedSearchResponse:
        """
        @summary Obtains resources based on the fields in the resource properties by using a SELECT statement.
        
        @description When you write a `SELECT` statement, you must obtain the fields and the data types of the fields from the property file of the resource type. For more information about property files, see [Alibaba Cloud Config Resource Schema](javascript:void\\(0\\)).
        >
        Each resource type supported by Cloud Config has a property file. Property files are named based on the related resource types. For example, the property file of the `ACS::ECS::Instance` resource type is named `ACS_ECS_Instance.properties.json`. Property files of different resource types are placed under the `config/properties/resource-types` path.
        For more information about the examples and limits on SQL query statements, see [Examples of SQL query statements](https://help.aliyun.com/document_detail/398718.html) and [Limits on SQL query statements](https://help.aliyun.com/document_detail/398750.html).
        This topic provides an example on how to obtain all resources whose tag key is `business` and whose tag value is `online` within the current account by using the advanced search feature.
        
        @param request: ListResourcesByAdvancedSearchRequest
        @return: ListResourcesByAdvancedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_by_advanced_search_with_options_async(request, runtime)

    def list_supported_products_with_options(
        self,
        request: config_20200907_models.ListSupportedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListSupportedProductsResponse:
        """
        @summary Queries the cloud services and resource types that are supported by Cloud Config.
        
        @description This topic provides an example on how to query the Alibaba Cloud services and resource types supported by a Cloud Config.
        
        @param request: ListSupportedProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSupportedProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSupportedProducts',
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
            config_20200907_models.ListSupportedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_supported_products_with_options_async(
        self,
        request: config_20200907_models.ListSupportedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListSupportedProductsResponse:
        """
        @summary Queries the cloud services and resource types that are supported by Cloud Config.
        
        @description This topic provides an example on how to query the Alibaba Cloud services and resource types supported by a Cloud Config.
        
        @param request: ListSupportedProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSupportedProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSupportedProducts',
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
            config_20200907_models.ListSupportedProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_supported_products(
        self,
        request: config_20200907_models.ListSupportedProductsRequest,
    ) -> config_20200907_models.ListSupportedProductsResponse:
        """
        @summary Queries the cloud services and resource types that are supported by Cloud Config.
        
        @description This topic provides an example on how to query the Alibaba Cloud services and resource types supported by a Cloud Config.
        
        @param request: ListSupportedProductsRequest
        @return: ListSupportedProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_supported_products_with_options(request, runtime)

    async def list_supported_products_async(
        self,
        request: config_20200907_models.ListSupportedProductsRequest,
    ) -> config_20200907_models.ListSupportedProductsResponse:
        """
        @summary Queries the cloud services and resource types that are supported by Cloud Config.
        
        @description This topic provides an example on how to query the Alibaba Cloud services and resource types supported by a Cloud Config.
        
        @param request: ListSupportedProductsRequest
        @return: ListSupportedProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_supported_products_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: config_20200907_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListTagResourcesResponse:
        """
        @summary Queries tags that are added to specified resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            config_20200907_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: config_20200907_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListTagResourcesResponse:
        """
        @summary Queries tags that are added to specified resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            config_20200907_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: config_20200907_models.ListTagResourcesRequest,
    ) -> config_20200907_models.ListTagResourcesResponse:
        """
        @summary Queries tags that are added to specified resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: config_20200907_models.ListTagResourcesRequest,
    ) -> config_20200907_models.ListTagResourcesResponse:
        """
        @summary Queries tags that are added to specified resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def put_evaluations_with_options(
        self,
        request: config_20200907_models.PutEvaluationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.PutEvaluationsResponse:
        """
        @summary Submits the evaluation results of a rule from Function Compute.
        
        @description For more information about the definition, use scenarios, and execution of custom function rules, see [Definition and execution of custom function rules](https://help.aliyun.com/document_detail/127405.html).
        
        @param request: PutEvaluationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEvaluationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.delete_mode):
            body['DeleteMode'] = request.delete_mode
        if not UtilClient.is_unset(request.evaluations):
            body['Evaluations'] = request.evaluations
        if not UtilClient.is_unset(request.result_token):
            body['ResultToken'] = request.result_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutEvaluations',
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
            config_20200907_models.PutEvaluationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_evaluations_with_options_async(
        self,
        request: config_20200907_models.PutEvaluationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.PutEvaluationsResponse:
        """
        @summary Submits the evaluation results of a rule from Function Compute.
        
        @description For more information about the definition, use scenarios, and execution of custom function rules, see [Definition and execution of custom function rules](https://help.aliyun.com/document_detail/127405.html).
        
        @param request: PutEvaluationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEvaluationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.delete_mode):
            body['DeleteMode'] = request.delete_mode
        if not UtilClient.is_unset(request.evaluations):
            body['Evaluations'] = request.evaluations
        if not UtilClient.is_unset(request.result_token):
            body['ResultToken'] = request.result_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutEvaluations',
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
            config_20200907_models.PutEvaluationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_evaluations(
        self,
        request: config_20200907_models.PutEvaluationsRequest,
    ) -> config_20200907_models.PutEvaluationsResponse:
        """
        @summary Submits the evaluation results of a rule from Function Compute.
        
        @description For more information about the definition, use scenarios, and execution of custom function rules, see [Definition and execution of custom function rules](https://help.aliyun.com/document_detail/127405.html).
        
        @param request: PutEvaluationsRequest
        @return: PutEvaluationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_evaluations_with_options(request, runtime)

    async def put_evaluations_async(
        self,
        request: config_20200907_models.PutEvaluationsRequest,
    ) -> config_20200907_models.PutEvaluationsResponse:
        """
        @summary Submits the evaluation results of a rule from Function Compute.
        
        @description For more information about the definition, use scenarios, and execution of custom function rules, see [Definition and execution of custom function rules](https://help.aliyun.com/document_detail/127405.html).
        
        @param request: PutEvaluationsRequest
        @return: PutEvaluationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_evaluations_with_options_async(request, runtime)

    def revert_aggregate_evaluation_results_with_options(
        self,
        tmp_req: config_20200907_models.RevertAggregateEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.RevertAggregateEvaluationResultsResponse:
        """
        @summary Re-evaluates resources that are evaluated based on a rule after the evaluation results on some resources of an ignored rule in an account group are resumed.
        
        @description ### [](#)Prerequisites
        One or more non-compliant resources that are evaluated by a rule are ignored. For more information, see [IgnoreAggregateEvaluationResults](https://help.aliyun.com/document_detail/607054.html).
        ### [](#)Description
        This topic provides an example on how to re-evaluate the non-compliant resource that is evaluated by the `cr-7e72626622af0051***` rule of the `120886317861****` member in the `ca-5b6c626622af008f****` group account. The ID of the region in which the resource resides is `cn-beijing`, the type of the resource is `ACS::SLB::LoadBalancer`, and the ID of the resource is `lb-hp3a3b4ztyfm2plgm****`.
        
        @param tmp_req: RevertAggregateEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertAggregateEvaluationResultsResponse
        """
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
        """
        @summary Re-evaluates resources that are evaluated based on a rule after the evaluation results on some resources of an ignored rule in an account group are resumed.
        
        @description ### [](#)Prerequisites
        One or more non-compliant resources that are evaluated by a rule are ignored. For more information, see [IgnoreAggregateEvaluationResults](https://help.aliyun.com/document_detail/607054.html).
        ### [](#)Description
        This topic provides an example on how to re-evaluate the non-compliant resource that is evaluated by the `cr-7e72626622af0051***` rule of the `120886317861****` member in the `ca-5b6c626622af008f****` group account. The ID of the region in which the resource resides is `cn-beijing`, the type of the resource is `ACS::SLB::LoadBalancer`, and the ID of the resource is `lb-hp3a3b4ztyfm2plgm****`.
        
        @param tmp_req: RevertAggregateEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertAggregateEvaluationResultsResponse
        """
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
        """
        @summary Re-evaluates resources that are evaluated based on a rule after the evaluation results on some resources of an ignored rule in an account group are resumed.
        
        @description ### [](#)Prerequisites
        One or more non-compliant resources that are evaluated by a rule are ignored. For more information, see [IgnoreAggregateEvaluationResults](https://help.aliyun.com/document_detail/607054.html).
        ### [](#)Description
        This topic provides an example on how to re-evaluate the non-compliant resource that is evaluated by the `cr-7e72626622af0051***` rule of the `120886317861****` member in the `ca-5b6c626622af008f****` group account. The ID of the region in which the resource resides is `cn-beijing`, the type of the resource is `ACS::SLB::LoadBalancer`, and the ID of the resource is `lb-hp3a3b4ztyfm2plgm****`.
        
        @param request: RevertAggregateEvaluationResultsRequest
        @return: RevertAggregateEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revert_aggregate_evaluation_results_with_options(request, runtime)

    async def revert_aggregate_evaluation_results_async(
        self,
        request: config_20200907_models.RevertAggregateEvaluationResultsRequest,
    ) -> config_20200907_models.RevertAggregateEvaluationResultsResponse:
        """
        @summary Re-evaluates resources that are evaluated based on a rule after the evaluation results on some resources of an ignored rule in an account group are resumed.
        
        @description ### [](#)Prerequisites
        One or more non-compliant resources that are evaluated by a rule are ignored. For more information, see [IgnoreAggregateEvaluationResults](https://help.aliyun.com/document_detail/607054.html).
        ### [](#)Description
        This topic provides an example on how to re-evaluate the non-compliant resource that is evaluated by the `cr-7e72626622af0051***` rule of the `120886317861****` member in the `ca-5b6c626622af008f****` group account. The ID of the region in which the resource resides is `cn-beijing`, the type of the resource is `ACS::SLB::LoadBalancer`, and the ID of the resource is `lb-hp3a3b4ztyfm2plgm****`.
        
        @param request: RevertAggregateEvaluationResultsRequest
        @return: RevertAggregateEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revert_aggregate_evaluation_results_with_options_async(request, runtime)

    def revert_evaluation_results_with_options(
        self,
        tmp_req: config_20200907_models.RevertEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.RevertEvaluationResultsResponse:
        """
        @summary Re-evaluates resources that are evaluated based on a rule after the evaluation results on some resources of an ignored rule are resumed.
        
        @description ### [](#)Prerequisites
        One or more non-compliant resources that are evaluated by a rule are ignored. For more information, see [IgnoreEvaluationResults](https://help.aliyun.com/document_detail/606990.html).
        ### [](#)Description
        This topic provides an example on how to re-evaluate the `lb-hp3a3b4ztyfm2plgm***` non-compliant resource that is evaluated by the `cr-7e72626622af0051****` rule. The ID of the region in which the resource resides is`cn-beijing`, the type of the resource is `ACS::SLB::LoadBalancer`, and the ID of the resource is `lb-hp3a3b4ztyfm2plgm****`.
        
        @param tmp_req: RevertEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertEvaluationResultsResponse
        """
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
        """
        @summary Re-evaluates resources that are evaluated based on a rule after the evaluation results on some resources of an ignored rule are resumed.
        
        @description ### [](#)Prerequisites
        One or more non-compliant resources that are evaluated by a rule are ignored. For more information, see [IgnoreEvaluationResults](https://help.aliyun.com/document_detail/606990.html).
        ### [](#)Description
        This topic provides an example on how to re-evaluate the `lb-hp3a3b4ztyfm2plgm***` non-compliant resource that is evaluated by the `cr-7e72626622af0051****` rule. The ID of the region in which the resource resides is`cn-beijing`, the type of the resource is `ACS::SLB::LoadBalancer`, and the ID of the resource is `lb-hp3a3b4ztyfm2plgm****`.
        
        @param tmp_req: RevertEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertEvaluationResultsResponse
        """
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
        """
        @summary Re-evaluates resources that are evaluated based on a rule after the evaluation results on some resources of an ignored rule are resumed.
        
        @description ### [](#)Prerequisites
        One or more non-compliant resources that are evaluated by a rule are ignored. For more information, see [IgnoreEvaluationResults](https://help.aliyun.com/document_detail/606990.html).
        ### [](#)Description
        This topic provides an example on how to re-evaluate the `lb-hp3a3b4ztyfm2plgm***` non-compliant resource that is evaluated by the `cr-7e72626622af0051****` rule. The ID of the region in which the resource resides is`cn-beijing`, the type of the resource is `ACS::SLB::LoadBalancer`, and the ID of the resource is `lb-hp3a3b4ztyfm2plgm****`.
        
        @param request: RevertEvaluationResultsRequest
        @return: RevertEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revert_evaluation_results_with_options(request, runtime)

    async def revert_evaluation_results_async(
        self,
        request: config_20200907_models.RevertEvaluationResultsRequest,
    ) -> config_20200907_models.RevertEvaluationResultsResponse:
        """
        @summary Re-evaluates resources that are evaluated based on a rule after the evaluation results on some resources of an ignored rule are resumed.
        
        @description ### [](#)Prerequisites
        One or more non-compliant resources that are evaluated by a rule are ignored. For more information, see [IgnoreEvaluationResults](https://help.aliyun.com/document_detail/606990.html).
        ### [](#)Description
        This topic provides an example on how to re-evaluate the `lb-hp3a3b4ztyfm2plgm***` non-compliant resource that is evaluated by the `cr-7e72626622af0051****` rule. The ID of the region in which the resource resides is`cn-beijing`, the type of the resource is `ACS::SLB::LoadBalancer`, and the ID of the resource is `lb-hp3a3b4ztyfm2plgm****`.
        
        @param request: RevertEvaluationResultsRequest
        @return: RevertEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revert_evaluation_results_with_options_async(request, runtime)

    def start_aggregate_config_rule_evaluation_with_options(
        self,
        request: config_20200907_models.StartAggregateConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateConfigRuleEvaluationResponse:
        """
        @summary Re-evaluates the compliance of resources based on a rule or based on all rules in a compliance package in a specific account group.
        
        @description > After you call this operation, the compliance evaluation is performed only once. To query the compliance evaluation results returned by the rule, call the ListAggregateConfigRuleEvaluationResults operation. For more information, see [ListAggregateConfigRuleEvaluationResults](https://help.aliyun.com/document_detail/265979.html).
        The sample request in this topic shows how to use the `cr-c169626622af009f***` rule in the `ca-3a58626622af0005****` account group to evaluate resources.
        
        @param request: StartAggregateConfigRuleEvaluationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAggregateConfigRuleEvaluationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.revert_evaluation):
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
        """
        @summary Re-evaluates the compliance of resources based on a rule or based on all rules in a compliance package in a specific account group.
        
        @description > After you call this operation, the compliance evaluation is performed only once. To query the compliance evaluation results returned by the rule, call the ListAggregateConfigRuleEvaluationResults operation. For more information, see [ListAggregateConfigRuleEvaluationResults](https://help.aliyun.com/document_detail/265979.html).
        The sample request in this topic shows how to use the `cr-c169626622af009f***` rule in the `ca-3a58626622af0005****` account group to evaluate resources.
        
        @param request: StartAggregateConfigRuleEvaluationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAggregateConfigRuleEvaluationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.revert_evaluation):
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
        """
        @summary Re-evaluates the compliance of resources based on a rule or based on all rules in a compliance package in a specific account group.
        
        @description > After you call this operation, the compliance evaluation is performed only once. To query the compliance evaluation results returned by the rule, call the ListAggregateConfigRuleEvaluationResults operation. For more information, see [ListAggregateConfigRuleEvaluationResults](https://help.aliyun.com/document_detail/265979.html).
        The sample request in this topic shows how to use the `cr-c169626622af009f***` rule in the `ca-3a58626622af0005****` account group to evaluate resources.
        
        @param request: StartAggregateConfigRuleEvaluationRequest
        @return: StartAggregateConfigRuleEvaluationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_aggregate_config_rule_evaluation_with_options(request, runtime)

    async def start_aggregate_config_rule_evaluation_async(
        self,
        request: config_20200907_models.StartAggregateConfigRuleEvaluationRequest,
    ) -> config_20200907_models.StartAggregateConfigRuleEvaluationResponse:
        """
        @summary Re-evaluates the compliance of resources based on a rule or based on all rules in a compliance package in a specific account group.
        
        @description > After you call this operation, the compliance evaluation is performed only once. To query the compliance evaluation results returned by the rule, call the ListAggregateConfigRuleEvaluationResults operation. For more information, see [ListAggregateConfigRuleEvaluationResults](https://help.aliyun.com/document_detail/265979.html).
        The sample request in this topic shows how to use the `cr-c169626622af009f***` rule in the `ca-3a58626622af0005****` account group to evaluate resources.
        
        @param request: StartAggregateConfigRuleEvaluationRequest
        @return: StartAggregateConfigRuleEvaluationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_aggregate_config_rule_evaluation_with_options_async(request, runtime)

    def start_aggregate_remediation_with_options(
        self,
        request: config_20200907_models.StartAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateRemediationResponse:
        """
        @summary Performs a remediation operation by using a rule in an account group.
        
        @description This topic provides an example on how to manually perform a remediation operation by using the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`. The return result shows that the manual execution is successful.
        
        @param request: StartAggregateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAggregateRemediationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAggregateRemediation',
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
            config_20200907_models.StartAggregateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aggregate_remediation_with_options_async(
        self,
        request: config_20200907_models.StartAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartAggregateRemediationResponse:
        """
        @summary Performs a remediation operation by using a rule in an account group.
        
        @description This topic provides an example on how to manually perform a remediation operation by using the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`. The return result shows that the manual execution is successful.
        
        @param request: StartAggregateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAggregateRemediationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.resource_account_id):
            query['ResourceAccountId'] = request.resource_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAggregateRemediation',
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
            config_20200907_models.StartAggregateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aggregate_remediation(
        self,
        request: config_20200907_models.StartAggregateRemediationRequest,
    ) -> config_20200907_models.StartAggregateRemediationResponse:
        """
        @summary Performs a remediation operation by using a rule in an account group.
        
        @description This topic provides an example on how to manually perform a remediation operation by using the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`. The return result shows that the manual execution is successful.
        
        @param request: StartAggregateRemediationRequest
        @return: StartAggregateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_aggregate_remediation_with_options(request, runtime)

    async def start_aggregate_remediation_async(
        self,
        request: config_20200907_models.StartAggregateRemediationRequest,
    ) -> config_20200907_models.StartAggregateRemediationResponse:
        """
        @summary Performs a remediation operation by using a rule in an account group.
        
        @description This topic provides an example on how to manually perform a remediation operation by using the rule whose ID is `cr-6b7c626622af00b4***` in the account group whose ID is `ca-6b4a626622af0012****`. The return result shows that the manual execution is successful.
        
        @param request: StartAggregateRemediationRequest
        @return: StartAggregateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_aggregate_remediation_with_options_async(request, runtime)

    def start_config_rule_evaluation_with_options(
        self,
        request: config_20200907_models.StartConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartConfigRuleEvaluationResponse:
        """
        @summary Re-evaluates the compliance of resources based on a rule or based on all rules in a compliance package.
        
        @description In this example, the cr-9920626622af0035\\\\*\\*\\* rule is used to re-evaluate the compliance of resources.
        
        @param request: StartConfigRuleEvaluationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartConfigRuleEvaluationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.revert_evaluation):
            query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartConfigRuleEvaluation',
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
            config_20200907_models.StartConfigRuleEvaluationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_config_rule_evaluation_with_options_async(
        self,
        request: config_20200907_models.StartConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartConfigRuleEvaluationResponse:
        """
        @summary Re-evaluates the compliance of resources based on a rule or based on all rules in a compliance package.
        
        @description In this example, the cr-9920626622af0035\\\\*\\*\\* rule is used to re-evaluate the compliance of resources.
        
        @param request: StartConfigRuleEvaluationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartConfigRuleEvaluationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compliance_pack_id):
            query['CompliancePackId'] = request.compliance_pack_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        if not UtilClient.is_unset(request.revert_evaluation):
            query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartConfigRuleEvaluation',
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
            config_20200907_models.StartConfigRuleEvaluationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_config_rule_evaluation(
        self,
        request: config_20200907_models.StartConfigRuleEvaluationRequest,
    ) -> config_20200907_models.StartConfigRuleEvaluationResponse:
        """
        @summary Re-evaluates the compliance of resources based on a rule or based on all rules in a compliance package.
        
        @description In this example, the cr-9920626622af0035\\\\*\\*\\* rule is used to re-evaluate the compliance of resources.
        
        @param request: StartConfigRuleEvaluationRequest
        @return: StartConfigRuleEvaluationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_config_rule_evaluation_with_options(request, runtime)

    async def start_config_rule_evaluation_async(
        self,
        request: config_20200907_models.StartConfigRuleEvaluationRequest,
    ) -> config_20200907_models.StartConfigRuleEvaluationResponse:
        """
        @summary Re-evaluates the compliance of resources based on a rule or based on all rules in a compliance package.
        
        @description In this example, the cr-9920626622af0035\\\\*\\*\\* rule is used to re-evaluate the compliance of resources.
        
        @param request: StartConfigRuleEvaluationRequest
        @return: StartConfigRuleEvaluationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_config_rule_evaluation_with_options_async(request, runtime)

    def start_configuration_recorder_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartConfigurationRecorderResponse:
        """
        @summary Enables Cloud Config to monitor the resources of your Alibaba Cloud account.
        
        @description This topic provides an example on how to enable Cloud Config to monitor the resources of your Alibaba Cloud account.
        
        @param request: StartConfigurationRecorderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartConfigurationRecorderResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='StartConfigurationRecorder',
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
            config_20200907_models.StartConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_configuration_recorder_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartConfigurationRecorderResponse:
        """
        @summary Enables Cloud Config to monitor the resources of your Alibaba Cloud account.
        
        @description This topic provides an example on how to enable Cloud Config to monitor the resources of your Alibaba Cloud account.
        
        @param request: StartConfigurationRecorderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartConfigurationRecorderResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='StartConfigurationRecorder',
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
            config_20200907_models.StartConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_configuration_recorder(self) -> config_20200907_models.StartConfigurationRecorderResponse:
        """
        @summary Enables Cloud Config to monitor the resources of your Alibaba Cloud account.
        
        @description This topic provides an example on how to enable Cloud Config to monitor the resources of your Alibaba Cloud account.
        
        @return: StartConfigurationRecorderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_configuration_recorder_with_options(runtime)

    async def start_configuration_recorder_async(self) -> config_20200907_models.StartConfigurationRecorderResponse:
        """
        @summary Enables Cloud Config to monitor the resources of your Alibaba Cloud account.
        
        @description This topic provides an example on how to enable Cloud Config to monitor the resources of your Alibaba Cloud account.
        
        @return: StartConfigurationRecorderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_configuration_recorder_with_options_async(runtime)

    def start_remediation_with_options(
        self,
        request: config_20200907_models.StartRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartRemediationResponse:
        """
        @summary Performs a remediation operation by using a rule.
        
        @description This topic provides an example on how to perform a remediation operation by using the rule whose ID is `cr-8a973ac2e2be00a2***`. The returned result shows that the manual execution is successful.
        
        @param request: StartRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRemediationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRemediation',
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
            config_20200907_models.StartRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_remediation_with_options_async(
        self,
        request: config_20200907_models.StartRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StartRemediationResponse:
        """
        @summary Performs a remediation operation by using a rule.
        
        @description This topic provides an example on how to perform a remediation operation by using the rule whose ID is `cr-8a973ac2e2be00a2***`. The returned result shows that the manual execution is successful.
        
        @param request: StartRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRemediationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRemediation',
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
            config_20200907_models.StartRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_remediation(
        self,
        request: config_20200907_models.StartRemediationRequest,
    ) -> config_20200907_models.StartRemediationResponse:
        """
        @summary Performs a remediation operation by using a rule.
        
        @description This topic provides an example on how to perform a remediation operation by using the rule whose ID is `cr-8a973ac2e2be00a2***`. The returned result shows that the manual execution is successful.
        
        @param request: StartRemediationRequest
        @return: StartRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_remediation_with_options(request, runtime)

    async def start_remediation_async(
        self,
        request: config_20200907_models.StartRemediationRequest,
    ) -> config_20200907_models.StartRemediationResponse:
        """
        @summary Performs a remediation operation by using a rule.
        
        @description This topic provides an example on how to perform a remediation operation by using the rule whose ID is `cr-8a973ac2e2be00a2***`. The returned result shows that the manual execution is successful.
        
        @param request: StartRemediationRequest
        @return: StartRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_remediation_with_options_async(request, runtime)

    def stop_configuration_recorder_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StopConfigurationRecorderResponse:
        """
        @summary Deactivates Cloud Config.
        
        @description >  After you deactivate Cloud Config, the resource configurations, created rules, and compliance evaluation results that are stored in Cloud Config are automatically cleared and cannot be restored. Proceed with caution.
        
        @param request: StopConfigurationRecorderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopConfigurationRecorderResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='StopConfigurationRecorder',
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
            config_20200907_models.StopConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_configuration_recorder_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.StopConfigurationRecorderResponse:
        """
        @summary Deactivates Cloud Config.
        
        @description >  After you deactivate Cloud Config, the resource configurations, created rules, and compliance evaluation results that are stored in Cloud Config are automatically cleared and cannot be restored. Proceed with caution.
        
        @param request: StopConfigurationRecorderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopConfigurationRecorderResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='StopConfigurationRecorder',
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
            config_20200907_models.StopConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_configuration_recorder(self) -> config_20200907_models.StopConfigurationRecorderResponse:
        """
        @summary Deactivates Cloud Config.
        
        @description >  After you deactivate Cloud Config, the resource configurations, created rules, and compliance evaluation results that are stored in Cloud Config are automatically cleared and cannot be restored. Proceed with caution.
        
        @return: StopConfigurationRecorderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_configuration_recorder_with_options(runtime)

    async def stop_configuration_recorder_async(self) -> config_20200907_models.StopConfigurationRecorderResponse:
        """
        @summary Deactivates Cloud Config.
        
        @description >  After you deactivate Cloud Config, the resource configurations, created rules, and compliance evaluation results that are stored in Cloud Config are automatically cleared and cannot be restored. Proceed with caution.
        
        @return: StopConfigurationRecorderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_configuration_recorder_with_options_async(runtime)

    def tag_resources_with_options(
        self,
        tmp_req: config_20200907_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param tmp_req: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.TagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            config_20200907_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        tmp_req: config_20200907_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param tmp_req: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.TagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            config_20200907_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: config_20200907_models.TagResourcesRequest,
    ) -> config_20200907_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: config_20200907_models.TagResourcesRequest,
    ) -> config_20200907_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: config_20200907_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UntagResourcesResponse:
        """
        @summary Removes tags from specified resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
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
            config_20200907_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: config_20200907_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UntagResourcesResponse:
        """
        @summary Removes tags from specified resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
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
            config_20200907_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: config_20200907_models.UntagResourcesRequest,
    ) -> config_20200907_models.UntagResourcesResponse:
        """
        @summary Removes tags from specified resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: config_20200907_models.UntagResourcesRequest,
    ) -> config_20200907_models.UntagResourcesResponse:
        """
        @summary Removes tags from specified resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_aggregate_compliance_pack_with_options(
        self,
        tmp_req: config_20200907_models.UpdateAggregateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateCompliancePackResponse:
        """
        @summary Modifies the configurations of a compliance package in an account group.
        
        @description This topic provides an example on how to change the value of the `eip-bandwidth-limit` parameter in the rule template of the compliance package `cp-fdc8626622af00f9***` in the account group `ca-f632626622af0079****` to `20`.
        
        @param tmp_req: UpdateAggregateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregateCompliancePackResponse
        """
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
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Modifies the configurations of a compliance package in an account group.
        
        @description This topic provides an example on how to change the value of the `eip-bandwidth-limit` parameter in the rule template of the compliance package `cp-fdc8626622af00f9***` in the account group `ca-f632626622af0079****` to `20`.
        
        @param tmp_req: UpdateAggregateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregateCompliancePackResponse
        """
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
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Modifies the configurations of a compliance package in an account group.
        
        @description This topic provides an example on how to change the value of the `eip-bandwidth-limit` parameter in the rule template of the compliance package `cp-fdc8626622af00f9***` in the account group `ca-f632626622af0079****` to `20`.
        
        @param request: UpdateAggregateCompliancePackRequest
        @return: UpdateAggregateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_aggregate_compliance_pack_with_options(request, runtime)

    async def update_aggregate_compliance_pack_async(
        self,
        request: config_20200907_models.UpdateAggregateCompliancePackRequest,
    ) -> config_20200907_models.UpdateAggregateCompliancePackResponse:
        """
        @summary Modifies the configurations of a compliance package in an account group.
        
        @description This topic provides an example on how to change the value of the `eip-bandwidth-limit` parameter in the rule template of the compliance package `cp-fdc8626622af00f9***` in the account group `ca-f632626622af0079****` to `20`.
        
        @param request: UpdateAggregateCompliancePackRequest
        @return: UpdateAggregateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregate_compliance_pack_with_options_async(request, runtime)

    def update_aggregate_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.UpdateAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateConfigDeliveryChannelResponse:
        """
        @summary Modifies a delivery channel in an account group.
        
        @description This topic provides an example on how to disable a delivery channel in an account group. The ID of the account group is `ca-a4e5626622af0079***`, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`. The Status parameter is set to `0`. After the delivery channel is disabled, Cloud Config retains the most recent delivery configuration and stops resource data delivery.
        
        @param request: UpdateAggregateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not UtilClient.is_unset(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAggregateConfigDeliveryChannel',
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
            config_20200907_models.UpdateAggregateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregate_config_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.UpdateAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateConfigDeliveryChannelResponse:
        """
        @summary Modifies a delivery channel in an account group.
        
        @description This topic provides an example on how to disable a delivery channel in an account group. The ID of the account group is `ca-a4e5626622af0079***`, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`. The Status parameter is set to `0`. After the delivery channel is disabled, Cloud Config retains the most recent delivery configuration and stops resource data delivery.
        
        @param request: UpdateAggregateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not UtilClient.is_unset(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAggregateConfigDeliveryChannel',
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
            config_20200907_models.UpdateAggregateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregate_config_delivery_channel(
        self,
        request: config_20200907_models.UpdateAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.UpdateAggregateConfigDeliveryChannelResponse:
        """
        @summary Modifies a delivery channel in an account group.
        
        @description This topic provides an example on how to disable a delivery channel in an account group. The ID of the account group is `ca-a4e5626622af0079***`, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`. The Status parameter is set to `0`. After the delivery channel is disabled, Cloud Config retains the most recent delivery configuration and stops resource data delivery.
        
        @param request: UpdateAggregateConfigDeliveryChannelRequest
        @return: UpdateAggregateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_aggregate_config_delivery_channel_with_options(request, runtime)

    async def update_aggregate_config_delivery_channel_async(
        self,
        request: config_20200907_models.UpdateAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.UpdateAggregateConfigDeliveryChannelResponse:
        """
        @summary Modifies a delivery channel in an account group.
        
        @description This topic provides an example on how to disable a delivery channel in an account group. The ID of the account group is `ca-a4e5626622af0079***`, and the ID of the delivery channel is `cdc-8e45ff4e06a3a8****`. The Status parameter is set to `0`. After the delivery channel is disabled, Cloud Config retains the most recent delivery configuration and stops resource data delivery.
        
        @param request: UpdateAggregateConfigDeliveryChannelRequest
        @return: UpdateAggregateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def update_aggregate_config_rule_with_options(
        self,
        tmp_req: config_20200907_models.UpdateAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateConfigRuleResponse:
        """
        @summary Modifies the description, input parameters, and risk level of a rule in a specific account group.
        
        @description This topic provides an example on how to change the risk level of the rule `cr-4e3d626622af0080***` in an account group `ca-a4e5626622af0079****` to `3`, which indicates low risk level.
        
        @param tmp_req: UpdateAggregateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregateConfigRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateAggregateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.account_ids_scope):
            body['AccountIdsScope'] = request.account_ids_scope
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
        if not UtilClient.is_unset(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not UtilClient.is_unset(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.folder_ids_scope):
            body['FolderIdsScope'] = request.folder_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Modifies the description, input parameters, and risk level of a rule in a specific account group.
        
        @description This topic provides an example on how to change the risk level of the rule `cr-4e3d626622af0080***` in an account group `ca-a4e5626622af0079****` to `3`, which indicates low risk level.
        
        @param tmp_req: UpdateAggregateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregateConfigRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = config_20200907_models.UpdateAggregateConfigRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_parameters):
            request.input_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_parameters, 'InputParameters', 'json')
        if not UtilClient.is_unset(tmp_req.resource_types_scope):
            request.resource_types_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types_scope, 'ResourceTypesScope', 'simple')
        body = {}
        if not UtilClient.is_unset(request.account_ids_scope):
            body['AccountIdsScope'] = request.account_ids_scope
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
        if not UtilClient.is_unset(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not UtilClient.is_unset(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.folder_ids_scope):
            body['FolderIdsScope'] = request.folder_ids_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Modifies the description, input parameters, and risk level of a rule in a specific account group.
        
        @description This topic provides an example on how to change the risk level of the rule `cr-4e3d626622af0080***` in an account group `ca-a4e5626622af0079****` to `3`, which indicates low risk level.
        
        @param request: UpdateAggregateConfigRuleRequest
        @return: UpdateAggregateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_aggregate_config_rule_with_options(request, runtime)

    async def update_aggregate_config_rule_async(
        self,
        request: config_20200907_models.UpdateAggregateConfigRuleRequest,
    ) -> config_20200907_models.UpdateAggregateConfigRuleResponse:
        """
        @summary Modifies the description, input parameters, and risk level of a rule in a specific account group.
        
        @description This topic provides an example on how to change the risk level of the rule `cr-4e3d626622af0080***` in an account group `ca-a4e5626622af0079****` to `3`, which indicates low risk level.
        
        @param request: UpdateAggregateConfigRuleRequest
        @return: UpdateAggregateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregate_config_rule_with_options_async(request, runtime)

    def update_aggregate_remediation_with_options(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
        """
        @summary Modifies a remediation template for a rule in an account group.
        
        @description This topic describes how to change the execution mode of the `crr-909ba2d4716700eb***` remediation setting for a rule in the `ca-6b4a626622af0012****` account group to `AUTO_EXECUTION`, which specifies automatic remediation. This topic also provides a sample request.
        
        @param request: UpdateAggregateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregateRemediationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.remediation_id):
            body['RemediationId'] = request.remediation_id
        if not UtilClient.is_unset(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not UtilClient.is_unset(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggregateRemediation',
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
            config_20200907_models.UpdateAggregateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aggregate_remediation_with_options_async(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
        """
        @summary Modifies a remediation template for a rule in an account group.
        
        @description This topic describes how to change the execution mode of the `crr-909ba2d4716700eb***` remediation setting for a rule in the `ca-6b4a626622af0012****` account group to `AUTO_EXECUTION`, which specifies automatic remediation. This topic also provides a sample request.
        
        @param request: UpdateAggregateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregateRemediationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator_id):
            body['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.remediation_id):
            body['RemediationId'] = request.remediation_id
        if not UtilClient.is_unset(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not UtilClient.is_unset(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggregateRemediation',
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
            config_20200907_models.UpdateAggregateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aggregate_remediation(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
        """
        @summary Modifies a remediation template for a rule in an account group.
        
        @description This topic describes how to change the execution mode of the `crr-909ba2d4716700eb***` remediation setting for a rule in the `ca-6b4a626622af0012****` account group to `AUTO_EXECUTION`, which specifies automatic remediation. This topic also provides a sample request.
        
        @param request: UpdateAggregateRemediationRequest
        @return: UpdateAggregateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_aggregate_remediation_with_options(request, runtime)

    async def update_aggregate_remediation_async(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
        """
        @summary Modifies a remediation template for a rule in an account group.
        
        @description This topic describes how to change the execution mode of the `crr-909ba2d4716700eb***` remediation setting for a rule in the `ca-6b4a626622af0012****` account group to `AUTO_EXECUTION`, which specifies automatic remediation. This topic also provides a sample request.
        
        @param request: UpdateAggregateRemediationRequest
        @return: UpdateAggregateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregate_remediation_with_options_async(request, runtime)

    def update_aggregator_with_options(
        self,
        tmp_req: config_20200907_models.UpdateAggregatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregatorResponse:
        """
        @summary The management account or delegated administrator account of a resource directory can be used to modify the name and description of an account group. The management account or delegated administrator account can also be used to add or remove members from the account group.
        
        @description This topic provides an example on how to add a member to the account group `ca-dacf86d8314e00eb***`. The member ID is `173808452267****`, the member name is `Tony`, and the member belongs to the resource directory `ResourceDirectory`.
        
        @param tmp_req: UpdateAggregatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregatorResponse
        """
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
        """
        @summary The management account or delegated administrator account of a resource directory can be used to modify the name and description of an account group. The management account or delegated administrator account can also be used to add or remove members from the account group.
        
        @description This topic provides an example on how to add a member to the account group `ca-dacf86d8314e00eb***`. The member ID is `173808452267****`, the member name is `Tony`, and the member belongs to the resource directory `ResourceDirectory`.
        
        @param tmp_req: UpdateAggregatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggregatorResponse
        """
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
        """
        @summary The management account or delegated administrator account of a resource directory can be used to modify the name and description of an account group. The management account or delegated administrator account can also be used to add or remove members from the account group.
        
        @description This topic provides an example on how to add a member to the account group `ca-dacf86d8314e00eb***`. The member ID is `173808452267****`, the member name is `Tony`, and the member belongs to the resource directory `ResourceDirectory`.
        
        @param request: UpdateAggregatorRequest
        @return: UpdateAggregatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_aggregator_with_options(request, runtime)

    async def update_aggregator_async(
        self,
        request: config_20200907_models.UpdateAggregatorRequest,
    ) -> config_20200907_models.UpdateAggregatorResponse:
        """
        @summary The management account or delegated administrator account of a resource directory can be used to modify the name and description of an account group. The management account or delegated administrator account can also be used to add or remove members from the account group.
        
        @description This topic provides an example on how to add a member to the account group `ca-dacf86d8314e00eb***`. The member ID is `173808452267****`, the member name is `Tony`, and the member belongs to the resource directory `ResourceDirectory`.
        
        @param request: UpdateAggregatorRequest
        @return: UpdateAggregatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregator_with_options_async(request, runtime)

    def update_compliance_pack_with_options(
        self,
        tmp_req: config_20200907_models.UpdateCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateCompliancePackResponse:
        """
        @summary Modifies the configurations of a specific compliance package in the current account.
        
        @description This topic provides an example on how to change the value of the `eip-bandwidth-limit` parameter of a rule in the compliance package `cp-a8a8626622af0082***` to `20`.
        
        @param tmp_req: UpdateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCompliancePackResponse
        """
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
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Modifies the configurations of a specific compliance package in the current account.
        
        @description This topic provides an example on how to change the value of the `eip-bandwidth-limit` parameter of a rule in the compliance package `cp-a8a8626622af0082***` to `20`.
        
        @param tmp_req: UpdateCompliancePackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCompliancePackResponse
        """
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
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Modifies the configurations of a specific compliance package in the current account.
        
        @description This topic provides an example on how to change the value of the `eip-bandwidth-limit` parameter of a rule in the compliance package `cp-a8a8626622af0082***` to `20`.
        
        @param request: UpdateCompliancePackRequest
        @return: UpdateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_compliance_pack_with_options(request, runtime)

    async def update_compliance_pack_async(
        self,
        request: config_20200907_models.UpdateCompliancePackRequest,
    ) -> config_20200907_models.UpdateCompliancePackResponse:
        """
        @summary Modifies the configurations of a specific compliance package in the current account.
        
        @description This topic provides an example on how to change the value of the `eip-bandwidth-limit` parameter of a rule in the compliance package `cp-a8a8626622af0082***` to `20`.
        
        @param request: UpdateCompliancePackRequest
        @return: UpdateCompliancePackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_compliance_pack_with_options_async(request, runtime)

    def update_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.UpdateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateConfigDeliveryChannelResponse:
        """
        @summary Modifies a delivery channel.
        
        @description In this example, a delivery channel is disabled. The ID of the delivery channel is `cdc-8e45ff4e06a3a8***```. The Status parameter is set to 0. After the delivery channel is disabled, Cloud Config retains the most recent delivery configuration and stops the delivery of resource data.
        
        @param request: UpdateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not UtilClient.is_unset(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConfigDeliveryChannel',
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
            config_20200907_models.UpdateConfigDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.UpdateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateConfigDeliveryChannelResponse:
        """
        @summary Modifies a delivery channel.
        
        @description In this example, a delivery channel is disabled. The ID of the delivery channel is `cdc-8e45ff4e06a3a8***```. The Status parameter is set to 0. After the delivery channel is disabled, Cloud Config retains the most recent delivery configuration and stops the delivery of resource data.
        
        @param request: UpdateConfigDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigDeliveryChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliant_snapshot):
            query['CompliantSnapshot'] = request.compliant_snapshot
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            query['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            query['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_condition):
            query['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not UtilClient.is_unset(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            query['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.delivery_snapshot_time):
            query['DeliverySnapshotTime'] = request.delivery_snapshot_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            query['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            query['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConfigDeliveryChannel',
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
            config_20200907_models.UpdateConfigDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_delivery_channel(
        self,
        request: config_20200907_models.UpdateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.UpdateConfigDeliveryChannelResponse:
        """
        @summary Modifies a delivery channel.
        
        @description In this example, a delivery channel is disabled. The ID of the delivery channel is `cdc-8e45ff4e06a3a8***```. The Status parameter is set to 0. After the delivery channel is disabled, Cloud Config retains the most recent delivery configuration and stops the delivery of resource data.
        
        @param request: UpdateConfigDeliveryChannelRequest
        @return: UpdateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_config_delivery_channel_with_options(request, runtime)

    async def update_config_delivery_channel_async(
        self,
        request: config_20200907_models.UpdateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.UpdateConfigDeliveryChannelResponse:
        """
        @summary Modifies a delivery channel.
        
        @description In this example, a delivery channel is disabled. The ID of the delivery channel is `cdc-8e45ff4e06a3a8***```. The Status parameter is set to 0. After the delivery channel is disabled, Cloud Config retains the most recent delivery configuration and stops the delivery of resource data.
        
        @param request: UpdateConfigDeliveryChannelRequest
        @return: UpdateConfigDeliveryChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_config_delivery_channel_with_options_async(request, runtime)

    def update_config_rule_with_options(
        self,
        tmp_req: config_20200907_models.UpdateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateConfigRuleResponse:
        """
        @summary Modifies the description, input parameters, and risk level of a rule.
        
        @description This topic provides an example on how to change the risk level of the rule `cr-a260626622af0005***` to `3`, which indicates low risk level.
        
        @param tmp_req: UpdateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigRuleResponse
        """
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
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Modifies the description, input parameters, and risk level of a rule.
        
        @description This topic provides an example on how to change the risk level of the rule `cr-a260626622af0005***` to `3`, which indicates low risk level.
        
        @param tmp_req: UpdateConfigRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigRuleResponse
        """
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
        if not UtilClient.is_unset(request.exclude_region_ids_scope):
            body['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_group_ids_scope):
            body['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        body_flat = {}
        if not UtilClient.is_unset(request.exclude_tags_scope):
            body_flat['ExcludeTagsScope'] = request.exclude_tags_scope
        if not UtilClient.is_unset(request.input_parameters_shrink):
            body['InputParameters'] = request.input_parameters_shrink
        if not UtilClient.is_unset(request.maximum_execution_frequency):
            body['MaximumExecutionFrequency'] = request.maximum_execution_frequency
        if not UtilClient.is_unset(request.region_ids_scope):
            body['RegionIdsScope'] = request.region_ids_scope
        if not UtilClient.is_unset(request.resource_group_ids_scope):
            body['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not UtilClient.is_unset(request.resource_ids_scope):
            body['ResourceIdsScope'] = request.resource_ids_scope
        if not UtilClient.is_unset(request.resource_types_scope_shrink):
            body['ResourceTypesScope'] = request.resource_types_scope_shrink
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
        if not UtilClient.is_unset(request.tag_key_scope):
            body['TagKeyScope'] = request.tag_key_scope
        if not UtilClient.is_unset(request.tag_value_scope):
            body['TagValueScope'] = request.tag_value_scope
        if not UtilClient.is_unset(request.tags_scope):
            body_flat['TagsScope'] = request.tags_scope
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Modifies the description, input parameters, and risk level of a rule.
        
        @description This topic provides an example on how to change the risk level of the rule `cr-a260626622af0005***` to `3`, which indicates low risk level.
        
        @param request: UpdateConfigRuleRequest
        @return: UpdateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_config_rule_with_options(request, runtime)

    async def update_config_rule_async(
        self,
        request: config_20200907_models.UpdateConfigRuleRequest,
    ) -> config_20200907_models.UpdateConfigRuleResponse:
        """
        @summary Modifies the description, input parameters, and risk level of a rule.
        
        @description This topic provides an example on how to change the risk level of the rule `cr-a260626622af0005***` to `3`, which indicates low risk level.
        
        @param request: UpdateConfigRuleRequest
        @return: UpdateConfigRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_config_rule_with_options_async(request, runtime)

    def update_configuration_recorder_with_options(
        self,
        request: config_20200907_models.UpdateConfigurationRecorderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateConfigurationRecorderResponse:
        """
        @summary Modifies the resource monitoring scope of the current account.
        
        @description This topic provides an example on how to change the resource monitoring scope of the current account to ACS::ECS::Instance.
        
        @param request: UpdateConfigurationRecorderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigurationRecorderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_types):
            body['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigurationRecorder',
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
            config_20200907_models.UpdateConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_configuration_recorder_with_options_async(
        self,
        request: config_20200907_models.UpdateConfigurationRecorderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateConfigurationRecorderResponse:
        """
        @summary Modifies the resource monitoring scope of the current account.
        
        @description This topic provides an example on how to change the resource monitoring scope of the current account to ACS::ECS::Instance.
        
        @param request: UpdateConfigurationRecorderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigurationRecorderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_types):
            body['ResourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigurationRecorder',
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
            config_20200907_models.UpdateConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_configuration_recorder(
        self,
        request: config_20200907_models.UpdateConfigurationRecorderRequest,
    ) -> config_20200907_models.UpdateConfigurationRecorderResponse:
        """
        @summary Modifies the resource monitoring scope of the current account.
        
        @description This topic provides an example on how to change the resource monitoring scope of the current account to ACS::ECS::Instance.
        
        @param request: UpdateConfigurationRecorderRequest
        @return: UpdateConfigurationRecorderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_configuration_recorder_with_options(request, runtime)

    async def update_configuration_recorder_async(
        self,
        request: config_20200907_models.UpdateConfigurationRecorderRequest,
    ) -> config_20200907_models.UpdateConfigurationRecorderResponse:
        """
        @summary Modifies the resource monitoring scope of the current account.
        
        @description This topic provides an example on how to change the resource monitoring scope of the current account to ACS::ECS::Instance.
        
        @param request: UpdateConfigurationRecorderRequest
        @return: UpdateConfigurationRecorderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_configuration_recorder_with_options_async(request, runtime)

    def update_delivery_channel_with_options(
        self,
        request: config_20200907_models.UpdateDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateDeliveryChannelResponse:
        """
        @deprecated OpenAPI UpdateDeliveryChannel is deprecated, please use Config::2020-09-07::UpdateConfigDeliveryChannel,Config::2020-09-07::UpdateAggregateConfigDeliveryChannel instead.
        
        @summary Modifies a delivery channel.
        
        @description This topic provides an example on how to change the status of the delivery channel whose ID is `cdc-8e45ff4e06a3a8***` to 0, which indicates that the delivery channel is disabled. After the delivery channel is disabled, Cloud Config retains the last delivery configuration and stops resource data delivery.
        
        @param request: UpdateDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeliveryChannelResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            body['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            body['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_assume_role_arn):
            body['DeliveryChannelAssumeRoleArn'] = request.delivery_channel_assume_role_arn
        if not UtilClient.is_unset(request.delivery_channel_condition):
            body['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_id):
            body['DeliveryChannelId'] = request.delivery_channel_id
        if not UtilClient.is_unset(request.delivery_channel_name):
            body['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            body['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            body['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            body['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeliveryChannel',
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
            config_20200907_models.UpdateDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_delivery_channel_with_options_async(
        self,
        request: config_20200907_models.UpdateDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateDeliveryChannelResponse:
        """
        @deprecated OpenAPI UpdateDeliveryChannel is deprecated, please use Config::2020-09-07::UpdateConfigDeliveryChannel,Config::2020-09-07::UpdateAggregateConfigDeliveryChannel instead.
        
        @summary Modifies a delivery channel.
        
        @description This topic provides an example on how to change the status of the delivery channel whose ID is `cdc-8e45ff4e06a3a8***` to 0, which indicates that the delivery channel is disabled. After the delivery channel is disabled, Cloud Config retains the last delivery configuration and stops resource data delivery.
        
        @param request: UpdateDeliveryChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeliveryChannelResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_item_change_notification):
            body['ConfigurationItemChangeNotification'] = request.configuration_item_change_notification
        if not UtilClient.is_unset(request.configuration_snapshot):
            body['ConfigurationSnapshot'] = request.configuration_snapshot
        if not UtilClient.is_unset(request.delivery_channel_assume_role_arn):
            body['DeliveryChannelAssumeRoleArn'] = request.delivery_channel_assume_role_arn
        if not UtilClient.is_unset(request.delivery_channel_condition):
            body['DeliveryChannelCondition'] = request.delivery_channel_condition
        if not UtilClient.is_unset(request.delivery_channel_id):
            body['DeliveryChannelId'] = request.delivery_channel_id
        if not UtilClient.is_unset(request.delivery_channel_name):
            body['DeliveryChannelName'] = request.delivery_channel_name
        if not UtilClient.is_unset(request.delivery_channel_target_arn):
            body['DeliveryChannelTargetArn'] = request.delivery_channel_target_arn
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.non_compliant_notification):
            body['NonCompliantNotification'] = request.non_compliant_notification
        if not UtilClient.is_unset(request.oversized_data_osstarget_arn):
            body['OversizedDataOSSTargetArn'] = request.oversized_data_osstarget_arn
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeliveryChannel',
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
            config_20200907_models.UpdateDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_delivery_channel(
        self,
        request: config_20200907_models.UpdateDeliveryChannelRequest,
    ) -> config_20200907_models.UpdateDeliveryChannelResponse:
        """
        @deprecated OpenAPI UpdateDeliveryChannel is deprecated, please use Config::2020-09-07::UpdateConfigDeliveryChannel,Config::2020-09-07::UpdateAggregateConfigDeliveryChannel instead.
        
        @summary Modifies a delivery channel.
        
        @description This topic provides an example on how to change the status of the delivery channel whose ID is `cdc-8e45ff4e06a3a8***` to 0, which indicates that the delivery channel is disabled. After the delivery channel is disabled, Cloud Config retains the last delivery configuration and stops resource data delivery.
        
        @param request: UpdateDeliveryChannelRequest
        @return: UpdateDeliveryChannelResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_delivery_channel_with_options(request, runtime)

    async def update_delivery_channel_async(
        self,
        request: config_20200907_models.UpdateDeliveryChannelRequest,
    ) -> config_20200907_models.UpdateDeliveryChannelResponse:
        """
        @deprecated OpenAPI UpdateDeliveryChannel is deprecated, please use Config::2020-09-07::UpdateConfigDeliveryChannel,Config::2020-09-07::UpdateAggregateConfigDeliveryChannel instead.
        
        @summary Modifies a delivery channel.
        
        @description This topic provides an example on how to change the status of the delivery channel whose ID is `cdc-8e45ff4e06a3a8***` to 0, which indicates that the delivery channel is disabled. After the delivery channel is disabled, Cloud Config retains the last delivery configuration and stops resource data delivery.
        
        @param request: UpdateDeliveryChannelRequest
        @return: UpdateDeliveryChannelResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_delivery_channel_with_options_async(request, runtime)

    def update_integrated_service_status_with_options(
        self,
        request: config_20200907_models.UpdateIntegratedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateIntegratedServiceStatusResponse:
        """
        @summary Enables or disables the integration of a cloud service.
        
        @param request: UpdateIntegratedServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIntegratedServiceStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integrated_types):
            body['IntegratedTypes'] = request.integrated_types
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegratedServiceStatus',
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
            config_20200907_models.UpdateIntegratedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_integrated_service_status_with_options_async(
        self,
        request: config_20200907_models.UpdateIntegratedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateIntegratedServiceStatusResponse:
        """
        @summary Enables or disables the integration of a cloud service.
        
        @param request: UpdateIntegratedServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIntegratedServiceStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integrated_types):
            body['IntegratedTypes'] = request.integrated_types
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegratedServiceStatus',
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
            config_20200907_models.UpdateIntegratedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_integrated_service_status(
        self,
        request: config_20200907_models.UpdateIntegratedServiceStatusRequest,
    ) -> config_20200907_models.UpdateIntegratedServiceStatusResponse:
        """
        @summary Enables or disables the integration of a cloud service.
        
        @param request: UpdateIntegratedServiceStatusRequest
        @return: UpdateIntegratedServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_integrated_service_status_with_options(request, runtime)

    async def update_integrated_service_status_async(
        self,
        request: config_20200907_models.UpdateIntegratedServiceStatusRequest,
    ) -> config_20200907_models.UpdateIntegratedServiceStatusResponse:
        """
        @summary Enables or disables the integration of a cloud service.
        
        @param request: UpdateIntegratedServiceStatusRequest
        @return: UpdateIntegratedServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_integrated_service_status_with_options_async(request, runtime)

    def update_remediation_with_options(
        self,
        request: config_20200907_models.UpdateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateRemediationResponse:
        """
        @summary Updates a remediation template for a rule.
        
        @description This topic describes how to change the execution mode of the `crr-909ba2d4716700eb***` remediation setting to `AUTO_EXECUTION`, which specifies automatic remediation. This topic also provides a sample request.
        
        @param request: UpdateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRemediationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.remediation_id):
            body['RemediationId'] = request.remediation_id
        if not UtilClient.is_unset(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not UtilClient.is_unset(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRemediation',
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
            config_20200907_models.UpdateRemediationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_remediation_with_options_async(
        self,
        request: config_20200907_models.UpdateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateRemediationResponse:
        """
        @summary Updates a remediation template for a rule.
        
        @description This topic describes how to change the execution mode of the `crr-909ba2d4716700eb***` remediation setting to `AUTO_EXECUTION`, which specifies automatic remediation. This topic also provides a sample request.
        
        @param request: UpdateRemediationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRemediationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.remediation_id):
            body['RemediationId'] = request.remediation_id
        if not UtilClient.is_unset(request.remediation_template_id):
            body['RemediationTemplateId'] = request.remediation_template_id
        if not UtilClient.is_unset(request.remediation_type):
            body['RemediationType'] = request.remediation_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRemediation',
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
            config_20200907_models.UpdateRemediationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_remediation(
        self,
        request: config_20200907_models.UpdateRemediationRequest,
    ) -> config_20200907_models.UpdateRemediationResponse:
        """
        @summary Updates a remediation template for a rule.
        
        @description This topic describes how to change the execution mode of the `crr-909ba2d4716700eb***` remediation setting to `AUTO_EXECUTION`, which specifies automatic remediation. This topic also provides a sample request.
        
        @param request: UpdateRemediationRequest
        @return: UpdateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_remediation_with_options(request, runtime)

    async def update_remediation_async(
        self,
        request: config_20200907_models.UpdateRemediationRequest,
    ) -> config_20200907_models.UpdateRemediationResponse:
        """
        @summary Updates a remediation template for a rule.
        
        @description This topic describes how to change the execution mode of the `crr-909ba2d4716700eb***` remediation setting to `AUTO_EXECUTION`, which specifies automatic remediation. This topic also provides a sample request.
        
        @param request: UpdateRemediationRequest
        @return: UpdateRemediationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_remediation_with_options_async(request, runtime)
