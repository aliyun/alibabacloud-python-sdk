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

    def create_aggregate_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.CreateAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateConfigDeliveryChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        runtime = util_models.RuntimeOptions()
        return self.create_aggregate_config_delivery_channel_with_options(request, runtime)

    async def create_aggregate_config_delivery_channel_async(
        self,
        request: config_20200907_models.CreateAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.CreateAggregateConfigDeliveryChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aggregate_config_delivery_channel_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not UtilClient.is_unset(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
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
        if not UtilClient.is_unset(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not UtilClient.is_unset(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
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

    def create_aggregate_remediation_with_options(
        self,
        request: config_20200907_models.CreateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateAggregateRemediationResponse:
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

    def create_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.CreateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateConfigDeliveryChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        runtime = util_models.RuntimeOptions()
        return self.create_config_delivery_channel_with_options(request, runtime)

    async def create_config_delivery_channel_async(
        self,
        request: config_20200907_models.CreateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.CreateConfigDeliveryChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_config_delivery_channel_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
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
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
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

    def create_remediation_with_options(
        self,
        request: config_20200907_models.CreateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.CreateRemediationResponse:
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

    def delete_remediations_with_options(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DeleteRemediationsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_remediations_with_options(request, runtime)

    async def delete_remediations_async(
        self,
        request: config_20200907_models.DeleteRemediationsRequest,
    ) -> config_20200907_models.DeleteRemediationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_remediations_with_options_async(request, runtime)

    def detach_aggregate_config_rule_to_compliance_pack_with_options(
        self,
        request: config_20200907_models.DetachAggregateConfigRuleToCompliancePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.DetachAggregateConfigRuleToCompliancePackResponse:
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

    def get_aggregate_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigDeliveryChannelResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_delivery_channel_with_options(request, runtime)

    async def get_aggregate_config_delivery_channel_async(
        self,
        request: config_20200907_models.GetAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.GetAggregateConfigDeliveryChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_delivery_channel_with_options_async(request, runtime)

    def get_aggregate_config_rule_with_options(
        self,
        request: config_20200907_models.GetAggregateConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateConfigRuleResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_config_rules_report_with_options(request, runtime)

    async def get_aggregate_config_rules_report_async(
        self,
        request: config_20200907_models.GetAggregateConfigRulesReportRequest,
    ) -> config_20200907_models.GetAggregateConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_config_rules_report_with_options_async(request, runtime)

    def get_aggregate_discovered_resource_with_options(
        self,
        request: config_20200907_models.GetAggregateDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateDiscoveredResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateDiscoveredResource',
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
            config_20200907_models.GetAggregateDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_discovered_resource_with_options_async(
        self,
        request: config_20200907_models.GetAggregateDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateDiscoveredResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateDiscoveredResource',
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
            config_20200907_models.GetAggregateDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_discovered_resource(
        self,
        request: config_20200907_models.GetAggregateDiscoveredResourceRequest,
    ) -> config_20200907_models.GetAggregateDiscoveredResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_discovered_resource_with_options(request, runtime)

    async def get_aggregate_discovered_resource_async(
        self,
        request: config_20200907_models.GetAggregateDiscoveredResourceRequest,
    ) -> config_20200907_models.GetAggregateDiscoveredResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_discovered_resource_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_by_config_rule_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceByConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceByConfigRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.compliance_type):
            query['ComplianceType'] = request.compliance_type
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
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

    def get_aggregate_resource_compliance_group_by_region_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByRegionResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_group_by_region_with_options(request, runtime)

    async def get_aggregate_resource_compliance_group_by_region_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByRegionRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_group_by_region_with_options_async(request, runtime)

    def get_aggregate_resource_compliance_group_by_resource_type_with_options(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_resource_compliance_group_by_resource_type_with_options(request, runtime)

    async def get_aggregate_resource_compliance_group_by_resource_type_async(
        self,
        request: config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetAggregateResourceComplianceGroupByResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_resource_compliance_group_by_resource_type_with_options_async(request, runtime)

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

    def get_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.GetConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigDeliveryChannelResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_config_delivery_channel_with_options(request, runtime)

    async def get_config_delivery_channel_async(
        self,
        request: config_20200907_models.GetConfigDeliveryChannelRequest,
    ) -> config_20200907_models.GetConfigDeliveryChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_delivery_channel_with_options_async(request, runtime)

    def get_config_rule_with_options(
        self,
        request: config_20200907_models.GetConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRuleResponse:
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
        request: config_20200907_models.GetConfigRulesReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_config_rules_report_with_options(request, runtime)

    async def get_config_rules_report_async(
        self,
        request: config_20200907_models.GetConfigRulesReportRequest,
    ) -> config_20200907_models.GetConfigRulesReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_rules_report_with_options_async(request, runtime)

    def get_discovered_resource_with_options(
        self,
        request: config_20200907_models.GetDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResource',
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
            config_20200907_models.GetDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_with_options_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetDiscoveredResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResource',
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
            config_20200907_models.GetDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource(
        self,
        request: config_20200907_models.GetDiscoveredResourceRequest,
    ) -> config_20200907_models.GetDiscoveredResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_with_options(request, runtime)

    async def get_discovered_resource_async(
        self,
        request: config_20200907_models.GetDiscoveredResourceRequest,
    ) -> config_20200907_models.GetDiscoveredResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_discovered_resource_with_options_async(request, runtime)

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

    def get_managed_rule_with_options(
        self,
        request: config_20200907_models.GetManagedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetManagedRuleResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_managed_rule_with_options(request, runtime)

    async def get_managed_rule_async(
        self,
        request: config_20200907_models.GetManagedRuleRequest,
    ) -> config_20200907_models.GetManagedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_managed_rule_with_options_async(request, runtime)

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

    def get_resource_compliance_group_by_region_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceGroupByRegionResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_group_by_region_with_options(request, runtime)

    async def get_resource_compliance_group_by_region_async(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByRegionRequest,
    ) -> config_20200907_models.GetResourceComplianceGroupByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_group_by_region_with_options_async(request, runtime)

    def get_resource_compliance_group_by_resource_type_with_options(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.GetResourceComplianceGroupByResourceTypeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_group_by_resource_type_with_options(request, runtime)

    async def get_resource_compliance_group_by_resource_type_async(
        self,
        request: config_20200907_models.GetResourceComplianceGroupByResourceTypeRequest,
    ) -> config_20200907_models.GetResourceComplianceGroupByResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_group_by_resource_type_with_options_async(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_compliance_packs_with_options(request, runtime)

    async def list_aggregate_compliance_packs_async(
        self,
        request: config_20200907_models.ListAggregateCompliancePacksRequest,
    ) -> config_20200907_models.ListAggregateCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_compliance_packs_with_options_async(request, runtime)

    def list_aggregate_config_delivery_channels_with_options(
        self,
        request: config_20200907_models.ListAggregateConfigDeliveryChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateConfigDeliveryChannelsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_config_delivery_channels_with_options(request, runtime)

    async def list_aggregate_config_delivery_channels_async(
        self,
        request: config_20200907_models.ListAggregateConfigDeliveryChannelsRequest,
    ) -> config_20200907_models.ListAggregateConfigDeliveryChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_config_delivery_channels_with_options_async(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_config_rules_with_options(request, runtime)

    async def list_aggregate_config_rules_async(
        self,
        request: config_20200907_models.ListAggregateConfigRulesRequest,
    ) -> config_20200907_models.ListAggregateConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_config_rules_with_options_async(request, runtime)

    def list_aggregate_discovered_resources_with_options(
        self,
        request: config_20200907_models.ListAggregateDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateDiscoveredResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_discovered_resources_with_options(request, runtime)

    async def list_aggregate_discovered_resources_async(
        self,
        request: config_20200907_models.ListAggregateDiscoveredResourcesRequest,
    ) -> config_20200907_models.ListAggregateDiscoveredResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_discovered_resources_with_options_async(request, runtime)

    def list_aggregate_remediations_with_options(
        self,
        request: config_20200907_models.ListAggregateRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListAggregateRemediationsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_compliance_packs_with_options(request, runtime)

    async def list_compliance_packs_async(
        self,
        request: config_20200907_models.ListCompliancePacksRequest,
    ) -> config_20200907_models.ListCompliancePacksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_compliance_packs_with_options_async(request, runtime)

    def list_config_delivery_channels_with_options(
        self,
        request: config_20200907_models.ListConfigDeliveryChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListConfigDeliveryChannelsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_config_delivery_channels_with_options(request, runtime)

    async def list_config_delivery_channels_async(
        self,
        request: config_20200907_models.ListConfigDeliveryChannelsRequest,
    ) -> config_20200907_models.ListConfigDeliveryChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_delivery_channels_with_options_async(request, runtime)

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

    def list_discovered_resources_with_options(
        self,
        request: config_20200907_models.ListDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListDiscoveredResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_discovered_resources_with_options(request, runtime)

    async def list_discovered_resources_async(
        self,
        request: config_20200907_models.ListDiscoveredResourcesRequest,
    ) -> config_20200907_models.ListDiscoveredResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_discovered_resources_with_options_async(request, runtime)

    def list_managed_rules_with_options(
        self,
        request: config_20200907_models.ListManagedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListManagedRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
        runtime = util_models.RuntimeOptions()
        return self.list_managed_rules_with_options(request, runtime)

    async def list_managed_rules_async(
        self,
        request: config_20200907_models.ListManagedRulesRequest,
    ) -> config_20200907_models.ListManagedRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_managed_rules_with_options_async(request, runtime)

    def list_remediation_templates_with_options(
        self,
        request: config_20200907_models.ListRemediationTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.managed_rule_identifier):
            query['ManagedRuleIdentifier'] = request.managed_rule_identifier
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.managed_rule_identifier):
            query['ManagedRuleIdentifier'] = request.managed_rule_identifier
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
        runtime = util_models.RuntimeOptions()
        return self.list_remediation_templates_with_options(request, runtime)

    async def list_remediation_templates_async(
        self,
        request: config_20200907_models.ListRemediationTemplatesRequest,
    ) -> config_20200907_models.ListRemediationTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_remediation_templates_with_options_async(request, runtime)

    def list_remediations_with_options(
        self,
        request: config_20200907_models.ListRemediationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListRemediationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_rule_ids):
            query['ConfigRuleIds'] = request.config_rule_ids
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
        runtime = util_models.RuntimeOptions()
        return self.list_resource_evaluation_results_with_options(request, runtime)

    async def list_resource_evaluation_results_async(
        self,
        request: config_20200907_models.ListResourceEvaluationResultsRequest,
    ) -> config_20200907_models.ListResourceEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_evaluation_results_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: config_20200907_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.ListTagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: config_20200907_models.ListTagResourcesRequest,
    ) -> config_20200907_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.config_rule_id):
            query['ConfigRuleId'] = request.config_rule_id
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
        runtime = util_models.RuntimeOptions()
        return self.start_remediation_with_options(request, runtime)

    async def start_remediation_async(
        self,
        request: config_20200907_models.StartRemediationRequest,
    ) -> config_20200907_models.StartRemediationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_remediation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        tmp_req: config_20200907_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.TagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: config_20200907_models.TagResourcesRequest,
    ) -> config_20200907_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: config_20200907_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UntagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: config_20200907_models.UntagResourcesRequest,
    ) -> config_20200907_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

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

    def update_aggregate_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.UpdateAggregateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateConfigDeliveryChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator_id):
            query['AggregatorId'] = request.aggregator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        runtime = util_models.RuntimeOptions()
        return self.update_aggregate_config_delivery_channel_with_options(request, runtime)

    async def update_aggregate_config_delivery_channel_async(
        self,
        request: config_20200907_models.UpdateAggregateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.UpdateAggregateConfigDeliveryChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aggregate_config_delivery_channel_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not UtilClient.is_unset(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
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
        if not UtilClient.is_unset(request.exclude_account_ids_scope):
            body['ExcludeAccountIdsScope'] = request.exclude_account_ids_scope
        if not UtilClient.is_unset(request.exclude_folder_ids_scope):
            body['ExcludeFolderIdsScope'] = request.exclude_folder_ids_scope
        if not UtilClient.is_unset(request.exclude_resource_ids_scope):
            body['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
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

    def update_aggregate_remediation_with_options(
        self,
        request: config_20200907_models.UpdateAggregateRemediationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateAggregateRemediationResponse:
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

    def update_config_delivery_channel_with_options(
        self,
        request: config_20200907_models.UpdateConfigDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20200907_models.UpdateConfigDeliveryChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        runtime = util_models.RuntimeOptions()
        return self.update_config_delivery_channel_with_options(request, runtime)

    async def update_config_delivery_channel_async(
        self,
        request: config_20200907_models.UpdateConfigDeliveryChannelRequest,
    ) -> config_20200907_models.UpdateConfigDeliveryChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_config_delivery_channel_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
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
        if not UtilClient.is_unset(request.tag_key_logic_scope):
            body['TagKeyLogicScope'] = request.tag_key_logic_scope
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
