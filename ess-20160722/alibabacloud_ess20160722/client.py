# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ess20160722 import models as ess_20160722_models
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
        self._endpoint_map = {
            'cn-qingdao': 'ess.aliyuncs.com',
            'cn-beijing': 'ess.aliyuncs.com',
            'cn-hangzhou': 'ess.aliyuncs.com',
            'cn-shanghai': 'ess.aliyuncs.com',
            'cn-shenzhen': 'ess.aliyuncs.com',
            'cn-hongkong': 'ess.aliyuncs.com',
            'ap-southeast-1': 'ess.aliyuncs.com',
            'us-east-1': 'ess.aliyuncs.com',
            'us-west-1': 'ess.aliyuncs.com',
            'cn-shanghai-finance-1': 'ess.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ess.aliyuncs.com',
            'cn-north-2-gov-1': 'ess.aliyuncs.com',
            'ap-northeast-2-pop': 'ess.aliyuncs.com',
            'cn-beijing-finance-pop': 'ess.aliyuncs.com',
            'cn-beijing-gov-1': 'ess.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ess.aliyuncs.com',
            'cn-edge-1': 'ess.aliyuncs.com',
            'cn-fujian': 'ess.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ess.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ess.aliyuncs.com',
            'cn-hangzhou-finance': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ess.aliyuncs.com',
            'cn-hangzhou-test-306': 'ess.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ess.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ess.aliyuncs.com',
            'cn-qingdao-nebula': 'ess.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ess.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ess.aliyuncs.com',
            'cn-shanghai-inner': 'ess.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ess.aliyuncs.com',
            'cn-shenzhen-inner': 'ess.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ess.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ess.aliyuncs.com',
            'cn-wuhan': 'ess.aliyuncs.com',
            'cn-yushanfang': 'ess.aliyuncs.com',
            'cn-zhangbei': 'ess.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ess.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ess.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ess.aliyuncs.com',
            'eu-west-1-oxs': 'ess.aliyuncs.com',
            'rus-west-1-pop': 'ess.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ess', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_instances_with_options(
        self,
        request: ess_20160722_models.AttachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.AttachInstancesResponse:
        """
        @deprecated OpenAPI AttachInstances is deprecated, please use Ess::2014-08-28::AttachInstances,Ess::2022-02-22::AttachInstances instead.
        
        @param request: AttachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.AttachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_instances_with_options_async(
        self,
        request: ess_20160722_models.AttachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.AttachInstancesResponse:
        """
        @deprecated OpenAPI AttachInstances is deprecated, please use Ess::2014-08-28::AttachInstances,Ess::2022-02-22::AttachInstances instead.
        
        @param request: AttachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.AttachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_instances(
        self,
        request: ess_20160722_models.AttachInstancesRequest,
    ) -> ess_20160722_models.AttachInstancesResponse:
        """
        @deprecated OpenAPI AttachInstances is deprecated, please use Ess::2014-08-28::AttachInstances,Ess::2022-02-22::AttachInstances instead.
        
        @param request: AttachInstancesRequest
        @return: AttachInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_instances_with_options(request, runtime)

    async def attach_instances_async(
        self,
        request: ess_20160722_models.AttachInstancesRequest,
    ) -> ess_20160722_models.AttachInstancesResponse:
        """
        @deprecated OpenAPI AttachInstances is deprecated, please use Ess::2014-08-28::AttachInstances,Ess::2022-02-22::AttachInstances instead.
        
        @param request: AttachInstancesRequest
        @return: AttachInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_instances_with_options_async(request, runtime)

    def create_scaling_configuration_with_options(
        self,
        request: ess_20160722_models.CreateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.CreateScalingConfigurationResponse:
        """
        @deprecated OpenAPI CreateScalingConfiguration is deprecated, please use Ess::2022-02-22::CreateScalingConfiguration,Ess::2014-08-28::CreateScalingConfiguration instead.
        
        @param request: CreateScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingConfigurationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingConfiguration',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.CreateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_configuration_with_options_async(
        self,
        request: ess_20160722_models.CreateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.CreateScalingConfigurationResponse:
        """
        @deprecated OpenAPI CreateScalingConfiguration is deprecated, please use Ess::2022-02-22::CreateScalingConfiguration,Ess::2014-08-28::CreateScalingConfiguration instead.
        
        @param request: CreateScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingConfigurationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingConfiguration',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.CreateScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_configuration(
        self,
        request: ess_20160722_models.CreateScalingConfigurationRequest,
    ) -> ess_20160722_models.CreateScalingConfigurationResponse:
        """
        @deprecated OpenAPI CreateScalingConfiguration is deprecated, please use Ess::2022-02-22::CreateScalingConfiguration,Ess::2014-08-28::CreateScalingConfiguration instead.
        
        @param request: CreateScalingConfigurationRequest
        @return: CreateScalingConfigurationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_configuration_with_options(request, runtime)

    async def create_scaling_configuration_async(
        self,
        request: ess_20160722_models.CreateScalingConfigurationRequest,
    ) -> ess_20160722_models.CreateScalingConfigurationResponse:
        """
        @deprecated OpenAPI CreateScalingConfiguration is deprecated, please use Ess::2022-02-22::CreateScalingConfiguration,Ess::2014-08-28::CreateScalingConfiguration instead.
        
        @param request: CreateScalingConfigurationRequest
        @return: CreateScalingConfigurationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_configuration_with_options_async(request, runtime)

    def create_scaling_group_with_options(
        self,
        request: ess_20160722_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.CreateScalingGroupResponse:
        """
        @deprecated OpenAPI CreateScalingGroup is deprecated, please use Ess::2022-02-22::CreateScalingGroup,Ess::2014-08-28::CreateScalingGroup instead.
        
        @param request: CreateScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.removal_policy):
            query['RemovalPolicy'] = request.removal_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.CreateScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_group_with_options_async(
        self,
        request: ess_20160722_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.CreateScalingGroupResponse:
        """
        @deprecated OpenAPI CreateScalingGroup is deprecated, please use Ess::2022-02-22::CreateScalingGroup,Ess::2014-08-28::CreateScalingGroup instead.
        
        @param request: CreateScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.removal_policy):
            query['RemovalPolicy'] = request.removal_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.CreateScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_group(
        self,
        request: ess_20160722_models.CreateScalingGroupRequest,
    ) -> ess_20160722_models.CreateScalingGroupResponse:
        """
        @deprecated OpenAPI CreateScalingGroup is deprecated, please use Ess::2022-02-22::CreateScalingGroup,Ess::2014-08-28::CreateScalingGroup instead.
        
        @param request: CreateScalingGroupRequest
        @return: CreateScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    async def create_scaling_group_async(
        self,
        request: ess_20160722_models.CreateScalingGroupRequest,
    ) -> ess_20160722_models.CreateScalingGroupResponse:
        """
        @deprecated OpenAPI CreateScalingGroup is deprecated, please use Ess::2022-02-22::CreateScalingGroup,Ess::2014-08-28::CreateScalingGroup instead.
        
        @param request: CreateScalingGroupRequest
        @return: CreateScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_group_with_options_async(request, runtime)

    def create_scaling_rule_with_options(
        self,
        request: ess_20160722_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.CreateScalingRuleResponse:
        """
        @deprecated OpenAPI CreateScalingRule is deprecated, please use Ess::2022-02-22::CreateScalingRule,Ess::2014-08-28::CreateScalingRule instead.
        
        @param request: CreateScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.CreateScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_rule_with_options_async(
        self,
        request: ess_20160722_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.CreateScalingRuleResponse:
        """
        @deprecated OpenAPI CreateScalingRule is deprecated, please use Ess::2022-02-22::CreateScalingRule,Ess::2014-08-28::CreateScalingRule instead.
        
        @param request: CreateScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.CreateScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_rule(
        self,
        request: ess_20160722_models.CreateScalingRuleRequest,
    ) -> ess_20160722_models.CreateScalingRuleResponse:
        """
        @deprecated OpenAPI CreateScalingRule is deprecated, please use Ess::2022-02-22::CreateScalingRule,Ess::2014-08-28::CreateScalingRule instead.
        
        @param request: CreateScalingRuleRequest
        @return: CreateScalingRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_rule_with_options(request, runtime)

    async def create_scaling_rule_async(
        self,
        request: ess_20160722_models.CreateScalingRuleRequest,
    ) -> ess_20160722_models.CreateScalingRuleResponse:
        """
        @deprecated OpenAPI CreateScalingRule is deprecated, please use Ess::2022-02-22::CreateScalingRule,Ess::2014-08-28::CreateScalingRule instead.
        
        @param request: CreateScalingRuleRequest
        @return: CreateScalingRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_rule_with_options_async(request, runtime)

    def create_scheduled_task_with_options(
        self,
        request: ess_20160722_models.CreateScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.CreateScheduledTaskResponse:
        """
        @deprecated OpenAPI CreateScheduledTask is deprecated, please use Ess::2022-02-22::CreateScheduledTask,Ess::2014-08-28::CreateScheduledTask instead.
        
        @param request: CreateScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledTaskResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScheduledTask',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        request: ess_20160722_models.CreateScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.CreateScheduledTaskResponse:
        """
        @deprecated OpenAPI CreateScheduledTask is deprecated, please use Ess::2022-02-22::CreateScheduledTask,Ess::2014-08-28::CreateScheduledTask instead.
        
        @param request: CreateScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledTaskResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScheduledTask',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.CreateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_task(
        self,
        request: ess_20160722_models.CreateScheduledTaskRequest,
    ) -> ess_20160722_models.CreateScheduledTaskResponse:
        """
        @deprecated OpenAPI CreateScheduledTask is deprecated, please use Ess::2022-02-22::CreateScheduledTask,Ess::2014-08-28::CreateScheduledTask instead.
        
        @param request: CreateScheduledTaskRequest
        @return: CreateScheduledTaskResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_task_with_options(request, runtime)

    async def create_scheduled_task_async(
        self,
        request: ess_20160722_models.CreateScheduledTaskRequest,
    ) -> ess_20160722_models.CreateScheduledTaskResponse:
        """
        @deprecated OpenAPI CreateScheduledTask is deprecated, please use Ess::2022-02-22::CreateScheduledTask,Ess::2014-08-28::CreateScheduledTask instead.
        
        @param request: CreateScheduledTaskRequest
        @return: CreateScheduledTaskResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduled_task_with_options_async(request, runtime)

    def delete_scaling_configuration_with_options(
        self,
        request: ess_20160722_models.DeleteScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DeleteScalingConfigurationResponse:
        """
        @deprecated OpenAPI DeleteScalingConfiguration is deprecated, please use Ess::2022-02-22::DeleteScalingConfiguration,Ess::2014-08-28::DeleteScalingConfiguration instead.
        
        @param request: DeleteScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingConfigurationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingConfiguration',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DeleteScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_configuration_with_options_async(
        self,
        request: ess_20160722_models.DeleteScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DeleteScalingConfigurationResponse:
        """
        @deprecated OpenAPI DeleteScalingConfiguration is deprecated, please use Ess::2022-02-22::DeleteScalingConfiguration,Ess::2014-08-28::DeleteScalingConfiguration instead.
        
        @param request: DeleteScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingConfigurationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingConfiguration',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DeleteScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_configuration(
        self,
        request: ess_20160722_models.DeleteScalingConfigurationRequest,
    ) -> ess_20160722_models.DeleteScalingConfigurationResponse:
        """
        @deprecated OpenAPI DeleteScalingConfiguration is deprecated, please use Ess::2022-02-22::DeleteScalingConfiguration,Ess::2014-08-28::DeleteScalingConfiguration instead.
        
        @param request: DeleteScalingConfigurationRequest
        @return: DeleteScalingConfigurationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_configuration_with_options(request, runtime)

    async def delete_scaling_configuration_async(
        self,
        request: ess_20160722_models.DeleteScalingConfigurationRequest,
    ) -> ess_20160722_models.DeleteScalingConfigurationResponse:
        """
        @deprecated OpenAPI DeleteScalingConfiguration is deprecated, please use Ess::2022-02-22::DeleteScalingConfiguration,Ess::2014-08-28::DeleteScalingConfiguration instead.
        
        @param request: DeleteScalingConfigurationRequest
        @return: DeleteScalingConfigurationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_configuration_with_options_async(request, runtime)

    def delete_scaling_group_with_options(
        self,
        request: ess_20160722_models.DeleteScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DeleteScalingGroupResponse:
        """
        @deprecated OpenAPI DeleteScalingGroup is deprecated, please use Ess::2022-02-22::DeleteScalingGroup,Ess::2014-08-28::DeleteScalingGroup instead.
        
        @param request: DeleteScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DeleteScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_group_with_options_async(
        self,
        request: ess_20160722_models.DeleteScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DeleteScalingGroupResponse:
        """
        @deprecated OpenAPI DeleteScalingGroup is deprecated, please use Ess::2022-02-22::DeleteScalingGroup,Ess::2014-08-28::DeleteScalingGroup instead.
        
        @param request: DeleteScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DeleteScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_group(
        self,
        request: ess_20160722_models.DeleteScalingGroupRequest,
    ) -> ess_20160722_models.DeleteScalingGroupResponse:
        """
        @deprecated OpenAPI DeleteScalingGroup is deprecated, please use Ess::2022-02-22::DeleteScalingGroup,Ess::2014-08-28::DeleteScalingGroup instead.
        
        @param request: DeleteScalingGroupRequest
        @return: DeleteScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_group_with_options(request, runtime)

    async def delete_scaling_group_async(
        self,
        request: ess_20160722_models.DeleteScalingGroupRequest,
    ) -> ess_20160722_models.DeleteScalingGroupResponse:
        """
        @deprecated OpenAPI DeleteScalingGroup is deprecated, please use Ess::2022-02-22::DeleteScalingGroup,Ess::2014-08-28::DeleteScalingGroup instead.
        
        @param request: DeleteScalingGroupRequest
        @return: DeleteScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_group_with_options_async(request, runtime)

    def delete_scaling_rule_with_options(
        self,
        request: ess_20160722_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DeleteScalingRuleResponse:
        """
        @deprecated OpenAPI DeleteScalingRule is deprecated, please use Ess::2022-02-22::DeleteScalingRule,Ess::2014-08-28::DeleteScalingRule instead.
        
        @param request: DeleteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DeleteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_rule_with_options_async(
        self,
        request: ess_20160722_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DeleteScalingRuleResponse:
        """
        @deprecated OpenAPI DeleteScalingRule is deprecated, please use Ess::2022-02-22::DeleteScalingRule,Ess::2014-08-28::DeleteScalingRule instead.
        
        @param request: DeleteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DeleteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_rule(
        self,
        request: ess_20160722_models.DeleteScalingRuleRequest,
    ) -> ess_20160722_models.DeleteScalingRuleResponse:
        """
        @deprecated OpenAPI DeleteScalingRule is deprecated, please use Ess::2022-02-22::DeleteScalingRule,Ess::2014-08-28::DeleteScalingRule instead.
        
        @param request: DeleteScalingRuleRequest
        @return: DeleteScalingRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_rule_with_options(request, runtime)

    async def delete_scaling_rule_async(
        self,
        request: ess_20160722_models.DeleteScalingRuleRequest,
    ) -> ess_20160722_models.DeleteScalingRuleResponse:
        """
        @deprecated OpenAPI DeleteScalingRule is deprecated, please use Ess::2022-02-22::DeleteScalingRule,Ess::2014-08-28::DeleteScalingRule instead.
        
        @param request: DeleteScalingRuleRequest
        @return: DeleteScalingRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_rule_with_options_async(request, runtime)

    def delete_scheduled_task_with_options(
        self,
        request: ess_20160722_models.DeleteScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DeleteScheduledTaskResponse:
        """
        @deprecated OpenAPI DeleteScheduledTask is deprecated, please use Ess::2022-02-22::DeleteScheduledTask,Ess::2014-08-28::DeleteScheduledTask instead.
        
        @param request: DeleteScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledTaskResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledTask',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DeleteScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_task_with_options_async(
        self,
        request: ess_20160722_models.DeleteScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DeleteScheduledTaskResponse:
        """
        @deprecated OpenAPI DeleteScheduledTask is deprecated, please use Ess::2022-02-22::DeleteScheduledTask,Ess::2014-08-28::DeleteScheduledTask instead.
        
        @param request: DeleteScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledTaskResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledTask',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DeleteScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_task(
        self,
        request: ess_20160722_models.DeleteScheduledTaskRequest,
    ) -> ess_20160722_models.DeleteScheduledTaskResponse:
        """
        @deprecated OpenAPI DeleteScheduledTask is deprecated, please use Ess::2022-02-22::DeleteScheduledTask,Ess::2014-08-28::DeleteScheduledTask instead.
        
        @param request: DeleteScheduledTaskRequest
        @return: DeleteScheduledTaskResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_task_with_options(request, runtime)

    async def delete_scheduled_task_async(
        self,
        request: ess_20160722_models.DeleteScheduledTaskRequest,
    ) -> ess_20160722_models.DeleteScheduledTaskResponse:
        """
        @deprecated OpenAPI DeleteScheduledTask is deprecated, please use Ess::2022-02-22::DeleteScheduledTask,Ess::2014-08-28::DeleteScheduledTask instead.
        
        @param request: DeleteScheduledTaskRequest
        @return: DeleteScheduledTaskResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduled_task_with_options_async(request, runtime)

    def describe_account_attributes_with_options(
        self,
        request: ess_20160722_models.DescribeAccountAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeAccountAttributesResponse:
        """
        @deprecated OpenAPI DescribeAccountAttributes is deprecated, please use Ess::2022-02-22::DescribeLimitation,Ess::2014-08-28::DescribeLimitation instead.
        
        @param request: DescribeAccountAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAttributesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAttributes',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeAccountAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_attributes_with_options_async(
        self,
        request: ess_20160722_models.DescribeAccountAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeAccountAttributesResponse:
        """
        @deprecated OpenAPI DescribeAccountAttributes is deprecated, please use Ess::2022-02-22::DescribeLimitation,Ess::2014-08-28::DescribeLimitation instead.
        
        @param request: DescribeAccountAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAttributesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAttributes',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeAccountAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_attributes(
        self,
        request: ess_20160722_models.DescribeAccountAttributesRequest,
    ) -> ess_20160722_models.DescribeAccountAttributesResponse:
        """
        @deprecated OpenAPI DescribeAccountAttributes is deprecated, please use Ess::2022-02-22::DescribeLimitation,Ess::2014-08-28::DescribeLimitation instead.
        
        @param request: DescribeAccountAttributesRequest
        @return: DescribeAccountAttributesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_attributes_with_options(request, runtime)

    async def describe_account_attributes_async(
        self,
        request: ess_20160722_models.DescribeAccountAttributesRequest,
    ) -> ess_20160722_models.DescribeAccountAttributesResponse:
        """
        @deprecated OpenAPI DescribeAccountAttributes is deprecated, please use Ess::2022-02-22::DescribeLimitation,Ess::2014-08-28::DescribeLimitation instead.
        
        @param request: DescribeAccountAttributesRequest
        @return: DescribeAccountAttributesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_attributes_with_options_async(request, runtime)

    def describe_capacity_history_with_options(
        self,
        request: ess_20160722_models.DescribeCapacityHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeCapacityHistoryResponse:
        """
        @deprecated OpenAPI DescribeCapacityHistory is deprecated, please use Ess::2022-02-22::DescribeScalingActivities,Ess::2014-08-28::DescribeScalingActivities instead.
        
        @param request: DescribeCapacityHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCapacityHistoryResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCapacityHistory',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeCapacityHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_capacity_history_with_options_async(
        self,
        request: ess_20160722_models.DescribeCapacityHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeCapacityHistoryResponse:
        """
        @deprecated OpenAPI DescribeCapacityHistory is deprecated, please use Ess::2022-02-22::DescribeScalingActivities,Ess::2014-08-28::DescribeScalingActivities instead.
        
        @param request: DescribeCapacityHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCapacityHistoryResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCapacityHistory',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeCapacityHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_capacity_history(
        self,
        request: ess_20160722_models.DescribeCapacityHistoryRequest,
    ) -> ess_20160722_models.DescribeCapacityHistoryResponse:
        """
        @deprecated OpenAPI DescribeCapacityHistory is deprecated, please use Ess::2022-02-22::DescribeScalingActivities,Ess::2014-08-28::DescribeScalingActivities instead.
        
        @param request: DescribeCapacityHistoryRequest
        @return: DescribeCapacityHistoryResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_history_with_options(request, runtime)

    async def describe_capacity_history_async(
        self,
        request: ess_20160722_models.DescribeCapacityHistoryRequest,
    ) -> ess_20160722_models.DescribeCapacityHistoryResponse:
        """
        @deprecated OpenAPI DescribeCapacityHistory is deprecated, please use Ess::2022-02-22::DescribeScalingActivities,Ess::2014-08-28::DescribeScalingActivities instead.
        
        @param request: DescribeCapacityHistoryRequest
        @return: DescribeCapacityHistoryResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_capacity_history_with_options_async(request, runtime)

    def describe_limitation_with_options(
        self,
        request: ess_20160722_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeLimitationResponse:
        """
        @deprecated OpenAPI DescribeLimitation is deprecated, please use Ess::2022-02-22::DescribeLimitation,Ess::2014-08-28::DescribeLimitation instead.
        
        @param request: DescribeLimitationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLimitationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLimitation',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeLimitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_limitation_with_options_async(
        self,
        request: ess_20160722_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeLimitationResponse:
        """
        @deprecated OpenAPI DescribeLimitation is deprecated, please use Ess::2022-02-22::DescribeLimitation,Ess::2014-08-28::DescribeLimitation instead.
        
        @param request: DescribeLimitationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLimitationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLimitation',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeLimitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_limitation(
        self,
        request: ess_20160722_models.DescribeLimitationRequest,
    ) -> ess_20160722_models.DescribeLimitationResponse:
        """
        @deprecated OpenAPI DescribeLimitation is deprecated, please use Ess::2022-02-22::DescribeLimitation,Ess::2014-08-28::DescribeLimitation instead.
        
        @param request: DescribeLimitationRequest
        @return: DescribeLimitationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    async def describe_limitation_async(
        self,
        request: ess_20160722_models.DescribeLimitationRequest,
    ) -> ess_20160722_models.DescribeLimitationResponse:
        """
        @deprecated OpenAPI DescribeLimitation is deprecated, please use Ess::2022-02-22::DescribeLimitation,Ess::2014-08-28::DescribeLimitation instead.
        
        @param request: DescribeLimitationRequest
        @return: DescribeLimitationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_limitation_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ess_20160722_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeRegionsResponse:
        """
        @deprecated OpenAPI DescribeRegions is deprecated, please use Ess::2022-02-22::DescribeRegions,Ess::2014-08-28::DescribeRegions instead.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ess_20160722_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeRegionsResponse:
        """
        @deprecated OpenAPI DescribeRegions is deprecated, please use Ess::2022-02-22::DescribeRegions,Ess::2014-08-28::DescribeRegions instead.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ess_20160722_models.DescribeRegionsRequest,
    ) -> ess_20160722_models.DescribeRegionsResponse:
        """
        @deprecated OpenAPI DescribeRegions is deprecated, please use Ess::2022-02-22::DescribeRegions,Ess::2014-08-28::DescribeRegions instead.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ess_20160722_models.DescribeRegionsRequest,
    ) -> ess_20160722_models.DescribeRegionsResponse:
        """
        @deprecated OpenAPI DescribeRegions is deprecated, please use Ess::2022-02-22::DescribeRegions,Ess::2014-08-28::DescribeRegions instead.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_scaling_activities_with_options(
        self,
        request: ess_20160722_models.DescribeScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingActivitiesResponse:
        """
        @deprecated OpenAPI DescribeScalingActivities is deprecated, please use Ess::2022-02-22::DescribeScalingActivities,Ess::2014-08-28::DescribeScalingActivities instead.
        
        @param request: DescribeScalingActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivitiesResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivities',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activities_with_options_async(
        self,
        request: ess_20160722_models.DescribeScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingActivitiesResponse:
        """
        @deprecated OpenAPI DescribeScalingActivities is deprecated, please use Ess::2022-02-22::DescribeScalingActivities,Ess::2014-08-28::DescribeScalingActivities instead.
        
        @param request: DescribeScalingActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivitiesResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivities',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activities(
        self,
        request: ess_20160722_models.DescribeScalingActivitiesRequest,
    ) -> ess_20160722_models.DescribeScalingActivitiesResponse:
        """
        @deprecated OpenAPI DescribeScalingActivities is deprecated, please use Ess::2022-02-22::DescribeScalingActivities,Ess::2014-08-28::DescribeScalingActivities instead.
        
        @param request: DescribeScalingActivitiesRequest
        @return: DescribeScalingActivitiesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activities_with_options(request, runtime)

    async def describe_scaling_activities_async(
        self,
        request: ess_20160722_models.DescribeScalingActivitiesRequest,
    ) -> ess_20160722_models.DescribeScalingActivitiesResponse:
        """
        @deprecated OpenAPI DescribeScalingActivities is deprecated, please use Ess::2022-02-22::DescribeScalingActivities,Ess::2014-08-28::DescribeScalingActivities instead.
        
        @param request: DescribeScalingActivitiesRequest
        @return: DescribeScalingActivitiesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activities_with_options_async(request, runtime)

    def describe_scaling_activity_detail_with_options(
        self,
        request: ess_20160722_models.DescribeScalingActivityDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingActivityDetailResponse:
        """
        @deprecated OpenAPI DescribeScalingActivityDetail is deprecated, please use Ess::2022-02-22::DescribeScalingActivityDetail,Ess::2014-08-28::DescribeScalingActivityDetail instead.
        
        @param request: DescribeScalingActivityDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivityDetailResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivityDetail',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingActivityDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activity_detail_with_options_async(
        self,
        request: ess_20160722_models.DescribeScalingActivityDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingActivityDetailResponse:
        """
        @deprecated OpenAPI DescribeScalingActivityDetail is deprecated, please use Ess::2022-02-22::DescribeScalingActivityDetail,Ess::2014-08-28::DescribeScalingActivityDetail instead.
        
        @param request: DescribeScalingActivityDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivityDetailResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivityDetail',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingActivityDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activity_detail(
        self,
        request: ess_20160722_models.DescribeScalingActivityDetailRequest,
    ) -> ess_20160722_models.DescribeScalingActivityDetailResponse:
        """
        @deprecated OpenAPI DescribeScalingActivityDetail is deprecated, please use Ess::2022-02-22::DescribeScalingActivityDetail,Ess::2014-08-28::DescribeScalingActivityDetail instead.
        
        @param request: DescribeScalingActivityDetailRequest
        @return: DescribeScalingActivityDetailResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activity_detail_with_options(request, runtime)

    async def describe_scaling_activity_detail_async(
        self,
        request: ess_20160722_models.DescribeScalingActivityDetailRequest,
    ) -> ess_20160722_models.DescribeScalingActivityDetailResponse:
        """
        @deprecated OpenAPI DescribeScalingActivityDetail is deprecated, please use Ess::2022-02-22::DescribeScalingActivityDetail,Ess::2014-08-28::DescribeScalingActivityDetail instead.
        
        @param request: DescribeScalingActivityDetailRequest
        @return: DescribeScalingActivityDetailResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activity_detail_with_options_async(request, runtime)

    def describe_scaling_configurations_with_options(
        self,
        request: ess_20160722_models.DescribeScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingConfigurationsResponse:
        """
        @deprecated OpenAPI DescribeScalingConfigurations is deprecated, please use Ess::2022-02-22::DescribeScalingConfigurations,Ess::2014-08-28::DescribeScalingConfigurations instead.
        
        @param request: DescribeScalingConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingConfigurationsResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigurations',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_configurations_with_options_async(
        self,
        request: ess_20160722_models.DescribeScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingConfigurationsResponse:
        """
        @deprecated OpenAPI DescribeScalingConfigurations is deprecated, please use Ess::2022-02-22::DescribeScalingConfigurations,Ess::2014-08-28::DescribeScalingConfigurations instead.
        
        @param request: DescribeScalingConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingConfigurationsResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigurations',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_configurations(
        self,
        request: ess_20160722_models.DescribeScalingConfigurationsRequest,
    ) -> ess_20160722_models.DescribeScalingConfigurationsResponse:
        """
        @deprecated OpenAPI DescribeScalingConfigurations is deprecated, please use Ess::2022-02-22::DescribeScalingConfigurations,Ess::2014-08-28::DescribeScalingConfigurations instead.
        
        @param request: DescribeScalingConfigurationsRequest
        @return: DescribeScalingConfigurationsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_configurations_with_options(request, runtime)

    async def describe_scaling_configurations_async(
        self,
        request: ess_20160722_models.DescribeScalingConfigurationsRequest,
    ) -> ess_20160722_models.DescribeScalingConfigurationsResponse:
        """
        @deprecated OpenAPI DescribeScalingConfigurations is deprecated, please use Ess::2022-02-22::DescribeScalingConfigurations,Ess::2014-08-28::DescribeScalingConfigurations instead.
        
        @param request: DescribeScalingConfigurationsRequest
        @return: DescribeScalingConfigurationsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_configurations_with_options_async(request, runtime)

    def describe_scaling_groups_with_options(
        self,
        request: ess_20160722_models.DescribeScalingGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingGroupsResponse:
        """
        @deprecated OpenAPI DescribeScalingGroups is deprecated, please use Ess::2022-02-22::DescribeScalingGroups,Ess::2014-08-28::DescribeScalingGroups instead.
        
        @param request: DescribeScalingGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingGroupsResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroups',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_groups_with_options_async(
        self,
        request: ess_20160722_models.DescribeScalingGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingGroupsResponse:
        """
        @deprecated OpenAPI DescribeScalingGroups is deprecated, please use Ess::2022-02-22::DescribeScalingGroups,Ess::2014-08-28::DescribeScalingGroups instead.
        
        @param request: DescribeScalingGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingGroupsResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroups',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_groups(
        self,
        request: ess_20160722_models.DescribeScalingGroupsRequest,
    ) -> ess_20160722_models.DescribeScalingGroupsResponse:
        """
        @deprecated OpenAPI DescribeScalingGroups is deprecated, please use Ess::2022-02-22::DescribeScalingGroups,Ess::2014-08-28::DescribeScalingGroups instead.
        
        @param request: DescribeScalingGroupsRequest
        @return: DescribeScalingGroupsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_groups_with_options(request, runtime)

    async def describe_scaling_groups_async(
        self,
        request: ess_20160722_models.DescribeScalingGroupsRequest,
    ) -> ess_20160722_models.DescribeScalingGroupsResponse:
        """
        @deprecated OpenAPI DescribeScalingGroups is deprecated, please use Ess::2022-02-22::DescribeScalingGroups,Ess::2014-08-28::DescribeScalingGroups instead.
        
        @param request: DescribeScalingGroupsRequest
        @return: DescribeScalingGroupsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_groups_with_options_async(request, runtime)

    def describe_scaling_instances_with_options(
        self,
        request: ess_20160722_models.DescribeScalingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingInstancesResponse:
        """
        @deprecated OpenAPI DescribeScalingInstances is deprecated, please use Ess::2022-02-22::DescribeScalingInstances,Ess::2014-08-28::DescribeScalingInstances instead.
        
        @param request: DescribeScalingInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_type):
            query['CreationType'] = request.creation_type
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.lifecycle_state):
            query['LifecycleState'] = request.lifecycle_state
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingInstances',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_instances_with_options_async(
        self,
        request: ess_20160722_models.DescribeScalingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingInstancesResponse:
        """
        @deprecated OpenAPI DescribeScalingInstances is deprecated, please use Ess::2022-02-22::DescribeScalingInstances,Ess::2014-08-28::DescribeScalingInstances instead.
        
        @param request: DescribeScalingInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_type):
            query['CreationType'] = request.creation_type
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.lifecycle_state):
            query['LifecycleState'] = request.lifecycle_state
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingInstances',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_instances(
        self,
        request: ess_20160722_models.DescribeScalingInstancesRequest,
    ) -> ess_20160722_models.DescribeScalingInstancesResponse:
        """
        @deprecated OpenAPI DescribeScalingInstances is deprecated, please use Ess::2022-02-22::DescribeScalingInstances,Ess::2014-08-28::DescribeScalingInstances instead.
        
        @param request: DescribeScalingInstancesRequest
        @return: DescribeScalingInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_instances_with_options(request, runtime)

    async def describe_scaling_instances_async(
        self,
        request: ess_20160722_models.DescribeScalingInstancesRequest,
    ) -> ess_20160722_models.DescribeScalingInstancesResponse:
        """
        @deprecated OpenAPI DescribeScalingInstances is deprecated, please use Ess::2022-02-22::DescribeScalingInstances,Ess::2014-08-28::DescribeScalingInstances instead.
        
        @param request: DescribeScalingInstancesRequest
        @return: DescribeScalingInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_instances_with_options_async(request, runtime)

    def describe_scaling_rules_with_options(
        self,
        request: ess_20160722_models.DescribeScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingRulesResponse:
        """
        @deprecated OpenAPI DescribeScalingRules is deprecated, please use Ess::2022-02-22::DescribeScalingRules,Ess::2014-08-28::DescribeScalingRules instead.
        
        @param request: DescribeScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingRulesResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingRules',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_rules_with_options_async(
        self,
        request: ess_20160722_models.DescribeScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScalingRulesResponse:
        """
        @deprecated OpenAPI DescribeScalingRules is deprecated, please use Ess::2022-02-22::DescribeScalingRules,Ess::2014-08-28::DescribeScalingRules instead.
        
        @param request: DescribeScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingRulesResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingRules',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_rules(
        self,
        request: ess_20160722_models.DescribeScalingRulesRequest,
    ) -> ess_20160722_models.DescribeScalingRulesResponse:
        """
        @deprecated OpenAPI DescribeScalingRules is deprecated, please use Ess::2022-02-22::DescribeScalingRules,Ess::2014-08-28::DescribeScalingRules instead.
        
        @param request: DescribeScalingRulesRequest
        @return: DescribeScalingRulesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_rules_with_options(request, runtime)

    async def describe_scaling_rules_async(
        self,
        request: ess_20160722_models.DescribeScalingRulesRequest,
    ) -> ess_20160722_models.DescribeScalingRulesResponse:
        """
        @deprecated OpenAPI DescribeScalingRules is deprecated, please use Ess::2022-02-22::DescribeScalingRules,Ess::2014-08-28::DescribeScalingRules instead.
        
        @param request: DescribeScalingRulesRequest
        @return: DescribeScalingRulesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_rules_with_options_async(request, runtime)

    def describe_scheduled_tasks_with_options(
        self,
        request: ess_20160722_models.DescribeScheduledTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScheduledTasksResponse:
        """
        @deprecated OpenAPI DescribeScheduledTasks is deprecated, please use Ess::2022-02-22::DescribeScheduledTasks,Ess::2014-08-28::DescribeScheduledTasks instead.
        
        @param request: DescribeScheduledTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduledTasksResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduledTasks',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scheduled_tasks_with_options_async(
        self,
        request: ess_20160722_models.DescribeScheduledTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DescribeScheduledTasksResponse:
        """
        @deprecated OpenAPI DescribeScheduledTasks is deprecated, please use Ess::2022-02-22::DescribeScheduledTasks,Ess::2014-08-28::DescribeScheduledTasks instead.
        
        @param request: DescribeScheduledTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduledTasksResponse
        Deprecated
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduledTasks',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DescribeScheduledTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scheduled_tasks(
        self,
        request: ess_20160722_models.DescribeScheduledTasksRequest,
    ) -> ess_20160722_models.DescribeScheduledTasksResponse:
        """
        @deprecated OpenAPI DescribeScheduledTasks is deprecated, please use Ess::2022-02-22::DescribeScheduledTasks,Ess::2014-08-28::DescribeScheduledTasks instead.
        
        @param request: DescribeScheduledTasksRequest
        @return: DescribeScheduledTasksResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduled_tasks_with_options(request, runtime)

    async def describe_scheduled_tasks_async(
        self,
        request: ess_20160722_models.DescribeScheduledTasksRequest,
    ) -> ess_20160722_models.DescribeScheduledTasksResponse:
        """
        @deprecated OpenAPI DescribeScheduledTasks is deprecated, please use Ess::2022-02-22::DescribeScheduledTasks,Ess::2014-08-28::DescribeScheduledTasks instead.
        
        @param request: DescribeScheduledTasksRequest
        @return: DescribeScheduledTasksResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scheduled_tasks_with_options_async(request, runtime)

    def detach_instances_with_options(
        self,
        request: ess_20160722_models.DetachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DetachInstancesResponse:
        """
        @deprecated OpenAPI DetachInstances is deprecated, please use Ess::2022-02-22::DetachInstances,Ess::2014-08-28::DetachInstances instead.
        
        @param request: DetachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachInstances',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DetachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_instances_with_options_async(
        self,
        request: ess_20160722_models.DetachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DetachInstancesResponse:
        """
        @deprecated OpenAPI DetachInstances is deprecated, please use Ess::2022-02-22::DetachInstances,Ess::2014-08-28::DetachInstances instead.
        
        @param request: DetachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachInstances',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DetachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_instances(
        self,
        request: ess_20160722_models.DetachInstancesRequest,
    ) -> ess_20160722_models.DetachInstancesResponse:
        """
        @deprecated OpenAPI DetachInstances is deprecated, please use Ess::2022-02-22::DetachInstances,Ess::2014-08-28::DetachInstances instead.
        
        @param request: DetachInstancesRequest
        @return: DetachInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_instances_with_options(request, runtime)

    async def detach_instances_async(
        self,
        request: ess_20160722_models.DetachInstancesRequest,
    ) -> ess_20160722_models.DetachInstancesResponse:
        """
        @deprecated OpenAPI DetachInstances is deprecated, please use Ess::2022-02-22::DetachInstances,Ess::2014-08-28::DetachInstances instead.
        
        @param request: DetachInstancesRequest
        @return: DetachInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_instances_with_options_async(request, runtime)

    def disable_scaling_group_with_options(
        self,
        request: ess_20160722_models.DisableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DisableScalingGroupResponse:
        """
        @deprecated OpenAPI DisableScalingGroup is deprecated, please use Ess::2022-02-22::DisableScalingGroup,Ess::2014-08-28::DisableScalingGroup instead.
        
        @param request: DisableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DisableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_scaling_group_with_options_async(
        self,
        request: ess_20160722_models.DisableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.DisableScalingGroupResponse:
        """
        @deprecated OpenAPI DisableScalingGroup is deprecated, please use Ess::2022-02-22::DisableScalingGroup,Ess::2014-08-28::DisableScalingGroup instead.
        
        @param request: DisableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.DisableScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_scaling_group(
        self,
        request: ess_20160722_models.DisableScalingGroupRequest,
    ) -> ess_20160722_models.DisableScalingGroupResponse:
        """
        @deprecated OpenAPI DisableScalingGroup is deprecated, please use Ess::2022-02-22::DisableScalingGroup,Ess::2014-08-28::DisableScalingGroup instead.
        
        @param request: DisableScalingGroupRequest
        @return: DisableScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_scaling_group_with_options(request, runtime)

    async def disable_scaling_group_async(
        self,
        request: ess_20160722_models.DisableScalingGroupRequest,
    ) -> ess_20160722_models.DisableScalingGroupResponse:
        """
        @deprecated OpenAPI DisableScalingGroup is deprecated, please use Ess::2022-02-22::DisableScalingGroup,Ess::2014-08-28::DisableScalingGroup instead.
        
        @param request: DisableScalingGroupRequest
        @return: DisableScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_scaling_group_with_options_async(request, runtime)

    def enable_scaling_group_with_options(
        self,
        request: ess_20160722_models.EnableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.EnableScalingGroupResponse:
        """
        @deprecated OpenAPI EnableScalingGroup is deprecated, please use Ess::2014-08-28::EnableScalingGroup,Ess::2022-02-22::EnableScalingGroup instead.
        
        @param request: EnableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.EnableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_scaling_group_with_options_async(
        self,
        request: ess_20160722_models.EnableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.EnableScalingGroupResponse:
        """
        @deprecated OpenAPI EnableScalingGroup is deprecated, please use Ess::2014-08-28::EnableScalingGroup,Ess::2022-02-22::EnableScalingGroup instead.
        
        @param request: EnableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.EnableScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_scaling_group(
        self,
        request: ess_20160722_models.EnableScalingGroupRequest,
    ) -> ess_20160722_models.EnableScalingGroupResponse:
        """
        @deprecated OpenAPI EnableScalingGroup is deprecated, please use Ess::2014-08-28::EnableScalingGroup,Ess::2022-02-22::EnableScalingGroup instead.
        
        @param request: EnableScalingGroupRequest
        @return: EnableScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_scaling_group_with_options(request, runtime)

    async def enable_scaling_group_async(
        self,
        request: ess_20160722_models.EnableScalingGroupRequest,
    ) -> ess_20160722_models.EnableScalingGroupResponse:
        """
        @deprecated OpenAPI EnableScalingGroup is deprecated, please use Ess::2014-08-28::EnableScalingGroup,Ess::2022-02-22::EnableScalingGroup instead.
        
        @param request: EnableScalingGroupRequest
        @return: EnableScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_scaling_group_with_options_async(request, runtime)

    def execute_scaling_rule_with_options(
        self,
        request: ess_20160722_models.ExecuteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.ExecuteScalingRuleResponse:
        """
        @deprecated OpenAPI ExecuteScalingRule is deprecated, please use Ess::2014-08-28::ExecuteScalingRule,Ess::2022-02-22::ExecuteScalingRule instead.
        
        @param request: ExecuteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteScalingRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScalingRule',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.ExecuteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_scaling_rule_with_options_async(
        self,
        request: ess_20160722_models.ExecuteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.ExecuteScalingRuleResponse:
        """
        @deprecated OpenAPI ExecuteScalingRule is deprecated, please use Ess::2014-08-28::ExecuteScalingRule,Ess::2022-02-22::ExecuteScalingRule instead.
        
        @param request: ExecuteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteScalingRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScalingRule',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.ExecuteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_scaling_rule(
        self,
        request: ess_20160722_models.ExecuteScalingRuleRequest,
    ) -> ess_20160722_models.ExecuteScalingRuleResponse:
        """
        @deprecated OpenAPI ExecuteScalingRule is deprecated, please use Ess::2014-08-28::ExecuteScalingRule,Ess::2022-02-22::ExecuteScalingRule instead.
        
        @param request: ExecuteScalingRuleRequest
        @return: ExecuteScalingRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_scaling_rule_with_options(request, runtime)

    async def execute_scaling_rule_async(
        self,
        request: ess_20160722_models.ExecuteScalingRuleRequest,
    ) -> ess_20160722_models.ExecuteScalingRuleResponse:
        """
        @deprecated OpenAPI ExecuteScalingRule is deprecated, please use Ess::2014-08-28::ExecuteScalingRule,Ess::2022-02-22::ExecuteScalingRule instead.
        
        @param request: ExecuteScalingRuleRequest
        @return: ExecuteScalingRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_scaling_rule_with_options_async(request, runtime)

    def modify_scaling_group_with_options(
        self,
        request: ess_20160722_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.ModifyScalingGroupResponse:
        """
        @deprecated OpenAPI ModifyScalingGroup is deprecated, please use Ess::2014-08-28::ModifyScalingGroup,Ess::2022-02-22::ModifyScalingGroup instead.
        
        @param request: ModifyScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.removal_policy):
            query['RemovalPolicy'] = request.removal_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.ModifyScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_group_with_options_async(
        self,
        request: ess_20160722_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.ModifyScalingGroupResponse:
        """
        @deprecated OpenAPI ModifyScalingGroup is deprecated, please use Ess::2014-08-28::ModifyScalingGroup,Ess::2022-02-22::ModifyScalingGroup instead.
        
        @param request: ModifyScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.removal_policy):
            query['RemovalPolicy'] = request.removal_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroup',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.ModifyScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_group(
        self,
        request: ess_20160722_models.ModifyScalingGroupRequest,
    ) -> ess_20160722_models.ModifyScalingGroupResponse:
        """
        @deprecated OpenAPI ModifyScalingGroup is deprecated, please use Ess::2014-08-28::ModifyScalingGroup,Ess::2022-02-22::ModifyScalingGroup instead.
        
        @param request: ModifyScalingGroupRequest
        @return: ModifyScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    async def modify_scaling_group_async(
        self,
        request: ess_20160722_models.ModifyScalingGroupRequest,
    ) -> ess_20160722_models.ModifyScalingGroupResponse:
        """
        @deprecated OpenAPI ModifyScalingGroup is deprecated, please use Ess::2014-08-28::ModifyScalingGroup,Ess::2022-02-22::ModifyScalingGroup instead.
        
        @param request: ModifyScalingGroupRequest
        @return: ModifyScalingGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_group_with_options_async(request, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: ess_20160722_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.ModifyScalingRuleResponse:
        """
        @deprecated OpenAPI ModifyScalingRule is deprecated, please use Ess::2014-08-28::ModifyScalingRule,Ess::2022-02-22::ModifyScalingRule instead.
        
        @param request: ModifyScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: ess_20160722_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.ModifyScalingRuleResponse:
        """
        @deprecated OpenAPI ModifyScalingRule is deprecated, please use Ess::2014-08-28::ModifyScalingRule,Ess::2022-02-22::ModifyScalingRule instead.
        
        @param request: ModifyScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.ModifyScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: ess_20160722_models.ModifyScalingRuleRequest,
    ) -> ess_20160722_models.ModifyScalingRuleResponse:
        """
        @deprecated OpenAPI ModifyScalingRule is deprecated, please use Ess::2014-08-28::ModifyScalingRule,Ess::2022-02-22::ModifyScalingRule instead.
        
        @param request: ModifyScalingRuleRequest
        @return: ModifyScalingRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_rule_with_options(request, runtime)

    async def modify_scaling_rule_async(
        self,
        request: ess_20160722_models.ModifyScalingRuleRequest,
    ) -> ess_20160722_models.ModifyScalingRuleResponse:
        """
        @deprecated OpenAPI ModifyScalingRule is deprecated, please use Ess::2014-08-28::ModifyScalingRule,Ess::2022-02-22::ModifyScalingRule instead.
        
        @param request: ModifyScalingRuleRequest
        @return: ModifyScalingRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_rule_with_options_async(request, runtime)

    def modify_scheduled_task_with_options(
        self,
        request: ess_20160722_models.ModifyScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.ModifyScheduledTaskResponse:
        """
        @deprecated OpenAPI ModifyScheduledTask is deprecated, please use Ess::2014-08-28::ModifyScheduledTask,Ess::2022-02-22::ModifyScheduledTask instead.
        
        @param request: ModifyScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledTaskResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScheduledTask',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        request: ess_20160722_models.ModifyScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.ModifyScheduledTaskResponse:
        """
        @deprecated OpenAPI ModifyScheduledTask is deprecated, please use Ess::2014-08-28::ModifyScheduledTask,Ess::2022-02-22::ModifyScheduledTask instead.
        
        @param request: ModifyScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledTaskResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScheduledTask',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.ModifyScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_task(
        self,
        request: ess_20160722_models.ModifyScheduledTaskRequest,
    ) -> ess_20160722_models.ModifyScheduledTaskResponse:
        """
        @deprecated OpenAPI ModifyScheduledTask is deprecated, please use Ess::2014-08-28::ModifyScheduledTask,Ess::2022-02-22::ModifyScheduledTask instead.
        
        @param request: ModifyScheduledTaskRequest
        @return: ModifyScheduledTaskResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduled_task_with_options(request, runtime)

    async def modify_scheduled_task_async(
        self,
        request: ess_20160722_models.ModifyScheduledTaskRequest,
    ) -> ess_20160722_models.ModifyScheduledTaskResponse:
        """
        @deprecated OpenAPI ModifyScheduledTask is deprecated, please use Ess::2014-08-28::ModifyScheduledTask,Ess::2022-02-22::ModifyScheduledTask instead.
        
        @param request: ModifyScheduledTaskRequest
        @return: ModifyScheduledTaskResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scheduled_task_with_options_async(request, runtime)

    def remove_instances_with_options(
        self,
        request: ess_20160722_models.RemoveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.RemoveInstancesResponse:
        """
        @deprecated OpenAPI RemoveInstances is deprecated, please use Ess::2014-08-28::RemoveInstances,Ess::2022-02-22::RemoveInstances instead.
        
        @param request: RemoveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstances',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.RemoveInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_instances_with_options_async(
        self,
        request: ess_20160722_models.RemoveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.RemoveInstancesResponse:
        """
        @deprecated OpenAPI RemoveInstances is deprecated, please use Ess::2014-08-28::RemoveInstances,Ess::2022-02-22::RemoveInstances instead.
        
        @param request: RemoveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstances',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.RemoveInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_instances(
        self,
        request: ess_20160722_models.RemoveInstancesRequest,
    ) -> ess_20160722_models.RemoveInstancesResponse:
        """
        @deprecated OpenAPI RemoveInstances is deprecated, please use Ess::2014-08-28::RemoveInstances,Ess::2022-02-22::RemoveInstances instead.
        
        @param request: RemoveInstancesRequest
        @return: RemoveInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_instances_with_options(request, runtime)

    async def remove_instances_async(
        self,
        request: ess_20160722_models.RemoveInstancesRequest,
    ) -> ess_20160722_models.RemoveInstancesResponse:
        """
        @deprecated OpenAPI RemoveInstances is deprecated, please use Ess::2014-08-28::RemoveInstances,Ess::2022-02-22::RemoveInstances instead.
        
        @param request: RemoveInstancesRequest
        @return: RemoveInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_instances_with_options_async(request, runtime)

    def verify_authentication_with_options(
        self,
        request: ess_20160722_models.VerifyAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.VerifyAuthenticationResponse:
        """
        @deprecated OpenAPI VerifyAuthentication is deprecated, please use Ess::2014-08-28::VerifyAuthentication instead.
        
        @param request: VerifyAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyAuthenticationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyAuthentication',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.VerifyAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_authentication_with_options_async(
        self,
        request: ess_20160722_models.VerifyAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.VerifyAuthenticationResponse:
        """
        @deprecated OpenAPI VerifyAuthentication is deprecated, please use Ess::2014-08-28::VerifyAuthentication instead.
        
        @param request: VerifyAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyAuthenticationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyAuthentication',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20160722_models.VerifyAuthenticationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_authentication(
        self,
        request: ess_20160722_models.VerifyAuthenticationRequest,
    ) -> ess_20160722_models.VerifyAuthenticationResponse:
        """
        @deprecated OpenAPI VerifyAuthentication is deprecated, please use Ess::2014-08-28::VerifyAuthentication instead.
        
        @param request: VerifyAuthenticationRequest
        @return: VerifyAuthenticationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_authentication_with_options(request, runtime)

    async def verify_authentication_async(
        self,
        request: ess_20160722_models.VerifyAuthenticationRequest,
    ) -> ess_20160722_models.VerifyAuthenticationResponse:
        """
        @deprecated OpenAPI VerifyAuthentication is deprecated, please use Ess::2014-08-28::VerifyAuthentication instead.
        
        @param request: VerifyAuthenticationRequest
        @return: VerifyAuthenticationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_authentication_with_options_async(request, runtime)

    def verify_user_with_options(
        self,
        request: ess_20160722_models.VerifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.VerifyUserResponse:
        """
        @deprecated OpenAPI VerifyUser is deprecated, please use Ess::2014-08-28::VerifyUser instead.
        
        @param request: VerifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyUserResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyUser',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            ess_20160722_models.VerifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_user_with_options_async(
        self,
        request: ess_20160722_models.VerifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20160722_models.VerifyUserResponse:
        """
        @deprecated OpenAPI VerifyUser is deprecated, please use Ess::2014-08-28::VerifyUser instead.
        
        @param request: VerifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyUserResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyUser',
            version='2016-07-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            ess_20160722_models.VerifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_user(
        self,
        request: ess_20160722_models.VerifyUserRequest,
    ) -> ess_20160722_models.VerifyUserResponse:
        """
        @deprecated OpenAPI VerifyUser is deprecated, please use Ess::2014-08-28::VerifyUser instead.
        
        @param request: VerifyUserRequest
        @return: VerifyUserResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_user_with_options(request, runtime)

    async def verify_user_async(
        self,
        request: ess_20160722_models.VerifyUserRequest,
    ) -> ess_20160722_models.VerifyUserResponse:
        """
        @deprecated OpenAPI VerifyUser is deprecated, please use Ess::2014-08-28::VerifyUser instead.
        
        @param request: VerifyUserRequest
        @return: VerifyUserResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_user_with_options_async(request, runtime)
