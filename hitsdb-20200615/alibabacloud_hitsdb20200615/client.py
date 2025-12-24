# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_hitsdb20200615 import models as main_models
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
        self._endpoint = self.get_endpoint('hitsdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_ldps_columnar_index_status_with_options(
        self,
        request: main_models.CheckLdpsColumnarIndexStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckLdpsColumnarIndexStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckLdpsColumnarIndexStatus',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckLdpsColumnarIndexStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_ldps_columnar_index_status_with_options_async(
        self,
        request: main_models.CheckLdpsColumnarIndexStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckLdpsColumnarIndexStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckLdpsColumnarIndexStatus',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckLdpsColumnarIndexStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_ldps_columnar_index_status(
        self,
        request: main_models.CheckLdpsColumnarIndexStatusRequest,
    ) -> main_models.CheckLdpsColumnarIndexStatusResponse:
        runtime = RuntimeOptions()
        return self.check_ldps_columnar_index_status_with_options(request, runtime)

    async def check_ldps_columnar_index_status_async(
        self,
        request: main_models.CheckLdpsColumnarIndexStatusRequest,
    ) -> main_models.CheckLdpsColumnarIndexStatusResponse:
        runtime = RuntimeOptions()
        return await self.check_ldps_columnar_index_status_with_options_async(request, runtime)

    def create_auto_scaling_config_with_options(
        self,
        tmp_req: main_models.CreateAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoScalingConfigResponse:
        tmp_req.validate()
        request = main_models.CreateAutoScalingConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scale_rule_list):
            request.scale_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scale_rule_list, 'ScaleRuleList', 'json')
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.effective_time_end):
            query['EffectiveTimeEnd'] = request.effective_time_end
        if not DaraCore.is_null(request.effective_time_start):
            query['EffectiveTimeStart'] = request.effective_time_start
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nodes_max):
            query['NodesMax'] = request.nodes_max
        if not DaraCore.is_null(request.nodes_min):
            query['NodesMin'] = request.nodes_min
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_rule_list_shrink):
            query['ScaleRuleList'] = request.scale_rule_list_shrink
        if not DaraCore.is_null(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        if not DaraCore.is_null(request.storage_capacity_max):
            query['StorageCapacityMax'] = request.storage_capacity_max
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoScalingConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_scaling_config_with_options_async(
        self,
        tmp_req: main_models.CreateAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoScalingConfigResponse:
        tmp_req.validate()
        request = main_models.CreateAutoScalingConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scale_rule_list):
            request.scale_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scale_rule_list, 'ScaleRuleList', 'json')
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.effective_time_end):
            query['EffectiveTimeEnd'] = request.effective_time_end
        if not DaraCore.is_null(request.effective_time_start):
            query['EffectiveTimeStart'] = request.effective_time_start
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nodes_max):
            query['NodesMax'] = request.nodes_max
        if not DaraCore.is_null(request.nodes_min):
            query['NodesMin'] = request.nodes_min
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_rule_list_shrink):
            query['ScaleRuleList'] = request.scale_rule_list_shrink
        if not DaraCore.is_null(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        if not DaraCore.is_null(request.storage_capacity_max):
            query['StorageCapacityMax'] = request.storage_capacity_max
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoScalingConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_scaling_config(
        self,
        request: main_models.CreateAutoScalingConfigRequest,
    ) -> main_models.CreateAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return self.create_auto_scaling_config_with_options(request, runtime)

    async def create_auto_scaling_config_async(
        self,
        request: main_models.CreateAutoScalingConfigRequest,
    ) -> main_models.CreateAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_auto_scaling_config_with_options_async(request, runtime)

    def create_auto_scaling_rule_with_options(
        self,
        request: main_models.CreateAutoScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.observation_window):
            query['ObservationWindow'] = request.observation_window
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.scale_in_step):
            query['ScaleInStep'] = request.scale_in_step
        if not DaraCore.is_null(request.scale_out_step):
            query['ScaleOutStep'] = request.scale_out_step
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_metric):
            query['TargetMetric'] = request.target_metric
        if not DaraCore.is_null(request.target_nodes):
            query['TargetNodes'] = request.target_nodes
        if not DaraCore.is_null(request.threshold_lower):
            query['ThresholdLower'] = request.threshold_lower
        if not DaraCore.is_null(request.threshold_upper):
            query['ThresholdUpper'] = request.threshold_upper
        if not DaraCore.is_null(request.trigger_cron_expr):
            query['TriggerCronExpr'] = request.trigger_cron_expr
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoScalingRule',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_scaling_rule_with_options_async(
        self,
        request: main_models.CreateAutoScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.observation_window):
            query['ObservationWindow'] = request.observation_window
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.scale_in_step):
            query['ScaleInStep'] = request.scale_in_step
        if not DaraCore.is_null(request.scale_out_step):
            query['ScaleOutStep'] = request.scale_out_step
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_metric):
            query['TargetMetric'] = request.target_metric
        if not DaraCore.is_null(request.target_nodes):
            query['TargetNodes'] = request.target_nodes
        if not DaraCore.is_null(request.threshold_lower):
            query['ThresholdLower'] = request.threshold_lower
        if not DaraCore.is_null(request.threshold_upper):
            query['ThresholdUpper'] = request.threshold_upper
        if not DaraCore.is_null(request.trigger_cron_expr):
            query['TriggerCronExpr'] = request.trigger_cron_expr
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoScalingRule',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_scaling_rule(
        self,
        request: main_models.CreateAutoScalingRuleRequest,
    ) -> main_models.CreateAutoScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.create_auto_scaling_rule_with_options(request, runtime)

    async def create_auto_scaling_rule_async(
        self,
        request: main_models.CreateAutoScalingRuleRequest,
    ) -> main_models.CreateAutoScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_auto_scaling_rule_with_options_async(request, runtime)

    def create_ldps_compute_group_with_options(
        self,
        request: main_models.CreateLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLdpsComputeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ldps_compute_group_with_options_async(
        self,
        request: main_models.CreateLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLdpsComputeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ldps_compute_group(
        self,
        request: main_models.CreateLdpsComputeGroupRequest,
    ) -> main_models.CreateLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return self.create_ldps_compute_group_with_options(request, runtime)

    async def create_ldps_compute_group_async(
        self,
        request: main_models.CreateLdpsComputeGroupRequest,
    ) -> main_models.CreateLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_ldps_compute_group_with_options_async(request, runtime)

    def create_lindorm_instance_with_options(
        self,
        request: main_models.CreateLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not DaraCore.is_null(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not DaraCore.is_null(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not DaraCore.is_null(request.core_spec):
            query['CoreSpec'] = request.core_spec
        if not DaraCore.is_null(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not DaraCore.is_null(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not DaraCore.is_null(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not DaraCore.is_null(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
        if not DaraCore.is_null(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not DaraCore.is_null(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not DaraCore.is_null(request.log_disk_category):
            query['LogDiskCategory'] = request.log_disk_category
        if not DaraCore.is_null(request.log_num):
            query['LogNum'] = request.log_num
        if not DaraCore.is_null(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not DaraCore.is_null(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not DaraCore.is_null(request.lts_num):
            query['LtsNum'] = request.lts_num
        if not DaraCore.is_null(request.lts_spec):
            query['LtsSpec'] = request.lts_spec
        if not DaraCore.is_null(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not DaraCore.is_null(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.stream_num):
            query['StreamNum'] = request.stream_num
        if not DaraCore.is_null(request.stream_spec):
            query['StreamSpec'] = request.stream_spec
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not DaraCore.is_null(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lindorm_instance_with_options_async(
        self,
        request: main_models.CreateLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not DaraCore.is_null(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not DaraCore.is_null(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not DaraCore.is_null(request.core_spec):
            query['CoreSpec'] = request.core_spec
        if not DaraCore.is_null(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not DaraCore.is_null(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not DaraCore.is_null(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not DaraCore.is_null(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
        if not DaraCore.is_null(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not DaraCore.is_null(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not DaraCore.is_null(request.log_disk_category):
            query['LogDiskCategory'] = request.log_disk_category
        if not DaraCore.is_null(request.log_num):
            query['LogNum'] = request.log_num
        if not DaraCore.is_null(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not DaraCore.is_null(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not DaraCore.is_null(request.lts_num):
            query['LtsNum'] = request.lts_num
        if not DaraCore.is_null(request.lts_spec):
            query['LtsSpec'] = request.lts_spec
        if not DaraCore.is_null(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not DaraCore.is_null(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.stream_num):
            query['StreamNum'] = request.stream_num
        if not DaraCore.is_null(request.stream_spec):
            query['StreamSpec'] = request.stream_spec
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not DaraCore.is_null(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lindorm_instance(
        self,
        request: main_models.CreateLindormInstanceRequest,
    ) -> main_models.CreateLindormInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_lindorm_instance_with_options(request, runtime)

    async def create_lindorm_instance_async(
        self,
        request: main_models.CreateLindormInstanceRequest,
    ) -> main_models.CreateLindormInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_lindorm_instance_with_options_async(request, runtime)

    def create_lindorm_v2instance_with_options(
        self,
        request: main_models.CreateLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not DaraCore.is_null(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.capacity_storage_size):
            query['CapacityStorageSize'] = request.capacity_storage_size
        if not DaraCore.is_null(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not DaraCore.is_null(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_pattern):
            query['ClusterPattern'] = request.cluster_pattern
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.enable_capacity_storage):
            query['EnableCapacityStorage'] = request.enable_capacity_storage
        if not DaraCore.is_null(request.engine_list):
            query['EngineList'] = request.engine_list
        if not DaraCore.is_null(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLindormV2InstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lindorm_v2instance_with_options_async(
        self,
        request: main_models.CreateLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not DaraCore.is_null(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.capacity_storage_size):
            query['CapacityStorageSize'] = request.capacity_storage_size
        if not DaraCore.is_null(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not DaraCore.is_null(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_pattern):
            query['ClusterPattern'] = request.cluster_pattern
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.enable_capacity_storage):
            query['EnableCapacityStorage'] = request.enable_capacity_storage
        if not DaraCore.is_null(request.engine_list):
            query['EngineList'] = request.engine_list
        if not DaraCore.is_null(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLindormV2InstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lindorm_v2instance(
        self,
        request: main_models.CreateLindormV2InstanceRequest,
    ) -> main_models.CreateLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return self.create_lindorm_v2instance_with_options(request, runtime)

    async def create_lindorm_v2instance_async(
        self,
        request: main_models.CreateLindormV2InstanceRequest,
    ) -> main_models.CreateLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_lindorm_v2instance_with_options_async(request, runtime)

    def delete_auto_scaling_config_with_options(
        self,
        request: main_models.DeleteAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoScalingConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_scaling_config_with_options_async(
        self,
        request: main_models.DeleteAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoScalingConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_scaling_config(
        self,
        request: main_models.DeleteAutoScalingConfigRequest,
    ) -> main_models.DeleteAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_auto_scaling_config_with_options(request, runtime)

    async def delete_auto_scaling_config_async(
        self,
        request: main_models.DeleteAutoScalingConfigRequest,
    ) -> main_models.DeleteAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_auto_scaling_config_with_options_async(request, runtime)

    def delete_auto_scaling_rule_with_options(
        self,
        request: main_models.DeleteAutoScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoScalingRule',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_scaling_rule_with_options_async(
        self,
        request: main_models.DeleteAutoScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoScalingRule',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_scaling_rule(
        self,
        request: main_models.DeleteAutoScalingRuleRequest,
    ) -> main_models.DeleteAutoScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_auto_scaling_rule_with_options(request, runtime)

    async def delete_auto_scaling_rule_async(
        self,
        request: main_models.DeleteAutoScalingRuleRequest,
    ) -> main_models.DeleteAutoScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_auto_scaling_rule_with_options_async(request, runtime)

    def delete_custom_resource_with_options(
        self,
        request: main_models.DeleteCustomResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomResource',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_resource_with_options_async(
        self,
        request: main_models.DeleteCustomResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomResource',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_resource(
        self,
        request: main_models.DeleteCustomResourceRequest,
    ) -> main_models.DeleteCustomResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_resource_with_options(request, runtime)

    async def delete_custom_resource_async(
        self,
        request: main_models.DeleteCustomResourceRequest,
    ) -> main_models.DeleteCustomResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_resource_with_options_async(request, runtime)

    def delete_ldps_compute_group_with_options(
        self,
        request: main_models.DeleteLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLdpsComputeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ldps_compute_group_with_options_async(
        self,
        request: main_models.DeleteLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLdpsComputeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ldps_compute_group(
        self,
        request: main_models.DeleteLdpsComputeGroupRequest,
    ) -> main_models.DeleteLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_ldps_compute_group_with_options(request, runtime)

    async def delete_ldps_compute_group_async(
        self,
        request: main_models.DeleteLdpsComputeGroupRequest,
    ) -> main_models.DeleteLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_ldps_compute_group_with_options_async(request, runtime)

    def deploy_ldps_semi_managed_component_with_options(
        self,
        request: main_models.DeployLdpsSemiManagedComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployLdpsSemiManagedComponentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployLdpsSemiManagedComponent',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployLdpsSemiManagedComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_ldps_semi_managed_component_with_options_async(
        self,
        request: main_models.DeployLdpsSemiManagedComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployLdpsSemiManagedComponentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployLdpsSemiManagedComponent',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployLdpsSemiManagedComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_ldps_semi_managed_component(
        self,
        request: main_models.DeployLdpsSemiManagedComponentRequest,
    ) -> main_models.DeployLdpsSemiManagedComponentResponse:
        runtime = RuntimeOptions()
        return self.deploy_ldps_semi_managed_component_with_options(request, runtime)

    async def deploy_ldps_semi_managed_component_async(
        self,
        request: main_models.DeployLdpsSemiManagedComponentRequest,
    ) -> main_models.DeployLdpsSemiManagedComponentResponse:
        runtime = RuntimeOptions()
        return await self.deploy_ldps_semi_managed_component_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def get_auto_scaling_config_with_options(
        self,
        request: main_models.GetAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_config_with_options_async(
        self,
        request: main_models.GetAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_config(
        self,
        request: main_models.GetAutoScalingConfigRequest,
    ) -> main_models.GetAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return self.get_auto_scaling_config_with_options(request, runtime)

    async def get_auto_scaling_config_async(
        self,
        request: main_models.GetAutoScalingConfigRequest,
    ) -> main_models.GetAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_scaling_config_with_options_async(request, runtime)

    def get_auto_scaling_rule_with_options(
        self,
        request: main_models.GetAutoScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingRule',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_rule_with_options_async(
        self,
        request: main_models.GetAutoScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingRule',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_rule(
        self,
        request: main_models.GetAutoScalingRuleRequest,
    ) -> main_models.GetAutoScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.get_auto_scaling_rule_with_options(request, runtime)

    async def get_auto_scaling_rule_async(
        self,
        request: main_models.GetAutoScalingRuleRequest,
    ) -> main_models.GetAutoScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_scaling_rule_with_options_async(request, runtime)

    def get_client_source_ip_with_options(
        self,
        request: main_models.GetClientSourceIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientSourceIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientSourceIp',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientSourceIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_client_source_ip_with_options_async(
        self,
        request: main_models.GetClientSourceIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientSourceIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientSourceIp',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientSourceIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_client_source_ip(
        self,
        request: main_models.GetClientSourceIpRequest,
    ) -> main_models.GetClientSourceIpResponse:
        runtime = RuntimeOptions()
        return self.get_client_source_ip_with_options(request, runtime)

    async def get_client_source_ip_async(
        self,
        request: main_models.GetClientSourceIpRequest,
    ) -> main_models.GetClientSourceIpResponse:
        runtime = RuntimeOptions()
        return await self.get_client_source_ip_with_options_async(request, runtime)

    def get_engine_default_auth_with_options(
        self,
        request: main_models.GetEngineDefaultAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEngineDefaultAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEngineDefaultAuth',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEngineDefaultAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_engine_default_auth_with_options_async(
        self,
        request: main_models.GetEngineDefaultAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEngineDefaultAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEngineDefaultAuth',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEngineDefaultAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_engine_default_auth(
        self,
        request: main_models.GetEngineDefaultAuthRequest,
    ) -> main_models.GetEngineDefaultAuthResponse:
        runtime = RuntimeOptions()
        return self.get_engine_default_auth_with_options(request, runtime)

    async def get_engine_default_auth_async(
        self,
        request: main_models.GetEngineDefaultAuthRequest,
    ) -> main_models.GetEngineDefaultAuthResponse:
        runtime = RuntimeOptions()
        return await self.get_engine_default_auth_with_options_async(request, runtime)

    def get_instance_ip_white_list_with_options(
        self,
        request: main_models.GetInstanceIpWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceIpWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceIpWhiteList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_ip_white_list_with_options_async(
        self,
        request: main_models.GetInstanceIpWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceIpWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceIpWhiteList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_ip_white_list(
        self,
        request: main_models.GetInstanceIpWhiteListRequest,
    ) -> main_models.GetInstanceIpWhiteListResponse:
        runtime = RuntimeOptions()
        return self.get_instance_ip_white_list_with_options(request, runtime)

    async def get_instance_ip_white_list_async(
        self,
        request: main_models.GetInstanceIpWhiteListRequest,
    ) -> main_models.GetInstanceIpWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_ip_white_list_with_options_async(request, runtime)

    def get_instance_security_groups_with_options(
        self,
        request: main_models.GetInstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceSecurityGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_security_groups_with_options_async(
        self,
        request: main_models.GetInstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceSecurityGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_security_groups(
        self,
        request: main_models.GetInstanceSecurityGroupsRequest,
    ) -> main_models.GetInstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return self.get_instance_security_groups_with_options(request, runtime)

    async def get_instance_security_groups_async(
        self,
        request: main_models.GetInstanceSecurityGroupsRequest,
    ) -> main_models.GetInstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_security_groups_with_options_async(request, runtime)

    def get_instance_summary_with_options(
        self,
        request: main_models.GetInstanceSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceSummary',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_summary_with_options_async(
        self,
        request: main_models.GetInstanceSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceSummary',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_summary(
        self,
        request: main_models.GetInstanceSummaryRequest,
    ) -> main_models.GetInstanceSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_instance_summary_with_options(request, runtime)

    async def get_instance_summary_async(
        self,
        request: main_models.GetInstanceSummaryRequest,
    ) -> main_models.GetInstanceSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_summary_with_options_async(request, runtime)

    def get_ldps_compute_group_with_options(
        self,
        request: main_models.GetLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLdpsComputeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ldps_compute_group_with_options_async(
        self,
        request: main_models.GetLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLdpsComputeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ldps_compute_group(
        self,
        request: main_models.GetLdpsComputeGroupRequest,
    ) -> main_models.GetLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return self.get_ldps_compute_group_with_options(request, runtime)

    async def get_ldps_compute_group_async(
        self,
        request: main_models.GetLdpsComputeGroupRequest,
    ) -> main_models.GetLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_ldps_compute_group_with_options_async(request, runtime)

    def get_ldps_namespaced_quota_with_options(
        self,
        request: main_models.GetLdpsNamespacedQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLdpsNamespacedQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLdpsNamespacedQuota',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLdpsNamespacedQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ldps_namespaced_quota_with_options_async(
        self,
        request: main_models.GetLdpsNamespacedQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLdpsNamespacedQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLdpsNamespacedQuota',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLdpsNamespacedQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ldps_namespaced_quota(
        self,
        request: main_models.GetLdpsNamespacedQuotaRequest,
    ) -> main_models.GetLdpsNamespacedQuotaResponse:
        runtime = RuntimeOptions()
        return self.get_ldps_namespaced_quota_with_options(request, runtime)

    async def get_ldps_namespaced_quota_async(
        self,
        request: main_models.GetLdpsNamespacedQuotaRequest,
    ) -> main_models.GetLdpsNamespacedQuotaResponse:
        runtime = RuntimeOptions()
        return await self.get_ldps_namespaced_quota_with_options_async(request, runtime)

    def get_ldps_resource_cost_with_options(
        self,
        request: main_models.GetLdpsResourceCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLdpsResourceCostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLdpsResourceCost',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLdpsResourceCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ldps_resource_cost_with_options_async(
        self,
        request: main_models.GetLdpsResourceCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLdpsResourceCostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLdpsResourceCost',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLdpsResourceCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ldps_resource_cost(
        self,
        request: main_models.GetLdpsResourceCostRequest,
    ) -> main_models.GetLdpsResourceCostResponse:
        runtime = RuntimeOptions()
        return self.get_ldps_resource_cost_with_options(request, runtime)

    async def get_ldps_resource_cost_async(
        self,
        request: main_models.GetLdpsResourceCostRequest,
    ) -> main_models.GetLdpsResourceCostResponse:
        runtime = RuntimeOptions()
        return await self.get_ldps_resource_cost_with_options_async(request, runtime)

    def get_lindorm_engine_config_with_options(
        self,
        request: main_models.GetLindormEngineConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormEngineConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormEngineConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_engine_config_with_options_async(
        self,
        request: main_models.GetLindormEngineConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormEngineConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormEngineConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_engine_config(
        self,
        request: main_models.GetLindormEngineConfigRequest,
    ) -> main_models.GetLindormEngineConfigResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_engine_config_with_options(request, runtime)

    async def get_lindorm_engine_config_async(
        self,
        request: main_models.GetLindormEngineConfigRequest,
    ) -> main_models.GetLindormEngineConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_engine_config_with_options_async(request, runtime)

    def get_lindorm_fs_used_detail_with_options(
        self,
        request: main_models.GetLindormFsUsedDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormFsUsedDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormFsUsedDetail',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormFsUsedDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_fs_used_detail_with_options_async(
        self,
        request: main_models.GetLindormFsUsedDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormFsUsedDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormFsUsedDetail',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormFsUsedDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_fs_used_detail(
        self,
        request: main_models.GetLindormFsUsedDetailRequest,
    ) -> main_models.GetLindormFsUsedDetailResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_fs_used_detail_with_options(request, runtime)

    async def get_lindorm_fs_used_detail_async(
        self,
        request: main_models.GetLindormFsUsedDetailRequest,
    ) -> main_models.GetLindormFsUsedDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_fs_used_detail_with_options_async(request, runtime)

    def get_lindorm_instance_with_options(
        self,
        request: main_models.GetLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_instance_with_options_async(
        self,
        request: main_models.GetLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_instance(
        self,
        request: main_models.GetLindormInstanceRequest,
    ) -> main_models.GetLindormInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_instance_with_options(request, runtime)

    async def get_lindorm_instance_async(
        self,
        request: main_models.GetLindormInstanceRequest,
    ) -> main_models.GetLindormInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_instance_with_options_async(request, runtime)

    def get_lindorm_instance_engine_list_with_options(
        self,
        request: main_models.GetLindormInstanceEngineListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormInstanceEngineListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormInstanceEngineList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormInstanceEngineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_instance_engine_list_with_options_async(
        self,
        request: main_models.GetLindormInstanceEngineListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormInstanceEngineListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormInstanceEngineList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormInstanceEngineListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_instance_engine_list(
        self,
        request: main_models.GetLindormInstanceEngineListRequest,
    ) -> main_models.GetLindormInstanceEngineListResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_instance_engine_list_with_options(request, runtime)

    async def get_lindorm_instance_engine_list_async(
        self,
        request: main_models.GetLindormInstanceEngineListRequest,
    ) -> main_models.GetLindormInstanceEngineListResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_instance_engine_list_with_options_async(request, runtime)

    def get_lindorm_instance_list_with_options(
        self,
        request: main_models.GetLindormInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_str):
            query['QueryStr'] = request.query_str
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.support_engine):
            query['SupportEngine'] = request.support_engine
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormInstanceList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_instance_list_with_options_async(
        self,
        request: main_models.GetLindormInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_str):
            query['QueryStr'] = request.query_str
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.support_engine):
            query['SupportEngine'] = request.support_engine
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormInstanceList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_instance_list(
        self,
        request: main_models.GetLindormInstanceListRequest,
    ) -> main_models.GetLindormInstanceListResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_instance_list_with_options(request, runtime)

    async def get_lindorm_instance_list_async(
        self,
        request: main_models.GetLindormInstanceListRequest,
    ) -> main_models.GetLindormInstanceListResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_instance_list_with_options_async(request, runtime)

    def get_lindorm_v2instance_with_options(
        self,
        request: main_models.GetLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_v2instance_with_options_async(
        self,
        request: main_models.GetLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_v2instance(
        self,
        request: main_models.GetLindormV2InstanceRequest,
    ) -> main_models.GetLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_v2instance_with_options(request, runtime)

    async def get_lindorm_v2instance_async(
        self,
        request: main_models.GetLindormV2InstanceRequest,
    ) -> main_models.GetLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_v2instance_with_options_async(request, runtime)

    def get_lindorm_v2instance_details_with_options(
        self,
        request: main_models.GetLindormV2InstanceDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2InstanceDetails',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_v2instance_details_with_options_async(
        self,
        request: main_models.GetLindormV2InstanceDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2InstanceDetails',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_v2instance_details(
        self,
        request: main_models.GetLindormV2InstanceDetailsRequest,
    ) -> main_models.GetLindormV2InstanceDetailsResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_v2instance_details_with_options(request, runtime)

    async def get_lindorm_v2instance_details_async(
        self,
        request: main_models.GetLindormV2InstanceDetailsRequest,
    ) -> main_models.GetLindormV2InstanceDetailsResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_v2instance_details_with_options_async(request, runtime)

    def get_lindorm_v2instance_engine_list_with_options(
        self,
        request: main_models.GetLindormV2InstanceEngineListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceEngineListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2InstanceEngineList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceEngineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_v2instance_engine_list_with_options_async(
        self,
        request: main_models.GetLindormV2InstanceEngineListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceEngineListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2InstanceEngineList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceEngineListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_v2instance_engine_list(
        self,
        request: main_models.GetLindormV2InstanceEngineListRequest,
    ) -> main_models.GetLindormV2InstanceEngineListResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_v2instance_engine_list_with_options(request, runtime)

    async def get_lindorm_v2instance_engine_list_async(
        self,
        request: main_models.GetLindormV2InstanceEngineListRequest,
    ) -> main_models.GetLindormV2InstanceEngineListResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_v2instance_engine_list_with_options_async(request, runtime)

    def get_lindorm_v2instance_for_terraform_with_options(
        self,
        request: main_models.GetLindormV2InstanceForTerraformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceForTerraformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2InstanceForTerraform',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceForTerraformResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_v2instance_for_terraform_with_options_async(
        self,
        request: main_models.GetLindormV2InstanceForTerraformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceForTerraformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2InstanceForTerraform',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceForTerraformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_v2instance_for_terraform(
        self,
        request: main_models.GetLindormV2InstanceForTerraformRequest,
    ) -> main_models.GetLindormV2InstanceForTerraformResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_v2instance_for_terraform_with_options(request, runtime)

    async def get_lindorm_v2instance_for_terraform_async(
        self,
        request: main_models.GetLindormV2InstanceForTerraformRequest,
    ) -> main_models.GetLindormV2InstanceForTerraformResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_v2instance_for_terraform_with_options_async(request, runtime)

    def get_lindorm_v2instance_security_groups_with_options(
        self,
        request: main_models.GetLindormV2InstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2InstanceSecurityGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_v2instance_security_groups_with_options_async(
        self,
        request: main_models.GetLindormV2InstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2InstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2InstanceSecurityGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2InstanceSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_v2instance_security_groups(
        self,
        request: main_models.GetLindormV2InstanceSecurityGroupsRequest,
    ) -> main_models.GetLindormV2InstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_v2instance_security_groups_with_options(request, runtime)

    async def get_lindorm_v2instance_security_groups_async(
        self,
        request: main_models.GetLindormV2InstanceSecurityGroupsRequest,
    ) -> main_models.GetLindormV2InstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_v2instance_security_groups_with_options_async(request, runtime)

    def get_lindorm_v2storage_usage_with_options(
        self,
        request: main_models.GetLindormV2StorageUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2StorageUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2StorageUsage',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2StorageUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_v2storage_usage_with_options_async(
        self,
        request: main_models.GetLindormV2StorageUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2StorageUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2StorageUsage',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2StorageUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_v2storage_usage(
        self,
        request: main_models.GetLindormV2StorageUsageRequest,
    ) -> main_models.GetLindormV2StorageUsageResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_v2storage_usage_with_options(request, runtime)

    async def get_lindorm_v2storage_usage_async(
        self,
        request: main_models.GetLindormV2StorageUsageRequest,
    ) -> main_models.GetLindormV2StorageUsageResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_v2storage_usage_with_options_async(request, runtime)

    def get_lindorm_v2stream_engine_info_with_options(
        self,
        request: main_models.GetLindormV2StreamEngineInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2StreamEngineInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2StreamEngineInfo',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2StreamEngineInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_v2stream_engine_info_with_options_async(
        self,
        request: main_models.GetLindormV2StreamEngineInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLindormV2StreamEngineInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLindormV2StreamEngineInfo',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLindormV2StreamEngineInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_v2stream_engine_info(
        self,
        request: main_models.GetLindormV2StreamEngineInfoRequest,
    ) -> main_models.GetLindormV2StreamEngineInfoResponse:
        runtime = RuntimeOptions()
        return self.get_lindorm_v2stream_engine_info_with_options(request, runtime)

    async def get_lindorm_v2stream_engine_info_async(
        self,
        request: main_models.GetLindormV2StreamEngineInfoRequest,
    ) -> main_models.GetLindormV2StreamEngineInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_lindorm_v2stream_engine_info_with_options_async(request, runtime)

    def list_auto_scaling_configs_with_options(
        self,
        tmp_req: main_models.ListAutoScalingConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoScalingConfigsResponse:
        tmp_req.validate()
        request = main_models.ListAutoScalingConfigsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scale_types):
            request.scale_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.scale_types, 'ScaleTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_types_shrink):
            query['ScaleTypes'] = request.scale_types_shrink
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoScalingConfigs',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoScalingConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_configs_with_options_async(
        self,
        tmp_req: main_models.ListAutoScalingConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoScalingConfigsResponse:
        tmp_req.validate()
        request = main_models.ListAutoScalingConfigsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scale_types):
            request.scale_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.scale_types, 'ScaleTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_types_shrink):
            query['ScaleTypes'] = request.scale_types_shrink
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoScalingConfigs',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoScalingConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_configs(
        self,
        request: main_models.ListAutoScalingConfigsRequest,
    ) -> main_models.ListAutoScalingConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_auto_scaling_configs_with_options(request, runtime)

    async def list_auto_scaling_configs_async(
        self,
        request: main_models.ListAutoScalingConfigsRequest,
    ) -> main_models.ListAutoScalingConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_auto_scaling_configs_with_options_async(request, runtime)

    def list_auto_scaling_records_with_options(
        self,
        tmp_req: main_models.ListAutoScalingRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoScalingRecordsResponse:
        tmp_req.validate()
        request = main_models.ListAutoScalingRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scale_types):
            request.scale_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.scale_types, 'ScaleTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_types_shrink):
            query['ScaleTypes'] = request.scale_types_shrink
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoScalingRecords',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoScalingRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_records_with_options_async(
        self,
        tmp_req: main_models.ListAutoScalingRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoScalingRecordsResponse:
        tmp_req.validate()
        request = main_models.ListAutoScalingRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scale_types):
            request.scale_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.scale_types, 'ScaleTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_types_shrink):
            query['ScaleTypes'] = request.scale_types_shrink
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoScalingRecords',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoScalingRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_records(
        self,
        request: main_models.ListAutoScalingRecordsRequest,
    ) -> main_models.ListAutoScalingRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_auto_scaling_records_with_options(request, runtime)

    async def list_auto_scaling_records_async(
        self,
        request: main_models.ListAutoScalingRecordsRequest,
    ) -> main_models.ListAutoScalingRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_auto_scaling_records_with_options_async(request, runtime)

    def list_auto_scaling_rules_with_options(
        self,
        request: main_models.ListAutoScalingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoScalingRules',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_rules_with_options_async(
        self,
        request: main_models.ListAutoScalingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoScalingRules',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_rules(
        self,
        request: main_models.ListAutoScalingRulesRequest,
    ) -> main_models.ListAutoScalingRulesResponse:
        runtime = RuntimeOptions()
        return self.list_auto_scaling_rules_with_options(request, runtime)

    async def list_auto_scaling_rules_async(
        self,
        request: main_models.ListAutoScalingRulesRequest,
    ) -> main_models.ListAutoScalingRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_auto_scaling_rules_with_options_async(request, runtime)

    def list_ldps_compute_groups_with_options(
        self,
        request: main_models.ListLdpsComputeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLdpsComputeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLdpsComputeGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLdpsComputeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ldps_compute_groups_with_options_async(
        self,
        request: main_models.ListLdpsComputeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLdpsComputeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLdpsComputeGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLdpsComputeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ldps_compute_groups(
        self,
        request: main_models.ListLdpsComputeGroupsRequest,
    ) -> main_models.ListLdpsComputeGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_ldps_compute_groups_with_options(request, runtime)

    async def list_ldps_compute_groups_async(
        self,
        request: main_models.ListLdpsComputeGroupsRequest,
    ) -> main_models.ListLdpsComputeGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_ldps_compute_groups_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-06-15',
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
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-06-15',
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

    def migrate_single_zone_to_multi_zone_with_options(
        self,
        request: main_models.MigrateSingleZoneToMultiZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateSingleZoneToMultiZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbitrary_vswitch_id):
            query['ArbitraryVSwitchId'] = request.arbitrary_vswitch_id
        if not DaraCore.is_null(request.arbitrary_zone_id):
            query['ArbitraryZoneId'] = request.arbitrary_zone_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateSingleZoneToMultiZone',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateSingleZoneToMultiZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_single_zone_to_multi_zone_with_options_async(
        self,
        request: main_models.MigrateSingleZoneToMultiZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateSingleZoneToMultiZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbitrary_vswitch_id):
            query['ArbitraryVSwitchId'] = request.arbitrary_vswitch_id
        if not DaraCore.is_null(request.arbitrary_zone_id):
            query['ArbitraryZoneId'] = request.arbitrary_zone_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateSingleZoneToMultiZone',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateSingleZoneToMultiZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_single_zone_to_multi_zone(
        self,
        request: main_models.MigrateSingleZoneToMultiZoneRequest,
    ) -> main_models.MigrateSingleZoneToMultiZoneResponse:
        runtime = RuntimeOptions()
        return self.migrate_single_zone_to_multi_zone_with_options(request, runtime)

    async def migrate_single_zone_to_multi_zone_async(
        self,
        request: main_models.MigrateSingleZoneToMultiZoneRequest,
    ) -> main_models.MigrateSingleZoneToMultiZoneResponse:
        runtime = RuntimeOptions()
        return await self.migrate_single_zone_to_multi_zone_with_options_async(request, runtime)

    def modify_auto_scaling_config_with_options(
        self,
        tmp_req: main_models.ModifyAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoScalingConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyAutoScalingConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scale_rule_list):
            request.scale_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scale_rule_list, 'ScaleRuleList', 'json')
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.effective_time_end):
            query['EffectiveTimeEnd'] = request.effective_time_end
        if not DaraCore.is_null(request.effective_time_start):
            query['EffectiveTimeStart'] = request.effective_time_start
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nodes_max):
            query['NodesMax'] = request.nodes_max
        if not DaraCore.is_null(request.nodes_min):
            query['NodesMin'] = request.nodes_min
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_rule_list_shrink):
            query['ScaleRuleList'] = request.scale_rule_list_shrink
        if not DaraCore.is_null(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        if not DaraCore.is_null(request.storage_capacity_max):
            query['StorageCapacityMax'] = request.storage_capacity_max
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoScalingConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_scaling_config_with_options_async(
        self,
        tmp_req: main_models.ModifyAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoScalingConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyAutoScalingConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scale_rule_list):
            request.scale_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scale_rule_list, 'ScaleRuleList', 'json')
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.effective_time_end):
            query['EffectiveTimeEnd'] = request.effective_time_end
        if not DaraCore.is_null(request.effective_time_start):
            query['EffectiveTimeStart'] = request.effective_time_start
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nodes_max):
            query['NodesMax'] = request.nodes_max
        if not DaraCore.is_null(request.nodes_min):
            query['NodesMin'] = request.nodes_min
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_rule_list_shrink):
            query['ScaleRuleList'] = request.scale_rule_list_shrink
        if not DaraCore.is_null(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        if not DaraCore.is_null(request.storage_capacity_max):
            query['StorageCapacityMax'] = request.storage_capacity_max
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoScalingConfig',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_scaling_config(
        self,
        request: main_models.ModifyAutoScalingConfigRequest,
    ) -> main_models.ModifyAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_auto_scaling_config_with_options(request, runtime)

    async def modify_auto_scaling_config_async(
        self,
        request: main_models.ModifyAutoScalingConfigRequest,
    ) -> main_models.ModifyAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_auto_scaling_config_with_options_async(request, runtime)

    def modify_auto_scaling_rule_with_options(
        self,
        request: main_models.ModifyAutoScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.observation_window):
            query['ObservationWindow'] = request.observation_window
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.scale_in_step):
            query['ScaleInStep'] = request.scale_in_step
        if not DaraCore.is_null(request.scale_out_step):
            query['ScaleOutStep'] = request.scale_out_step
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_metric):
            query['TargetMetric'] = request.target_metric
        if not DaraCore.is_null(request.target_nodes):
            query['TargetNodes'] = request.target_nodes
        if not DaraCore.is_null(request.threshold_lower):
            query['ThresholdLower'] = request.threshold_lower
        if not DaraCore.is_null(request.threshold_upper):
            query['ThresholdUpper'] = request.threshold_upper
        if not DaraCore.is_null(request.trigger_cron_expr):
            query['TriggerCronExpr'] = request.trigger_cron_expr
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoScalingRule',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_scaling_rule_with_options_async(
        self,
        request: main_models.ModifyAutoScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.observation_window):
            query['ObservationWindow'] = request.observation_window
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.scale_in_step):
            query['ScaleInStep'] = request.scale_in_step
        if not DaraCore.is_null(request.scale_out_step):
            query['ScaleOutStep'] = request.scale_out_step
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_metric):
            query['TargetMetric'] = request.target_metric
        if not DaraCore.is_null(request.target_nodes):
            query['TargetNodes'] = request.target_nodes
        if not DaraCore.is_null(request.threshold_lower):
            query['ThresholdLower'] = request.threshold_lower
        if not DaraCore.is_null(request.threshold_upper):
            query['ThresholdUpper'] = request.threshold_upper
        if not DaraCore.is_null(request.trigger_cron_expr):
            query['TriggerCronExpr'] = request.trigger_cron_expr
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoScalingRule',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_scaling_rule(
        self,
        request: main_models.ModifyAutoScalingRuleRequest,
    ) -> main_models.ModifyAutoScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_auto_scaling_rule_with_options(request, runtime)

    async def modify_auto_scaling_rule_async(
        self,
        request: main_models.ModifyAutoScalingRuleRequest,
    ) -> main_models.ModifyAutoScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_auto_scaling_rule_with_options_async(request, runtime)

    def modify_instance_pay_type_with_options(
        self,
        request: main_models.ModifyInstancePayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstancePayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstancePayType',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_pay_type_with_options_async(
        self,
        request: main_models.ModifyInstancePayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstancePayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstancePayType',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstancePayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_pay_type(
        self,
        request: main_models.ModifyInstancePayTypeRequest,
    ) -> main_models.ModifyInstancePayTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_pay_type_with_options(request, runtime)

    async def modify_instance_pay_type_async(
        self,
        request: main_models.ModifyInstancePayTypeRequest,
    ) -> main_models.ModifyInstancePayTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_pay_type_with_options_async(request, runtime)

    def modify_lindorm_v2instance_with_options(
        self,
        request: main_models.ModifyLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not DaraCore.is_null(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_list):
            query['NodeGroupList'] = request.node_group_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLindormV2InstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lindorm_v2instance_with_options_async(
        self,
        request: main_models.ModifyLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not DaraCore.is_null(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_list):
            query['NodeGroupList'] = request.node_group_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLindormV2InstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lindorm_v2instance(
        self,
        request: main_models.ModifyLindormV2InstanceRequest,
    ) -> main_models.ModifyLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_lindorm_v2instance_with_options(request, runtime)

    async def modify_lindorm_v2instance_async(
        self,
        request: main_models.ModifyLindormV2InstanceRequest,
    ) -> main_models.ModifyLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_lindorm_v2instance_with_options_async(request, runtime)

    def modify_lindorm_v2instance_security_groups_with_options(
        self,
        request: main_models.ModifyLindormV2InstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLindormV2InstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_groups):
            query['SecurityGroups'] = request.security_groups
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLindormV2InstanceSecurityGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLindormV2InstanceSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lindorm_v2instance_security_groups_with_options_async(
        self,
        request: main_models.ModifyLindormV2InstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLindormV2InstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_groups):
            query['SecurityGroups'] = request.security_groups
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLindormV2InstanceSecurityGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLindormV2InstanceSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lindorm_v2instance_security_groups(
        self,
        request: main_models.ModifyLindormV2InstanceSecurityGroupsRequest,
    ) -> main_models.ModifyLindormV2InstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return self.modify_lindorm_v2instance_security_groups_with_options(request, runtime)

    async def modify_lindorm_v2instance_security_groups_async(
        self,
        request: main_models.ModifyLindormV2InstanceSecurityGroupsRequest,
    ) -> main_models.ModifyLindormV2InstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return await self.modify_lindorm_v2instance_security_groups_with_options_async(request, runtime)

    def modify_lindorm_v2white_ip_list_with_options(
        self,
        request: main_models.ModifyLindormV2WhiteIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLindormV2WhiteIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_group):
            query['DeleteGroup'] = request.delete_group
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.white_ip_list):
            query['WhiteIpList'] = request.white_ip_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLindormV2WhiteIpList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLindormV2WhiteIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lindorm_v2white_ip_list_with_options_async(
        self,
        request: main_models.ModifyLindormV2WhiteIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLindormV2WhiteIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_group):
            query['DeleteGroup'] = request.delete_group
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.white_ip_list):
            query['WhiteIpList'] = request.white_ip_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLindormV2WhiteIpList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLindormV2WhiteIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lindorm_v2white_ip_list(
        self,
        request: main_models.ModifyLindormV2WhiteIpListRequest,
    ) -> main_models.ModifyLindormV2WhiteIpListResponse:
        runtime = RuntimeOptions()
        return self.modify_lindorm_v2white_ip_list_with_options(request, runtime)

    async def modify_lindorm_v2white_ip_list_async(
        self,
        request: main_models.ModifyLindormV2WhiteIpListRequest,
    ) -> main_models.ModifyLindormV2WhiteIpListResponse:
        runtime = RuntimeOptions()
        return await self.modify_lindorm_v2white_ip_list_with_options_async(request, runtime)

    def open_compute_engine_with_options(
        self,
        request: main_models.OpenComputeEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenComputeEngineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenComputeEngine',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenComputeEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_compute_engine_with_options_async(
        self,
        request: main_models.OpenComputeEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenComputeEngineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenComputeEngine',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenComputeEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_compute_engine(
        self,
        request: main_models.OpenComputeEngineRequest,
    ) -> main_models.OpenComputeEngineResponse:
        runtime = RuntimeOptions()
        return self.open_compute_engine_with_options(request, runtime)

    async def open_compute_engine_async(
        self,
        request: main_models.OpenComputeEngineRequest,
    ) -> main_models.OpenComputeEngineResponse:
        runtime = RuntimeOptions()
        return await self.open_compute_engine_with_options_async(request, runtime)

    def open_compute_pre_check_with_options(
        self,
        request: main_models.OpenComputePreCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenComputePreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenComputePreCheck',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenComputePreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_compute_pre_check_with_options_async(
        self,
        request: main_models.OpenComputePreCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenComputePreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenComputePreCheck',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenComputePreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_compute_pre_check(
        self,
        request: main_models.OpenComputePreCheckRequest,
    ) -> main_models.OpenComputePreCheckResponse:
        runtime = RuntimeOptions()
        return self.open_compute_pre_check_with_options(request, runtime)

    async def open_compute_pre_check_async(
        self,
        request: main_models.OpenComputePreCheckRequest,
    ) -> main_models.OpenComputePreCheckResponse:
        runtime = RuntimeOptions()
        return await self.open_compute_pre_check_with_options_async(request, runtime)

    def open_ldps_columnar_index_with_options(
        self,
        request: main_models.OpenLdpsColumnarIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenLdpsColumnarIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenLdpsColumnarIndex',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenLdpsColumnarIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_ldps_columnar_index_with_options_async(
        self,
        request: main_models.OpenLdpsColumnarIndexRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenLdpsColumnarIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenLdpsColumnarIndex',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenLdpsColumnarIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_ldps_columnar_index(
        self,
        request: main_models.OpenLdpsColumnarIndexRequest,
    ) -> main_models.OpenLdpsColumnarIndexResponse:
        runtime = RuntimeOptions()
        return self.open_ldps_columnar_index_with_options(request, runtime)

    async def open_ldps_columnar_index_async(
        self,
        request: main_models.OpenLdpsColumnarIndexRequest,
    ) -> main_models.OpenLdpsColumnarIndexResponse:
        runtime = RuntimeOptions()
        return await self.open_ldps_columnar_index_with_options_async(request, runtime)

    def release_lindorm_instance_with_options(
        self,
        request: main_models.ReleaseLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_lindorm_instance_with_options_async(
        self,
        request: main_models.ReleaseLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_lindorm_instance(
        self,
        request: main_models.ReleaseLindormInstanceRequest,
    ) -> main_models.ReleaseLindormInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_lindorm_instance_with_options(request, runtime)

    async def release_lindorm_instance_async(
        self,
        request: main_models.ReleaseLindormInstanceRequest,
    ) -> main_models.ReleaseLindormInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_lindorm_instance_with_options_async(request, runtime)

    def release_lindorm_v2instance_with_options(
        self,
        request: main_models.ReleaseLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseLindormV2InstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_lindorm_v2instance_with_options_async(
        self,
        request: main_models.ReleaseLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseLindormV2InstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_lindorm_v2instance(
        self,
        request: main_models.ReleaseLindormV2InstanceRequest,
    ) -> main_models.ReleaseLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return self.release_lindorm_v2instance_with_options(request, runtime)

    async def release_lindorm_v2instance_async(
        self,
        request: main_models.ReleaseLindormV2InstanceRequest,
    ) -> main_models.ReleaseLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_lindorm_v2instance_with_options_async(request, runtime)

    def renew_lindorm_instance_with_options(
        self,
        request: main_models.RenewLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_lindorm_instance_with_options_async(
        self,
        request: main_models.RenewLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_lindorm_instance(
        self,
        request: main_models.RenewLindormInstanceRequest,
    ) -> main_models.RenewLindormInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_lindorm_instance_with_options(request, runtime)

    async def renew_lindorm_instance_async(
        self,
        request: main_models.RenewLindormInstanceRequest,
    ) -> main_models.RenewLindormInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_lindorm_instance_with_options_async(request, runtime)

    def restart_ldps_compute_group_with_options(
        self,
        request: main_models.RestartLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartLdpsComputeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_ldps_compute_group_with_options_async(
        self,
        request: main_models.RestartLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartLdpsComputeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_ldps_compute_group(
        self,
        request: main_models.RestartLdpsComputeGroupRequest,
    ) -> main_models.RestartLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return self.restart_ldps_compute_group_with_options(request, runtime)

    async def restart_ldps_compute_group_async(
        self,
        request: main_models.RestartLdpsComputeGroupRequest,
    ) -> main_models.RestartLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return await self.restart_ldps_compute_group_with_options_async(request, runtime)

    def set_default_olap_compute_group_with_options(
        self,
        request: main_models.SetDefaultOlapComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultOlapComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultOlapComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultOlapComputeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_olap_compute_group_with_options_async(
        self,
        request: main_models.SetDefaultOlapComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultOlapComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultOlapComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultOlapComputeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_olap_compute_group(
        self,
        request: main_models.SetDefaultOlapComputeGroupRequest,
    ) -> main_models.SetDefaultOlapComputeGroupResponse:
        runtime = RuntimeOptions()
        return self.set_default_olap_compute_group_with_options(request, runtime)

    async def set_default_olap_compute_group_async(
        self,
        request: main_models.SetDefaultOlapComputeGroupRequest,
    ) -> main_models.SetDefaultOlapComputeGroupResponse:
        runtime = RuntimeOptions()
        return await self.set_default_olap_compute_group_with_options_async(request, runtime)

    def switch_lsqlv3my_sqlservice_with_options(
        self,
        request: main_models.SwitchLSQLV3MySQLServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchLSQLV3MySQLServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchLSQLV3MySQLService',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchLSQLV3MySQLServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_lsqlv3my_sqlservice_with_options_async(
        self,
        request: main_models.SwitchLSQLV3MySQLServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchLSQLV3MySQLServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchLSQLV3MySQLService',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchLSQLV3MySQLServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_lsqlv3my_sqlservice(
        self,
        request: main_models.SwitchLSQLV3MySQLServiceRequest,
    ) -> main_models.SwitchLSQLV3MySQLServiceResponse:
        runtime = RuntimeOptions()
        return self.switch_lsqlv3my_sqlservice_with_options(request, runtime)

    async def switch_lsqlv3my_sqlservice_async(
        self,
        request: main_models.SwitchLSQLV3MySQLServiceRequest,
    ) -> main_models.SwitchLSQLV3MySQLServiceResponse:
        runtime = RuntimeOptions()
        return await self.switch_lsqlv3my_sqlservice_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-06-15',
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
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-06-15',
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

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-06-15',
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
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-06-15',
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

    def update_instance_ip_white_list_with_options(
        self,
        request: main_models.UpdateInstanceIpWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceIpWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete):
            query['Delete'] = request.delete
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_ip_list):
            query['SecurityIpList'] = request.security_ip_list
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceIpWhiteList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_ip_white_list_with_options_async(
        self,
        request: main_models.UpdateInstanceIpWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceIpWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete):
            query['Delete'] = request.delete
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_ip_list):
            query['SecurityIpList'] = request.security_ip_list
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceIpWhiteList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_ip_white_list(
        self,
        request: main_models.UpdateInstanceIpWhiteListRequest,
    ) -> main_models.UpdateInstanceIpWhiteListResponse:
        runtime = RuntimeOptions()
        return self.update_instance_ip_white_list_with_options(request, runtime)

    async def update_instance_ip_white_list_async(
        self,
        request: main_models.UpdateInstanceIpWhiteListRequest,
    ) -> main_models.UpdateInstanceIpWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_ip_white_list_with_options_async(request, runtime)

    def update_instance_security_groups_with_options(
        self,
        request: main_models.UpdateInstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_groups):
            query['SecurityGroups'] = request.security_groups
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceSecurityGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_security_groups_with_options_async(
        self,
        request: main_models.UpdateInstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_groups):
            query['SecurityGroups'] = request.security_groups
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceSecurityGroups',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_security_groups(
        self,
        request: main_models.UpdateInstanceSecurityGroupsRequest,
    ) -> main_models.UpdateInstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return self.update_instance_security_groups_with_options(request, runtime)

    async def update_instance_security_groups_async(
        self,
        request: main_models.UpdateInstanceSecurityGroupsRequest,
    ) -> main_models.UpdateInstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_security_groups_with_options_async(request, runtime)

    def update_ldps_compute_group_with_options(
        self,
        request: main_models.UpdateLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLdpsComputeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ldps_compute_group_with_options_async(
        self,
        request: main_models.UpdateLdpsComputeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLdpsComputeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLdpsComputeGroup',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLdpsComputeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ldps_compute_group(
        self,
        request: main_models.UpdateLdpsComputeGroupRequest,
    ) -> main_models.UpdateLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return self.update_ldps_compute_group_with_options(request, runtime)

    async def update_ldps_compute_group_async(
        self,
        request: main_models.UpdateLdpsComputeGroupRequest,
    ) -> main_models.UpdateLdpsComputeGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_ldps_compute_group_with_options_async(request, runtime)

    def update_lindorm_instance_attribute_with_options(
        self,
        request: main_models.UpdateLindormInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLindormInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLindormInstanceAttribute',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLindormInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_lindorm_instance_attribute_with_options_async(
        self,
        request: main_models.UpdateLindormInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLindormInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLindormInstanceAttribute',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLindormInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_lindorm_instance_attribute(
        self,
        request: main_models.UpdateLindormInstanceAttributeRequest,
    ) -> main_models.UpdateLindormInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_lindorm_instance_attribute_with_options(request, runtime)

    async def update_lindorm_instance_attribute_async(
        self,
        request: main_models.UpdateLindormInstanceAttributeRequest,
    ) -> main_models.UpdateLindormInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_lindorm_instance_attribute_with_options_async(request, runtime)

    def update_lindorm_v2instance_with_options(
        self,
        request: main_models.UpdateLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity_storage_size):
            query['CapacityStorageSize'] = request.capacity_storage_size
        if not DaraCore.is_null(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not DaraCore.is_null(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not DaraCore.is_null(request.enable_capacity_storage):
            query['EnableCapacityStorage'] = request.enable_capacity_storage
        if not DaraCore.is_null(request.engine_list):
            query['EngineList'] = request.engine_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLindormV2InstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_lindorm_v2instance_with_options_async(
        self,
        request: main_models.UpdateLindormV2InstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLindormV2InstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity_storage_size):
            query['CapacityStorageSize'] = request.capacity_storage_size
        if not DaraCore.is_null(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not DaraCore.is_null(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not DaraCore.is_null(request.enable_capacity_storage):
            query['EnableCapacityStorage'] = request.enable_capacity_storage
        if not DaraCore.is_null(request.engine_list):
            query['EngineList'] = request.engine_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLindormV2Instance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLindormV2InstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_lindorm_v2instance(
        self,
        request: main_models.UpdateLindormV2InstanceRequest,
    ) -> main_models.UpdateLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return self.update_lindorm_v2instance_with_options(request, runtime)

    async def update_lindorm_v2instance_async(
        self,
        request: main_models.UpdateLindormV2InstanceRequest,
    ) -> main_models.UpdateLindormV2InstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_lindorm_v2instance_with_options_async(request, runtime)

    def update_lindorm_v2instance_parameter_with_options(
        self,
        request: main_models.UpdateLindormV2InstanceParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLindormV2InstanceParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameter_key):
            query['ParameterKey'] = request.parameter_key
        if not DaraCore.is_null(request.parameter_value):
            query['ParameterValue'] = request.parameter_value
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLindormV2InstanceParameter',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLindormV2InstanceParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_lindorm_v2instance_parameter_with_options_async(
        self,
        request: main_models.UpdateLindormV2InstanceParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLindormV2InstanceParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameter_key):
            query['ParameterKey'] = request.parameter_key
        if not DaraCore.is_null(request.parameter_value):
            query['ParameterValue'] = request.parameter_value
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLindormV2InstanceParameter',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLindormV2InstanceParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_lindorm_v2instance_parameter(
        self,
        request: main_models.UpdateLindormV2InstanceParameterRequest,
    ) -> main_models.UpdateLindormV2InstanceParameterResponse:
        runtime = RuntimeOptions()
        return self.update_lindorm_v2instance_parameter_with_options(request, runtime)

    async def update_lindorm_v2instance_parameter_async(
        self,
        request: main_models.UpdateLindormV2InstanceParameterRequest,
    ) -> main_models.UpdateLindormV2InstanceParameterResponse:
        runtime = RuntimeOptions()
        return await self.update_lindorm_v2instance_parameter_with_options_async(request, runtime)

    def update_lindorm_v2white_ip_list_with_options(
        self,
        request: main_models.UpdateLindormV2WhiteIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLindormV2WhiteIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.white_ip_group_list):
            query['WhiteIpGroupList'] = request.white_ip_group_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLindormV2WhiteIpList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLindormV2WhiteIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_lindorm_v2white_ip_list_with_options_async(
        self,
        request: main_models.UpdateLindormV2WhiteIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLindormV2WhiteIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.white_ip_group_list):
            query['WhiteIpGroupList'] = request.white_ip_group_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLindormV2WhiteIpList',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLindormV2WhiteIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_lindorm_v2white_ip_list(
        self,
        request: main_models.UpdateLindormV2WhiteIpListRequest,
    ) -> main_models.UpdateLindormV2WhiteIpListResponse:
        runtime = RuntimeOptions()
        return self.update_lindorm_v2white_ip_list_with_options(request, runtime)

    async def update_lindorm_v2white_ip_list_async(
        self,
        request: main_models.UpdateLindormV2WhiteIpListRequest,
    ) -> main_models.UpdateLindormV2WhiteIpListResponse:
        runtime = RuntimeOptions()
        return await self.update_lindorm_v2white_ip_list_with_options_async(request, runtime)

    def upgrade_lindorm_instance_with_options(
        self,
        request: main_models.UpgradeLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_storage):
            query['ClusterStorage'] = request.cluster_storage
        if not DaraCore.is_null(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not DaraCore.is_null(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not DaraCore.is_null(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not DaraCore.is_null(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not DaraCore.is_null(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not DaraCore.is_null(request.log_num):
            query['LogNum'] = request.log_num
        if not DaraCore.is_null(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not DaraCore.is_null(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not DaraCore.is_null(request.lts_core_num):
            query['LtsCoreNum'] = request.lts_core_num
        if not DaraCore.is_null(request.lts_core_spec):
            query['LtsCoreSpec'] = request.lts_core_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not DaraCore.is_null(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not DaraCore.is_null(request.stream_num):
            query['StreamNum'] = request.stream_num
        if not DaraCore.is_null(request.stream_spec):
            query['StreamSpec'] = request.stream_spec
        if not DaraCore.is_null(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not DaraCore.is_null(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_lindorm_instance_with_options_async(
        self,
        request: main_models.UpgradeLindormInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeLindormInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_storage):
            query['ClusterStorage'] = request.cluster_storage
        if not DaraCore.is_null(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not DaraCore.is_null(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not DaraCore.is_null(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not DaraCore.is_null(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not DaraCore.is_null(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not DaraCore.is_null(request.log_num):
            query['LogNum'] = request.log_num
        if not DaraCore.is_null(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not DaraCore.is_null(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not DaraCore.is_null(request.lts_core_num):
            query['LtsCoreNum'] = request.lts_core_num
        if not DaraCore.is_null(request.lts_core_spec):
            query['LtsCoreSpec'] = request.lts_core_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not DaraCore.is_null(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not DaraCore.is_null(request.stream_num):
            query['StreamNum'] = request.stream_num
        if not DaraCore.is_null(request.stream_spec):
            query['StreamSpec'] = request.stream_spec
        if not DaraCore.is_null(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not DaraCore.is_null(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeLindormInstance',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_lindorm_instance(
        self,
        request: main_models.UpgradeLindormInstanceRequest,
    ) -> main_models.UpgradeLindormInstanceResponse:
        runtime = RuntimeOptions()
        return self.upgrade_lindorm_instance_with_options(request, runtime)

    async def upgrade_lindorm_instance_async(
        self,
        request: main_models.UpgradeLindormInstanceRequest,
    ) -> main_models.UpgradeLindormInstanceResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_lindorm_instance_with_options_async(request, runtime)

    def upgrade_lindorm_v2stream_engine_with_options(
        self,
        request: main_models.UpgradeLindormV2StreamEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeLindormV2StreamEngineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_config):
            query['CustomConfig'] = request.custom_config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeLindormV2StreamEngine',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeLindormV2StreamEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_lindorm_v2stream_engine_with_options_async(
        self,
        request: main_models.UpgradeLindormV2StreamEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeLindormV2StreamEngineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_config):
            query['CustomConfig'] = request.custom_config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeLindormV2StreamEngine',
            version = '2020-06-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeLindormV2StreamEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_lindorm_v2stream_engine(
        self,
        request: main_models.UpgradeLindormV2StreamEngineRequest,
    ) -> main_models.UpgradeLindormV2StreamEngineResponse:
        runtime = RuntimeOptions()
        return self.upgrade_lindorm_v2stream_engine_with_options(request, runtime)

    async def upgrade_lindorm_v2stream_engine_async(
        self,
        request: main_models.UpgradeLindormV2StreamEngineRequest,
    ) -> main_models.UpgradeLindormV2StreamEngineResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_lindorm_v2stream_engine_with_options_async(request, runtime)
