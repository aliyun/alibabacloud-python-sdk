# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ess20220222 import models as ess_20220222_models
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

    def attach_alb_server_groups_with_options(
        self,
        request: ess_20220222_models.AttachAlbServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachAlbServerGroupsResponse:
        """
        Associates one or more Application Load Balancer (ALB) server groups with a scaling group.
        
        @param request: AttachAlbServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachAlbServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachAlbServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_alb_server_groups_with_options_async(
        self,
        request: ess_20220222_models.AttachAlbServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachAlbServerGroupsResponse:
        """
        Associates one or more Application Load Balancer (ALB) server groups with a scaling group.
        
        @param request: AttachAlbServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachAlbServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachAlbServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_alb_server_groups(
        self,
        request: ess_20220222_models.AttachAlbServerGroupsRequest,
    ) -> ess_20220222_models.AttachAlbServerGroupsResponse:
        """
        Associates one or more Application Load Balancer (ALB) server groups with a scaling group.
        
        @param request: AttachAlbServerGroupsRequest
        @return: AttachAlbServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_alb_server_groups_with_options(request, runtime)

    async def attach_alb_server_groups_async(
        self,
        request: ess_20220222_models.AttachAlbServerGroupsRequest,
    ) -> ess_20220222_models.AttachAlbServerGroupsResponse:
        """
        Associates one or more Application Load Balancer (ALB) server groups with a scaling group.
        
        @param request: AttachAlbServerGroupsRequest
        @return: AttachAlbServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_alb_server_groups_with_options_async(request, runtime)

    def attach_dbinstances_with_options(
        self,
        request: ess_20220222_models.AttachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachDBInstancesResponse:
        """
        Associates one or more ApsaraDB RDS instances with a scaling group.
        
        @param request: AttachDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_dbinstances_with_options_async(
        self,
        request: ess_20220222_models.AttachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachDBInstancesResponse:
        """
        Associates one or more ApsaraDB RDS instances with a scaling group.
        
        @param request: AttachDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_dbinstances(
        self,
        request: ess_20220222_models.AttachDBInstancesRequest,
    ) -> ess_20220222_models.AttachDBInstancesResponse:
        """
        Associates one or more ApsaraDB RDS instances with a scaling group.
        
        @param request: AttachDBInstancesRequest
        @return: AttachDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_dbinstances_with_options(request, runtime)

    async def attach_dbinstances_async(
        self,
        request: ess_20220222_models.AttachDBInstancesRequest,
    ) -> ess_20220222_models.AttachDBInstancesResponse:
        """
        Associates one or more ApsaraDB RDS instances with a scaling group.
        
        @param request: AttachDBInstancesRequest
        @return: AttachDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_dbinstances_with_options_async(request, runtime)

    def attach_instances_with_options(
        self,
        request: ess_20220222_models.AttachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachInstancesResponse:
        """
        Manually adds Elastic Compute Service (ECS) instances or elastic container instances to a scaling group.
        
        @param request: AttachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_instances_with_options_async(
        self,
        request: ess_20220222_models.AttachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachInstancesResponse:
        """
        Manually adds Elastic Compute Service (ECS) instances or elastic container instances to a scaling group.
        
        @param request: AttachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_instances(
        self,
        request: ess_20220222_models.AttachInstancesRequest,
    ) -> ess_20220222_models.AttachInstancesResponse:
        """
        Manually adds Elastic Compute Service (ECS) instances or elastic container instances to a scaling group.
        
        @param request: AttachInstancesRequest
        @return: AttachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_instances_with_options(request, runtime)

    async def attach_instances_async(
        self,
        request: ess_20220222_models.AttachInstancesRequest,
    ) -> ess_20220222_models.AttachInstancesResponse:
        """
        Manually adds Elastic Compute Service (ECS) instances or elastic container instances to a scaling group.
        
        @param request: AttachInstancesRequest
        @return: AttachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_instances_with_options_async(request, runtime)

    def attach_load_balancers_with_options(
        self,
        request: ess_20220222_models.AttachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachLoadBalancersResponse:
        """
        Attaches one or more Classic Load Balancer (CLB) instances to a scaling group.
        
        @param request: AttachLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
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
            action='AttachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_load_balancers_with_options_async(
        self,
        request: ess_20220222_models.AttachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachLoadBalancersResponse:
        """
        Attaches one or more Classic Load Balancer (CLB) instances to a scaling group.
        
        @param request: AttachLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
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
            action='AttachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_load_balancers(
        self,
        request: ess_20220222_models.AttachLoadBalancersRequest,
    ) -> ess_20220222_models.AttachLoadBalancersResponse:
        """
        Attaches one or more Classic Load Balancer (CLB) instances to a scaling group.
        
        @param request: AttachLoadBalancersRequest
        @return: AttachLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_load_balancers_with_options(request, runtime)

    async def attach_load_balancers_async(
        self,
        request: ess_20220222_models.AttachLoadBalancersRequest,
    ) -> ess_20220222_models.AttachLoadBalancersResponse:
        """
        Attaches one or more Classic Load Balancer (CLB) instances to a scaling group.
        
        @param request: AttachLoadBalancersRequest
        @return: AttachLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_load_balancers_with_options_async(request, runtime)

    def attach_server_groups_with_options(
        self,
        request: ess_20220222_models.AttachServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_server_groups_with_options_async(
        self,
        request: ess_20220222_models.AttachServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_server_groups(
        self,
        request: ess_20220222_models.AttachServerGroupsRequest,
    ) -> ess_20220222_models.AttachServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_server_groups_with_options(request, runtime)

    async def attach_server_groups_async(
        self,
        request: ess_20220222_models.AttachServerGroupsRequest,
    ) -> ess_20220222_models.AttachServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_server_groups_with_options_async(request, runtime)

    def attach_vserver_groups_with_options(
        self,
        request: ess_20220222_models.AttachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachVServerGroupsResponse:
        """
        Attaches one or more vServer groups of a Classic Load Balancer (CLB) instance to a scaling group.
        
        @param request: AttachVServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_vserver_groups_with_options_async(
        self,
        request: ess_20220222_models.AttachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachVServerGroupsResponse:
        """
        Attaches one or more vServer groups of a Classic Load Balancer (CLB) instance to a scaling group.
        
        @param request: AttachVServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachVServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_vserver_groups(
        self,
        request: ess_20220222_models.AttachVServerGroupsRequest,
    ) -> ess_20220222_models.AttachVServerGroupsResponse:
        """
        Attaches one or more vServer groups of a Classic Load Balancer (CLB) instance to a scaling group.
        
        @param request: AttachVServerGroupsRequest
        @return: AttachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_vserver_groups_with_options(request, runtime)

    async def attach_vserver_groups_async(
        self,
        request: ess_20220222_models.AttachVServerGroupsRequest,
    ) -> ess_20220222_models.AttachVServerGroupsResponse:
        """
        Attaches one or more vServer groups of a Classic Load Balancer (CLB) instance to a scaling group.
        
        @param request: AttachVServerGroupsRequest
        @return: AttachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_vserver_groups_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: ess_20220222_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ChangeResourceGroupResponse:
        """
        A resource is an entity of cloud services that you create on Alibaba Cloud. For example, a scaling group is a resource. A resource group is a collection of infrastructure for projects, environments, or stacks. In a resource group, you can manage resources, monitor resources, and perform operations in a centralized manner. This way, you do not need to view and check your Alibaba Cloud resources in each Alibaba Cloud service.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: ess_20220222_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ChangeResourceGroupResponse:
        """
        A resource is an entity of cloud services that you create on Alibaba Cloud. For example, a scaling group is a resource. A resource group is a collection of infrastructure for projects, environments, or stacks. In a resource group, you can manage resources, monitor resources, and perform operations in a centralized manner. This way, you do not need to view and check your Alibaba Cloud resources in each Alibaba Cloud service.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: ess_20220222_models.ChangeResourceGroupRequest,
    ) -> ess_20220222_models.ChangeResourceGroupResponse:
        """
        A resource is an entity of cloud services that you create on Alibaba Cloud. For example, a scaling group is a resource. A resource group is a collection of infrastructure for projects, environments, or stacks. In a resource group, you can manage resources, monitor resources, and perform operations in a centralized manner. This way, you do not need to view and check your Alibaba Cloud resources in each Alibaba Cloud service.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: ess_20220222_models.ChangeResourceGroupRequest,
    ) -> ess_20220222_models.ChangeResourceGroupResponse:
        """
        A resource is an entity of cloud services that you create on Alibaba Cloud. For example, a scaling group is a resource. A resource group is a collection of infrastructure for projects, environments, or stacks. In a resource group, you can manage resources, monitor resources, and perform operations in a centralized manner. This way, you do not need to view and check your Alibaba Cloud resources in each Alibaba Cloud service.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def complete_lifecycle_action_with_options(
        self,
        request: ess_20220222_models.CompleteLifecycleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CompleteLifecycleActionResponse:
        """
        When you call this operation to end a lifecycle hook ahead of schedule, you can use the LifecycleActionResult parameter to specify the action that you want Auto Scaling to perform after the lifecycle hook ends. You can set the LifecycleActionResult parameter to CONTINUE or ABANDON.
        
        @param request: CompleteLifecycleActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompleteLifecycleActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lifecycle_action_result):
            query['LifecycleActionResult'] = request.lifecycle_action_result
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['LifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteLifecycleAction',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CompleteLifecycleActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_lifecycle_action_with_options_async(
        self,
        request: ess_20220222_models.CompleteLifecycleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CompleteLifecycleActionResponse:
        """
        When you call this operation to end a lifecycle hook ahead of schedule, you can use the LifecycleActionResult parameter to specify the action that you want Auto Scaling to perform after the lifecycle hook ends. You can set the LifecycleActionResult parameter to CONTINUE or ABANDON.
        
        @param request: CompleteLifecycleActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompleteLifecycleActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lifecycle_action_result):
            query['LifecycleActionResult'] = request.lifecycle_action_result
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['LifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteLifecycleAction',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CompleteLifecycleActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_lifecycle_action(
        self,
        request: ess_20220222_models.CompleteLifecycleActionRequest,
    ) -> ess_20220222_models.CompleteLifecycleActionResponse:
        """
        When you call this operation to end a lifecycle hook ahead of schedule, you can use the LifecycleActionResult parameter to specify the action that you want Auto Scaling to perform after the lifecycle hook ends. You can set the LifecycleActionResult parameter to CONTINUE or ABANDON.
        
        @param request: CompleteLifecycleActionRequest
        @return: CompleteLifecycleActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.complete_lifecycle_action_with_options(request, runtime)

    async def complete_lifecycle_action_async(
        self,
        request: ess_20220222_models.CompleteLifecycleActionRequest,
    ) -> ess_20220222_models.CompleteLifecycleActionResponse:
        """
        When you call this operation to end a lifecycle hook ahead of schedule, you can use the LifecycleActionResult parameter to specify the action that you want Auto Scaling to perform after the lifecycle hook ends. You can set the LifecycleActionResult parameter to CONTINUE or ABANDON.
        
        @param request: CompleteLifecycleActionRequest
        @return: CompleteLifecycleActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.complete_lifecycle_action_with_options_async(request, runtime)

    def create_alarm_with_options(
        self,
        request: ess_20220222_models.CreateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateAlarmResponse:
        """
        If you set the MetricType parameter to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using custom metrics. For more information, see [Custom monitoring event-triggered tasks](~~74861~~).
        *   When you create an event-triggered task, you must specify the MetricName, DimensionKey, and DimensionValue parameters to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        *   If you set the MetricType parameter to custom, the valid values are your custom metrics.
        *   For information about the supported metrics when you set the MetricType parameter to system, see [Event-triggered task for system monitoring](~~74854~~).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see the `DimensionKey` and `DimensionValue` parameters in the "Request parameters" section of this topic.
        
        @param request: CreateAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alarm_with_options_async(
        self,
        request: ess_20220222_models.CreateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateAlarmResponse:
        """
        If you set the MetricType parameter to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using custom metrics. For more information, see [Custom monitoring event-triggered tasks](~~74861~~).
        *   When you create an event-triggered task, you must specify the MetricName, DimensionKey, and DimensionValue parameters to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        *   If you set the MetricType parameter to custom, the valid values are your custom metrics.
        *   For information about the supported metrics when you set the MetricType parameter to system, see [Event-triggered task for system monitoring](~~74854~~).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see the `DimensionKey` and `DimensionValue` parameters in the "Request parameters" section of this topic.
        
        @param request: CreateAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alarm(
        self,
        request: ess_20220222_models.CreateAlarmRequest,
    ) -> ess_20220222_models.CreateAlarmResponse:
        """
        If you set the MetricType parameter to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using custom metrics. For more information, see [Custom monitoring event-triggered tasks](~~74861~~).
        *   When you create an event-triggered task, you must specify the MetricName, DimensionKey, and DimensionValue parameters to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        *   If you set the MetricType parameter to custom, the valid values are your custom metrics.
        *   For information about the supported metrics when you set the MetricType parameter to system, see [Event-triggered task for system monitoring](~~74854~~).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see the `DimensionKey` and `DimensionValue` parameters in the "Request parameters" section of this topic.
        
        @param request: CreateAlarmRequest
        @return: CreateAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_with_options(request, runtime)

    async def create_alarm_async(
        self,
        request: ess_20220222_models.CreateAlarmRequest,
    ) -> ess_20220222_models.CreateAlarmResponse:
        """
        If you set the MetricType parameter to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using custom metrics. For more information, see [Custom monitoring event-triggered tasks](~~74861~~).
        *   When you create an event-triggered task, you must specify the MetricName, DimensionKey, and DimensionValue parameters to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        *   If you set the MetricType parameter to custom, the valid values are your custom metrics.
        *   For information about the supported metrics when you set the MetricType parameter to system, see [Event-triggered task for system monitoring](~~74854~~).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see the `DimensionKey` and `DimensionValue` parameters in the "Request parameters" section of this topic.
        
        @param request: CreateAlarmRequest
        @return: CreateAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_alarm_with_options_async(request, runtime)

    def create_eci_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.CreateEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateEciScalingConfigurationResponse:
        """
        A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        
        @param request: CreateEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.security_context_sysctls):
            query['SecurityContextSysctls'] = request.security_context_sysctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eci_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.CreateEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateEciScalingConfigurationResponse:
        """
        A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        
        @param request: CreateEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.security_context_sysctls):
            query['SecurityContextSysctls'] = request.security_context_sysctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eci_scaling_configuration(
        self,
        request: ess_20220222_models.CreateEciScalingConfigurationRequest,
    ) -> ess_20220222_models.CreateEciScalingConfigurationResponse:
        """
        A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        
        @param request: CreateEciScalingConfigurationRequest
        @return: CreateEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eci_scaling_configuration_with_options(request, runtime)

    async def create_eci_scaling_configuration_async(
        self,
        request: ess_20220222_models.CreateEciScalingConfigurationRequest,
    ) -> ess_20220222_models.CreateEciScalingConfigurationResponse:
        """
        A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        
        @param request: CreateEciScalingConfigurationRequest
        @return: CreateEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_eci_scaling_configuration_with_options_async(request, runtime)

    def create_lifecycle_hook_with_options(
        self,
        request: ess_20220222_models.CreateLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateLifecycleHookResponse:
        """
        You can create up to six lifecycle hooks for each scaling group. After a lifecycle hook is created for a scaling group, Elastic Compute Service (ECS) instances in the scaling group waits to be added to or removed from the scaling group during scaling activities. You can use the HeartbeatTimeout parameter to specify the timeout period of the lifecycle hook. During the timeout period of a lifecycle hook, you can perform custom operations such as initialize ECS instance configurations and download ECS instance data on the ECS instances for which the lifecycle hook is applied.
        During a scale-out activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be added to the associated whitelist that manages access to the ApsaraDB RDS instance. The ECS instances also wait to be added to the backend server group of the associated Classic Load Balancer (CLB) instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are added to the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also added to the backend server group of the associated CLB instance. During a scale-in activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances also wait to be removed from the backend server group of the associated CLB instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also removed from the backend server group of the associated CLB instance.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook is triggered, a notification can be sent to the specified Message Service (MNS) topic or queue, or an operation can be performed based on the specified Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a Resource Access Management (RAM) role for OOS. For more information, see [Grant RAM permissions to OOS](~~120810~~).
        > If your scaling group has existing ECS instances and you configured an OOS template that is used to add the private IP addresses of ECS instances to or remove the private IP addresses of ECS instances from the whitelists that manage access to cloud databases that are not ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the whitelists that manage access to the cloud databases.
        
        @param request: CreateLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
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
            action='CreateLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_hook_with_options_async(
        self,
        request: ess_20220222_models.CreateLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateLifecycleHookResponse:
        """
        You can create up to six lifecycle hooks for each scaling group. After a lifecycle hook is created for a scaling group, Elastic Compute Service (ECS) instances in the scaling group waits to be added to or removed from the scaling group during scaling activities. You can use the HeartbeatTimeout parameter to specify the timeout period of the lifecycle hook. During the timeout period of a lifecycle hook, you can perform custom operations such as initialize ECS instance configurations and download ECS instance data on the ECS instances for which the lifecycle hook is applied.
        During a scale-out activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be added to the associated whitelist that manages access to the ApsaraDB RDS instance. The ECS instances also wait to be added to the backend server group of the associated Classic Load Balancer (CLB) instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are added to the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also added to the backend server group of the associated CLB instance. During a scale-in activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances also wait to be removed from the backend server group of the associated CLB instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also removed from the backend server group of the associated CLB instance.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook is triggered, a notification can be sent to the specified Message Service (MNS) topic or queue, or an operation can be performed based on the specified Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a Resource Access Management (RAM) role for OOS. For more information, see [Grant RAM permissions to OOS](~~120810~~).
        > If your scaling group has existing ECS instances and you configured an OOS template that is used to add the private IP addresses of ECS instances to or remove the private IP addresses of ECS instances from the whitelists that manage access to cloud databases that are not ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the whitelists that manage access to the cloud databases.
        
        @param request: CreateLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
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
            action='CreateLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lifecycle_hook(
        self,
        request: ess_20220222_models.CreateLifecycleHookRequest,
    ) -> ess_20220222_models.CreateLifecycleHookResponse:
        """
        You can create up to six lifecycle hooks for each scaling group. After a lifecycle hook is created for a scaling group, Elastic Compute Service (ECS) instances in the scaling group waits to be added to or removed from the scaling group during scaling activities. You can use the HeartbeatTimeout parameter to specify the timeout period of the lifecycle hook. During the timeout period of a lifecycle hook, you can perform custom operations such as initialize ECS instance configurations and download ECS instance data on the ECS instances for which the lifecycle hook is applied.
        During a scale-out activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be added to the associated whitelist that manages access to the ApsaraDB RDS instance. The ECS instances also wait to be added to the backend server group of the associated Classic Load Balancer (CLB) instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are added to the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also added to the backend server group of the associated CLB instance. During a scale-in activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances also wait to be removed from the backend server group of the associated CLB instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also removed from the backend server group of the associated CLB instance.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook is triggered, a notification can be sent to the specified Message Service (MNS) topic or queue, or an operation can be performed based on the specified Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a Resource Access Management (RAM) role for OOS. For more information, see [Grant RAM permissions to OOS](~~120810~~).
        > If your scaling group has existing ECS instances and you configured an OOS template that is used to add the private IP addresses of ECS instances to or remove the private IP addresses of ECS instances from the whitelists that manage access to cloud databases that are not ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the whitelists that manage access to the cloud databases.
        
        @param request: CreateLifecycleHookRequest
        @return: CreateLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_hook_with_options(request, runtime)

    async def create_lifecycle_hook_async(
        self,
        request: ess_20220222_models.CreateLifecycleHookRequest,
    ) -> ess_20220222_models.CreateLifecycleHookResponse:
        """
        You can create up to six lifecycle hooks for each scaling group. After a lifecycle hook is created for a scaling group, Elastic Compute Service (ECS) instances in the scaling group waits to be added to or removed from the scaling group during scaling activities. You can use the HeartbeatTimeout parameter to specify the timeout period of the lifecycle hook. During the timeout period of a lifecycle hook, you can perform custom operations such as initialize ECS instance configurations and download ECS instance data on the ECS instances for which the lifecycle hook is applied.
        During a scale-out activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be added to the associated whitelist that manages access to the ApsaraDB RDS instance. The ECS instances also wait to be added to the backend server group of the associated Classic Load Balancer (CLB) instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are added to the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also added to the backend server group of the associated CLB instance. During a scale-in activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances also wait to be removed from the backend server group of the associated CLB instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also removed from the backend server group of the associated CLB instance.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook is triggered, a notification can be sent to the specified Message Service (MNS) topic or queue, or an operation can be performed based on the specified Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a Resource Access Management (RAM) role for OOS. For more information, see [Grant RAM permissions to OOS](~~120810~~).
        > If your scaling group has existing ECS instances and you configured an OOS template that is used to add the private IP addresses of ECS instances to or remove the private IP addresses of ECS instances from the whitelists that manage access to cloud databases that are not ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the whitelists that manage access to the cloud databases.
        
        @param request: CreateLifecycleHookRequest
        @return: CreateLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lifecycle_hook_with_options_async(request, runtime)

    def create_notification_configuration_with_options(
        self,
        request: ess_20220222_models.CreateNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateNotificationConfigurationResponse:
        """
        Creates a notification.
        
        @param request: CreateNotificationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_notification_configuration_with_options_async(
        self,
        request: ess_20220222_models.CreateNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateNotificationConfigurationResponse:
        """
        Creates a notification.
        
        @param request: CreateNotificationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_notification_configuration(
        self,
        request: ess_20220222_models.CreateNotificationConfigurationRequest,
    ) -> ess_20220222_models.CreateNotificationConfigurationResponse:
        """
        Creates a notification.
        
        @param request: CreateNotificationConfigurationRequest
        @return: CreateNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_notification_configuration_with_options(request, runtime)

    async def create_notification_configuration_async(
        self,
        request: ess_20220222_models.CreateNotificationConfigurationRequest,
    ) -> ess_20220222_models.CreateNotificationConfigurationResponse:
        """
        Creates a notification.
        
        @param request: CreateNotificationConfigurationRequest
        @return: CreateNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_notification_configuration_with_options_async(request, runtime)

    def create_scaling_configuration_with_options(
        self,
        tmp_req: ess_20220222_models.CreateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingConfigurationResponse:
        """
        Auto Scaling automatically scales out Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be configured in the following modes:
        *   InstancePatternInfo.N: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. The system selects an instance type that is provided at the lowest price based on your configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode helps reduce the failures of scale-out activities caused by insufficient inventory of instance types.
        *   InstanceType: In this mode, you must specify one instance type.
        *   InstanceTypes.N: In this mode, you must specify multiple instance types.
        *   InstanceTypeOverride.N: In this mode, you must specify multiple instance types and specify weights for the instance types.
        *   Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines a set of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling preferentially creates ECS instances of the instance type that is provided at the lowest price. This mode is available only if the Scaling Policy parameter is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot use InstanceType, InstanceTypes, InstanceTypeOverride, and Cpu and Memory at the same time. You can use InstanceType and InstancePatternInfos or use InstanceTypes and InstancePatternInfos at the same time. If you use InstanceType and InstancePatternInfos or use InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-out activities. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-out activities.
        
        @param tmp_req: CreateScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.CreateScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_configuration_with_options_async(
        self,
        tmp_req: ess_20220222_models.CreateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingConfigurationResponse:
        """
        Auto Scaling automatically scales out Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be configured in the following modes:
        *   InstancePatternInfo.N: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. The system selects an instance type that is provided at the lowest price based on your configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode helps reduce the failures of scale-out activities caused by insufficient inventory of instance types.
        *   InstanceType: In this mode, you must specify one instance type.
        *   InstanceTypes.N: In this mode, you must specify multiple instance types.
        *   InstanceTypeOverride.N: In this mode, you must specify multiple instance types and specify weights for the instance types.
        *   Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines a set of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling preferentially creates ECS instances of the instance type that is provided at the lowest price. This mode is available only if the Scaling Policy parameter is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot use InstanceType, InstanceTypes, InstanceTypeOverride, and Cpu and Memory at the same time. You can use InstanceType and InstancePatternInfos or use InstanceTypes and InstancePatternInfos at the same time. If you use InstanceType and InstancePatternInfos or use InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-out activities. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-out activities.
        
        @param tmp_req: CreateScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.CreateScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_configuration(
        self,
        request: ess_20220222_models.CreateScalingConfigurationRequest,
    ) -> ess_20220222_models.CreateScalingConfigurationResponse:
        """
        Auto Scaling automatically scales out Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be configured in the following modes:
        *   InstancePatternInfo.N: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. The system selects an instance type that is provided at the lowest price based on your configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode helps reduce the failures of scale-out activities caused by insufficient inventory of instance types.
        *   InstanceType: In this mode, you must specify one instance type.
        *   InstanceTypes.N: In this mode, you must specify multiple instance types.
        *   InstanceTypeOverride.N: In this mode, you must specify multiple instance types and specify weights for the instance types.
        *   Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines a set of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling preferentially creates ECS instances of the instance type that is provided at the lowest price. This mode is available only if the Scaling Policy parameter is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot use InstanceType, InstanceTypes, InstanceTypeOverride, and Cpu and Memory at the same time. You can use InstanceType and InstancePatternInfos or use InstanceTypes and InstancePatternInfos at the same time. If you use InstanceType and InstancePatternInfos or use InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-out activities. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-out activities.
        
        @param request: CreateScalingConfigurationRequest
        @return: CreateScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_configuration_with_options(request, runtime)

    async def create_scaling_configuration_async(
        self,
        request: ess_20220222_models.CreateScalingConfigurationRequest,
    ) -> ess_20220222_models.CreateScalingConfigurationResponse:
        """
        Auto Scaling automatically scales out Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be configured in the following modes:
        *   InstancePatternInfo.N: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. The system selects an instance type that is provided at the lowest price based on your configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode helps reduce the failures of scale-out activities caused by insufficient inventory of instance types.
        *   InstanceType: In this mode, you must specify one instance type.
        *   InstanceTypes.N: In this mode, you must specify multiple instance types.
        *   InstanceTypeOverride.N: In this mode, you must specify multiple instance types and specify weights for the instance types.
        *   Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines a set of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling preferentially creates ECS instances of the instance type that is provided at the lowest price. This mode is available only if the Scaling Policy parameter is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot use InstanceType, InstanceTypes, InstanceTypeOverride, and Cpu and Memory at the same time. You can use InstanceType and InstancePatternInfos or use InstanceTypes and InstancePatternInfos at the same time. If you use InstanceType and InstancePatternInfos or use InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-out activities. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-out activities.
        
        @param request: CreateScalingConfigurationRequest
        @return: CreateScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_configuration_with_options_async(request, runtime)

    def create_scaling_group_with_options(
        self,
        request: ess_20220222_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingGroupResponse:
        """
        A scaling group is a group of Elastic Compute Service (ECS) instances that can be used in similar business scenarios.
        You can create only a limited number of scaling groups in a region. Go to Quota Center to check the quota of the scaling groups.
        A scaling group does not immediately take effect after you create it. You must call the EnableScalingGroup operation to enable a scaling group. After you enable a scaling group, Auto Scaling can execute scaling rules to trigger scaling activities in the scaling group.
        The Classic Load Balancer (CLB) instances and ApsaraDB RDS instances that you want to associate with a scaling group must reside in the same region as the scaling group. CLB instances are formerly known as Server Load Balancer (SLB) instances. For more information, see the "Regions and zones" topic in ECS Product Introduction.
        If you associate a CLB instance with a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the backend server group of the CLB instance. You can specify a server group to which ECS instances can be added. You can add ECS instances to the following types of server groups:
        *   Default server group: a group of ECS instances that are used to receive requests. If you do not specify a vServer group or a primary/secondary server group for a listener, requests are forwarded to the ECS instances in the default server group.
        *   vServer group: If you want to forward requests to backend servers that are not in the default server group or configure domain name-based or URL-based forwarding rules, you can use vServer groups.
        > If you specify the default server group and multiple vServer groups at the same time, ECS instances are added to all specified server groups.
        The default weight of an ECS instance that is added as a backend server of a CLB instance is 50. The CLB instance that you want to associate with your scaling group must meet the following requirements:
        *   The CLB instance must be in the Active state. You can call the DescribeLoadBalancers operation to query the state of the CLB instance.
        *   The health check feature must be enabled on all listener ports that are configured for the CLB instance. Otherwise, the scaling group fails to be created.
        If you associate an Application Load Balancer (ALB) server group with a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the ALB server group to process requests distributed by the ALB instance to which the ALB server group belongs. You can specify multiple ALB server groups. The server groups must reside in the same virtual private cloud (VPC) as the scaling group. For more information, see the "AttachAlbServerGroups" topic.
        If you associate an ApsaraDB RDS instance with a scaling group, Auto Scaling automatically adds the private IP addresses of the ECS instances in the scaling group to the IP address whitelist of the ApsaraDB RDS instance. The ApsaraDB RDS instance that you want to associate with your scaling group must meet the following requirements:
        *   The ApsaraDB RDS instance must be in the Running state. You can call the DescribeDBInstances operation to query the state of the ApsaraDB RDS instance.
        *   The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance cannot exceed the upper limit. For more information, see the "Configure whitelists" topic in ApsaraDB RDS User Guide.
        If you set the MultiAZPolicy parameter of the scaling group to COST_OPTIMIZED, take note of the following items:
        *   You can use the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools parameters to specify the instance allocation method based on the cost optimization policy. This instance allocation method is prioritized during scaling.
        *   If you do not specify the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools parameter, the instance types that are provided at the lowest price are used to create instances based on the cost optimization policy.
        If you set the `Tags.Propagate` parameter for the scaling group to true, the following rules apply:
        *   Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        *   If you specify instance tags in the scaling configuration that is used to create instances, and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        *   If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group that uses the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        
        @param request: CreateScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.lifecycle_hooks):
            query['LifecycleHooks'] = request.lifecycle_hooks
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.sync_alarm_rule_to_cms):
            query['SyncAlarmRuleToCms'] = request.sync_alarm_rule_to_cms
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingGroupResponse:
        """
        A scaling group is a group of Elastic Compute Service (ECS) instances that can be used in similar business scenarios.
        You can create only a limited number of scaling groups in a region. Go to Quota Center to check the quota of the scaling groups.
        A scaling group does not immediately take effect after you create it. You must call the EnableScalingGroup operation to enable a scaling group. After you enable a scaling group, Auto Scaling can execute scaling rules to trigger scaling activities in the scaling group.
        The Classic Load Balancer (CLB) instances and ApsaraDB RDS instances that you want to associate with a scaling group must reside in the same region as the scaling group. CLB instances are formerly known as Server Load Balancer (SLB) instances. For more information, see the "Regions and zones" topic in ECS Product Introduction.
        If you associate a CLB instance with a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the backend server group of the CLB instance. You can specify a server group to which ECS instances can be added. You can add ECS instances to the following types of server groups:
        *   Default server group: a group of ECS instances that are used to receive requests. If you do not specify a vServer group or a primary/secondary server group for a listener, requests are forwarded to the ECS instances in the default server group.
        *   vServer group: If you want to forward requests to backend servers that are not in the default server group or configure domain name-based or URL-based forwarding rules, you can use vServer groups.
        > If you specify the default server group and multiple vServer groups at the same time, ECS instances are added to all specified server groups.
        The default weight of an ECS instance that is added as a backend server of a CLB instance is 50. The CLB instance that you want to associate with your scaling group must meet the following requirements:
        *   The CLB instance must be in the Active state. You can call the DescribeLoadBalancers operation to query the state of the CLB instance.
        *   The health check feature must be enabled on all listener ports that are configured for the CLB instance. Otherwise, the scaling group fails to be created.
        If you associate an Application Load Balancer (ALB) server group with a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the ALB server group to process requests distributed by the ALB instance to which the ALB server group belongs. You can specify multiple ALB server groups. The server groups must reside in the same virtual private cloud (VPC) as the scaling group. For more information, see the "AttachAlbServerGroups" topic.
        If you associate an ApsaraDB RDS instance with a scaling group, Auto Scaling automatically adds the private IP addresses of the ECS instances in the scaling group to the IP address whitelist of the ApsaraDB RDS instance. The ApsaraDB RDS instance that you want to associate with your scaling group must meet the following requirements:
        *   The ApsaraDB RDS instance must be in the Running state. You can call the DescribeDBInstances operation to query the state of the ApsaraDB RDS instance.
        *   The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance cannot exceed the upper limit. For more information, see the "Configure whitelists" topic in ApsaraDB RDS User Guide.
        If you set the MultiAZPolicy parameter of the scaling group to COST_OPTIMIZED, take note of the following items:
        *   You can use the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools parameters to specify the instance allocation method based on the cost optimization policy. This instance allocation method is prioritized during scaling.
        *   If you do not specify the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools parameter, the instance types that are provided at the lowest price are used to create instances based on the cost optimization policy.
        If you set the `Tags.Propagate` parameter for the scaling group to true, the following rules apply:
        *   Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        *   If you specify instance tags in the scaling configuration that is used to create instances, and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        *   If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group that uses the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        
        @param request: CreateScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.lifecycle_hooks):
            query['LifecycleHooks'] = request.lifecycle_hooks
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.sync_alarm_rule_to_cms):
            query['SyncAlarmRuleToCms'] = request.sync_alarm_rule_to_cms
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_group(
        self,
        request: ess_20220222_models.CreateScalingGroupRequest,
    ) -> ess_20220222_models.CreateScalingGroupResponse:
        """
        A scaling group is a group of Elastic Compute Service (ECS) instances that can be used in similar business scenarios.
        You can create only a limited number of scaling groups in a region. Go to Quota Center to check the quota of the scaling groups.
        A scaling group does not immediately take effect after you create it. You must call the EnableScalingGroup operation to enable a scaling group. After you enable a scaling group, Auto Scaling can execute scaling rules to trigger scaling activities in the scaling group.
        The Classic Load Balancer (CLB) instances and ApsaraDB RDS instances that you want to associate with a scaling group must reside in the same region as the scaling group. CLB instances are formerly known as Server Load Balancer (SLB) instances. For more information, see the "Regions and zones" topic in ECS Product Introduction.
        If you associate a CLB instance with a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the backend server group of the CLB instance. You can specify a server group to which ECS instances can be added. You can add ECS instances to the following types of server groups:
        *   Default server group: a group of ECS instances that are used to receive requests. If you do not specify a vServer group or a primary/secondary server group for a listener, requests are forwarded to the ECS instances in the default server group.
        *   vServer group: If you want to forward requests to backend servers that are not in the default server group or configure domain name-based or URL-based forwarding rules, you can use vServer groups.
        > If you specify the default server group and multiple vServer groups at the same time, ECS instances are added to all specified server groups.
        The default weight of an ECS instance that is added as a backend server of a CLB instance is 50. The CLB instance that you want to associate with your scaling group must meet the following requirements:
        *   The CLB instance must be in the Active state. You can call the DescribeLoadBalancers operation to query the state of the CLB instance.
        *   The health check feature must be enabled on all listener ports that are configured for the CLB instance. Otherwise, the scaling group fails to be created.
        If you associate an Application Load Balancer (ALB) server group with a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the ALB server group to process requests distributed by the ALB instance to which the ALB server group belongs. You can specify multiple ALB server groups. The server groups must reside in the same virtual private cloud (VPC) as the scaling group. For more information, see the "AttachAlbServerGroups" topic.
        If you associate an ApsaraDB RDS instance with a scaling group, Auto Scaling automatically adds the private IP addresses of the ECS instances in the scaling group to the IP address whitelist of the ApsaraDB RDS instance. The ApsaraDB RDS instance that you want to associate with your scaling group must meet the following requirements:
        *   The ApsaraDB RDS instance must be in the Running state. You can call the DescribeDBInstances operation to query the state of the ApsaraDB RDS instance.
        *   The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance cannot exceed the upper limit. For more information, see the "Configure whitelists" topic in ApsaraDB RDS User Guide.
        If you set the MultiAZPolicy parameter of the scaling group to COST_OPTIMIZED, take note of the following items:
        *   You can use the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools parameters to specify the instance allocation method based on the cost optimization policy. This instance allocation method is prioritized during scaling.
        *   If you do not specify the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools parameter, the instance types that are provided at the lowest price are used to create instances based on the cost optimization policy.
        If you set the `Tags.Propagate` parameter for the scaling group to true, the following rules apply:
        *   Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        *   If you specify instance tags in the scaling configuration that is used to create instances, and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        *   If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group that uses the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        
        @param request: CreateScalingGroupRequest
        @return: CreateScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    async def create_scaling_group_async(
        self,
        request: ess_20220222_models.CreateScalingGroupRequest,
    ) -> ess_20220222_models.CreateScalingGroupResponse:
        """
        A scaling group is a group of Elastic Compute Service (ECS) instances that can be used in similar business scenarios.
        You can create only a limited number of scaling groups in a region. Go to Quota Center to check the quota of the scaling groups.
        A scaling group does not immediately take effect after you create it. You must call the EnableScalingGroup operation to enable a scaling group. After you enable a scaling group, Auto Scaling can execute scaling rules to trigger scaling activities in the scaling group.
        The Classic Load Balancer (CLB) instances and ApsaraDB RDS instances that you want to associate with a scaling group must reside in the same region as the scaling group. CLB instances are formerly known as Server Load Balancer (SLB) instances. For more information, see the "Regions and zones" topic in ECS Product Introduction.
        If you associate a CLB instance with a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the backend server group of the CLB instance. You can specify a server group to which ECS instances can be added. You can add ECS instances to the following types of server groups:
        *   Default server group: a group of ECS instances that are used to receive requests. If you do not specify a vServer group or a primary/secondary server group for a listener, requests are forwarded to the ECS instances in the default server group.
        *   vServer group: If you want to forward requests to backend servers that are not in the default server group or configure domain name-based or URL-based forwarding rules, you can use vServer groups.
        > If you specify the default server group and multiple vServer groups at the same time, ECS instances are added to all specified server groups.
        The default weight of an ECS instance that is added as a backend server of a CLB instance is 50. The CLB instance that you want to associate with your scaling group must meet the following requirements:
        *   The CLB instance must be in the Active state. You can call the DescribeLoadBalancers operation to query the state of the CLB instance.
        *   The health check feature must be enabled on all listener ports that are configured for the CLB instance. Otherwise, the scaling group fails to be created.
        If you associate an Application Load Balancer (ALB) server group with a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the ALB server group to process requests distributed by the ALB instance to which the ALB server group belongs. You can specify multiple ALB server groups. The server groups must reside in the same virtual private cloud (VPC) as the scaling group. For more information, see the "AttachAlbServerGroups" topic.
        If you associate an ApsaraDB RDS instance with a scaling group, Auto Scaling automatically adds the private IP addresses of the ECS instances in the scaling group to the IP address whitelist of the ApsaraDB RDS instance. The ApsaraDB RDS instance that you want to associate with your scaling group must meet the following requirements:
        *   The ApsaraDB RDS instance must be in the Running state. You can call the DescribeDBInstances operation to query the state of the ApsaraDB RDS instance.
        *   The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance cannot exceed the upper limit. For more information, see the "Configure whitelists" topic in ApsaraDB RDS User Guide.
        If you set the MultiAZPolicy parameter of the scaling group to COST_OPTIMIZED, take note of the following items:
        *   You can use the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools parameters to specify the instance allocation method based on the cost optimization policy. This instance allocation method is prioritized during scaling.
        *   If you do not specify the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools parameter, the instance types that are provided at the lowest price are used to create instances based on the cost optimization policy.
        If you set the `Tags.Propagate` parameter for the scaling group to true, the following rules apply:
        *   Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        *   If you specify instance tags in the scaling configuration that is used to create instances, and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        *   If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group that uses the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        
        @param request: CreateScalingGroupRequest
        @return: CreateScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_group_with_options_async(request, runtime)

    def create_scaling_rule_with_options(
        self,
        request: ess_20220222_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingRuleResponse:
        """
        Creates a scaling rule.
        
        @param request: CreateScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_rule_with_options_async(
        self,
        request: ess_20220222_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingRuleResponse:
        """
        Creates a scaling rule.
        
        @param request: CreateScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_rule(
        self,
        request: ess_20220222_models.CreateScalingRuleRequest,
    ) -> ess_20220222_models.CreateScalingRuleResponse:
        """
        Creates a scaling rule.
        
        @param request: CreateScalingRuleRequest
        @return: CreateScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_rule_with_options(request, runtime)

    async def create_scaling_rule_async(
        self,
        request: ess_20220222_models.CreateScalingRuleRequest,
    ) -> ess_20220222_models.CreateScalingRuleResponse:
        """
        Creates a scaling rule.
        
        @param request: CreateScalingRuleRequest
        @return: CreateScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_rule_with_options_async(request, runtime)

    def create_scheduled_task_with_options(
        self,
        request: ess_20220222_models.CreateScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScheduledTaskResponse:
        """
        Creates a scheduled task.
        
        @param request: CreateScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        request: ess_20220222_models.CreateScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScheduledTaskResponse:
        """
        Creates a scheduled task.
        
        @param request: CreateScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_task(
        self,
        request: ess_20220222_models.CreateScheduledTaskRequest,
    ) -> ess_20220222_models.CreateScheduledTaskResponse:
        """
        Creates a scheduled task.
        
        @param request: CreateScheduledTaskRequest
        @return: CreateScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_task_with_options(request, runtime)

    async def create_scheduled_task_async(
        self,
        request: ess_20220222_models.CreateScheduledTaskRequest,
    ) -> ess_20220222_models.CreateScheduledTaskResponse:
        """
        Creates a scheduled task.
        
        @param request: CreateScheduledTaskRequest
        @return: CreateScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduled_task_with_options_async(request, runtime)

    def deactivate_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.DeactivateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeactivateScalingConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeactivateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactivate_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.DeactivateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeactivateScalingConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeactivateScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactivate_scaling_configuration(
        self,
        request: ess_20220222_models.DeactivateScalingConfigurationRequest,
    ) -> ess_20220222_models.DeactivateScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactivate_scaling_configuration_with_options(request, runtime)

    async def deactivate_scaling_configuration_async(
        self,
        request: ess_20220222_models.DeactivateScalingConfigurationRequest,
    ) -> ess_20220222_models.DeactivateScalingConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactivate_scaling_configuration_with_options_async(request, runtime)

    def delete_alarm_with_options(
        self,
        request: ess_20220222_models.DeleteAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alarm_with_options_async(
        self,
        request: ess_20220222_models.DeleteAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alarm(
        self,
        request: ess_20220222_models.DeleteAlarmRequest,
    ) -> ess_20220222_models.DeleteAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_with_options(request, runtime)

    async def delete_alarm_async(
        self,
        request: ess_20220222_models.DeleteAlarmRequest,
    ) -> ess_20220222_models.DeleteAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alarm_with_options_async(request, runtime)

    def delete_eci_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.DeleteEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteEciScalingConfigurationResponse:
        """
        Deletes a scaling configuration that is used to create elastic container instances.
        
        @param request: DeleteEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_eci_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.DeleteEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteEciScalingConfigurationResponse:
        """
        Deletes a scaling configuration that is used to create elastic container instances.
        
        @param request: DeleteEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_eci_scaling_configuration(
        self,
        request: ess_20220222_models.DeleteEciScalingConfigurationRequest,
    ) -> ess_20220222_models.DeleteEciScalingConfigurationResponse:
        """
        Deletes a scaling configuration that is used to create elastic container instances.
        
        @param request: DeleteEciScalingConfigurationRequest
        @return: DeleteEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_eci_scaling_configuration_with_options(request, runtime)

    async def delete_eci_scaling_configuration_async(
        self,
        request: ess_20220222_models.DeleteEciScalingConfigurationRequest,
    ) -> ess_20220222_models.DeleteEciScalingConfigurationResponse:
        """
        Deletes a scaling configuration that is used to create elastic container instances.
        
        @param request: DeleteEciScalingConfigurationRequest
        @return: DeleteEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_eci_scaling_configuration_with_options_async(request, runtime)

    def delete_lifecycle_hook_with_options(
        self,
        request: ess_20220222_models.DeleteLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteLifecycleHookResponse:
        """
        If you delete a lifecycle hook that is in effect in a scaling group, instances exit the Pending state in advance. You can use one of the following methods to specify the lifecycle hooks that you want to delete:
        *   Specify the scaling group ID of the lifecycle hook that you want to delete by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter.
        *   Specify the lifecycle hook ID by using the LifecycleHookId parameter. In this case, the ScalingGroupId parameter and the LifecycleHookName parameter are ignored.
        
        @param request: DeleteLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lifecycle_hook_with_options_async(
        self,
        request: ess_20220222_models.DeleteLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteLifecycleHookResponse:
        """
        If you delete a lifecycle hook that is in effect in a scaling group, instances exit the Pending state in advance. You can use one of the following methods to specify the lifecycle hooks that you want to delete:
        *   Specify the scaling group ID of the lifecycle hook that you want to delete by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter.
        *   Specify the lifecycle hook ID by using the LifecycleHookId parameter. In this case, the ScalingGroupId parameter and the LifecycleHookName parameter are ignored.
        
        @param request: DeleteLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lifecycle_hook(
        self,
        request: ess_20220222_models.DeleteLifecycleHookRequest,
    ) -> ess_20220222_models.DeleteLifecycleHookResponse:
        """
        If you delete a lifecycle hook that is in effect in a scaling group, instances exit the Pending state in advance. You can use one of the following methods to specify the lifecycle hooks that you want to delete:
        *   Specify the scaling group ID of the lifecycle hook that you want to delete by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter.
        *   Specify the lifecycle hook ID by using the LifecycleHookId parameter. In this case, the ScalingGroupId parameter and the LifecycleHookName parameter are ignored.
        
        @param request: DeleteLifecycleHookRequest
        @return: DeleteLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_lifecycle_hook_with_options(request, runtime)

    async def delete_lifecycle_hook_async(
        self,
        request: ess_20220222_models.DeleteLifecycleHookRequest,
    ) -> ess_20220222_models.DeleteLifecycleHookResponse:
        """
        If you delete a lifecycle hook that is in effect in a scaling group, instances exit the Pending state in advance. You can use one of the following methods to specify the lifecycle hooks that you want to delete:
        *   Specify the scaling group ID of the lifecycle hook that you want to delete by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter.
        *   Specify the lifecycle hook ID by using the LifecycleHookId parameter. In this case, the ScalingGroupId parameter and the LifecycleHookName parameter are ignored.
        
        @param request: DeleteLifecycleHookRequest
        @return: DeleteLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_lifecycle_hook_with_options_async(request, runtime)

    def delete_notification_configuration_with_options(
        self,
        request: ess_20220222_models.DeleteNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_notification_configuration_with_options_async(
        self,
        request: ess_20220222_models.DeleteNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_notification_configuration(
        self,
        request: ess_20220222_models.DeleteNotificationConfigurationRequest,
    ) -> ess_20220222_models.DeleteNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_configuration_with_options(request, runtime)

    async def delete_notification_configuration_async(
        self,
        request: ess_20220222_models.DeleteNotificationConfigurationRequest,
    ) -> ess_20220222_models.DeleteNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_notification_configuration_with_options_async(request, runtime)

    def delete_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.DeleteScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingConfigurationResponse:
        """
        Deletes a scaling configuration that is used to create Elastic Compute Service (ECS) instances.
        
        @param request: DeleteScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.DeleteScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingConfigurationResponse:
        """
        Deletes a scaling configuration that is used to create Elastic Compute Service (ECS) instances.
        
        @param request: DeleteScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_configuration(
        self,
        request: ess_20220222_models.DeleteScalingConfigurationRequest,
    ) -> ess_20220222_models.DeleteScalingConfigurationResponse:
        """
        Deletes a scaling configuration that is used to create Elastic Compute Service (ECS) instances.
        
        @param request: DeleteScalingConfigurationRequest
        @return: DeleteScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_configuration_with_options(request, runtime)

    async def delete_scaling_configuration_async(
        self,
        request: ess_20220222_models.DeleteScalingConfigurationRequest,
    ) -> ess_20220222_models.DeleteScalingConfigurationResponse:
        """
        Deletes a scaling configuration that is used to create Elastic Compute Service (ECS) instances.
        
        @param request: DeleteScalingConfigurationRequest
        @return: DeleteScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_configuration_with_options_async(request, runtime)

    def delete_scaling_group_with_options(
        self,
        request: ess_20220222_models.DeleteScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingGroupResponse:
        """
        Deletes a scaling group.
        
        @param request: DeleteScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.DeleteScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingGroupResponse:
        """
        Deletes a scaling group.
        
        @param request: DeleteScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_group(
        self,
        request: ess_20220222_models.DeleteScalingGroupRequest,
    ) -> ess_20220222_models.DeleteScalingGroupResponse:
        """
        Deletes a scaling group.
        
        @param request: DeleteScalingGroupRequest
        @return: DeleteScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_group_with_options(request, runtime)

    async def delete_scaling_group_async(
        self,
        request: ess_20220222_models.DeleteScalingGroupRequest,
    ) -> ess_20220222_models.DeleteScalingGroupResponse:
        """
        Deletes a scaling group.
        
        @param request: DeleteScalingGroupRequest
        @return: DeleteScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_group_with_options_async(request, runtime)

    def delete_scaling_rule_with_options(
        self,
        request: ess_20220222_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_rule_with_options_async(
        self,
        request: ess_20220222_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_rule(
        self,
        request: ess_20220222_models.DeleteScalingRuleRequest,
    ) -> ess_20220222_models.DeleteScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_rule_with_options(request, runtime)

    async def delete_scaling_rule_async(
        self,
        request: ess_20220222_models.DeleteScalingRuleRequest,
    ) -> ess_20220222_models.DeleteScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_rule_with_options_async(request, runtime)

    def delete_scheduled_task_with_options(
        self,
        request: ess_20220222_models.DeleteScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScheduledTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_task_with_options_async(
        self,
        request: ess_20220222_models.DeleteScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScheduledTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_task(
        self,
        request: ess_20220222_models.DeleteScheduledTaskRequest,
    ) -> ess_20220222_models.DeleteScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_task_with_options(request, runtime)

    async def delete_scheduled_task_async(
        self,
        request: ess_20220222_models.DeleteScheduledTaskRequest,
    ) -> ess_20220222_models.DeleteScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduled_task_with_options_async(request, runtime)

    def describe_alarms_with_options(
        self,
        request: ess_20220222_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeAlarmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
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
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarms_with_options_async(
        self,
        request: ess_20220222_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeAlarmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
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
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarms(
        self,
        request: ess_20220222_models.DescribeAlarmsRequest,
    ) -> ess_20220222_models.DescribeAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    async def describe_alarms_async(
        self,
        request: ess_20220222_models.DescribeAlarmsRequest,
    ) -> ess_20220222_models.DescribeAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarms_with_options_async(request, runtime)

    def describe_eci_scaling_configurations_with_options(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationsResponse:
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
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeEciScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eci_scaling_configurations_with_options_async(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationsResponse:
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
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeEciScalingConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eci_scaling_configurations(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationsRequest,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eci_scaling_configurations_with_options(request, runtime)

    async def describe_eci_scaling_configurations_async(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationsRequest,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eci_scaling_configurations_with_options_async(request, runtime)

    def describe_lifecycle_actions_with_options(
        self,
        request: ess_20220222_models.DescribeLifecycleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLifecycleActionsResponse:
        """
        Queries lifecycle actions.
        
        @param request: DescribeLifecycleActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecycleActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_action_status):
            query['LifecycleActionStatus'] = request.lifecycle_action_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleActions',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_actions_with_options_async(
        self,
        request: ess_20220222_models.DescribeLifecycleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLifecycleActionsResponse:
        """
        Queries lifecycle actions.
        
        @param request: DescribeLifecycleActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecycleActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_action_status):
            query['LifecycleActionStatus'] = request.lifecycle_action_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleActions',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lifecycle_actions(
        self,
        request: ess_20220222_models.DescribeLifecycleActionsRequest,
    ) -> ess_20220222_models.DescribeLifecycleActionsResponse:
        """
        Queries lifecycle actions.
        
        @param request: DescribeLifecycleActionsRequest
        @return: DescribeLifecycleActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_actions_with_options(request, runtime)

    async def describe_lifecycle_actions_async(
        self,
        request: ess_20220222_models.DescribeLifecycleActionsRequest,
    ) -> ess_20220222_models.DescribeLifecycleActionsResponse:
        """
        Queries lifecycle actions.
        
        @param request: DescribeLifecycleActionsRequest
        @return: DescribeLifecycleActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lifecycle_actions_with_options_async(request, runtime)

    def describe_lifecycle_hooks_with_options(
        self,
        request: ess_20220222_models.DescribeLifecycleHooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLifecycleHooksResponse:
        """
        You can use one of the following methods to query lifecycle hooks:
        *   Specify a list of lifecycle hook IDs by using the LifecycleHookIds parameter. In this case, you do not need to specify the ScalingGroupId and LifecycleHookName parameters.
        *   Specify the scaling group ID by using the ScalingGroupId parameter.
        *   Specify the scaling group ID by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter at the same time.
        
        @param request: DescribeLifecycleHooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecycleHooksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_ids):
            query['LifecycleHookIds'] = request.lifecycle_hook_ids
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleHooks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleHooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_hooks_with_options_async(
        self,
        request: ess_20220222_models.DescribeLifecycleHooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLifecycleHooksResponse:
        """
        You can use one of the following methods to query lifecycle hooks:
        *   Specify a list of lifecycle hook IDs by using the LifecycleHookIds parameter. In this case, you do not need to specify the ScalingGroupId and LifecycleHookName parameters.
        *   Specify the scaling group ID by using the ScalingGroupId parameter.
        *   Specify the scaling group ID by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter at the same time.
        
        @param request: DescribeLifecycleHooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecycleHooksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_ids):
            query['LifecycleHookIds'] = request.lifecycle_hook_ids
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleHooks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleHooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lifecycle_hooks(
        self,
        request: ess_20220222_models.DescribeLifecycleHooksRequest,
    ) -> ess_20220222_models.DescribeLifecycleHooksResponse:
        """
        You can use one of the following methods to query lifecycle hooks:
        *   Specify a list of lifecycle hook IDs by using the LifecycleHookIds parameter. In this case, you do not need to specify the ScalingGroupId and LifecycleHookName parameters.
        *   Specify the scaling group ID by using the ScalingGroupId parameter.
        *   Specify the scaling group ID by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter at the same time.
        
        @param request: DescribeLifecycleHooksRequest
        @return: DescribeLifecycleHooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_hooks_with_options(request, runtime)

    async def describe_lifecycle_hooks_async(
        self,
        request: ess_20220222_models.DescribeLifecycleHooksRequest,
    ) -> ess_20220222_models.DescribeLifecycleHooksResponse:
        """
        You can use one of the following methods to query lifecycle hooks:
        *   Specify a list of lifecycle hook IDs by using the LifecycleHookIds parameter. In this case, you do not need to specify the ScalingGroupId and LifecycleHookName parameters.
        *   Specify the scaling group ID by using the ScalingGroupId parameter.
        *   Specify the scaling group ID by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter at the same time.
        
        @param request: DescribeLifecycleHooksRequest
        @return: DescribeLifecycleHooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lifecycle_hooks_with_options_async(request, runtime)

    def describe_limitation_with_options(
        self,
        request: ess_20220222_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLimitationResponse:
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
            action='DescribeLimitation',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLimitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_limitation_with_options_async(
        self,
        request: ess_20220222_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLimitationResponse:
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
            action='DescribeLimitation',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLimitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_limitation(
        self,
        request: ess_20220222_models.DescribeLimitationRequest,
    ) -> ess_20220222_models.DescribeLimitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    async def describe_limitation_async(
        self,
        request: ess_20220222_models.DescribeLimitationRequest,
    ) -> ess_20220222_models.DescribeLimitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_limitation_with_options_async(request, runtime)

    def describe_notification_configurations_with_options(
        self,
        request: ess_20220222_models.DescribeNotificationConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeNotificationConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notification_configurations_with_options_async(
        self,
        request: ess_20220222_models.DescribeNotificationConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeNotificationConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notification_configurations(
        self,
        request: ess_20220222_models.DescribeNotificationConfigurationsRequest,
    ) -> ess_20220222_models.DescribeNotificationConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_configurations_with_options(request, runtime)

    async def describe_notification_configurations_async(
        self,
        request: ess_20220222_models.DescribeNotificationConfigurationsRequest,
    ) -> ess_20220222_models.DescribeNotificationConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_notification_configurations_with_options_async(request, runtime)

    def describe_notification_types_with_options(
        self,
        request: ess_20220222_models.DescribeNotificationTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeNotificationTypesResponse:
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
            action='DescribeNotificationTypes',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notification_types_with_options_async(
        self,
        request: ess_20220222_models.DescribeNotificationTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeNotificationTypesResponse:
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
            action='DescribeNotificationTypes',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notification_types(
        self,
        request: ess_20220222_models.DescribeNotificationTypesRequest,
    ) -> ess_20220222_models.DescribeNotificationTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_types_with_options(request, runtime)

    async def describe_notification_types_async(
        self,
        request: ess_20220222_models.DescribeNotificationTypesRequest,
    ) -> ess_20220222_models.DescribeNotificationTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_notification_types_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ess_20220222_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ess_20220222_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ess_20220222_models.DescribeRegionsRequest,
    ) -> ess_20220222_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ess_20220222_models.DescribeRegionsRequest,
    ) -> ess_20220222_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_scaling_activities_with_options(
        self,
        request: ess_20220222_models.DescribeScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingActivitiesResponse:
        """
        You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        
        @param request: DescribeScalingActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivitiesResponse
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
        if not UtilClient.is_unset(request.scaling_activity_ids):
            query['ScalingActivityIds'] = request.scaling_activity_ids
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivities',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activities_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingActivitiesResponse:
        """
        You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        
        @param request: DescribeScalingActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivitiesResponse
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
        if not UtilClient.is_unset(request.scaling_activity_ids):
            query['ScalingActivityIds'] = request.scaling_activity_ids
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivities',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activities(
        self,
        request: ess_20220222_models.DescribeScalingActivitiesRequest,
    ) -> ess_20220222_models.DescribeScalingActivitiesResponse:
        """
        You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        
        @param request: DescribeScalingActivitiesRequest
        @return: DescribeScalingActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activities_with_options(request, runtime)

    async def describe_scaling_activities_async(
        self,
        request: ess_20220222_models.DescribeScalingActivitiesRequest,
    ) -> ess_20220222_models.DescribeScalingActivitiesResponse:
        """
        You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        
        @param request: DescribeScalingActivitiesRequest
        @return: DescribeScalingActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activities_with_options_async(request, runtime)

    def describe_scaling_activity_detail_with_options(
        self,
        request: ess_20220222_models.DescribeScalingActivityDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingActivityDetailResponse:
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivityDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activity_detail_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingActivityDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingActivityDetailResponse:
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivityDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activity_detail(
        self,
        request: ess_20220222_models.DescribeScalingActivityDetailRequest,
    ) -> ess_20220222_models.DescribeScalingActivityDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activity_detail_with_options(request, runtime)

    async def describe_scaling_activity_detail_async(
        self,
        request: ess_20220222_models.DescribeScalingActivityDetailRequest,
    ) -> ess_20220222_models.DescribeScalingActivityDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activity_detail_with_options_async(request, runtime)

    def describe_scaling_configurations_with_options(
        self,
        request: ess_20220222_models.DescribeScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingConfigurationsResponse:
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
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_configurations_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingConfigurationsResponse:
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
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_configurations(
        self,
        request: ess_20220222_models.DescribeScalingConfigurationsRequest,
    ) -> ess_20220222_models.DescribeScalingConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_configurations_with_options(request, runtime)

    async def describe_scaling_configurations_async(
        self,
        request: ess_20220222_models.DescribeScalingConfigurationsRequest,
    ) -> ess_20220222_models.DescribeScalingConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_configurations_with_options_async(request, runtime)

    def describe_scaling_groups_with_options(
        self,
        request: ess_20220222_models.DescribeScalingGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_ids):
            query['ScalingGroupIds'] = request.scaling_group_ids
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_group_names):
            query['ScalingGroupNames'] = request.scaling_group_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_groups_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_ids):
            query['ScalingGroupIds'] = request.scaling_group_ids
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_group_names):
            query['ScalingGroupNames'] = request.scaling_group_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_groups(
        self,
        request: ess_20220222_models.DescribeScalingGroupsRequest,
    ) -> ess_20220222_models.DescribeScalingGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_groups_with_options(request, runtime)

    async def describe_scaling_groups_async(
        self,
        request: ess_20220222_models.DescribeScalingGroupsRequest,
    ) -> ess_20220222_models.DescribeScalingGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_groups_with_options_async(request, runtime)

    def describe_scaling_instances_with_options(
        self,
        request: ess_20220222_models.DescribeScalingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingInstancesResponse:
        """
        You can query ECS instances by scaling group ID, scaling configuration ID, health status, lifecycle status, and instance creation method.
        
        @param request: DescribeScalingInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_type):
            query['CreationType'] = request.creation_type
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_instances_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingInstancesResponse:
        """
        You can query ECS instances by scaling group ID, scaling configuration ID, health status, lifecycle status, and instance creation method.
        
        @param request: DescribeScalingInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_type):
            query['CreationType'] = request.creation_type
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_instances(
        self,
        request: ess_20220222_models.DescribeScalingInstancesRequest,
    ) -> ess_20220222_models.DescribeScalingInstancesResponse:
        """
        You can query ECS instances by scaling group ID, scaling configuration ID, health status, lifecycle status, and instance creation method.
        
        @param request: DescribeScalingInstancesRequest
        @return: DescribeScalingInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_instances_with_options(request, runtime)

    async def describe_scaling_instances_async(
        self,
        request: ess_20220222_models.DescribeScalingInstancesRequest,
    ) -> ess_20220222_models.DescribeScalingInstancesResponse:
        """
        You can query ECS instances by scaling group ID, scaling configuration ID, health status, lifecycle status, and instance creation method.
        
        @param request: DescribeScalingInstancesRequest
        @return: DescribeScalingInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_instances_with_options_async(request, runtime)

    def describe_scaling_rules_with_options(
        self,
        request: ess_20220222_models.DescribeScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingRulesResponse:
        """
        Queries all scaling rules in a scaling group.
        
        @param request: DescribeScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingRulesResponse
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
        if not UtilClient.is_unset(request.scaling_rule_aris):
            query['ScalingRuleAris'] = request.scaling_rule_aris
        if not UtilClient.is_unset(request.scaling_rule_ids):
            query['ScalingRuleIds'] = request.scaling_rule_ids
        if not UtilClient.is_unset(request.scaling_rule_names):
            query['ScalingRuleNames'] = request.scaling_rule_names
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.show_alarm_rules):
            query['ShowAlarmRules'] = request.show_alarm_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingRules',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_rules_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingRulesResponse:
        """
        Queries all scaling rules in a scaling group.
        
        @param request: DescribeScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingRulesResponse
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
        if not UtilClient.is_unset(request.scaling_rule_aris):
            query['ScalingRuleAris'] = request.scaling_rule_aris
        if not UtilClient.is_unset(request.scaling_rule_ids):
            query['ScalingRuleIds'] = request.scaling_rule_ids
        if not UtilClient.is_unset(request.scaling_rule_names):
            query['ScalingRuleNames'] = request.scaling_rule_names
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.show_alarm_rules):
            query['ShowAlarmRules'] = request.show_alarm_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingRules',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_rules(
        self,
        request: ess_20220222_models.DescribeScalingRulesRequest,
    ) -> ess_20220222_models.DescribeScalingRulesResponse:
        """
        Queries all scaling rules in a scaling group.
        
        @param request: DescribeScalingRulesRequest
        @return: DescribeScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_rules_with_options(request, runtime)

    async def describe_scaling_rules_async(
        self,
        request: ess_20220222_models.DescribeScalingRulesRequest,
    ) -> ess_20220222_models.DescribeScalingRulesResponse:
        """
        Queries all scaling rules in a scaling group.
        
        @param request: DescribeScalingRulesRequest
        @return: DescribeScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_rules_with_options_async(request, runtime)

    def describe_scheduled_tasks_with_options(
        self,
        request: ess_20220222_models.DescribeScheduledTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScheduledTasksResponse:
        """
        You can query scheduled tasks by scaling rule, task ID, or task name.
        
        @param request: DescribeScheduledTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduledTasksResponse
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
        if not UtilClient.is_unset(request.scheduled_actions):
            query['ScheduledActions'] = request.scheduled_actions
        if not UtilClient.is_unset(request.scheduled_task_ids):
            query['ScheduledTaskIds'] = request.scheduled_task_ids
        if not UtilClient.is_unset(request.scheduled_task_names):
            query['ScheduledTaskNames'] = request.scheduled_task_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduledTasks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scheduled_tasks_with_options_async(
        self,
        request: ess_20220222_models.DescribeScheduledTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScheduledTasksResponse:
        """
        You can query scheduled tasks by scaling rule, task ID, or task name.
        
        @param request: DescribeScheduledTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduledTasksResponse
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
        if not UtilClient.is_unset(request.scheduled_actions):
            query['ScheduledActions'] = request.scheduled_actions
        if not UtilClient.is_unset(request.scheduled_task_ids):
            query['ScheduledTaskIds'] = request.scheduled_task_ids
        if not UtilClient.is_unset(request.scheduled_task_names):
            query['ScheduledTaskNames'] = request.scheduled_task_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduledTasks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScheduledTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scheduled_tasks(
        self,
        request: ess_20220222_models.DescribeScheduledTasksRequest,
    ) -> ess_20220222_models.DescribeScheduledTasksResponse:
        """
        You can query scheduled tasks by scaling rule, task ID, or task name.
        
        @param request: DescribeScheduledTasksRequest
        @return: DescribeScheduledTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduled_tasks_with_options(request, runtime)

    async def describe_scheduled_tasks_async(
        self,
        request: ess_20220222_models.DescribeScheduledTasksRequest,
    ) -> ess_20220222_models.DescribeScheduledTasksResponse:
        """
        You can query scheduled tasks by scaling rule, task ID, or task name.
        
        @param request: DescribeScheduledTasksRequest
        @return: DescribeScheduledTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scheduled_tasks_with_options_async(request, runtime)

    def detach_alb_server_groups_with_options(
        self,
        request: ess_20220222_models.DetachAlbServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachAlbServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachAlbServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_alb_server_groups_with_options_async(
        self,
        request: ess_20220222_models.DetachAlbServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachAlbServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachAlbServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_alb_server_groups(
        self,
        request: ess_20220222_models.DetachAlbServerGroupsRequest,
    ) -> ess_20220222_models.DetachAlbServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_alb_server_groups_with_options(request, runtime)

    async def detach_alb_server_groups_async(
        self,
        request: ess_20220222_models.DetachAlbServerGroupsRequest,
    ) -> ess_20220222_models.DetachAlbServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_alb_server_groups_with_options_async(request, runtime)

    def detach_dbinstances_with_options(
        self,
        request: ess_20220222_models.DetachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachDBInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_dbinstances_with_options_async(
        self,
        request: ess_20220222_models.DetachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachDBInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_dbinstances(
        self,
        request: ess_20220222_models.DetachDBInstancesRequest,
    ) -> ess_20220222_models.DetachDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_dbinstances_with_options(request, runtime)

    async def detach_dbinstances_async(
        self,
        request: ess_20220222_models.DetachDBInstancesRequest,
    ) -> ess_20220222_models.DetachDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_dbinstances_with_options_async(request, runtime)

    def detach_instances_with_options(
        self,
        request: ess_20220222_models.DetachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachInstancesResponse:
        """
        Removes one or more Elastic Compute Service (ECS) instances or elastic container instances from a scaling group.
        
        @param request: DetachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.detach_option):
            query['DetachOption'] = request.detach_option
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_instances_with_options_async(
        self,
        request: ess_20220222_models.DetachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachInstancesResponse:
        """
        Removes one or more Elastic Compute Service (ECS) instances or elastic container instances from a scaling group.
        
        @param request: DetachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.detach_option):
            query['DetachOption'] = request.detach_option
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_instances(
        self,
        request: ess_20220222_models.DetachInstancesRequest,
    ) -> ess_20220222_models.DetachInstancesResponse:
        """
        Removes one or more Elastic Compute Service (ECS) instances or elastic container instances from a scaling group.
        
        @param request: DetachInstancesRequest
        @return: DetachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_instances_with_options(request, runtime)

    async def detach_instances_async(
        self,
        request: ess_20220222_models.DetachInstancesRequest,
    ) -> ess_20220222_models.DetachInstancesResponse:
        """
        Removes one or more Elastic Compute Service (ECS) instances or elastic container instances from a scaling group.
        
        @param request: DetachInstancesRequest
        @return: DetachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_instances_with_options_async(request, runtime)

    def detach_load_balancers_with_options(
        self,
        request: ess_20220222_models.DetachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachLoadBalancersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_load_balancers_with_options_async(
        self,
        request: ess_20220222_models.DetachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachLoadBalancersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_load_balancers(
        self,
        request: ess_20220222_models.DetachLoadBalancersRequest,
    ) -> ess_20220222_models.DetachLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_load_balancers_with_options(request, runtime)

    async def detach_load_balancers_async(
        self,
        request: ess_20220222_models.DetachLoadBalancersRequest,
    ) -> ess_20220222_models.DetachLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_load_balancers_with_options_async(request, runtime)

    def detach_server_groups_with_options(
        self,
        request: ess_20220222_models.DetachServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_server_groups_with_options_async(
        self,
        request: ess_20220222_models.DetachServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_server_groups(
        self,
        request: ess_20220222_models.DetachServerGroupsRequest,
    ) -> ess_20220222_models.DetachServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_server_groups_with_options(request, runtime)

    async def detach_server_groups_async(
        self,
        request: ess_20220222_models.DetachServerGroupsRequest,
    ) -> ess_20220222_models.DetachServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_server_groups_with_options_async(request, runtime)

    def detach_vserver_groups_with_options(
        self,
        request: ess_20220222_models.DetachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachVServerGroupsResponse:
        """
        Detaches one or more vServer groups of a Classic Load Balancer (CLB) instance from a scaling group.
        
        @param request: DetachVServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_vserver_groups_with_options_async(
        self,
        request: ess_20220222_models.DetachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachVServerGroupsResponse:
        """
        Detaches one or more vServer groups of a Classic Load Balancer (CLB) instance from a scaling group.
        
        @param request: DetachVServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachVServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_vserver_groups(
        self,
        request: ess_20220222_models.DetachVServerGroupsRequest,
    ) -> ess_20220222_models.DetachVServerGroupsResponse:
        """
        Detaches one or more vServer groups of a Classic Load Balancer (CLB) instance from a scaling group.
        
        @param request: DetachVServerGroupsRequest
        @return: DetachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_vserver_groups_with_options(request, runtime)

    async def detach_vserver_groups_async(
        self,
        request: ess_20220222_models.DetachVServerGroupsRequest,
    ) -> ess_20220222_models.DetachVServerGroupsResponse:
        """
        Detaches one or more vServer groups of a Classic Load Balancer (CLB) instance from a scaling group.
        
        @param request: DetachVServerGroupsRequest
        @return: DetachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_vserver_groups_with_options_async(request, runtime)

    def disable_alarm_with_options(
        self,
        request: ess_20220222_models.DisableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DisableAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_alarm_with_options_async(
        self,
        request: ess_20220222_models.DisableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DisableAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_alarm(
        self,
        request: ess_20220222_models.DisableAlarmRequest,
    ) -> ess_20220222_models.DisableAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_alarm_with_options(request, runtime)

    async def disable_alarm_async(
        self,
        request: ess_20220222_models.DisableAlarmRequest,
    ) -> ess_20220222_models.DisableAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_alarm_with_options_async(request, runtime)

    def disable_scaling_group_with_options(
        self,
        request: ess_20220222_models.DisableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DisableScalingGroupResponse:
        """
        Disables a scaling group.
        
        @param request: DisableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableScalingGroupResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.DisableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DisableScalingGroupResponse:
        """
        Disables a scaling group.
        
        @param request: DisableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableScalingGroupResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_scaling_group(
        self,
        request: ess_20220222_models.DisableScalingGroupRequest,
    ) -> ess_20220222_models.DisableScalingGroupResponse:
        """
        Disables a scaling group.
        
        @param request: DisableScalingGroupRequest
        @return: DisableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_scaling_group_with_options(request, runtime)

    async def disable_scaling_group_async(
        self,
        request: ess_20220222_models.DisableScalingGroupRequest,
    ) -> ess_20220222_models.DisableScalingGroupResponse:
        """
        Disables a scaling group.
        
        @param request: DisableScalingGroupRequest
        @return: DisableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_scaling_group_with_options_async(request, runtime)

    def enable_alarm_with_options(
        self,
        request: ess_20220222_models.EnableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnableAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_alarm_with_options_async(
        self,
        request: ess_20220222_models.EnableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnableAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_alarm(
        self,
        request: ess_20220222_models.EnableAlarmRequest,
    ) -> ess_20220222_models.EnableAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_alarm_with_options(request, runtime)

    async def enable_alarm_async(
        self,
        request: ess_20220222_models.EnableAlarmRequest,
    ) -> ess_20220222_models.EnableAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_alarm_with_options_async(request, runtime)

    def enable_scaling_group_with_options(
        self,
        request: ess_20220222_models.EnableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnableScalingGroupResponse:
        """
        You can call this operation to enable a scaling group that is in the Inactive state and has an instance configuration source. The instance configuration source can be a scaling configuration, a launch template, or an Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If a scaling group is not in the Inactive state or does not have an active instance configuration source, you cannot call this operation to enable the scaling group.
        > A scaling group can have only one active instance configuration source. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If an instance configuration source has been configured for the scaling group before you call this operation, the scaling configuration or launch template that you specify in the request overwrites the original scaling configuration or launch template.
        If you specify a value for the InstanceId parameter when you call the operation, Auto Scaling checks whether the total number of ECS instances is within the range allowed in the scaling group after you call the operation.
        *   If the total number of ECS instances is less than the minimum number of instances allowed in the scaling group after you call the operation, Auto Scaling automatically creates the required number of pay-as-you-go ECS instances and adds the instances to the scaling group to reach the minimum number. For example, if the minimum number of instances allowed in your scaling group is five, and you specify the InstanceId parameter to add two created ECS instances to the scaling group, Auto Scaling automatically creates three instances in the scaling group after the two instances are added.
        *   If the value of the TotalCapactiy parameter is greater than the value of the MaxSize parameter, the call fails.
        
        @param request: EnableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.EnableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnableScalingGroupResponse:
        """
        You can call this operation to enable a scaling group that is in the Inactive state and has an instance configuration source. The instance configuration source can be a scaling configuration, a launch template, or an Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If a scaling group is not in the Inactive state or does not have an active instance configuration source, you cannot call this operation to enable the scaling group.
        > A scaling group can have only one active instance configuration source. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If an instance configuration source has been configured for the scaling group before you call this operation, the scaling configuration or launch template that you specify in the request overwrites the original scaling configuration or launch template.
        If you specify a value for the InstanceId parameter when you call the operation, Auto Scaling checks whether the total number of ECS instances is within the range allowed in the scaling group after you call the operation.
        *   If the total number of ECS instances is less than the minimum number of instances allowed in the scaling group after you call the operation, Auto Scaling automatically creates the required number of pay-as-you-go ECS instances and adds the instances to the scaling group to reach the minimum number. For example, if the minimum number of instances allowed in your scaling group is five, and you specify the InstanceId parameter to add two created ECS instances to the scaling group, Auto Scaling automatically creates three instances in the scaling group after the two instances are added.
        *   If the value of the TotalCapactiy parameter is greater than the value of the MaxSize parameter, the call fails.
        
        @param request: EnableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_scaling_group(
        self,
        request: ess_20220222_models.EnableScalingGroupRequest,
    ) -> ess_20220222_models.EnableScalingGroupResponse:
        """
        You can call this operation to enable a scaling group that is in the Inactive state and has an instance configuration source. The instance configuration source can be a scaling configuration, a launch template, or an Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If a scaling group is not in the Inactive state or does not have an active instance configuration source, you cannot call this operation to enable the scaling group.
        > A scaling group can have only one active instance configuration source. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If an instance configuration source has been configured for the scaling group before you call this operation, the scaling configuration or launch template that you specify in the request overwrites the original scaling configuration or launch template.
        If you specify a value for the InstanceId parameter when you call the operation, Auto Scaling checks whether the total number of ECS instances is within the range allowed in the scaling group after you call the operation.
        *   If the total number of ECS instances is less than the minimum number of instances allowed in the scaling group after you call the operation, Auto Scaling automatically creates the required number of pay-as-you-go ECS instances and adds the instances to the scaling group to reach the minimum number. For example, if the minimum number of instances allowed in your scaling group is five, and you specify the InstanceId parameter to add two created ECS instances to the scaling group, Auto Scaling automatically creates three instances in the scaling group after the two instances are added.
        *   If the value of the TotalCapactiy parameter is greater than the value of the MaxSize parameter, the call fails.
        
        @param request: EnableScalingGroupRequest
        @return: EnableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_scaling_group_with_options(request, runtime)

    async def enable_scaling_group_async(
        self,
        request: ess_20220222_models.EnableScalingGroupRequest,
    ) -> ess_20220222_models.EnableScalingGroupResponse:
        """
        You can call this operation to enable a scaling group that is in the Inactive state and has an instance configuration source. The instance configuration source can be a scaling configuration, a launch template, or an Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If a scaling group is not in the Inactive state or does not have an active instance configuration source, you cannot call this operation to enable the scaling group.
        > A scaling group can have only one active instance configuration source. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If an instance configuration source has been configured for the scaling group before you call this operation, the scaling configuration or launch template that you specify in the request overwrites the original scaling configuration or launch template.
        If you specify a value for the InstanceId parameter when you call the operation, Auto Scaling checks whether the total number of ECS instances is within the range allowed in the scaling group after you call the operation.
        *   If the total number of ECS instances is less than the minimum number of instances allowed in the scaling group after you call the operation, Auto Scaling automatically creates the required number of pay-as-you-go ECS instances and adds the instances to the scaling group to reach the minimum number. For example, if the minimum number of instances allowed in your scaling group is five, and you specify the InstanceId parameter to add two created ECS instances to the scaling group, Auto Scaling automatically creates three instances in the scaling group after the two instances are added.
        *   If the value of the TotalCapactiy parameter is greater than the value of the MaxSize parameter, the call fails.
        
        @param request: EnableScalingGroupRequest
        @return: EnableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_scaling_group_with_options_async(request, runtime)

    def enter_standby_with_options(
        self,
        request: ess_20220222_models.EnterStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnterStandbyResponse:
        """
        If you call the operation to set an Elastic Compute Service (ECS) instance in a scaling group that is associated with a Server Load Balancer (SLB) instance to the Standby state, the weight of the ECS instance as a backend server of the SLB instance is set to 0.
        *   You can remove an ECS instance that is in the Standby state from a scaling group and release the instance.
        *   When scale-in activities are triggered by changes in the number of scaling groups or by event-triggered tasks, the ECS instances that are in the Standby state are not removed from the scaling groups.
        *   If Auto Scaling considers an ECS instance that is in the Standby state unhealthy, such as in the Stopping or Restarting state, Auto Scaling does not update the health check status of the ECS instance or trigger scale-in activities to remove the ECS instance from the scaling group. Auto Scaling updates the health check status of the ECS instance only when the ECS instance is no longer in the Standby state.
        
        @param request: EnterStandbyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterStandbyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='EnterStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnterStandbyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enter_standby_with_options_async(
        self,
        request: ess_20220222_models.EnterStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnterStandbyResponse:
        """
        If you call the operation to set an Elastic Compute Service (ECS) instance in a scaling group that is associated with a Server Load Balancer (SLB) instance to the Standby state, the weight of the ECS instance as a backend server of the SLB instance is set to 0.
        *   You can remove an ECS instance that is in the Standby state from a scaling group and release the instance.
        *   When scale-in activities are triggered by changes in the number of scaling groups or by event-triggered tasks, the ECS instances that are in the Standby state are not removed from the scaling groups.
        *   If Auto Scaling considers an ECS instance that is in the Standby state unhealthy, such as in the Stopping or Restarting state, Auto Scaling does not update the health check status of the ECS instance or trigger scale-in activities to remove the ECS instance from the scaling group. Auto Scaling updates the health check status of the ECS instance only when the ECS instance is no longer in the Standby state.
        
        @param request: EnterStandbyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterStandbyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='EnterStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnterStandbyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enter_standby(
        self,
        request: ess_20220222_models.EnterStandbyRequest,
    ) -> ess_20220222_models.EnterStandbyResponse:
        """
        If you call the operation to set an Elastic Compute Service (ECS) instance in a scaling group that is associated with a Server Load Balancer (SLB) instance to the Standby state, the weight of the ECS instance as a backend server of the SLB instance is set to 0.
        *   You can remove an ECS instance that is in the Standby state from a scaling group and release the instance.
        *   When scale-in activities are triggered by changes in the number of scaling groups or by event-triggered tasks, the ECS instances that are in the Standby state are not removed from the scaling groups.
        *   If Auto Scaling considers an ECS instance that is in the Standby state unhealthy, such as in the Stopping or Restarting state, Auto Scaling does not update the health check status of the ECS instance or trigger scale-in activities to remove the ECS instance from the scaling group. Auto Scaling updates the health check status of the ECS instance only when the ECS instance is no longer in the Standby state.
        
        @param request: EnterStandbyRequest
        @return: EnterStandbyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enter_standby_with_options(request, runtime)

    async def enter_standby_async(
        self,
        request: ess_20220222_models.EnterStandbyRequest,
    ) -> ess_20220222_models.EnterStandbyResponse:
        """
        If you call the operation to set an Elastic Compute Service (ECS) instance in a scaling group that is associated with a Server Load Balancer (SLB) instance to the Standby state, the weight of the ECS instance as a backend server of the SLB instance is set to 0.
        *   You can remove an ECS instance that is in the Standby state from a scaling group and release the instance.
        *   When scale-in activities are triggered by changes in the number of scaling groups or by event-triggered tasks, the ECS instances that are in the Standby state are not removed from the scaling groups.
        *   If Auto Scaling considers an ECS instance that is in the Standby state unhealthy, such as in the Stopping or Restarting state, Auto Scaling does not update the health check status of the ECS instance or trigger scale-in activities to remove the ECS instance from the scaling group. Auto Scaling updates the health check status of the ECS instance only when the ECS instance is no longer in the Standby state.
        
        @param request: EnterStandbyRequest
        @return: EnterStandbyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enter_standby_with_options_async(request, runtime)

    def execute_scaling_rule_with_options(
        self,
        request: ess_20220222_models.ExecuteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ExecuteScalingRuleResponse:
        """
        Executes a scaling rule.
        
        @param request: ExecuteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.breach_threshold):
            query['BreachThreshold'] = request.breach_threshold
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.metric_value):
            query['MetricValue'] = request.metric_value
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
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExecuteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_scaling_rule_with_options_async(
        self,
        request: ess_20220222_models.ExecuteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ExecuteScalingRuleResponse:
        """
        Executes a scaling rule.
        
        @param request: ExecuteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.breach_threshold):
            query['BreachThreshold'] = request.breach_threshold
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.metric_value):
            query['MetricValue'] = request.metric_value
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
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExecuteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_scaling_rule(
        self,
        request: ess_20220222_models.ExecuteScalingRuleRequest,
    ) -> ess_20220222_models.ExecuteScalingRuleResponse:
        """
        Executes a scaling rule.
        
        @param request: ExecuteScalingRuleRequest
        @return: ExecuteScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_scaling_rule_with_options(request, runtime)

    async def execute_scaling_rule_async(
        self,
        request: ess_20220222_models.ExecuteScalingRuleRequest,
    ) -> ess_20220222_models.ExecuteScalingRuleResponse:
        """
        Executes a scaling rule.
        
        @param request: ExecuteScalingRuleRequest
        @return: ExecuteScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_scaling_rule_with_options_async(request, runtime)

    def exit_standby_with_options(
        self,
        request: ess_20220222_models.ExitStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ExitStandbyResponse:
        """
        If the scaling group is associated with a load balancing instance, the ECS instance weight will be set to the weight value defined in the scaling configuration.
        
        @param request: ExitStandbyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExitStandbyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExitStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExitStandbyResponse(),
            self.call_api(params, req, runtime)
        )

    async def exit_standby_with_options_async(
        self,
        request: ess_20220222_models.ExitStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ExitStandbyResponse:
        """
        If the scaling group is associated with a load balancing instance, the ECS instance weight will be set to the weight value defined in the scaling configuration.
        
        @param request: ExitStandbyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExitStandbyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExitStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExitStandbyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exit_standby(
        self,
        request: ess_20220222_models.ExitStandbyRequest,
    ) -> ess_20220222_models.ExitStandbyResponse:
        """
        If the scaling group is associated with a load balancing instance, the ECS instance weight will be set to the weight value defined in the scaling configuration.
        
        @param request: ExitStandbyRequest
        @return: ExitStandbyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.exit_standby_with_options(request, runtime)

    async def exit_standby_async(
        self,
        request: ess_20220222_models.ExitStandbyRequest,
    ) -> ess_20220222_models.ExitStandbyResponse:
        """
        If the scaling group is associated with a load balancing instance, the ECS instance weight will be set to the weight value defined in the scaling configuration.
        
        @param request: ExitStandbyRequest
        @return: ExitStandbyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.exit_standby_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ess_20220222_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ess_20220222_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: ess_20220222_models.ListTagKeysRequest,
    ) -> ess_20220222_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ess_20220222_models.ListTagKeysRequest,
    ) -> ess_20220222_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ess_20220222_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ess_20220222_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ess_20220222_models.ListTagResourcesRequest,
    ) -> ess_20220222_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ess_20220222_models.ListTagResourcesRequest,
    ) -> ess_20220222_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: ess_20220222_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: ess_20220222_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: ess_20220222_models.ListTagValuesRequest,
    ) -> ess_20220222_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: ess_20220222_models.ListTagValuesRequest,
    ) -> ess_20220222_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def modify_alarm_with_options(
        self,
        request: ess_20220222_models.ModifyAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyAlarmResponse:
        """
        Modifies an event-triggered task.
        
        @param request: ModifyAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_alarm_with_options_async(
        self,
        request: ess_20220222_models.ModifyAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyAlarmResponse:
        """
        Modifies an event-triggered task.
        
        @param request: ModifyAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_alarm(
        self,
        request: ess_20220222_models.ModifyAlarmRequest,
    ) -> ess_20220222_models.ModifyAlarmResponse:
        """
        Modifies an event-triggered task.
        
        @param request: ModifyAlarmRequest
        @return: ModifyAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_alarm_with_options(request, runtime)

    async def modify_alarm_async(
        self,
        request: ess_20220222_models.ModifyAlarmRequest,
    ) -> ess_20220222_models.ModifyAlarmResponse:
        """
        Modifies an event-triggered task.
        
        @param request: ModifyAlarmRequest
        @return: ModifyAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_alarm_with_options_async(request, runtime)

    def modify_eci_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.ModifyEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyEciScalingConfigurationResponse:
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.containers_update_type):
            query['ContainersUpdateType'] = request.containers_update_type
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.security_context_sys_ctls):
            query['SecurityContextSysCtls'] = request.security_context_sys_ctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_eci_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.ModifyEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyEciScalingConfigurationResponse:
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.containers_update_type):
            query['ContainersUpdateType'] = request.containers_update_type
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.security_context_sys_ctls):
            query['SecurityContextSysCtls'] = request.security_context_sys_ctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_eci_scaling_configuration(
        self,
        request: ess_20220222_models.ModifyEciScalingConfigurationRequest,
    ) -> ess_20220222_models.ModifyEciScalingConfigurationResponse:
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyEciScalingConfigurationRequest
        @return: ModifyEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_eci_scaling_configuration_with_options(request, runtime)

    async def modify_eci_scaling_configuration_async(
        self,
        request: ess_20220222_models.ModifyEciScalingConfigurationRequest,
    ) -> ess_20220222_models.ModifyEciScalingConfigurationResponse:
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyEciScalingConfigurationRequest
        @return: ModifyEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_eci_scaling_configuration_with_options_async(request, runtime)

    def modify_lifecycle_hook_with_options(
        self,
        request: ess_20220222_models.ModifyLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyLifecycleHookResponse:
        """
        Modifies a lifecycle hook.
        
        @param request: ModifyLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_hook_status):
            query['LifecycleHookStatus'] = request.lifecycle_hook_status
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lifecycle_hook_with_options_async(
        self,
        request: ess_20220222_models.ModifyLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyLifecycleHookResponse:
        """
        Modifies a lifecycle hook.
        
        @param request: ModifyLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_hook_status):
            query['LifecycleHookStatus'] = request.lifecycle_hook_status
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lifecycle_hook(
        self,
        request: ess_20220222_models.ModifyLifecycleHookRequest,
    ) -> ess_20220222_models.ModifyLifecycleHookResponse:
        """
        Modifies a lifecycle hook.
        
        @param request: ModifyLifecycleHookRequest
        @return: ModifyLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_lifecycle_hook_with_options(request, runtime)

    async def modify_lifecycle_hook_async(
        self,
        request: ess_20220222_models.ModifyLifecycleHookRequest,
    ) -> ess_20220222_models.ModifyLifecycleHookResponse:
        """
        Modifies a lifecycle hook.
        
        @param request: ModifyLifecycleHookRequest
        @return: ModifyLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_lifecycle_hook_with_options_async(request, runtime)

    def modify_notification_configuration_with_options(
        self,
        request: ess_20220222_models.ModifyNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_notification_configuration_with_options_async(
        self,
        request: ess_20220222_models.ModifyNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyNotificationConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_notification_configuration(
        self,
        request: ess_20220222_models.ModifyNotificationConfigurationRequest,
    ) -> ess_20220222_models.ModifyNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_notification_configuration_with_options(request, runtime)

    async def modify_notification_configuration_async(
        self,
        request: ess_20220222_models.ModifyNotificationConfigurationRequest,
    ) -> ess_20220222_models.ModifyNotificationConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_notification_configuration_with_options_async(request, runtime)

    def modify_scaling_configuration_with_options(
        self,
        tmp_req: ess_20220222_models.ModifyScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingConfigurationResponse:
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param tmp_req: ModifyScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.ModifyScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.override):
            query['Override'] = request.override
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_configuration_with_options_async(
        self,
        tmp_req: ess_20220222_models.ModifyScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingConfigurationResponse:
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param tmp_req: ModifyScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.ModifyScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.override):
            query['Override'] = request.override
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_configuration(
        self,
        request: ess_20220222_models.ModifyScalingConfigurationRequest,
    ) -> ess_20220222_models.ModifyScalingConfigurationResponse:
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyScalingConfigurationRequest
        @return: ModifyScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_configuration_with_options(request, runtime)

    async def modify_scaling_configuration_async(
        self,
        request: ess_20220222_models.ModifyScalingConfigurationRequest,
    ) -> ess_20220222_models.ModifyScalingConfigurationResponse:
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyScalingConfigurationRequest
        @return: ModifyScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_configuration_with_options_async(request, runtime)

    def modify_scaling_group_with_options(
        self,
        request: ess_20220222_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingGroupResponse:
        """
        Modifies a scaling group.
        
        @param request: ModifyScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingGroupResponse:
        """
        Modifies a scaling group.
        
        @param request: ModifyScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_group(
        self,
        request: ess_20220222_models.ModifyScalingGroupRequest,
    ) -> ess_20220222_models.ModifyScalingGroupResponse:
        """
        Modifies a scaling group.
        
        @param request: ModifyScalingGroupRequest
        @return: ModifyScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    async def modify_scaling_group_async(
        self,
        request: ess_20220222_models.ModifyScalingGroupRequest,
    ) -> ess_20220222_models.ModifyScalingGroupResponse:
        """
        Modifies a scaling group.
        
        @param request: ModifyScalingGroupRequest
        @return: ModifyScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_group_with_options_async(request, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: ess_20220222_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: ess_20220222_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: ess_20220222_models.ModifyScalingRuleRequest,
    ) -> ess_20220222_models.ModifyScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_rule_with_options(request, runtime)

    async def modify_scaling_rule_async(
        self,
        request: ess_20220222_models.ModifyScalingRuleRequest,
    ) -> ess_20220222_models.ModifyScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_rule_with_options_async(request, runtime)

    def modify_scheduled_task_with_options(
        self,
        request: ess_20220222_models.ModifyScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScheduledTaskResponse:
        """
        Modifies a scheduled task.
        
        @param request: ModifyScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        request: ess_20220222_models.ModifyScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScheduledTaskResponse:
        """
        Modifies a scheduled task.
        
        @param request: ModifyScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_task(
        self,
        request: ess_20220222_models.ModifyScheduledTaskRequest,
    ) -> ess_20220222_models.ModifyScheduledTaskResponse:
        """
        Modifies a scheduled task.
        
        @param request: ModifyScheduledTaskRequest
        @return: ModifyScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduled_task_with_options(request, runtime)

    async def modify_scheduled_task_async(
        self,
        request: ess_20220222_models.ModifyScheduledTaskRequest,
    ) -> ess_20220222_models.ModifyScheduledTaskResponse:
        """
        Modifies a scheduled task.
        
        @param request: ModifyScheduledTaskRequest
        @return: ModifyScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scheduled_task_with_options_async(request, runtime)

    def rebalance_instances_with_options(
        self,
        request: ess_20220222_models.RebalanceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RebalanceInstancesResponse:
        """
        Rebalances Elastic Compute Service (ECS) instances in a multi-zone scaling group across zones.
        
        @param request: RebalanceInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebalanceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebalanceInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RebalanceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebalance_instances_with_options_async(
        self,
        request: ess_20220222_models.RebalanceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RebalanceInstancesResponse:
        """
        Rebalances Elastic Compute Service (ECS) instances in a multi-zone scaling group across zones.
        
        @param request: RebalanceInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebalanceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebalanceInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RebalanceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebalance_instances(
        self,
        request: ess_20220222_models.RebalanceInstancesRequest,
    ) -> ess_20220222_models.RebalanceInstancesResponse:
        """
        Rebalances Elastic Compute Service (ECS) instances in a multi-zone scaling group across zones.
        
        @param request: RebalanceInstancesRequest
        @return: RebalanceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rebalance_instances_with_options(request, runtime)

    async def rebalance_instances_async(
        self,
        request: ess_20220222_models.RebalanceInstancesRequest,
    ) -> ess_20220222_models.RebalanceInstancesResponse:
        """
        Rebalances Elastic Compute Service (ECS) instances in a multi-zone scaling group across zones.
        
        @param request: RebalanceInstancesRequest
        @return: RebalanceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rebalance_instances_with_options_async(request, runtime)

    def record_lifecycle_action_heartbeat_with_options(
        self,
        request: ess_20220222_models.RecordLifecycleActionHeartbeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RecordLifecycleActionHeartbeatResponse:
        """
        Prolongs a lifecycle hook for Elastic Compute Service (ECS) instances.
        
        @param request: RecordLifecycleActionHeartbeatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecordLifecycleActionHeartbeatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['heartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['lifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['lifecycleHookId'] = request.lifecycle_hook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordLifecycleActionHeartbeat',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RecordLifecycleActionHeartbeatResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_lifecycle_action_heartbeat_with_options_async(
        self,
        request: ess_20220222_models.RecordLifecycleActionHeartbeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RecordLifecycleActionHeartbeatResponse:
        """
        Prolongs a lifecycle hook for Elastic Compute Service (ECS) instances.
        
        @param request: RecordLifecycleActionHeartbeatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecordLifecycleActionHeartbeatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['heartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['lifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['lifecycleHookId'] = request.lifecycle_hook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordLifecycleActionHeartbeat',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RecordLifecycleActionHeartbeatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_lifecycle_action_heartbeat(
        self,
        request: ess_20220222_models.RecordLifecycleActionHeartbeatRequest,
    ) -> ess_20220222_models.RecordLifecycleActionHeartbeatResponse:
        """
        Prolongs a lifecycle hook for Elastic Compute Service (ECS) instances.
        
        @param request: RecordLifecycleActionHeartbeatRequest
        @return: RecordLifecycleActionHeartbeatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.record_lifecycle_action_heartbeat_with_options(request, runtime)

    async def record_lifecycle_action_heartbeat_async(
        self,
        request: ess_20220222_models.RecordLifecycleActionHeartbeatRequest,
    ) -> ess_20220222_models.RecordLifecycleActionHeartbeatResponse:
        """
        Prolongs a lifecycle hook for Elastic Compute Service (ECS) instances.
        
        @param request: RecordLifecycleActionHeartbeatRequest
        @return: RecordLifecycleActionHeartbeatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.record_lifecycle_action_heartbeat_with_options_async(request, runtime)

    def remove_instances_with_options(
        self,
        request: ess_20220222_models.RemoveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RemoveInstancesResponse:
        """
        Before you call this operation, make sure that the following requirements are met:
        *   The scaling group is in the Active state.
        *   No scaling activity is in progress within the scaling group.
        > If no scaling activity is in progress within the scaling group, you can call the operation even within the cooldown period.
        *   If an ECS instance is automatically created by Auto Scaling, or if an ECS instance is manually added to a scaling group and managed by the scaling group, the ECS instance is stopped in economical mode or is released after the instance is removed from the scaling group.
        *   If an ECS instance is manually added to a scaling group and is not managed by the scaling group, the ECS instance is not stopped or released after the instance is removed from the scaling group.
        *   If the difference between the number of existing ECS instances specified by the TotalCapacity parameter and the number of ECS instances that you call this operation to remove is less than the value of the MinSize parameter, the call fails.
        A successful call only means that Auto Scaling accepts the request. The scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        
        @param request: RemoveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_policy):
            query['RemovePolicy'] = request.remove_policy
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RemoveInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_instances_with_options_async(
        self,
        request: ess_20220222_models.RemoveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RemoveInstancesResponse:
        """
        Before you call this operation, make sure that the following requirements are met:
        *   The scaling group is in the Active state.
        *   No scaling activity is in progress within the scaling group.
        > If no scaling activity is in progress within the scaling group, you can call the operation even within the cooldown period.
        *   If an ECS instance is automatically created by Auto Scaling, or if an ECS instance is manually added to a scaling group and managed by the scaling group, the ECS instance is stopped in economical mode or is released after the instance is removed from the scaling group.
        *   If an ECS instance is manually added to a scaling group and is not managed by the scaling group, the ECS instance is not stopped or released after the instance is removed from the scaling group.
        *   If the difference between the number of existing ECS instances specified by the TotalCapacity parameter and the number of ECS instances that you call this operation to remove is less than the value of the MinSize parameter, the call fails.
        A successful call only means that Auto Scaling accepts the request. The scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        
        @param request: RemoveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_policy):
            query['RemovePolicy'] = request.remove_policy
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RemoveInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_instances(
        self,
        request: ess_20220222_models.RemoveInstancesRequest,
    ) -> ess_20220222_models.RemoveInstancesResponse:
        """
        Before you call this operation, make sure that the following requirements are met:
        *   The scaling group is in the Active state.
        *   No scaling activity is in progress within the scaling group.
        > If no scaling activity is in progress within the scaling group, you can call the operation even within the cooldown period.
        *   If an ECS instance is automatically created by Auto Scaling, or if an ECS instance is manually added to a scaling group and managed by the scaling group, the ECS instance is stopped in economical mode or is released after the instance is removed from the scaling group.
        *   If an ECS instance is manually added to a scaling group and is not managed by the scaling group, the ECS instance is not stopped or released after the instance is removed from the scaling group.
        *   If the difference between the number of existing ECS instances specified by the TotalCapacity parameter and the number of ECS instances that you call this operation to remove is less than the value of the MinSize parameter, the call fails.
        A successful call only means that Auto Scaling accepts the request. The scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        
        @param request: RemoveInstancesRequest
        @return: RemoveInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_instances_with_options(request, runtime)

    async def remove_instances_async(
        self,
        request: ess_20220222_models.RemoveInstancesRequest,
    ) -> ess_20220222_models.RemoveInstancesResponse:
        """
        Before you call this operation, make sure that the following requirements are met:
        *   The scaling group is in the Active state.
        *   No scaling activity is in progress within the scaling group.
        > If no scaling activity is in progress within the scaling group, you can call the operation even within the cooldown period.
        *   If an ECS instance is automatically created by Auto Scaling, or if an ECS instance is manually added to a scaling group and managed by the scaling group, the ECS instance is stopped in economical mode or is released after the instance is removed from the scaling group.
        *   If an ECS instance is manually added to a scaling group and is not managed by the scaling group, the ECS instance is not stopped or released after the instance is removed from the scaling group.
        *   If the difference between the number of existing ECS instances specified by the TotalCapacity parameter and the number of ECS instances that you call this operation to remove is less than the value of the MinSize parameter, the call fails.
        A successful call only means that Auto Scaling accepts the request. The scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        
        @param request: RemoveInstancesRequest
        @return: RemoveInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_instances_with_options_async(request, runtime)

    def resume_processes_with_options(
        self,
        request: ess_20220222_models.ResumeProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ResumeProcessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ResumeProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_processes_with_options_async(
        self,
        request: ess_20220222_models.ResumeProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ResumeProcessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ResumeProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_processes(
        self,
        request: ess_20220222_models.ResumeProcessesRequest,
    ) -> ess_20220222_models.ResumeProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_processes_with_options(request, runtime)

    async def resume_processes_async(
        self,
        request: ess_20220222_models.ResumeProcessesRequest,
    ) -> ess_20220222_models.ResumeProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_processes_with_options_async(request, runtime)

    def scale_with_adjustment_with_options(
        self,
        request: ess_20220222_models.ScaleWithAdjustmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ScaleWithAdjustmentResponse:
        """
        Compared with the ExecuteScalingRule operation, the ScaleWithAdjustment operation does not require a scaling rule to be created in advance. Before you call the ScaleWithAdjustment operation, take note of the following items:
        *   The following conditions must be met:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        *   If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        *   If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        *   If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the `ScalingActivityId` parameter in the response.
        
        @param request: ScaleWithAdjustmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleWithAdjustmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.sync_activity):
            query['SyncActivity'] = request.sync_activity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleWithAdjustment',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ScaleWithAdjustmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_with_adjustment_with_options_async(
        self,
        request: ess_20220222_models.ScaleWithAdjustmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ScaleWithAdjustmentResponse:
        """
        Compared with the ExecuteScalingRule operation, the ScaleWithAdjustment operation does not require a scaling rule to be created in advance. Before you call the ScaleWithAdjustment operation, take note of the following items:
        *   The following conditions must be met:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        *   If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        *   If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        *   If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the `ScalingActivityId` parameter in the response.
        
        @param request: ScaleWithAdjustmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleWithAdjustmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.sync_activity):
            query['SyncActivity'] = request.sync_activity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleWithAdjustment',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ScaleWithAdjustmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_with_adjustment(
        self,
        request: ess_20220222_models.ScaleWithAdjustmentRequest,
    ) -> ess_20220222_models.ScaleWithAdjustmentResponse:
        """
        Compared with the ExecuteScalingRule operation, the ScaleWithAdjustment operation does not require a scaling rule to be created in advance. Before you call the ScaleWithAdjustment operation, take note of the following items:
        *   The following conditions must be met:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        *   If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        *   If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        *   If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the `ScalingActivityId` parameter in the response.
        
        @param request: ScaleWithAdjustmentRequest
        @return: ScaleWithAdjustmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.scale_with_adjustment_with_options(request, runtime)

    async def scale_with_adjustment_async(
        self,
        request: ess_20220222_models.ScaleWithAdjustmentRequest,
    ) -> ess_20220222_models.ScaleWithAdjustmentResponse:
        """
        Compared with the ExecuteScalingRule operation, the ScaleWithAdjustment operation does not require a scaling rule to be created in advance. Before you call the ScaleWithAdjustment operation, take note of the following items:
        *   The following conditions must be met:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        *   If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        *   If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        *   If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the `ScalingActivityId` parameter in the response.
        
        @param request: ScaleWithAdjustmentRequest
        @return: ScaleWithAdjustmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.scale_with_adjustment_with_options_async(request, runtime)

    def set_group_deletion_protection_with_options(
        self,
        request: ess_20220222_models.SetGroupDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetGroupDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGroupDeletionProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetGroupDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_group_deletion_protection_with_options_async(
        self,
        request: ess_20220222_models.SetGroupDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetGroupDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGroupDeletionProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetGroupDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_group_deletion_protection(
        self,
        request: ess_20220222_models.SetGroupDeletionProtectionRequest,
    ) -> ess_20220222_models.SetGroupDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_group_deletion_protection_with_options(request, runtime)

    async def set_group_deletion_protection_async(
        self,
        request: ess_20220222_models.SetGroupDeletionProtectionRequest,
    ) -> ess_20220222_models.SetGroupDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_group_deletion_protection_with_options_async(request, runtime)

    def set_instance_health_with_options(
        self,
        request: ess_20220222_models.SetInstanceHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetInstanceHealthResponse:
        """
        Configures the health check feature for Elastic Compute Service (ECS) instances.
        
        @param request: SetInstanceHealthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstanceHealthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstanceHealth',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstanceHealthResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instance_health_with_options_async(
        self,
        request: ess_20220222_models.SetInstanceHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetInstanceHealthResponse:
        """
        Configures the health check feature for Elastic Compute Service (ECS) instances.
        
        @param request: SetInstanceHealthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstanceHealthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstanceHealth',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstanceHealthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instance_health(
        self,
        request: ess_20220222_models.SetInstanceHealthRequest,
    ) -> ess_20220222_models.SetInstanceHealthResponse:
        """
        Configures the health check feature for Elastic Compute Service (ECS) instances.
        
        @param request: SetInstanceHealthRequest
        @return: SetInstanceHealthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_instance_health_with_options(request, runtime)

    async def set_instance_health_async(
        self,
        request: ess_20220222_models.SetInstanceHealthRequest,
    ) -> ess_20220222_models.SetInstanceHealthResponse:
        """
        Configures the health check feature for Elastic Compute Service (ECS) instances.
        
        @param request: SetInstanceHealthRequest
        @return: SetInstanceHealthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_health_with_options_async(request, runtime)

    def set_instances_protection_with_options(
        self,
        request: ess_20220222_models.SetInstancesProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetInstancesProtectionResponse:
        """
        Puts one or more Elastic Compute Service (ECS) instances into the Protected state.
        
        @param request: SetInstancesProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstancesProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protected_from_scale_in):
            query['ProtectedFromScaleIn'] = request.protected_from_scale_in
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstancesProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstancesProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instances_protection_with_options_async(
        self,
        request: ess_20220222_models.SetInstancesProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetInstancesProtectionResponse:
        """
        Puts one or more Elastic Compute Service (ECS) instances into the Protected state.
        
        @param request: SetInstancesProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstancesProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protected_from_scale_in):
            query['ProtectedFromScaleIn'] = request.protected_from_scale_in
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstancesProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstancesProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instances_protection(
        self,
        request: ess_20220222_models.SetInstancesProtectionRequest,
    ) -> ess_20220222_models.SetInstancesProtectionResponse:
        """
        Puts one or more Elastic Compute Service (ECS) instances into the Protected state.
        
        @param request: SetInstancesProtectionRequest
        @return: SetInstancesProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_instances_protection_with_options(request, runtime)

    async def set_instances_protection_async(
        self,
        request: ess_20220222_models.SetInstancesProtectionRequest,
    ) -> ess_20220222_models.SetInstancesProtectionResponse:
        """
        Puts one or more Elastic Compute Service (ECS) instances into the Protected state.
        
        @param request: SetInstancesProtectionRequest
        @return: SetInstancesProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_instances_protection_with_options_async(request, runtime)

    def suspend_processes_with_options(
        self,
        request: ess_20220222_models.SuspendProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SuspendProcessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SuspendProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_processes_with_options_async(
        self,
        request: ess_20220222_models.SuspendProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SuspendProcessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SuspendProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_processes(
        self,
        request: ess_20220222_models.SuspendProcessesRequest,
    ) -> ess_20220222_models.SuspendProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_processes_with_options(request, runtime)

    async def suspend_processes_async(
        self,
        request: ess_20220222_models.SuspendProcessesRequest,
    ) -> ess_20220222_models.SuspendProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_processes_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ess_20220222_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ess_20220222_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ess_20220222_models.TagResourcesRequest,
    ) -> ess_20220222_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ess_20220222_models.TagResourcesRequest,
    ) -> ess_20220222_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ess_20220222_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ess_20220222_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ess_20220222_models.UntagResourcesRequest,
    ) -> ess_20220222_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ess_20220222_models.UntagResourcesRequest,
    ) -> ess_20220222_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def verify_authentication_with_options(
        self,
        request: ess_20220222_models.VerifyAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.VerifyAuthenticationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.only_check):
            query['OnlyCheck'] = request.only_check
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_authentication_with_options_async(
        self,
        request: ess_20220222_models.VerifyAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.VerifyAuthenticationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.only_check):
            query['OnlyCheck'] = request.only_check
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
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyAuthenticationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_authentication(
        self,
        request: ess_20220222_models.VerifyAuthenticationRequest,
    ) -> ess_20220222_models.VerifyAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_authentication_with_options(request, runtime)

    async def verify_authentication_async(
        self,
        request: ess_20220222_models.VerifyAuthenticationRequest,
    ) -> ess_20220222_models.VerifyAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_authentication_with_options_async(request, runtime)

    def verify_user_with_options(
        self,
        request: ess_20220222_models.VerifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.VerifyUserResponse:
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
            action='VerifyUser',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_user_with_options_async(
        self,
        request: ess_20220222_models.VerifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.VerifyUserResponse:
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
            action='VerifyUser',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_user(
        self,
        request: ess_20220222_models.VerifyUserRequest,
    ) -> ess_20220222_models.VerifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_user_with_options(request, runtime)

    async def verify_user_async(
        self,
        request: ess_20220222_models.VerifyUserRequest,
    ) -> ess_20220222_models.VerifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_user_with_options_async(request, runtime)
