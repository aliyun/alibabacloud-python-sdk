# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hitsdb20200615 import models as hitsdb_20200615_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_resource_group_with_options(
        self,
        request: hitsdb_20200615_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ChangeResourceGroupResponse:
        """
        @summary Changes a resource group to another.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ChangeResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ChangeResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def change_resource_group_with_options_async(
        self,
        request: hitsdb_20200615_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ChangeResourceGroupResponse:
        """
        @summary Changes a resource group to another.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ChangeResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ChangeResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def change_resource_group(
        self,
        request: hitsdb_20200615_models.ChangeResourceGroupRequest,
    ) -> hitsdb_20200615_models.ChangeResourceGroupResponse:
        """
        @summary Changes a resource group to another.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: hitsdb_20200615_models.ChangeResourceGroupRequest,
    ) -> hitsdb_20200615_models.ChangeResourceGroupResponse:
        """
        @summary Changes a resource group to another.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_ldps_columnar_index_status_with_options(
        self,
        request: hitsdb_20200615_models.CheckLdpsColumnarIndexStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CheckLdpsColumnarIndexStatusResponse:
        """
        @param request: CheckLdpsColumnarIndexStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckLdpsColumnarIndexStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLdpsColumnarIndexStatus',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CheckLdpsColumnarIndexStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CheckLdpsColumnarIndexStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def check_ldps_columnar_index_status_with_options_async(
        self,
        request: hitsdb_20200615_models.CheckLdpsColumnarIndexStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CheckLdpsColumnarIndexStatusResponse:
        """
        @param request: CheckLdpsColumnarIndexStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckLdpsColumnarIndexStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLdpsColumnarIndexStatus',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CheckLdpsColumnarIndexStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CheckLdpsColumnarIndexStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def check_ldps_columnar_index_status(
        self,
        request: hitsdb_20200615_models.CheckLdpsColumnarIndexStatusRequest,
    ) -> hitsdb_20200615_models.CheckLdpsColumnarIndexStatusResponse:
        """
        @param request: CheckLdpsColumnarIndexStatusRequest
        @return: CheckLdpsColumnarIndexStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_ldps_columnar_index_status_with_options(request, runtime)

    async def check_ldps_columnar_index_status_async(
        self,
        request: hitsdb_20200615_models.CheckLdpsColumnarIndexStatusRequest,
    ) -> hitsdb_20200615_models.CheckLdpsColumnarIndexStatusResponse:
        """
        @param request: CheckLdpsColumnarIndexStatusRequest
        @return: CheckLdpsColumnarIndexStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_ldps_columnar_index_status_with_options_async(request, runtime)

    def create_auto_scaling_config_with_options(
        self,
        tmp_req: hitsdb_20200615_models.CreateAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateAutoScalingConfigResponse:
        """
        @param tmp_req: CreateAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoScalingConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hitsdb_20200615_models.CreateAutoScalingConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scale_rule_list):
            request.scale_rule_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scale_rule_list, 'ScaleRuleList', 'json')
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.effective_time_end):
            query['EffectiveTimeEnd'] = request.effective_time_end
        if not UtilClient.is_unset(request.effective_time_start):
            query['EffectiveTimeStart'] = request.effective_time_start
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nodes_max):
            query['NodesMax'] = request.nodes_max
        if not UtilClient.is_unset(request.nodes_min):
            query['NodesMin'] = request.nodes_min
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_rule_list_shrink):
            query['ScaleRuleList'] = request.scale_rule_list_shrink
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoScalingConfig',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateAutoScalingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateAutoScalingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def create_auto_scaling_config_with_options_async(
        self,
        tmp_req: hitsdb_20200615_models.CreateAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateAutoScalingConfigResponse:
        """
        @param tmp_req: CreateAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoScalingConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hitsdb_20200615_models.CreateAutoScalingConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scale_rule_list):
            request.scale_rule_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scale_rule_list, 'ScaleRuleList', 'json')
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.effective_time_end):
            query['EffectiveTimeEnd'] = request.effective_time_end
        if not UtilClient.is_unset(request.effective_time_start):
            query['EffectiveTimeStart'] = request.effective_time_start
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nodes_max):
            query['NodesMax'] = request.nodes_max
        if not UtilClient.is_unset(request.nodes_min):
            query['NodesMin'] = request.nodes_min
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_rule_list_shrink):
            query['ScaleRuleList'] = request.scale_rule_list_shrink
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoScalingConfig',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateAutoScalingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateAutoScalingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_auto_scaling_config(
        self,
        request: hitsdb_20200615_models.CreateAutoScalingConfigRequest,
    ) -> hitsdb_20200615_models.CreateAutoScalingConfigResponse:
        """
        @param request: CreateAutoScalingConfigRequest
        @return: CreateAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_auto_scaling_config_with_options(request, runtime)

    async def create_auto_scaling_config_async(
        self,
        request: hitsdb_20200615_models.CreateAutoScalingConfigRequest,
    ) -> hitsdb_20200615_models.CreateAutoScalingConfigResponse:
        """
        @param request: CreateAutoScalingConfigRequest
        @return: CreateAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_scaling_config_with_options_async(request, runtime)

    def create_auto_scaling_rule_with_options(
        self,
        request: hitsdb_20200615_models.CreateAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateAutoScalingRuleResponse:
        """
        @param request: CreateAutoScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.observation_window):
            query['ObservationWindow'] = request.observation_window
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scale_in_step):
            query['ScaleInStep'] = request.scale_in_step
        if not UtilClient.is_unset(request.scale_out_step):
            query['ScaleOutStep'] = request.scale_out_step
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_metric):
            query['TargetMetric'] = request.target_metric
        if not UtilClient.is_unset(request.target_nodes):
            query['TargetNodes'] = request.target_nodes
        if not UtilClient.is_unset(request.threshold_lower):
            query['ThresholdLower'] = request.threshold_lower
        if not UtilClient.is_unset(request.threshold_upper):
            query['ThresholdUpper'] = request.threshold_upper
        if not UtilClient.is_unset(request.trigger_cron_expr):
            query['TriggerCronExpr'] = request.trigger_cron_expr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoScalingRule',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateAutoScalingRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateAutoScalingRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_auto_scaling_rule_with_options_async(
        self,
        request: hitsdb_20200615_models.CreateAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateAutoScalingRuleResponse:
        """
        @param request: CreateAutoScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.observation_window):
            query['ObservationWindow'] = request.observation_window
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scale_in_step):
            query['ScaleInStep'] = request.scale_in_step
        if not UtilClient.is_unset(request.scale_out_step):
            query['ScaleOutStep'] = request.scale_out_step
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_metric):
            query['TargetMetric'] = request.target_metric
        if not UtilClient.is_unset(request.target_nodes):
            query['TargetNodes'] = request.target_nodes
        if not UtilClient.is_unset(request.threshold_lower):
            query['ThresholdLower'] = request.threshold_lower
        if not UtilClient.is_unset(request.threshold_upper):
            query['ThresholdUpper'] = request.threshold_upper
        if not UtilClient.is_unset(request.trigger_cron_expr):
            query['TriggerCronExpr'] = request.trigger_cron_expr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoScalingRule',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateAutoScalingRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateAutoScalingRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_auto_scaling_rule(
        self,
        request: hitsdb_20200615_models.CreateAutoScalingRuleRequest,
    ) -> hitsdb_20200615_models.CreateAutoScalingRuleResponse:
        """
        @param request: CreateAutoScalingRuleRequest
        @return: CreateAutoScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_auto_scaling_rule_with_options(request, runtime)

    async def create_auto_scaling_rule_async(
        self,
        request: hitsdb_20200615_models.CreateAutoScalingRuleRequest,
    ) -> hitsdb_20200615_models.CreateAutoScalingRuleResponse:
        """
        @param request: CreateAutoScalingRuleRequest
        @return: CreateAutoScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_scaling_rule_with_options_async(request, runtime)

    def create_ldps_compute_group_with_options(
        self,
        request: hitsdb_20200615_models.CreateLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateLdpsComputeGroupResponse:
        """
        @param request: CreateLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLdpsComputeGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLdpsComputeGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def create_ldps_compute_group_with_options_async(
        self,
        request: hitsdb_20200615_models.CreateLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateLdpsComputeGroupResponse:
        """
        @param request: CreateLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLdpsComputeGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLdpsComputeGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_ldps_compute_group(
        self,
        request: hitsdb_20200615_models.CreateLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.CreateLdpsComputeGroupResponse:
        """
        @param request: CreateLdpsComputeGroupRequest
        @return: CreateLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ldps_compute_group_with_options(request, runtime)

    async def create_ldps_compute_group_async(
        self,
        request: hitsdb_20200615_models.CreateLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.CreateLdpsComputeGroupResponse:
        """
        @param request: CreateLdpsComputeGroupRequest
        @return: CreateLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ldps_compute_group_with_options_async(request, runtime)

    def create_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.CreateLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateLindormInstanceResponse:
        """
        @summary Creates a Lindorm instance.
        
        @description You must select at least one engine when you create a Lindorm instance. For more information about how to select the storage type and engine type when you create a Lindorm instance, see [Select engine types](https://help.aliyun.com/document_detail/181971.html) and [Select storage types](https://help.aliyun.com/document_detail/174643.html).
        
        @param request: CreateLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not UtilClient.is_unset(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not UtilClient.is_unset(request.core_spec):
            query['CoreSpec'] = request.core_spec
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not UtilClient.is_unset(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
        if not UtilClient.is_unset(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not UtilClient.is_unset(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not UtilClient.is_unset(request.log_disk_category):
            query['LogDiskCategory'] = request.log_disk_category
        if not UtilClient.is_unset(request.log_num):
            query['LogNum'] = request.log_num
        if not UtilClient.is_unset(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not UtilClient.is_unset(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not UtilClient.is_unset(request.lts_num):
            query['LtsNum'] = request.lts_num
        if not UtilClient.is_unset(request.lts_spec):
            query['LtsSpec'] = request.lts_spec
        if not UtilClient.is_unset(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not UtilClient.is_unset(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.stream_num):
            query['StreamNum'] = request.stream_num
        if not UtilClient.is_unset(request.stream_spec):
            query['StreamSpec'] = request.stream_spec
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not UtilClient.is_unset(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLindormInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLindormInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.CreateLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateLindormInstanceResponse:
        """
        @summary Creates a Lindorm instance.
        
        @description You must select at least one engine when you create a Lindorm instance. For more information about how to select the storage type and engine type when you create a Lindorm instance, see [Select engine types](https://help.aliyun.com/document_detail/181971.html) and [Select storage types](https://help.aliyun.com/document_detail/174643.html).
        
        @param request: CreateLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not UtilClient.is_unset(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not UtilClient.is_unset(request.core_spec):
            query['CoreSpec'] = request.core_spec
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not UtilClient.is_unset(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
        if not UtilClient.is_unset(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not UtilClient.is_unset(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not UtilClient.is_unset(request.log_disk_category):
            query['LogDiskCategory'] = request.log_disk_category
        if not UtilClient.is_unset(request.log_num):
            query['LogNum'] = request.log_num
        if not UtilClient.is_unset(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not UtilClient.is_unset(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not UtilClient.is_unset(request.lts_num):
            query['LtsNum'] = request.lts_num
        if not UtilClient.is_unset(request.lts_spec):
            query['LtsSpec'] = request.lts_spec
        if not UtilClient.is_unset(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not UtilClient.is_unset(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.stream_num):
            query['StreamNum'] = request.stream_num
        if not UtilClient.is_unset(request.stream_spec):
            query['StreamSpec'] = request.stream_spec
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not UtilClient.is_unset(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLindormInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLindormInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_lindorm_instance(
        self,
        request: hitsdb_20200615_models.CreateLindormInstanceRequest,
    ) -> hitsdb_20200615_models.CreateLindormInstanceResponse:
        """
        @summary Creates a Lindorm instance.
        
        @description You must select at least one engine when you create a Lindorm instance. For more information about how to select the storage type and engine type when you create a Lindorm instance, see [Select engine types](https://help.aliyun.com/document_detail/181971.html) and [Select storage types](https://help.aliyun.com/document_detail/174643.html).
        
        @param request: CreateLindormInstanceRequest
        @return: CreateLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lindorm_instance_with_options(request, runtime)

    async def create_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.CreateLindormInstanceRequest,
    ) -> hitsdb_20200615_models.CreateLindormInstanceResponse:
        """
        @summary Creates a Lindorm instance.
        
        @description You must select at least one engine when you create a Lindorm instance. For more information about how to select the storage type and engine type when you create a Lindorm instance, see [Select engine types](https://help.aliyun.com/document_detail/181971.html) and [Select storage types](https://help.aliyun.com/document_detail/174643.html).
        
        @param request: CreateLindormInstanceRequest
        @return: CreateLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lindorm_instance_with_options_async(request, runtime)

    def create_lindorm_v2instance_with_options(
        self,
        request: hitsdb_20200615_models.CreateLindormV2InstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateLindormV2InstanceResponse:
        """
        @param request: CreateLindormV2InstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLindormV2InstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.capacity_storage_size):
            query['CapacityStorageSize'] = request.capacity_storage_size
        if not UtilClient.is_unset(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not UtilClient.is_unset(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_pattern):
            query['ClusterPattern'] = request.cluster_pattern
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.enable_capacity_storage):
            query['EnableCapacityStorage'] = request.enable_capacity_storage
        if not UtilClient.is_unset(request.engine_list):
            query['EngineList'] = request.engine_list
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLindormV2Instance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLindormV2InstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLindormV2InstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_lindorm_v2instance_with_options_async(
        self,
        request: hitsdb_20200615_models.CreateLindormV2InstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateLindormV2InstanceResponse:
        """
        @param request: CreateLindormV2InstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLindormV2InstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.capacity_storage_size):
            query['CapacityStorageSize'] = request.capacity_storage_size
        if not UtilClient.is_unset(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not UtilClient.is_unset(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_pattern):
            query['ClusterPattern'] = request.cluster_pattern
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.enable_capacity_storage):
            query['EnableCapacityStorage'] = request.enable_capacity_storage
        if not UtilClient.is_unset(request.engine_list):
            query['EngineList'] = request.engine_list
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLindormV2Instance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLindormV2InstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.CreateLindormV2InstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_lindorm_v2instance(
        self,
        request: hitsdb_20200615_models.CreateLindormV2InstanceRequest,
    ) -> hitsdb_20200615_models.CreateLindormV2InstanceResponse:
        """
        @param request: CreateLindormV2InstanceRequest
        @return: CreateLindormV2InstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lindorm_v2instance_with_options(request, runtime)

    async def create_lindorm_v2instance_async(
        self,
        request: hitsdb_20200615_models.CreateLindormV2InstanceRequest,
    ) -> hitsdb_20200615_models.CreateLindormV2InstanceResponse:
        """
        @param request: CreateLindormV2InstanceRequest
        @return: CreateLindormV2InstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lindorm_v2instance_with_options_async(request, runtime)

    def delete_auto_scaling_config_with_options(
        self,
        request: hitsdb_20200615_models.DeleteAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeleteAutoScalingConfigResponse:
        """
        @param request: DeleteAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoScalingConfig',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteAutoScalingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteAutoScalingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_auto_scaling_config_with_options_async(
        self,
        request: hitsdb_20200615_models.DeleteAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeleteAutoScalingConfigResponse:
        """
        @param request: DeleteAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoScalingConfig',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteAutoScalingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteAutoScalingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_auto_scaling_config(
        self,
        request: hitsdb_20200615_models.DeleteAutoScalingConfigRequest,
    ) -> hitsdb_20200615_models.DeleteAutoScalingConfigResponse:
        """
        @param request: DeleteAutoScalingConfigRequest
        @return: DeleteAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_scaling_config_with_options(request, runtime)

    async def delete_auto_scaling_config_async(
        self,
        request: hitsdb_20200615_models.DeleteAutoScalingConfigRequest,
    ) -> hitsdb_20200615_models.DeleteAutoScalingConfigResponse:
        """
        @param request: DeleteAutoScalingConfigRequest
        @return: DeleteAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_scaling_config_with_options_async(request, runtime)

    def delete_auto_scaling_rule_with_options(
        self,
        request: hitsdb_20200615_models.DeleteAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeleteAutoScalingRuleResponse:
        """
        @param request: DeleteAutoScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoScalingRule',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteAutoScalingRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteAutoScalingRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_auto_scaling_rule_with_options_async(
        self,
        request: hitsdb_20200615_models.DeleteAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeleteAutoScalingRuleResponse:
        """
        @param request: DeleteAutoScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoScalingRule',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteAutoScalingRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteAutoScalingRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_auto_scaling_rule(
        self,
        request: hitsdb_20200615_models.DeleteAutoScalingRuleRequest,
    ) -> hitsdb_20200615_models.DeleteAutoScalingRuleResponse:
        """
        @param request: DeleteAutoScalingRuleRequest
        @return: DeleteAutoScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_scaling_rule_with_options(request, runtime)

    async def delete_auto_scaling_rule_async(
        self,
        request: hitsdb_20200615_models.DeleteAutoScalingRuleRequest,
    ) -> hitsdb_20200615_models.DeleteAutoScalingRuleResponse:
        """
        @param request: DeleteAutoScalingRuleRequest
        @return: DeleteAutoScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_scaling_rule_with_options_async(request, runtime)

    def delete_custom_resource_with_options(
        self,
        request: hitsdb_20200615_models.DeleteCustomResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeleteCustomResourceResponse:
        """
        @param request: DeleteCustomResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomResource',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteCustomResourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteCustomResourceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_custom_resource_with_options_async(
        self,
        request: hitsdb_20200615_models.DeleteCustomResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeleteCustomResourceResponse:
        """
        @param request: DeleteCustomResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomResource',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteCustomResourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteCustomResourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_custom_resource(
        self,
        request: hitsdb_20200615_models.DeleteCustomResourceRequest,
    ) -> hitsdb_20200615_models.DeleteCustomResourceResponse:
        """
        @param request: DeleteCustomResourceRequest
        @return: DeleteCustomResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_resource_with_options(request, runtime)

    async def delete_custom_resource_async(
        self,
        request: hitsdb_20200615_models.DeleteCustomResourceRequest,
    ) -> hitsdb_20200615_models.DeleteCustomResourceResponse:
        """
        @param request: DeleteCustomResourceRequest
        @return: DeleteCustomResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_resource_with_options_async(request, runtime)

    def delete_ldps_compute_group_with_options(
        self,
        request: hitsdb_20200615_models.DeleteLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeleteLdpsComputeGroupResponse:
        """
        @param request: DeleteLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteLdpsComputeGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteLdpsComputeGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_ldps_compute_group_with_options_async(
        self,
        request: hitsdb_20200615_models.DeleteLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeleteLdpsComputeGroupResponse:
        """
        @param request: DeleteLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteLdpsComputeGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeleteLdpsComputeGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_ldps_compute_group(
        self,
        request: hitsdb_20200615_models.DeleteLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.DeleteLdpsComputeGroupResponse:
        """
        @param request: DeleteLdpsComputeGroupRequest
        @return: DeleteLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ldps_compute_group_with_options(request, runtime)

    async def delete_ldps_compute_group_async(
        self,
        request: hitsdb_20200615_models.DeleteLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.DeleteLdpsComputeGroupResponse:
        """
        @param request: DeleteLdpsComputeGroupRequest
        @return: DeleteLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ldps_compute_group_with_options_async(request, runtime)

    def deploy_ldps_semi_managed_component_with_options(
        self,
        request: hitsdb_20200615_models.DeployLdpsSemiManagedComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeployLdpsSemiManagedComponentResponse:
        """
        @param request: DeployLdpsSemiManagedComponentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployLdpsSemiManagedComponentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployLdpsSemiManagedComponent',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeployLdpsSemiManagedComponentResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeployLdpsSemiManagedComponentResponse(),
                self.execute(params, req, runtime)
            )

    async def deploy_ldps_semi_managed_component_with_options_async(
        self,
        request: hitsdb_20200615_models.DeployLdpsSemiManagedComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DeployLdpsSemiManagedComponentResponse:
        """
        @param request: DeployLdpsSemiManagedComponentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployLdpsSemiManagedComponentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployLdpsSemiManagedComponent',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DeployLdpsSemiManagedComponentResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DeployLdpsSemiManagedComponentResponse(),
                await self.execute_async(params, req, runtime)
            )

    def deploy_ldps_semi_managed_component(
        self,
        request: hitsdb_20200615_models.DeployLdpsSemiManagedComponentRequest,
    ) -> hitsdb_20200615_models.DeployLdpsSemiManagedComponentResponse:
        """
        @param request: DeployLdpsSemiManagedComponentRequest
        @return: DeployLdpsSemiManagedComponentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_ldps_semi_managed_component_with_options(request, runtime)

    async def deploy_ldps_semi_managed_component_async(
        self,
        request: hitsdb_20200615_models.DeployLdpsSemiManagedComponentRequest,
    ) -> hitsdb_20200615_models.DeployLdpsSemiManagedComponentResponse:
        """
        @param request: DeployLdpsSemiManagedComponentRequest
        @return: DeployLdpsSemiManagedComponentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deploy_ldps_semi_managed_component_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        """
        @summary Obtains the regions supported by Lindorm.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DescribeRegionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DescribeRegionsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_regions_with_options_async(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        """
        @summary Obtains the regions supported by Lindorm.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.DescribeRegionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.DescribeRegionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_regions(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        """
        @summary Obtains the regions supported by Lindorm.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        """
        @summary Obtains the regions supported by Lindorm.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def get_auto_scaling_config_with_options(
        self,
        request: hitsdb_20200615_models.GetAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetAutoScalingConfigResponse:
        """
        @param request: GetAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScalingConfig',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetAutoScalingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetAutoScalingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def get_auto_scaling_config_with_options_async(
        self,
        request: hitsdb_20200615_models.GetAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetAutoScalingConfigResponse:
        """
        @param request: GetAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScalingConfig',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetAutoScalingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetAutoScalingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_auto_scaling_config(
        self,
        request: hitsdb_20200615_models.GetAutoScalingConfigRequest,
    ) -> hitsdb_20200615_models.GetAutoScalingConfigResponse:
        """
        @param request: GetAutoScalingConfigRequest
        @return: GetAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_config_with_options(request, runtime)

    async def get_auto_scaling_config_async(
        self,
        request: hitsdb_20200615_models.GetAutoScalingConfigRequest,
    ) -> hitsdb_20200615_models.GetAutoScalingConfigResponse:
        """
        @param request: GetAutoScalingConfigRequest
        @return: GetAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scaling_config_with_options_async(request, runtime)

    def get_auto_scaling_rule_with_options(
        self,
        request: hitsdb_20200615_models.GetAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetAutoScalingRuleResponse:
        """
        @param request: GetAutoScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScalingRule',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetAutoScalingRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetAutoScalingRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def get_auto_scaling_rule_with_options_async(
        self,
        request: hitsdb_20200615_models.GetAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetAutoScalingRuleResponse:
        """
        @param request: GetAutoScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScalingRule',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetAutoScalingRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetAutoScalingRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_auto_scaling_rule(
        self,
        request: hitsdb_20200615_models.GetAutoScalingRuleRequest,
    ) -> hitsdb_20200615_models.GetAutoScalingRuleResponse:
        """
        @param request: GetAutoScalingRuleRequest
        @return: GetAutoScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_rule_with_options(request, runtime)

    async def get_auto_scaling_rule_async(
        self,
        request: hitsdb_20200615_models.GetAutoScalingRuleRequest,
    ) -> hitsdb_20200615_models.GetAutoScalingRuleResponse:
        """
        @param request: GetAutoScalingRuleRequest
        @return: GetAutoScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scaling_rule_with_options_async(request, runtime)

    def get_client_source_ip_with_options(
        self,
        request: hitsdb_20200615_models.GetClientSourceIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetClientSourceIpResponse:
        """
        @param request: GetClientSourceIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClientSourceIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClientSourceIp',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetClientSourceIpResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetClientSourceIpResponse(),
                self.execute(params, req, runtime)
            )

    async def get_client_source_ip_with_options_async(
        self,
        request: hitsdb_20200615_models.GetClientSourceIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetClientSourceIpResponse:
        """
        @param request: GetClientSourceIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClientSourceIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClientSourceIp',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetClientSourceIpResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetClientSourceIpResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_client_source_ip(
        self,
        request: hitsdb_20200615_models.GetClientSourceIpRequest,
    ) -> hitsdb_20200615_models.GetClientSourceIpResponse:
        """
        @param request: GetClientSourceIpRequest
        @return: GetClientSourceIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_client_source_ip_with_options(request, runtime)

    async def get_client_source_ip_async(
        self,
        request: hitsdb_20200615_models.GetClientSourceIpRequest,
    ) -> hitsdb_20200615_models.GetClientSourceIpResponse:
        """
        @param request: GetClientSourceIpRequest
        @return: GetClientSourceIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_client_source_ip_with_options_async(request, runtime)

    def get_engine_default_auth_with_options(
        self,
        request: hitsdb_20200615_models.GetEngineDefaultAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetEngineDefaultAuthResponse:
        """
        @param request: GetEngineDefaultAuthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEngineDefaultAuthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEngineDefaultAuth',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetEngineDefaultAuthResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetEngineDefaultAuthResponse(),
                self.execute(params, req, runtime)
            )

    async def get_engine_default_auth_with_options_async(
        self,
        request: hitsdb_20200615_models.GetEngineDefaultAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetEngineDefaultAuthResponse:
        """
        @param request: GetEngineDefaultAuthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEngineDefaultAuthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEngineDefaultAuth',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetEngineDefaultAuthResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetEngineDefaultAuthResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_engine_default_auth(
        self,
        request: hitsdb_20200615_models.GetEngineDefaultAuthRequest,
    ) -> hitsdb_20200615_models.GetEngineDefaultAuthResponse:
        """
        @param request: GetEngineDefaultAuthRequest
        @return: GetEngineDefaultAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_engine_default_auth_with_options(request, runtime)

    async def get_engine_default_auth_async(
        self,
        request: hitsdb_20200615_models.GetEngineDefaultAuthRequest,
    ) -> hitsdb_20200615_models.GetEngineDefaultAuthResponse:
        """
        @param request: GetEngineDefaultAuthRequest
        @return: GetEngineDefaultAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_engine_default_auth_with_options_async(request, runtime)

    def get_instance_ip_white_list_with_options(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        """
        @summary Queries the whitelists configured for a Lindorm instance.
        
        @param request: GetInstanceIpWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceIpWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceIpWhiteList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetInstanceIpWhiteListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetInstanceIpWhiteListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_instance_ip_white_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        """
        @summary Queries the whitelists configured for a Lindorm instance.
        
        @param request: GetInstanceIpWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceIpWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceIpWhiteList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetInstanceIpWhiteListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetInstanceIpWhiteListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_instance_ip_white_list(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        """
        @summary Queries the whitelists configured for a Lindorm instance.
        
        @param request: GetInstanceIpWhiteListRequest
        @return: GetInstanceIpWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_ip_white_list_with_options(request, runtime)

    async def get_instance_ip_white_list_async(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        """
        @summary Queries the whitelists configured for a Lindorm instance.
        
        @param request: GetInstanceIpWhiteListRequest
        @return: GetInstanceIpWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_ip_white_list_with_options_async(request, runtime)

    def get_instance_security_groups_with_options(
        self,
        request: hitsdb_20200615_models.GetInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetInstanceSecurityGroupsResponse:
        """
        @param request: GetInstanceSecurityGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceSecurityGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceSecurityGroups',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetInstanceSecurityGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetInstanceSecurityGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_instance_security_groups_with_options_async(
        self,
        request: hitsdb_20200615_models.GetInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetInstanceSecurityGroupsResponse:
        """
        @param request: GetInstanceSecurityGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceSecurityGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceSecurityGroups',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetInstanceSecurityGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetInstanceSecurityGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_instance_security_groups(
        self,
        request: hitsdb_20200615_models.GetInstanceSecurityGroupsRequest,
    ) -> hitsdb_20200615_models.GetInstanceSecurityGroupsResponse:
        """
        @param request: GetInstanceSecurityGroupsRequest
        @return: GetInstanceSecurityGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_security_groups_with_options(request, runtime)

    async def get_instance_security_groups_async(
        self,
        request: hitsdb_20200615_models.GetInstanceSecurityGroupsRequest,
    ) -> hitsdb_20200615_models.GetInstanceSecurityGroupsResponse:
        """
        @param request: GetInstanceSecurityGroupsRequest
        @return: GetInstanceSecurityGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_security_groups_with_options_async(request, runtime)

    def get_ldps_compute_group_with_options(
        self,
        request: hitsdb_20200615_models.GetLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLdpsComputeGroupResponse:
        """
        @param request: GetLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsComputeGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsComputeGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def get_ldps_compute_group_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLdpsComputeGroupResponse:
        """
        @param request: GetLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsComputeGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsComputeGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_ldps_compute_group(
        self,
        request: hitsdb_20200615_models.GetLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.GetLdpsComputeGroupResponse:
        """
        @param request: GetLdpsComputeGroupRequest
        @return: GetLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ldps_compute_group_with_options(request, runtime)

    async def get_ldps_compute_group_async(
        self,
        request: hitsdb_20200615_models.GetLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.GetLdpsComputeGroupResponse:
        """
        @param request: GetLdpsComputeGroupRequest
        @return: GetLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ldps_compute_group_with_options_async(request, runtime)

    def get_ldps_namespaced_quota_with_options(
        self,
        request: hitsdb_20200615_models.GetLdpsNamespacedQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLdpsNamespacedQuotaResponse:
        """
        @param request: GetLdpsNamespacedQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLdpsNamespacedQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLdpsNamespacedQuota',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsNamespacedQuotaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsNamespacedQuotaResponse(),
                self.execute(params, req, runtime)
            )

    async def get_ldps_namespaced_quota_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLdpsNamespacedQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLdpsNamespacedQuotaResponse:
        """
        @param request: GetLdpsNamespacedQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLdpsNamespacedQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLdpsNamespacedQuota',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsNamespacedQuotaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsNamespacedQuotaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_ldps_namespaced_quota(
        self,
        request: hitsdb_20200615_models.GetLdpsNamespacedQuotaRequest,
    ) -> hitsdb_20200615_models.GetLdpsNamespacedQuotaResponse:
        """
        @param request: GetLdpsNamespacedQuotaRequest
        @return: GetLdpsNamespacedQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ldps_namespaced_quota_with_options(request, runtime)

    async def get_ldps_namespaced_quota_async(
        self,
        request: hitsdb_20200615_models.GetLdpsNamespacedQuotaRequest,
    ) -> hitsdb_20200615_models.GetLdpsNamespacedQuotaResponse:
        """
        @param request: GetLdpsNamespacedQuotaRequest
        @return: GetLdpsNamespacedQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ldps_namespaced_quota_with_options_async(request, runtime)

    def get_ldps_resource_cost_with_options(
        self,
        request: hitsdb_20200615_models.GetLdpsResourceCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLdpsResourceCostResponse:
        """
        @param request: GetLdpsResourceCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLdpsResourceCostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLdpsResourceCost',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsResourceCostResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsResourceCostResponse(),
                self.execute(params, req, runtime)
            )

    async def get_ldps_resource_cost_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLdpsResourceCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLdpsResourceCostResponse:
        """
        @param request: GetLdpsResourceCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLdpsResourceCostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLdpsResourceCost',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsResourceCostResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLdpsResourceCostResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_ldps_resource_cost(
        self,
        request: hitsdb_20200615_models.GetLdpsResourceCostRequest,
    ) -> hitsdb_20200615_models.GetLdpsResourceCostResponse:
        """
        @param request: GetLdpsResourceCostRequest
        @return: GetLdpsResourceCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ldps_resource_cost_with_options(request, runtime)

    async def get_ldps_resource_cost_async(
        self,
        request: hitsdb_20200615_models.GetLdpsResourceCostRequest,
    ) -> hitsdb_20200615_models.GetLdpsResourceCostResponse:
        """
        @param request: GetLdpsResourceCostRequest
        @return: GetLdpsResourceCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ldps_resource_cost_with_options_async(request, runtime)

    def get_lindorm_fs_used_detail_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormFsUsedDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormFsUsedDetailResponse:
        """
        @param request: GetLindormFsUsedDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormFsUsedDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormFsUsedDetail',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormFsUsedDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormFsUsedDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def get_lindorm_fs_used_detail_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormFsUsedDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormFsUsedDetailResponse:
        """
        @param request: GetLindormFsUsedDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormFsUsedDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormFsUsedDetail',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormFsUsedDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormFsUsedDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_lindorm_fs_used_detail(
        self,
        request: hitsdb_20200615_models.GetLindormFsUsedDetailRequest,
    ) -> hitsdb_20200615_models.GetLindormFsUsedDetailResponse:
        """
        @param request: GetLindormFsUsedDetailRequest
        @return: GetLindormFsUsedDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_fs_used_detail_with_options(request, runtime)

    async def get_lindorm_fs_used_detail_async(
        self,
        request: hitsdb_20200615_models.GetLindormFsUsedDetailRequest,
    ) -> hitsdb_20200615_models.GetLindormFsUsedDetailResponse:
        """
        @param request: GetLindormFsUsedDetailRequest
        @return: GetLindormFsUsedDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_fs_used_detail_with_options_async(request, runtime)

    def get_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        """
        @summary Obtains the detailed information about a Lindorm instance, including the instance type, billing method, and VPC.
        
        @param request: GetLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def get_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        """
        @summary Obtains the detailed information about a Lindorm instance, including the instance type, billing method, and VPC.
        
        @param request: GetLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_lindorm_instance(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        """
        @summary Obtains the detailed information about a Lindorm instance, including the instance type, billing method, and VPC.
        
        @param request: GetLindormInstanceRequest
        @return: GetLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_with_options(request, runtime)

    async def get_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        """
        @summary Obtains the detailed information about a Lindorm instance, including the instance type, billing method, and VPC.
        
        @param request: GetLindormInstanceRequest
        @return: GetLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_with_options_async(request, runtime)

    def get_lindorm_instance_engine_list_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        """
        @summary Obtains the engine types supported by the specified Lindorm instance.
        
        @param request: GetLindormInstanceEngineListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormInstanceEngineListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstanceEngineList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceEngineListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceEngineListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_lindorm_instance_engine_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        """
        @summary Obtains the engine types supported by the specified Lindorm instance.
        
        @param request: GetLindormInstanceEngineListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormInstanceEngineListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstanceEngineList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceEngineListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceEngineListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_lindorm_instance_engine_list(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        """
        @summary Obtains the engine types supported by the specified Lindorm instance.
        
        @param request: GetLindormInstanceEngineListRequest
        @return: GetLindormInstanceEngineListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_engine_list_with_options(request, runtime)

    async def get_lindorm_instance_engine_list_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        """
        @summary Obtains the engine types supported by the specified Lindorm instance.
        
        @param request: GetLindormInstanceEngineListRequest
        @return: GetLindormInstanceEngineListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_engine_list_with_options_async(request, runtime)

    def get_lindorm_instance_list_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        """
        @summary Queries the instances that meet the specified conditions.
        
        @param request: GetLindormInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_str):
            query['QueryStr'] = request.query_str
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.support_engine):
            query['SupportEngine'] = request.support_engine
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstanceList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_lindorm_instance_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        """
        @summary Queries the instances that meet the specified conditions.
        
        @param request: GetLindormInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_str):
            query['QueryStr'] = request.query_str
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.support_engine):
            query['SupportEngine'] = request.support_engine
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstanceList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormInstanceListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_lindorm_instance_list(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        """
        @summary Queries the instances that meet the specified conditions.
        
        @param request: GetLindormInstanceListRequest
        @return: GetLindormInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_list_with_options(request, runtime)

    async def get_lindorm_instance_list_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        """
        @summary Queries the instances that meet the specified conditions.
        
        @param request: GetLindormInstanceListRequest
        @return: GetLindormInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_list_with_options_async(request, runtime)

    def get_lindorm_v2instance_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormV2InstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormV2InstanceResponse:
        """
        @param request: GetLindormV2InstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormV2InstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormV2Instance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2InstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2InstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def get_lindorm_v2instance_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormV2InstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormV2InstanceResponse:
        """
        @param request: GetLindormV2InstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormV2InstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormV2Instance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2InstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2InstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_lindorm_v2instance(
        self,
        request: hitsdb_20200615_models.GetLindormV2InstanceRequest,
    ) -> hitsdb_20200615_models.GetLindormV2InstanceResponse:
        """
        @param request: GetLindormV2InstanceRequest
        @return: GetLindormV2InstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_v2instance_with_options(request, runtime)

    async def get_lindorm_v2instance_async(
        self,
        request: hitsdb_20200615_models.GetLindormV2InstanceRequest,
    ) -> hitsdb_20200615_models.GetLindormV2InstanceResponse:
        """
        @param request: GetLindormV2InstanceRequest
        @return: GetLindormV2InstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_v2instance_with_options_async(request, runtime)

    def get_lindorm_v2instance_engine_list_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormV2InstanceEngineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormV2InstanceEngineListResponse:
        """
        @param request: GetLindormV2InstanceEngineListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormV2InstanceEngineListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormV2InstanceEngineList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2InstanceEngineListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2InstanceEngineListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_lindorm_v2instance_engine_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormV2InstanceEngineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormV2InstanceEngineListResponse:
        """
        @param request: GetLindormV2InstanceEngineListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormV2InstanceEngineListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormV2InstanceEngineList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2InstanceEngineListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2InstanceEngineListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_lindorm_v2instance_engine_list(
        self,
        request: hitsdb_20200615_models.GetLindormV2InstanceEngineListRequest,
    ) -> hitsdb_20200615_models.GetLindormV2InstanceEngineListResponse:
        """
        @param request: GetLindormV2InstanceEngineListRequest
        @return: GetLindormV2InstanceEngineListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_v2instance_engine_list_with_options(request, runtime)

    async def get_lindorm_v2instance_engine_list_async(
        self,
        request: hitsdb_20200615_models.GetLindormV2InstanceEngineListRequest,
    ) -> hitsdb_20200615_models.GetLindormV2InstanceEngineListResponse:
        """
        @param request: GetLindormV2InstanceEngineListRequest
        @return: GetLindormV2InstanceEngineListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_v2instance_engine_list_with_options_async(request, runtime)

    def get_lindorm_v2storage_usage_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormV2StorageUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormV2StorageUsageResponse:
        """
        @param request: GetLindormV2StorageUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormV2StorageUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormV2StorageUsage',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2StorageUsageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2StorageUsageResponse(),
                self.execute(params, req, runtime)
            )

    async def get_lindorm_v2storage_usage_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormV2StorageUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormV2StorageUsageResponse:
        """
        @param request: GetLindormV2StorageUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLindormV2StorageUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormV2StorageUsage',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2StorageUsageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.GetLindormV2StorageUsageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_lindorm_v2storage_usage(
        self,
        request: hitsdb_20200615_models.GetLindormV2StorageUsageRequest,
    ) -> hitsdb_20200615_models.GetLindormV2StorageUsageResponse:
        """
        @param request: GetLindormV2StorageUsageRequest
        @return: GetLindormV2StorageUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_v2storage_usage_with_options(request, runtime)

    async def get_lindorm_v2storage_usage_async(
        self,
        request: hitsdb_20200615_models.GetLindormV2StorageUsageRequest,
    ) -> hitsdb_20200615_models.GetLindormV2StorageUsageResponse:
        """
        @param request: GetLindormV2StorageUsageRequest
        @return: GetLindormV2StorageUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_v2storage_usage_with_options_async(request, runtime)

    def list_auto_scaling_configs_with_options(
        self,
        request: hitsdb_20200615_models.ListAutoScalingConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListAutoScalingConfigsResponse:
        """
        @param request: ListAutoScalingConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoScalingConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingConfigs',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingConfigsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingConfigsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_auto_scaling_configs_with_options_async(
        self,
        request: hitsdb_20200615_models.ListAutoScalingConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListAutoScalingConfigsResponse:
        """
        @param request: ListAutoScalingConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoScalingConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingConfigs',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingConfigsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingConfigsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_auto_scaling_configs(
        self,
        request: hitsdb_20200615_models.ListAutoScalingConfigsRequest,
    ) -> hitsdb_20200615_models.ListAutoScalingConfigsResponse:
        """
        @param request: ListAutoScalingConfigsRequest
        @return: ListAutoScalingConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_configs_with_options(request, runtime)

    async def list_auto_scaling_configs_async(
        self,
        request: hitsdb_20200615_models.ListAutoScalingConfigsRequest,
    ) -> hitsdb_20200615_models.ListAutoScalingConfigsResponse:
        """
        @param request: ListAutoScalingConfigsRequest
        @return: ListAutoScalingConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_scaling_configs_with_options_async(request, runtime)

    def list_auto_scaling_records_with_options(
        self,
        request: hitsdb_20200615_models.ListAutoScalingRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListAutoScalingRecordsResponse:
        """
        @param request: ListAutoScalingRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoScalingRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingRecords',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingRecordsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingRecordsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_auto_scaling_records_with_options_async(
        self,
        request: hitsdb_20200615_models.ListAutoScalingRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListAutoScalingRecordsResponse:
        """
        @param request: ListAutoScalingRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoScalingRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingRecords',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingRecordsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingRecordsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_auto_scaling_records(
        self,
        request: hitsdb_20200615_models.ListAutoScalingRecordsRequest,
    ) -> hitsdb_20200615_models.ListAutoScalingRecordsResponse:
        """
        @param request: ListAutoScalingRecordsRequest
        @return: ListAutoScalingRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_records_with_options(request, runtime)

    async def list_auto_scaling_records_async(
        self,
        request: hitsdb_20200615_models.ListAutoScalingRecordsRequest,
    ) -> hitsdb_20200615_models.ListAutoScalingRecordsResponse:
        """
        @param request: ListAutoScalingRecordsRequest
        @return: ListAutoScalingRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_scaling_records_with_options_async(request, runtime)

    def list_auto_scaling_rules_with_options(
        self,
        request: hitsdb_20200615_models.ListAutoScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListAutoScalingRulesResponse:
        """
        @param request: ListAutoScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingRules',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_auto_scaling_rules_with_options_async(
        self,
        request: hitsdb_20200615_models.ListAutoScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListAutoScalingRulesResponse:
        """
        @param request: ListAutoScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingRules',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListAutoScalingRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_auto_scaling_rules(
        self,
        request: hitsdb_20200615_models.ListAutoScalingRulesRequest,
    ) -> hitsdb_20200615_models.ListAutoScalingRulesResponse:
        """
        @param request: ListAutoScalingRulesRequest
        @return: ListAutoScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_rules_with_options(request, runtime)

    async def list_auto_scaling_rules_async(
        self,
        request: hitsdb_20200615_models.ListAutoScalingRulesRequest,
    ) -> hitsdb_20200615_models.ListAutoScalingRulesResponse:
        """
        @param request: ListAutoScalingRulesRequest
        @return: ListAutoScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_scaling_rules_with_options_async(request, runtime)

    def list_ldps_compute_groups_with_options(
        self,
        request: hitsdb_20200615_models.ListLdpsComputeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListLdpsComputeGroupsResponse:
        """
        @param request: ListLdpsComputeGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLdpsComputeGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLdpsComputeGroups',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListLdpsComputeGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListLdpsComputeGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_ldps_compute_groups_with_options_async(
        self,
        request: hitsdb_20200615_models.ListLdpsComputeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListLdpsComputeGroupsResponse:
        """
        @param request: ListLdpsComputeGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLdpsComputeGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLdpsComputeGroups',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListLdpsComputeGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListLdpsComputeGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_ldps_compute_groups(
        self,
        request: hitsdb_20200615_models.ListLdpsComputeGroupsRequest,
    ) -> hitsdb_20200615_models.ListLdpsComputeGroupsResponse:
        """
        @param request: ListLdpsComputeGroupsRequest
        @return: ListLdpsComputeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ldps_compute_groups_with_options(request, runtime)

    async def list_ldps_compute_groups_async(
        self,
        request: hitsdb_20200615_models.ListLdpsComputeGroupsRequest,
    ) -> hitsdb_20200615_models.ListLdpsComputeGroupsResponse:
        """
        @param request: ListLdpsComputeGroupsRequest
        @return: ListLdpsComputeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ldps_compute_groups_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: hitsdb_20200615_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListTagResourcesResponse:
        """
        @summary Queries the tags associated with the specified Lindorm instance.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: hitsdb_20200615_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListTagResourcesResponse:
        """
        @summary Queries the tags associated with the specified Lindorm instance.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: hitsdb_20200615_models.ListTagResourcesRequest,
    ) -> hitsdb_20200615_models.ListTagResourcesResponse:
        """
        @summary Queries the tags associated with the specified Lindorm instance.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: hitsdb_20200615_models.ListTagResourcesRequest,
    ) -> hitsdb_20200615_models.ListTagResourcesResponse:
        """
        @summary Queries the tags associated with the specified Lindorm instance.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_auto_scaling_config_with_options(
        self,
        request: hitsdb_20200615_models.ModifyAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyAutoScalingConfigResponse:
        """
        @param request: ModifyAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.effective_time_end):
            query['EffectiveTimeEnd'] = request.effective_time_end
        if not UtilClient.is_unset(request.effective_time_start):
            query['EffectiveTimeStart'] = request.effective_time_start
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nodes_max):
            query['NodesMax'] = request.nodes_max
        if not UtilClient.is_unset(request.nodes_min):
            query['NodesMin'] = request.nodes_min
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoScalingConfig',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyAutoScalingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyAutoScalingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_auto_scaling_config_with_options_async(
        self,
        request: hitsdb_20200615_models.ModifyAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyAutoScalingConfigResponse:
        """
        @param request: ModifyAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.effective_time_end):
            query['EffectiveTimeEnd'] = request.effective_time_end
        if not UtilClient.is_unset(request.effective_time_start):
            query['EffectiveTimeStart'] = request.effective_time_start
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nodes_max):
            query['NodesMax'] = request.nodes_max
        if not UtilClient.is_unset(request.nodes_min):
            query['NodesMin'] = request.nodes_min
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoScalingConfig',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyAutoScalingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyAutoScalingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_auto_scaling_config(
        self,
        request: hitsdb_20200615_models.ModifyAutoScalingConfigRequest,
    ) -> hitsdb_20200615_models.ModifyAutoScalingConfigResponse:
        """
        @param request: ModifyAutoScalingConfigRequest
        @return: ModifyAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_scaling_config_with_options(request, runtime)

    async def modify_auto_scaling_config_async(
        self,
        request: hitsdb_20200615_models.ModifyAutoScalingConfigRequest,
    ) -> hitsdb_20200615_models.ModifyAutoScalingConfigResponse:
        """
        @param request: ModifyAutoScalingConfigRequest
        @return: ModifyAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_scaling_config_with_options_async(request, runtime)

    def modify_auto_scaling_rule_with_options(
        self,
        request: hitsdb_20200615_models.ModifyAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyAutoScalingRuleResponse:
        """
        @param request: ModifyAutoScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.observation_window):
            query['ObservationWindow'] = request.observation_window
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scale_in_step):
            query['ScaleInStep'] = request.scale_in_step
        if not UtilClient.is_unset(request.scale_out_step):
            query['ScaleOutStep'] = request.scale_out_step
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_metric):
            query['TargetMetric'] = request.target_metric
        if not UtilClient.is_unset(request.target_nodes):
            query['TargetNodes'] = request.target_nodes
        if not UtilClient.is_unset(request.threshold_lower):
            query['ThresholdLower'] = request.threshold_lower
        if not UtilClient.is_unset(request.threshold_upper):
            query['ThresholdUpper'] = request.threshold_upper
        if not UtilClient.is_unset(request.trigger_cron_expr):
            query['TriggerCronExpr'] = request.trigger_cron_expr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoScalingRule',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyAutoScalingRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyAutoScalingRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_auto_scaling_rule_with_options_async(
        self,
        request: hitsdb_20200615_models.ModifyAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyAutoScalingRuleResponse:
        """
        @param request: ModifyAutoScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.observation_window):
            query['ObservationWindow'] = request.observation_window
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scale_in_step):
            query['ScaleInStep'] = request.scale_in_step
        if not UtilClient.is_unset(request.scale_out_step):
            query['ScaleOutStep'] = request.scale_out_step
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_metric):
            query['TargetMetric'] = request.target_metric
        if not UtilClient.is_unset(request.target_nodes):
            query['TargetNodes'] = request.target_nodes
        if not UtilClient.is_unset(request.threshold_lower):
            query['ThresholdLower'] = request.threshold_lower
        if not UtilClient.is_unset(request.threshold_upper):
            query['ThresholdUpper'] = request.threshold_upper
        if not UtilClient.is_unset(request.trigger_cron_expr):
            query['TriggerCronExpr'] = request.trigger_cron_expr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoScalingRule',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyAutoScalingRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyAutoScalingRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_auto_scaling_rule(
        self,
        request: hitsdb_20200615_models.ModifyAutoScalingRuleRequest,
    ) -> hitsdb_20200615_models.ModifyAutoScalingRuleResponse:
        """
        @param request: ModifyAutoScalingRuleRequest
        @return: ModifyAutoScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_scaling_rule_with_options(request, runtime)

    async def modify_auto_scaling_rule_async(
        self,
        request: hitsdb_20200615_models.ModifyAutoScalingRuleRequest,
    ) -> hitsdb_20200615_models.ModifyAutoScalingRuleResponse:
        """
        @param request: ModifyAutoScalingRuleRequest
        @return: ModifyAutoScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_scaling_rule_with_options_async(request, runtime)

    def modify_instance_pay_type_with_options(
        self,
        request: hitsdb_20200615_models.ModifyInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyInstancePayTypeResponse:
        """
        @summary Changes the billing method of the specified Lindorm instance.
        
        @description You can call this operation to change the billing method of an instance to subscription or pay-as-you-go.
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/en/pricing-calculator?spm=a2c63.p38356.0.0.2b024c2adcHeXL&_p_lc=1#/commodity/hitsdb_lindormpre_public_intl) of Lindorm. Published on only international site (alibabacloud.com).
        
        @param request: ModifyInstancePayTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstancePayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstancePayType',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyInstancePayTypeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyInstancePayTypeResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_pay_type_with_options_async(
        self,
        request: hitsdb_20200615_models.ModifyInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyInstancePayTypeResponse:
        """
        @summary Changes the billing method of the specified Lindorm instance.
        
        @description You can call this operation to change the billing method of an instance to subscription or pay-as-you-go.
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/en/pricing-calculator?spm=a2c63.p38356.0.0.2b024c2adcHeXL&_p_lc=1#/commodity/hitsdb_lindormpre_public_intl) of Lindorm. Published on only international site (alibabacloud.com).
        
        @param request: ModifyInstancePayTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstancePayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstancePayType',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyInstancePayTypeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyInstancePayTypeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_pay_type(
        self,
        request: hitsdb_20200615_models.ModifyInstancePayTypeRequest,
    ) -> hitsdb_20200615_models.ModifyInstancePayTypeResponse:
        """
        @summary Changes the billing method of the specified Lindorm instance.
        
        @description You can call this operation to change the billing method of an instance to subscription or pay-as-you-go.
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/en/pricing-calculator?spm=a2c63.p38356.0.0.2b024c2adcHeXL&_p_lc=1#/commodity/hitsdb_lindormpre_public_intl) of Lindorm. Published on only international site (alibabacloud.com).
        
        @param request: ModifyInstancePayTypeRequest
        @return: ModifyInstancePayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_pay_type_with_options(request, runtime)

    async def modify_instance_pay_type_async(
        self,
        request: hitsdb_20200615_models.ModifyInstancePayTypeRequest,
    ) -> hitsdb_20200615_models.ModifyInstancePayTypeResponse:
        """
        @summary Changes the billing method of the specified Lindorm instance.
        
        @description You can call this operation to change the billing method of an instance to subscription or pay-as-you-go.
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/en/pricing-calculator?spm=a2c63.p38356.0.0.2b024c2adcHeXL&_p_lc=1#/commodity/hitsdb_lindormpre_public_intl) of Lindorm. Published on only international site (alibabacloud.com).
        
        @param request: ModifyInstancePayTypeRequest
        @return: ModifyInstancePayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_pay_type_with_options_async(request, runtime)

    def modify_lindorm_v2instance_with_options(
        self,
        request: hitsdb_20200615_models.ModifyLindormV2InstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyLindormV2InstanceResponse:
        """
        @param request: ModifyLindormV2InstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLindormV2InstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not UtilClient.is_unset(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_list):
            query['NodeGroupList'] = request.node_group_list
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLindormV2Instance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyLindormV2InstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyLindormV2InstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_lindorm_v2instance_with_options_async(
        self,
        request: hitsdb_20200615_models.ModifyLindormV2InstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyLindormV2InstanceResponse:
        """
        @param request: ModifyLindormV2InstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLindormV2InstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_storage_size):
            query['CloudStorageSize'] = request.cloud_storage_size
        if not UtilClient.is_unset(request.cloud_storage_type):
            query['CloudStorageType'] = request.cloud_storage_type
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_list):
            query['NodeGroupList'] = request.node_group_list
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLindormV2Instance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyLindormV2InstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyLindormV2InstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_lindorm_v2instance(
        self,
        request: hitsdb_20200615_models.ModifyLindormV2InstanceRequest,
    ) -> hitsdb_20200615_models.ModifyLindormV2InstanceResponse:
        """
        @param request: ModifyLindormV2InstanceRequest
        @return: ModifyLindormV2InstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_lindorm_v2instance_with_options(request, runtime)

    async def modify_lindorm_v2instance_async(
        self,
        request: hitsdb_20200615_models.ModifyLindormV2InstanceRequest,
    ) -> hitsdb_20200615_models.ModifyLindormV2InstanceResponse:
        """
        @param request: ModifyLindormV2InstanceRequest
        @return: ModifyLindormV2InstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_lindorm_v2instance_with_options_async(request, runtime)

    def modify_lindorm_v2white_ip_list_with_options(
        self,
        request: hitsdb_20200615_models.ModifyLindormV2WhiteIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyLindormV2WhiteIpListResponse:
        """
        @param request: ModifyLindormV2WhiteIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLindormV2WhiteIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_group):
            query['DeleteGroup'] = request.delete_group
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.white_ip_list):
            query['WhiteIpList'] = request.white_ip_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLindormV2WhiteIpList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyLindormV2WhiteIpListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyLindormV2WhiteIpListResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_lindorm_v2white_ip_list_with_options_async(
        self,
        request: hitsdb_20200615_models.ModifyLindormV2WhiteIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyLindormV2WhiteIpListResponse:
        """
        @param request: ModifyLindormV2WhiteIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLindormV2WhiteIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_group):
            query['DeleteGroup'] = request.delete_group
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.white_ip_list):
            query['WhiteIpList'] = request.white_ip_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLindormV2WhiteIpList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyLindormV2WhiteIpListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ModifyLindormV2WhiteIpListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_lindorm_v2white_ip_list(
        self,
        request: hitsdb_20200615_models.ModifyLindormV2WhiteIpListRequest,
    ) -> hitsdb_20200615_models.ModifyLindormV2WhiteIpListResponse:
        """
        @param request: ModifyLindormV2WhiteIpListRequest
        @return: ModifyLindormV2WhiteIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_lindorm_v2white_ip_list_with_options(request, runtime)

    async def modify_lindorm_v2white_ip_list_async(
        self,
        request: hitsdb_20200615_models.ModifyLindormV2WhiteIpListRequest,
    ) -> hitsdb_20200615_models.ModifyLindormV2WhiteIpListResponse:
        """
        @param request: ModifyLindormV2WhiteIpListRequest
        @return: ModifyLindormV2WhiteIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_lindorm_v2white_ip_list_with_options_async(request, runtime)

    def open_compute_engine_with_options(
        self,
        request: hitsdb_20200615_models.OpenComputeEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.OpenComputeEngineResponse:
        """
        @param request: OpenComputeEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenComputeEngineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenComputeEngine',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.OpenComputeEngineResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.OpenComputeEngineResponse(),
                self.execute(params, req, runtime)
            )

    async def open_compute_engine_with_options_async(
        self,
        request: hitsdb_20200615_models.OpenComputeEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.OpenComputeEngineResponse:
        """
        @param request: OpenComputeEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenComputeEngineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenComputeEngine',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.OpenComputeEngineResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.OpenComputeEngineResponse(),
                await self.execute_async(params, req, runtime)
            )

    def open_compute_engine(
        self,
        request: hitsdb_20200615_models.OpenComputeEngineRequest,
    ) -> hitsdb_20200615_models.OpenComputeEngineResponse:
        """
        @param request: OpenComputeEngineRequest
        @return: OpenComputeEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_compute_engine_with_options(request, runtime)

    async def open_compute_engine_async(
        self,
        request: hitsdb_20200615_models.OpenComputeEngineRequest,
    ) -> hitsdb_20200615_models.OpenComputeEngineResponse:
        """
        @param request: OpenComputeEngineRequest
        @return: OpenComputeEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_compute_engine_with_options_async(request, runtime)

    def open_compute_pre_check_with_options(
        self,
        request: hitsdb_20200615_models.OpenComputePreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.OpenComputePreCheckResponse:
        """
        @param request: OpenComputePreCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenComputePreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenComputePreCheck',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.OpenComputePreCheckResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.OpenComputePreCheckResponse(),
                self.execute(params, req, runtime)
            )

    async def open_compute_pre_check_with_options_async(
        self,
        request: hitsdb_20200615_models.OpenComputePreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.OpenComputePreCheckResponse:
        """
        @param request: OpenComputePreCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenComputePreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenComputePreCheck',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.OpenComputePreCheckResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.OpenComputePreCheckResponse(),
                await self.execute_async(params, req, runtime)
            )

    def open_compute_pre_check(
        self,
        request: hitsdb_20200615_models.OpenComputePreCheckRequest,
    ) -> hitsdb_20200615_models.OpenComputePreCheckResponse:
        """
        @param request: OpenComputePreCheckRequest
        @return: OpenComputePreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_compute_pre_check_with_options(request, runtime)

    async def open_compute_pre_check_async(
        self,
        request: hitsdb_20200615_models.OpenComputePreCheckRequest,
    ) -> hitsdb_20200615_models.OpenComputePreCheckResponse:
        """
        @param request: OpenComputePreCheckRequest
        @return: OpenComputePreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_compute_pre_check_with_options_async(request, runtime)

    def release_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.ReleaseLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ReleaseLindormInstanceResponse:
        """
        @summary Releases a Lindorm instance.
        
        @param request: ReleaseLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.immediately):
            query['Immediately'] = request.immediately
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ReleaseLindormInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ReleaseLindormInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def release_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.ReleaseLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ReleaseLindormInstanceResponse:
        """
        @summary Releases a Lindorm instance.
        
        @param request: ReleaseLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.immediately):
            query['Immediately'] = request.immediately
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ReleaseLindormInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ReleaseLindormInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def release_lindorm_instance(
        self,
        request: hitsdb_20200615_models.ReleaseLindormInstanceRequest,
    ) -> hitsdb_20200615_models.ReleaseLindormInstanceResponse:
        """
        @summary Releases a Lindorm instance.
        
        @param request: ReleaseLindormInstanceRequest
        @return: ReleaseLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_lindorm_instance_with_options(request, runtime)

    async def release_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.ReleaseLindormInstanceRequest,
    ) -> hitsdb_20200615_models.ReleaseLindormInstanceResponse:
        """
        @summary Releases a Lindorm instance.
        
        @param request: ReleaseLindormInstanceRequest
        @return: ReleaseLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_lindorm_instance_with_options_async(request, runtime)

    def release_lindorm_v2instance_with_options(
        self,
        request: hitsdb_20200615_models.ReleaseLindormV2InstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ReleaseLindormV2InstanceResponse:
        """
        @param request: ReleaseLindormV2InstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseLindormV2InstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.immediately):
            query['Immediately'] = request.immediately
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseLindormV2Instance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ReleaseLindormV2InstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ReleaseLindormV2InstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def release_lindorm_v2instance_with_options_async(
        self,
        request: hitsdb_20200615_models.ReleaseLindormV2InstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ReleaseLindormV2InstanceResponse:
        """
        @param request: ReleaseLindormV2InstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseLindormV2InstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.immediately):
            query['Immediately'] = request.immediately
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseLindormV2Instance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.ReleaseLindormV2InstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.ReleaseLindormV2InstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def release_lindorm_v2instance(
        self,
        request: hitsdb_20200615_models.ReleaseLindormV2InstanceRequest,
    ) -> hitsdb_20200615_models.ReleaseLindormV2InstanceResponse:
        """
        @param request: ReleaseLindormV2InstanceRequest
        @return: ReleaseLindormV2InstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_lindorm_v2instance_with_options(request, runtime)

    async def release_lindorm_v2instance_async(
        self,
        request: hitsdb_20200615_models.ReleaseLindormV2InstanceRequest,
    ) -> hitsdb_20200615_models.ReleaseLindormV2InstanceResponse:
        """
        @param request: ReleaseLindormV2InstanceRequest
        @return: ReleaseLindormV2InstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_lindorm_v2instance_with_options_async(request, runtime)

    def renew_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.RenewLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.RenewLindormInstanceResponse:
        """
        @summary Renews a subscription Lindorm instance.
        
        @description You can call this operation to renew a subscription Lindorm instance for 1 to 9 months or 1 to 3 years.
        Before you call this operation, make sure that you fully understand the billing methods and pricing of Lindorm.
        
        @param request: RenewLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.RenewLindormInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.RenewLindormInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def renew_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.RenewLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.RenewLindormInstanceResponse:
        """
        @summary Renews a subscription Lindorm instance.
        
        @description You can call this operation to renew a subscription Lindorm instance for 1 to 9 months or 1 to 3 years.
        Before you call this operation, make sure that you fully understand the billing methods and pricing of Lindorm.
        
        @param request: RenewLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.RenewLindormInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.RenewLindormInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def renew_lindorm_instance(
        self,
        request: hitsdb_20200615_models.RenewLindormInstanceRequest,
    ) -> hitsdb_20200615_models.RenewLindormInstanceResponse:
        """
        @summary Renews a subscription Lindorm instance.
        
        @description You can call this operation to renew a subscription Lindorm instance for 1 to 9 months or 1 to 3 years.
        Before you call this operation, make sure that you fully understand the billing methods and pricing of Lindorm.
        
        @param request: RenewLindormInstanceRequest
        @return: RenewLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_lindorm_instance_with_options(request, runtime)

    async def renew_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.RenewLindormInstanceRequest,
    ) -> hitsdb_20200615_models.RenewLindormInstanceResponse:
        """
        @summary Renews a subscription Lindorm instance.
        
        @description You can call this operation to renew a subscription Lindorm instance for 1 to 9 months or 1 to 3 years.
        Before you call this operation, make sure that you fully understand the billing methods and pricing of Lindorm.
        
        @param request: RenewLindormInstanceRequest
        @return: RenewLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_lindorm_instance_with_options_async(request, runtime)

    def restart_ldps_compute_group_with_options(
        self,
        request: hitsdb_20200615_models.RestartLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.RestartLdpsComputeGroupResponse:
        """
        @param request: RestartLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.RestartLdpsComputeGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.RestartLdpsComputeGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def restart_ldps_compute_group_with_options_async(
        self,
        request: hitsdb_20200615_models.RestartLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.RestartLdpsComputeGroupResponse:
        """
        @param request: RestartLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.RestartLdpsComputeGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.RestartLdpsComputeGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def restart_ldps_compute_group(
        self,
        request: hitsdb_20200615_models.RestartLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.RestartLdpsComputeGroupResponse:
        """
        @param request: RestartLdpsComputeGroupRequest
        @return: RestartLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_ldps_compute_group_with_options(request, runtime)

    async def restart_ldps_compute_group_async(
        self,
        request: hitsdb_20200615_models.RestartLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.RestartLdpsComputeGroupResponse:
        """
        @param request: RestartLdpsComputeGroupRequest
        @return: RestartLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_ldps_compute_group_with_options_async(request, runtime)

    def set_default_olap_compute_group_with_options(
        self,
        request: hitsdb_20200615_models.SetDefaultOlapComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.SetDefaultOlapComputeGroupResponse:
        """
        @param request: SetDefaultOlapComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultOlapComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultOlapComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.SetDefaultOlapComputeGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.SetDefaultOlapComputeGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def set_default_olap_compute_group_with_options_async(
        self,
        request: hitsdb_20200615_models.SetDefaultOlapComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.SetDefaultOlapComputeGroupResponse:
        """
        @param request: SetDefaultOlapComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultOlapComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultOlapComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.SetDefaultOlapComputeGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.SetDefaultOlapComputeGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_default_olap_compute_group(
        self,
        request: hitsdb_20200615_models.SetDefaultOlapComputeGroupRequest,
    ) -> hitsdb_20200615_models.SetDefaultOlapComputeGroupResponse:
        """
        @param request: SetDefaultOlapComputeGroupRequest
        @return: SetDefaultOlapComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_default_olap_compute_group_with_options(request, runtime)

    async def set_default_olap_compute_group_async(
        self,
        request: hitsdb_20200615_models.SetDefaultOlapComputeGroupRequest,
    ) -> hitsdb_20200615_models.SetDefaultOlapComputeGroupResponse:
        """
        @param request: SetDefaultOlapComputeGroupRequest
        @return: SetDefaultOlapComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_default_olap_compute_group_with_options_async(request, runtime)

    def switch_lsqlv3my_sqlservice_with_options(
        self,
        request: hitsdb_20200615_models.SwitchLSQLV3MySQLServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.SwitchLSQLV3MySQLServiceResponse:
        """
        @summary Enables or disables the MySQL compatibility feature for a Lindorm instance.
        
        @description Prerequisites
        The LindormTable version of your instance is 2.6.0 or later.
        The LindormTable of your instance supports LindormSQL V3. The value of the EnableLsqlVersionV3 parameter in the response of the GetLindormInstance operation is true for Lindorm instances purchased after Oct 24, 2023, which indicates that LindormSQL is supported by these instances by default. If you want to enable LindormSQL for instances purchased before Oct 24, 2023, contact the on-duty technical support.
        You can enable the MySQL compatibility feature for a Lindorm instance only when the instance meets the preceding requirements.
        
        @param request: SwitchLSQLV3MySQLServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchLSQLV3MySQLServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchLSQLV3MySQLService',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.SwitchLSQLV3MySQLServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.SwitchLSQLV3MySQLServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def switch_lsqlv3my_sqlservice_with_options_async(
        self,
        request: hitsdb_20200615_models.SwitchLSQLV3MySQLServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.SwitchLSQLV3MySQLServiceResponse:
        """
        @summary Enables or disables the MySQL compatibility feature for a Lindorm instance.
        
        @description Prerequisites
        The LindormTable version of your instance is 2.6.0 or later.
        The LindormTable of your instance supports LindormSQL V3. The value of the EnableLsqlVersionV3 parameter in the response of the GetLindormInstance operation is true for Lindorm instances purchased after Oct 24, 2023, which indicates that LindormSQL is supported by these instances by default. If you want to enable LindormSQL for instances purchased before Oct 24, 2023, contact the on-duty technical support.
        You can enable the MySQL compatibility feature for a Lindorm instance only when the instance meets the preceding requirements.
        
        @param request: SwitchLSQLV3MySQLServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchLSQLV3MySQLServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchLSQLV3MySQLService',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.SwitchLSQLV3MySQLServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.SwitchLSQLV3MySQLServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def switch_lsqlv3my_sqlservice(
        self,
        request: hitsdb_20200615_models.SwitchLSQLV3MySQLServiceRequest,
    ) -> hitsdb_20200615_models.SwitchLSQLV3MySQLServiceResponse:
        """
        @summary Enables or disables the MySQL compatibility feature for a Lindorm instance.
        
        @description Prerequisites
        The LindormTable version of your instance is 2.6.0 or later.
        The LindormTable of your instance supports LindormSQL V3. The value of the EnableLsqlVersionV3 parameter in the response of the GetLindormInstance operation is true for Lindorm instances purchased after Oct 24, 2023, which indicates that LindormSQL is supported by these instances by default. If you want to enable LindormSQL for instances purchased before Oct 24, 2023, contact the on-duty technical support.
        You can enable the MySQL compatibility feature for a Lindorm instance only when the instance meets the preceding requirements.
        
        @param request: SwitchLSQLV3MySQLServiceRequest
        @return: SwitchLSQLV3MySQLServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_lsqlv3my_sqlservice_with_options(request, runtime)

    async def switch_lsqlv3my_sqlservice_async(
        self,
        request: hitsdb_20200615_models.SwitchLSQLV3MySQLServiceRequest,
    ) -> hitsdb_20200615_models.SwitchLSQLV3MySQLServiceResponse:
        """
        @summary Enables or disables the MySQL compatibility feature for a Lindorm instance.
        
        @description Prerequisites
        The LindormTable version of your instance is 2.6.0 or later.
        The LindormTable of your instance supports LindormSQL V3. The value of the EnableLsqlVersionV3 parameter in the response of the GetLindormInstance operation is true for Lindorm instances purchased after Oct 24, 2023, which indicates that LindormSQL is supported by these instances by default. If you want to enable LindormSQL for instances purchased before Oct 24, 2023, contact the on-duty technical support.
        You can enable the MySQL compatibility feature for a Lindorm instance only when the instance meets the preceding requirements.
        
        @param request: SwitchLSQLV3MySQLServiceRequest
        @return: SwitchLSQLV3MySQLServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_lsqlv3my_sqlservice_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: hitsdb_20200615_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.TagResourcesResponse:
        """
        @summary Associates tags with a single or multiple Lindorm instances.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: hitsdb_20200615_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.TagResourcesResponse:
        """
        @summary Associates tags with a single or multiple Lindorm instances.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: hitsdb_20200615_models.TagResourcesRequest,
    ) -> hitsdb_20200615_models.TagResourcesResponse:
        """
        @summary Associates tags with a single or multiple Lindorm instances.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: hitsdb_20200615_models.TagResourcesRequest,
    ) -> hitsdb_20200615_models.TagResourcesResponse:
        """
        @summary Associates tags with a single or multiple Lindorm instances.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: hitsdb_20200615_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UntagResourcesResponse:
        """
        @summary Removes tags from a Lindorm instance.
        
        @description If a tag is not added to any Lindorm instance, it is deleted.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        request: hitsdb_20200615_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UntagResourcesResponse:
        """
        @summary Removes tags from a Lindorm instance.
        
        @description If a tag is not added to any Lindorm instance, it is deleted.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: hitsdb_20200615_models.UntagResourcesRequest,
    ) -> hitsdb_20200615_models.UntagResourcesResponse:
        """
        @summary Removes tags from a Lindorm instance.
        
        @description If a tag is not added to any Lindorm instance, it is deleted.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: hitsdb_20200615_models.UntagResourcesRequest,
    ) -> hitsdb_20200615_models.UntagResourcesResponse:
        """
        @summary Removes tags from a Lindorm instance.
        
        @description If a tag is not added to any Lindorm instance, it is deleted.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_instance_ip_white_list_with_options(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        """
        @summary Configures an IP address whitelist for a Lindorm instance.
        
        @param request: UpdateInstanceIpWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceIpWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete):
            query['Delete'] = request.delete
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_list):
            query['SecurityIpList'] = request.security_ip_list
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceIpWhiteList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse(),
                self.execute(params, req, runtime)
            )

    async def update_instance_ip_white_list_with_options_async(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        """
        @summary Configures an IP address whitelist for a Lindorm instance.
        
        @param request: UpdateInstanceIpWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceIpWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete):
            query['Delete'] = request.delete
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_list):
            query['SecurityIpList'] = request.security_ip_list
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceIpWhiteList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_instance_ip_white_list(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        """
        @summary Configures an IP address whitelist for a Lindorm instance.
        
        @param request: UpdateInstanceIpWhiteListRequest
        @return: UpdateInstanceIpWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_ip_white_list_with_options(request, runtime)

    async def update_instance_ip_white_list_async(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        """
        @summary Configures an IP address whitelist for a Lindorm instance.
        
        @param request: UpdateInstanceIpWhiteListRequest
        @return: UpdateInstanceIpWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_ip_white_list_with_options_async(request, runtime)

    def update_instance_security_groups_with_options(
        self,
        request: hitsdb_20200615_models.UpdateInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateInstanceSecurityGroupsResponse:
        """
        @param request: UpdateInstanceSecurityGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceSecurityGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_groups):
            query['SecurityGroups'] = request.security_groups
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceSecurityGroups',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateInstanceSecurityGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateInstanceSecurityGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def update_instance_security_groups_with_options_async(
        self,
        request: hitsdb_20200615_models.UpdateInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateInstanceSecurityGroupsResponse:
        """
        @param request: UpdateInstanceSecurityGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceSecurityGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_groups):
            query['SecurityGroups'] = request.security_groups
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceSecurityGroups',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateInstanceSecurityGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateInstanceSecurityGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_instance_security_groups(
        self,
        request: hitsdb_20200615_models.UpdateInstanceSecurityGroupsRequest,
    ) -> hitsdb_20200615_models.UpdateInstanceSecurityGroupsResponse:
        """
        @param request: UpdateInstanceSecurityGroupsRequest
        @return: UpdateInstanceSecurityGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_security_groups_with_options(request, runtime)

    async def update_instance_security_groups_async(
        self,
        request: hitsdb_20200615_models.UpdateInstanceSecurityGroupsRequest,
    ) -> hitsdb_20200615_models.UpdateInstanceSecurityGroupsResponse:
        """
        @param request: UpdateInstanceSecurityGroupsRequest
        @return: UpdateInstanceSecurityGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_security_groups_with_options_async(request, runtime)

    def update_ldps_compute_group_with_options(
        self,
        request: hitsdb_20200615_models.UpdateLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateLdpsComputeGroupResponse:
        """
        @param request: UpdateLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateLdpsComputeGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateLdpsComputeGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def update_ldps_compute_group_with_options_async(
        self,
        request: hitsdb_20200615_models.UpdateLdpsComputeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateLdpsComputeGroupResponse:
        """
        @param request: UpdateLdpsComputeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLdpsComputeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLdpsComputeGroup',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateLdpsComputeGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateLdpsComputeGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_ldps_compute_group(
        self,
        request: hitsdb_20200615_models.UpdateLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.UpdateLdpsComputeGroupResponse:
        """
        @param request: UpdateLdpsComputeGroupRequest
        @return: UpdateLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ldps_compute_group_with_options(request, runtime)

    async def update_ldps_compute_group_async(
        self,
        request: hitsdb_20200615_models.UpdateLdpsComputeGroupRequest,
    ) -> hitsdb_20200615_models.UpdateLdpsComputeGroupResponse:
        """
        @param request: UpdateLdpsComputeGroupRequest
        @return: UpdateLdpsComputeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ldps_compute_group_with_options_async(request, runtime)

    def update_lindorm_v2instance_parameter_with_options(
        self,
        request: hitsdb_20200615_models.UpdateLindormV2InstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateLindormV2InstanceParameterResponse:
        """
        @param request: UpdateLindormV2InstanceParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLindormV2InstanceParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_key):
            query['ParameterKey'] = request.parameter_key
        if not UtilClient.is_unset(request.parameter_value):
            query['ParameterValue'] = request.parameter_value
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLindormV2InstanceParameter',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateLindormV2InstanceParameterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateLindormV2InstanceParameterResponse(),
                self.execute(params, req, runtime)
            )

    async def update_lindorm_v2instance_parameter_with_options_async(
        self,
        request: hitsdb_20200615_models.UpdateLindormV2InstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateLindormV2InstanceParameterResponse:
        """
        @param request: UpdateLindormV2InstanceParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLindormV2InstanceParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_key):
            query['ParameterKey'] = request.parameter_key
        if not UtilClient.is_unset(request.parameter_value):
            query['ParameterValue'] = request.parameter_value
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLindormV2InstanceParameter',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateLindormV2InstanceParameterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpdateLindormV2InstanceParameterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_lindorm_v2instance_parameter(
        self,
        request: hitsdb_20200615_models.UpdateLindormV2InstanceParameterRequest,
    ) -> hitsdb_20200615_models.UpdateLindormV2InstanceParameterResponse:
        """
        @param request: UpdateLindormV2InstanceParameterRequest
        @return: UpdateLindormV2InstanceParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_lindorm_v2instance_parameter_with_options(request, runtime)

    async def update_lindorm_v2instance_parameter_async(
        self,
        request: hitsdb_20200615_models.UpdateLindormV2InstanceParameterRequest,
    ) -> hitsdb_20200615_models.UpdateLindormV2InstanceParameterResponse:
        """
        @param request: UpdateLindormV2InstanceParameterRequest
        @return: UpdateLindormV2InstanceParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_lindorm_v2instance_parameter_with_options_async(request, runtime)

    def upgrade_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.UpgradeLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpgradeLindormInstanceResponse:
        """
        @summary Upgrades, scales up, or enable cold storage for a Lindorm instance.
        
        @description For more information about how to select the storage type and engine type when you create a Lindorm instance, see [Select engine typpes](https://help.aliyun.com/document_detail/181971.html) and [Select storage types](https://help.aliyun.com/document_detail/174643.html).
        
        @param request: UpgradeLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_storage):
            query['ClusterStorage'] = request.cluster_storage
        if not UtilClient.is_unset(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not UtilClient.is_unset(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not UtilClient.is_unset(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not UtilClient.is_unset(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not UtilClient.is_unset(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not UtilClient.is_unset(request.log_num):
            query['LogNum'] = request.log_num
        if not UtilClient.is_unset(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not UtilClient.is_unset(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not UtilClient.is_unset(request.lts_core_num):
            query['LtsCoreNum'] = request.lts_core_num
        if not UtilClient.is_unset(request.lts_core_spec):
            query['LtsCoreSpec'] = request.lts_core_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not UtilClient.is_unset(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not UtilClient.is_unset(request.stream_num):
            query['StreamNum'] = request.stream_num
        if not UtilClient.is_unset(request.stream_spec):
            query['StreamSpec'] = request.stream_spec
        if not UtilClient.is_unset(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not UtilClient.is_unset(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpgradeLindormInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpgradeLindormInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def upgrade_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.UpgradeLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpgradeLindormInstanceResponse:
        """
        @summary Upgrades, scales up, or enable cold storage for a Lindorm instance.
        
        @description For more information about how to select the storage type and engine type when you create a Lindorm instance, see [Select engine typpes](https://help.aliyun.com/document_detail/181971.html) and [Select storage types](https://help.aliyun.com/document_detail/174643.html).
        
        @param request: UpgradeLindormInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeLindormInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_storage):
            query['ClusterStorage'] = request.cluster_storage
        if not UtilClient.is_unset(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not UtilClient.is_unset(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not UtilClient.is_unset(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not UtilClient.is_unset(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not UtilClient.is_unset(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not UtilClient.is_unset(request.log_num):
            query['LogNum'] = request.log_num
        if not UtilClient.is_unset(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not UtilClient.is_unset(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not UtilClient.is_unset(request.lts_core_num):
            query['LtsCoreNum'] = request.lts_core_num
        if not UtilClient.is_unset(request.lts_core_spec):
            query['LtsCoreSpec'] = request.lts_core_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not UtilClient.is_unset(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not UtilClient.is_unset(request.stream_num):
            query['StreamNum'] = request.stream_num
        if not UtilClient.is_unset(request.stream_spec):
            query['StreamSpec'] = request.stream_spec
        if not UtilClient.is_unset(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not UtilClient.is_unset(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpgradeLindormInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpgradeLindormInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def upgrade_lindorm_instance(
        self,
        request: hitsdb_20200615_models.UpgradeLindormInstanceRequest,
    ) -> hitsdb_20200615_models.UpgradeLindormInstanceResponse:
        """
        @summary Upgrades, scales up, or enable cold storage for a Lindorm instance.
        
        @description For more information about how to select the storage type and engine type when you create a Lindorm instance, see [Select engine typpes](https://help.aliyun.com/document_detail/181971.html) and [Select storage types](https://help.aliyun.com/document_detail/174643.html).
        
        @param request: UpgradeLindormInstanceRequest
        @return: UpgradeLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_lindorm_instance_with_options(request, runtime)

    async def upgrade_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.UpgradeLindormInstanceRequest,
    ) -> hitsdb_20200615_models.UpgradeLindormInstanceResponse:
        """
        @summary Upgrades, scales up, or enable cold storage for a Lindorm instance.
        
        @description For more information about how to select the storage type and engine type when you create a Lindorm instance, see [Select engine typpes](https://help.aliyun.com/document_detail/181971.html) and [Select storage types](https://help.aliyun.com/document_detail/174643.html).
        
        @param request: UpgradeLindormInstanceRequest
        @return: UpgradeLindormInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_lindorm_instance_with_options_async(request, runtime)

    def upgrade_lindorm_v2stream_engine_with_options(
        self,
        request: hitsdb_20200615_models.UpgradeLindormV2StreamEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpgradeLindormV2StreamEngineResponse:
        """
        @param request: UpgradeLindormV2StreamEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeLindormV2StreamEngineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeLindormV2StreamEngine',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpgradeLindormV2StreamEngineResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpgradeLindormV2StreamEngineResponse(),
                self.execute(params, req, runtime)
            )

    async def upgrade_lindorm_v2stream_engine_with_options_async(
        self,
        request: hitsdb_20200615_models.UpgradeLindormV2StreamEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpgradeLindormV2StreamEngineResponse:
        """
        @param request: UpgradeLindormV2StreamEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeLindormV2StreamEngineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeLindormV2StreamEngine',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                hitsdb_20200615_models.UpgradeLindormV2StreamEngineResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                hitsdb_20200615_models.UpgradeLindormV2StreamEngineResponse(),
                await self.execute_async(params, req, runtime)
            )

    def upgrade_lindorm_v2stream_engine(
        self,
        request: hitsdb_20200615_models.UpgradeLindormV2StreamEngineRequest,
    ) -> hitsdb_20200615_models.UpgradeLindormV2StreamEngineResponse:
        """
        @param request: UpgradeLindormV2StreamEngineRequest
        @return: UpgradeLindormV2StreamEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_lindorm_v2stream_engine_with_options(request, runtime)

    async def upgrade_lindorm_v2stream_engine_async(
        self,
        request: hitsdb_20200615_models.UpgradeLindormV2StreamEngineRequest,
    ) -> hitsdb_20200615_models.UpgradeLindormV2StreamEngineResponse:
        """
        @param request: UpgradeLindormV2StreamEngineRequest
        @return: UpgradeLindormV2StreamEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_lindorm_v2stream_engine_with_options_async(request, runtime)
