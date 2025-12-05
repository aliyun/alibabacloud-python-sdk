# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_starrocks20221019 import models as starrocks_20221019_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('starrocks', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: starrocks_20221019_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceGroup/change',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: starrocks_20221019_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceGroup/change',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: starrocks_20221019_models.ChangeResourceGroupRequest,
    ) -> starrocks_20221019_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: starrocks_20221019_models.ChangeResourceGroupRequest,
    ) -> starrocks_20221019_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_instance_v1with_options(
        self,
        request: starrocks_20221019_models.CreateInstanceV1Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.CreateInstanceV1Response:
        """
        @summary 创建StarRocks集群
        
        @param request: CreateInstanceV1Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceV1Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.admin_password):
            body['AdminPassword'] = request.admin_password
        if not UtilClient.is_unset(request.agent_node_group):
            body['AgentNodeGroup'] = request.agent_node_group
        if not UtilClient.is_unset(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backend_node_groups):
            body['BackendNodeGroups'] = request.backend_node_groups
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dlf_catalog_name):
            body['DlfCatalogName'] = request.dlf_catalog_name
        if not UtilClient.is_unset(request.dlf_catalog_type):
            body['DlfCatalogType'] = request.dlf_catalog_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.encrypted):
            body['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.frontend_node_groups):
            body['FrontendNodeGroups'] = request.frontend_node_groups
        if not UtilClient.is_unset(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.kms_key_id):
            body['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.linked_ram_user_name):
            body['LinkedRamUserName'] = request.linked_ram_user_name
        if not UtilClient.is_unset(request.observer_node_groups):
            body['ObserverNodeGroups'] = request.observer_node_groups
        if not UtilClient.is_unset(request.oss_accessing_role_name):
            body['OssAccessingRoleName'] = request.oss_accessing_role_name
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.pay_type):
            body['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.promotion_option_no):
            body['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.ram_user_id):
            body['RamUserId'] = request.ram_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.run_mode):
            body['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceV1',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/createV1',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.CreateInstanceV1Response(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_v1with_options_async(
        self,
        request: starrocks_20221019_models.CreateInstanceV1Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.CreateInstanceV1Response:
        """
        @summary 创建StarRocks集群
        
        @param request: CreateInstanceV1Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceV1Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.admin_password):
            body['AdminPassword'] = request.admin_password
        if not UtilClient.is_unset(request.agent_node_group):
            body['AgentNodeGroup'] = request.agent_node_group
        if not UtilClient.is_unset(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backend_node_groups):
            body['BackendNodeGroups'] = request.backend_node_groups
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dlf_catalog_name):
            body['DlfCatalogName'] = request.dlf_catalog_name
        if not UtilClient.is_unset(request.dlf_catalog_type):
            body['DlfCatalogType'] = request.dlf_catalog_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.encrypted):
            body['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.frontend_node_groups):
            body['FrontendNodeGroups'] = request.frontend_node_groups
        if not UtilClient.is_unset(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.kms_key_id):
            body['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.linked_ram_user_name):
            body['LinkedRamUserName'] = request.linked_ram_user_name
        if not UtilClient.is_unset(request.observer_node_groups):
            body['ObserverNodeGroups'] = request.observer_node_groups
        if not UtilClient.is_unset(request.oss_accessing_role_name):
            body['OssAccessingRoleName'] = request.oss_accessing_role_name
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.pay_type):
            body['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.promotion_option_no):
            body['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.ram_user_id):
            body['RamUserId'] = request.ram_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.run_mode):
            body['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceV1',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/createV1',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.CreateInstanceV1Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_v1(
        self,
        request: starrocks_20221019_models.CreateInstanceV1Request,
    ) -> starrocks_20221019_models.CreateInstanceV1Response:
        """
        @summary 创建StarRocks集群
        
        @param request: CreateInstanceV1Request
        @return: CreateInstanceV1Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_v1with_options(request, headers, runtime)

    async def create_instance_v1_async(
        self,
        request: starrocks_20221019_models.CreateInstanceV1Request,
    ) -> starrocks_20221019_models.CreateInstanceV1Response:
        """
        @summary 创建StarRocks集群
        
        @param request: CreateInstanceV1Request
        @return: CreateInstanceV1Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_v1with_options_async(request, headers, runtime)

    def create_service_linked_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.CreateServiceLinkedRoleResponse:
        """
        @summary 为用户创建AliyunServiceRoleForEMRStarRocks
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/user/create_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.CreateServiceLinkedRoleResponse:
        """
        @summary 为用户创建AliyunServiceRoleForEMRStarRocks
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/user/create_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(self) -> starrocks_20221019_models.CreateServiceLinkedRoleResponse:
        """
        @summary 为用户创建AliyunServiceRoleForEMRStarRocks
        
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_linked_role_with_options(headers, runtime)

    async def create_service_linked_role_async(self) -> starrocks_20221019_models.CreateServiceLinkedRoleResponse:
        """
        @summary 为用户创建AliyunServiceRoleForEMRStarRocks
        
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_linked_role_with_options_async(headers, runtime)

    def describe_instances_with_options(
        self,
        tmp_req: starrocks_20221019_models.DescribeInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.DescribeInstancesResponse:
        """
        @summary 根据集群ID或者名称等信息过滤集群
        
        @param tmp_req: DescribeInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = starrocks_20221019_models.DescribeInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/starrocks/describeInstances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        tmp_req: starrocks_20221019_models.DescribeInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.DescribeInstancesResponse:
        """
        @summary 根据集群ID或者名称等信息过滤集群
        
        @param tmp_req: DescribeInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = starrocks_20221019_models.DescribeInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/starrocks/describeInstances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: starrocks_20221019_models.DescribeInstancesRequest,
    ) -> starrocks_20221019_models.DescribeInstancesResponse:
        """
        @summary 根据集群ID或者名称等信息过滤集群
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instances_with_options(request, headers, runtime)

    async def describe_instances_async(
        self,
        request: starrocks_20221019_models.DescribeInstancesRequest,
    ) -> starrocks_20221019_models.DescribeInstancesResponse:
        """
        @summary 根据集群ID或者名称等信息过滤集群
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instances_with_options_async(request, headers, runtime)

    def describe_node_groups_with_options(
        self,
        request: starrocks_20221019_models.DescribeNodeGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.DescribeNodeGroupsResponse:
        """
        @summary 获取节点组信息
        
        @param request: DescribeNodeGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.component_type):
            body['componentType'] = request.component_type
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_ids):
            body['nodeGroupIds'] = request.node_group_ids
        if not UtilClient.is_unset(request.node_group_name):
            body['nodeGroupName'] = request.node_group_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodeGroups',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/nodegroup/describeNodeGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.DescribeNodeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_groups_with_options_async(
        self,
        request: starrocks_20221019_models.DescribeNodeGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.DescribeNodeGroupsResponse:
        """
        @summary 获取节点组信息
        
        @param request: DescribeNodeGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.component_type):
            body['componentType'] = request.component_type
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_ids):
            body['nodeGroupIds'] = request.node_group_ids
        if not UtilClient.is_unset(request.node_group_name):
            body['nodeGroupName'] = request.node_group_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodeGroups',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/nodegroup/describeNodeGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.DescribeNodeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_groups(
        self,
        request: starrocks_20221019_models.DescribeNodeGroupsRequest,
    ) -> starrocks_20221019_models.DescribeNodeGroupsResponse:
        """
        @summary 获取节点组信息
        
        @param request: DescribeNodeGroupsRequest
        @return: DescribeNodeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_node_groups_with_options(request, headers, runtime)

    async def describe_node_groups_async(
        self,
        request: starrocks_20221019_models.DescribeNodeGroupsRequest,
    ) -> starrocks_20221019_models.DescribeNodeGroupsResponse:
        """
        @summary 获取节点组信息
        
        @param request: DescribeNodeGroupsRequest
        @return: DescribeNodeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_node_groups_with_options_async(request, headers, runtime)

    def modify_cu_with_options(
        self,
        request: starrocks_20221019_models.ModifyCuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyCuResponse:
        """
        @summary Modifies the number of CUs for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances.
        Before you call this operation, take note of the following items:
        You can modify the number of CUs for a warehouse of only StarRocks instances of Standard Edition.
        You can increase the number of disks only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you modify the number of CUs for a warehouse, the billing of CUs has the following changes:
        Pay-as-you-go StarRocks instances: You are charged based on the number of CUs.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of CUs before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyCuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCu',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyCu',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyCuResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cu_with_options_async(
        self,
        request: starrocks_20221019_models.ModifyCuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyCuResponse:
        """
        @summary Modifies the number of CUs for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances.
        Before you call this operation, take note of the following items:
        You can modify the number of CUs for a warehouse of only StarRocks instances of Standard Edition.
        You can increase the number of disks only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you modify the number of CUs for a warehouse, the billing of CUs has the following changes:
        Pay-as-you-go StarRocks instances: You are charged based on the number of CUs.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of CUs before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyCuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCu',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyCu',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyCuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cu(
        self,
        request: starrocks_20221019_models.ModifyCuRequest,
    ) -> starrocks_20221019_models.ModifyCuResponse:
        """
        @summary Modifies the number of CUs for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances.
        Before you call this operation, take note of the following items:
        You can modify the number of CUs for a warehouse of only StarRocks instances of Standard Edition.
        You can increase the number of disks only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you modify the number of CUs for a warehouse, the billing of CUs has the following changes:
        Pay-as-you-go StarRocks instances: You are charged based on the number of CUs.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of CUs before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyCuRequest
        @return: ModifyCuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cu_with_options(request, headers, runtime)

    async def modify_cu_async(
        self,
        request: starrocks_20221019_models.ModifyCuRequest,
    ) -> starrocks_20221019_models.ModifyCuResponse:
        """
        @summary Modifies the number of CUs for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances.
        Before you call this operation, take note of the following items:
        You can modify the number of CUs for a warehouse of only StarRocks instances of Standard Edition.
        You can increase the number of disks only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you modify the number of CUs for a warehouse, the billing of CUs has the following changes:
        Pay-as-you-go StarRocks instances: You are charged based on the number of CUs.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of CUs before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyCuRequest
        @return: ModifyCuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cu_with_options_async(request, headers, runtime)

    def modify_cu_pre_check_with_options(
        self,
        request: starrocks_20221019_models.ModifyCuPreCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyCuPreCheckResponse:
        """
        @summary Performs a precheck before you modify the number of CUs for a warehouse.
        
        @param request: ModifyCuPreCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCuPreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCuPreCheck',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyCuPreCheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyCuPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cu_pre_check_with_options_async(
        self,
        request: starrocks_20221019_models.ModifyCuPreCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyCuPreCheckResponse:
        """
        @summary Performs a precheck before you modify the number of CUs for a warehouse.
        
        @param request: ModifyCuPreCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCuPreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCuPreCheck',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyCuPreCheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyCuPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cu_pre_check(
        self,
        request: starrocks_20221019_models.ModifyCuPreCheckRequest,
    ) -> starrocks_20221019_models.ModifyCuPreCheckResponse:
        """
        @summary Performs a precheck before you modify the number of CUs for a warehouse.
        
        @param request: ModifyCuPreCheckRequest
        @return: ModifyCuPreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cu_pre_check_with_options(request, headers, runtime)

    async def modify_cu_pre_check_async(
        self,
        request: starrocks_20221019_models.ModifyCuPreCheckRequest,
    ) -> starrocks_20221019_models.ModifyCuPreCheckResponse:
        """
        @summary Performs a precheck before you modify the number of CUs for a warehouse.
        
        @param request: ModifyCuPreCheckRequest
        @return: ModifyCuPreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cu_pre_check_with_options_async(request, headers, runtime)

    def modify_disk_number_with_options(
        self,
        request: starrocks_20221019_models.ModifyDiskNumberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyDiskNumberResponse:
        """
        @summary Increases the number of disks for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can increase the number of disks only for StarRocks instances of Standard Edition.
        You can increase the number of disks only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you increase the number of disks for a warehouse, the billing of disks has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk type.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of disks before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskNumberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskNumber',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyDiskNumber',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyDiskNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_number_with_options_async(
        self,
        request: starrocks_20221019_models.ModifyDiskNumberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyDiskNumberResponse:
        """
        @summary Increases the number of disks for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can increase the number of disks only for StarRocks instances of Standard Edition.
        You can increase the number of disks only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you increase the number of disks for a warehouse, the billing of disks has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk type.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of disks before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskNumberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskNumber',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyDiskNumber',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyDiskNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_number(
        self,
        request: starrocks_20221019_models.ModifyDiskNumberRequest,
    ) -> starrocks_20221019_models.ModifyDiskNumberResponse:
        """
        @summary Increases the number of disks for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can increase the number of disks only for StarRocks instances of Standard Edition.
        You can increase the number of disks only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you increase the number of disks for a warehouse, the billing of disks has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk type.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of disks before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskNumberRequest
        @return: ModifyDiskNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_disk_number_with_options(request, headers, runtime)

    async def modify_disk_number_async(
        self,
        request: starrocks_20221019_models.ModifyDiskNumberRequest,
    ) -> starrocks_20221019_models.ModifyDiskNumberResponse:
        """
        @summary Increases the number of disks for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can increase the number of disks only for StarRocks instances of Standard Edition.
        You can increase the number of disks only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you increase the number of disks for a warehouse, the billing of disks has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk type.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of disks before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskNumberRequest
        @return: ModifyDiskNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_disk_number_with_options_async(request, headers, runtime)

    def modify_disk_performance_level_with_options(
        self,
        request: starrocks_20221019_models.ModifyDiskPerformanceLevelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyDiskPerformanceLevelResponse:
        """
        @summary Modifies the disk performance level for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/en/product/ecs?_p_lc=1&spm=openapi-amp.newDocPublishment.0.0.47c9281fkIZGiB#pricing) of EMR Serverless StarRocks instances.
        Before you call this operation, take note of the following items:
        You can modify the disk performance level only for StarRocks instances of Standard Edition.
        You can modify the disk performance level only for warehouses of the standard specifications.
        The instance must be in the Running state.
        You cannot downgrade the performance level to PL0.
        The performance level of an Enterprise SSD (ESSD) is limited by the ESSD disk size. If you cannot upgrade the performance level of an ESSD, expand the ESSD and try again. For more information, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        After the disk performance level is changed, the billing of the disk has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk type.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the disk performance level before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskPerformanceLevelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskPerformanceLevelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskPerformanceLevel',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyDiskPerformanceLevel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyDiskPerformanceLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_performance_level_with_options_async(
        self,
        request: starrocks_20221019_models.ModifyDiskPerformanceLevelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyDiskPerformanceLevelResponse:
        """
        @summary Modifies the disk performance level for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/en/product/ecs?_p_lc=1&spm=openapi-amp.newDocPublishment.0.0.47c9281fkIZGiB#pricing) of EMR Serverless StarRocks instances.
        Before you call this operation, take note of the following items:
        You can modify the disk performance level only for StarRocks instances of Standard Edition.
        You can modify the disk performance level only for warehouses of the standard specifications.
        The instance must be in the Running state.
        You cannot downgrade the performance level to PL0.
        The performance level of an Enterprise SSD (ESSD) is limited by the ESSD disk size. If you cannot upgrade the performance level of an ESSD, expand the ESSD and try again. For more information, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        After the disk performance level is changed, the billing of the disk has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk type.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the disk performance level before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskPerformanceLevelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskPerformanceLevelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskPerformanceLevel',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyDiskPerformanceLevel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyDiskPerformanceLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_performance_level(
        self,
        request: starrocks_20221019_models.ModifyDiskPerformanceLevelRequest,
    ) -> starrocks_20221019_models.ModifyDiskPerformanceLevelResponse:
        """
        @summary Modifies the disk performance level for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/en/product/ecs?_p_lc=1&spm=openapi-amp.newDocPublishment.0.0.47c9281fkIZGiB#pricing) of EMR Serverless StarRocks instances.
        Before you call this operation, take note of the following items:
        You can modify the disk performance level only for StarRocks instances of Standard Edition.
        You can modify the disk performance level only for warehouses of the standard specifications.
        The instance must be in the Running state.
        You cannot downgrade the performance level to PL0.
        The performance level of an Enterprise SSD (ESSD) is limited by the ESSD disk size. If you cannot upgrade the performance level of an ESSD, expand the ESSD and try again. For more information, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        After the disk performance level is changed, the billing of the disk has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk type.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the disk performance level before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskPerformanceLevelRequest
        @return: ModifyDiskPerformanceLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_disk_performance_level_with_options(request, headers, runtime)

    async def modify_disk_performance_level_async(
        self,
        request: starrocks_20221019_models.ModifyDiskPerformanceLevelRequest,
    ) -> starrocks_20221019_models.ModifyDiskPerformanceLevelResponse:
        """
        @summary Modifies the disk performance level for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/en/product/ecs?_p_lc=1&spm=openapi-amp.newDocPublishment.0.0.47c9281fkIZGiB#pricing) of EMR Serverless StarRocks instances.
        Before you call this operation, take note of the following items:
        You can modify the disk performance level only for StarRocks instances of Standard Edition.
        You can modify the disk performance level only for warehouses of the standard specifications.
        The instance must be in the Running state.
        You cannot downgrade the performance level to PL0.
        The performance level of an Enterprise SSD (ESSD) is limited by the ESSD disk size. If you cannot upgrade the performance level of an ESSD, expand the ESSD and try again. For more information, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        After the disk performance level is changed, the billing of the disk has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk type.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the disk performance level before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskPerformanceLevelRequest
        @return: ModifyDiskPerformanceLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_disk_performance_level_with_options_async(request, headers, runtime)

    def modify_disk_size_with_options(
        self,
        request: starrocks_20221019_models.ModifyDiskSizeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyDiskSizeResponse:
        """
        @summary Expands the disk size for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can expand the disk size only for StarRocks instances of Standard Edition.
        You can expand the disk size only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you expand the disk size, the billing of disks has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk size.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the disk size before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskSizeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskSizeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskSize',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyDiskSize',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyDiskSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_size_with_options_async(
        self,
        request: starrocks_20221019_models.ModifyDiskSizeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyDiskSizeResponse:
        """
        @summary Expands the disk size for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can expand the disk size only for StarRocks instances of Standard Edition.
        You can expand the disk size only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you expand the disk size, the billing of disks has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk size.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the disk size before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskSizeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskSizeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskSize',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyDiskSize',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyDiskSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_size(
        self,
        request: starrocks_20221019_models.ModifyDiskSizeRequest,
    ) -> starrocks_20221019_models.ModifyDiskSizeResponse:
        """
        @summary Expands the disk size for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can expand the disk size only for StarRocks instances of Standard Edition.
        You can expand the disk size only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you expand the disk size, the billing of disks has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk size.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the disk size before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskSizeRequest
        @return: ModifyDiskSizeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_disk_size_with_options(request, headers, runtime)

    async def modify_disk_size_async(
        self,
        request: starrocks_20221019_models.ModifyDiskSizeRequest,
    ) -> starrocks_20221019_models.ModifyDiskSizeResponse:
        """
        @summary Expands the disk size for a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can expand the disk size only for StarRocks instances of Standard Edition.
        You can expand the disk size only for warehouses of the standard specifications.
        The instance must be in the Running state.
        After you expand the disk size, the billing of disks has the following changes:
        Pay-as-you-go StarRocks instances: You are charged for the disk based on the new disk size.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the disk size before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyDiskSizeRequest
        @return: ModifyDiskSizeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_disk_size_with_options_async(request, headers, runtime)

    def modify_node_number_with_options(
        self,
        request: starrocks_20221019_models.ModifyNodeNumberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyNodeNumberResponse:
        """
        @summary Modifies the number of nodes in a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can modify the number of nodes in a warehouse of only StarRocks instances of Standard Edition.
        The instance must be in the Running state.
        The number of frontend nodes (FEs) cannot be an even number, and you cannot reduce the number of FE nodes.
        After you modify the number of nodes in a warehouse, the billing of nodes has the following changes:
        Pay-as-you-go StarRocks instances: You are charged based on the number of nodes.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of nodes before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyNodeNumberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNodeNumber',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyNodeNumber',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyNodeNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_number_with_options_async(
        self,
        request: starrocks_20221019_models.ModifyNodeNumberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyNodeNumberResponse:
        """
        @summary Modifies the number of nodes in a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can modify the number of nodes in a warehouse of only StarRocks instances of Standard Edition.
        The instance must be in the Running state.
        The number of frontend nodes (FEs) cannot be an even number, and you cannot reduce the number of FE nodes.
        After you modify the number of nodes in a warehouse, the billing of nodes has the following changes:
        Pay-as-you-go StarRocks instances: You are charged based on the number of nodes.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of nodes before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyNodeNumberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNodeNumber',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyNodeNumber',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyNodeNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_number(
        self,
        request: starrocks_20221019_models.ModifyNodeNumberRequest,
    ) -> starrocks_20221019_models.ModifyNodeNumberResponse:
        """
        @summary Modifies the number of nodes in a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can modify the number of nodes in a warehouse of only StarRocks instances of Standard Edition.
        The instance must be in the Running state.
        The number of frontend nodes (FEs) cannot be an even number, and you cannot reduce the number of FE nodes.
        After you modify the number of nodes in a warehouse, the billing of nodes has the following changes:
        Pay-as-you-go StarRocks instances: You are charged based on the number of nodes.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of nodes before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyNodeNumberRequest
        @return: ModifyNodeNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_node_number_with_options(request, headers, runtime)

    async def modify_node_number_async(
        self,
        request: starrocks_20221019_models.ModifyNodeNumberRequest,
    ) -> starrocks_20221019_models.ModifyNodeNumberResponse:
        """
        @summary Modifies the number of nodes in a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [billable items](https://www.alibabacloud.com/help/en/emr/emr-serverless-starrocks/product-overview/billable-items?spm=a2c63.p38356.help-menu-28066.d_0_1_0.3aaf4b0b69jN1P) of EMR Serverless StarRocks instances. Before you call this operation, take note of the following items:
        You can modify the number of nodes in a warehouse of only StarRocks instances of Standard Edition.
        The instance must be in the Running state.
        The number of frontend nodes (FEs) cannot be an even number, and you cannot reduce the number of FE nodes.
        After you modify the number of nodes in a warehouse, the billing of nodes has the following changes:
        Pay-as-you-go StarRocks instances: You are charged based on the number of nodes.
        Subscription StarRocks instances: You are charged additionally based on the price difference between the number of nodes before and after the change and the remaining days of the billing cycle. The billing cycle starts from 00:00 the next day until the end of the subscription period.
        
        @param request: ModifyNodeNumberRequest
        @return: ModifyNodeNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_node_number_with_options_async(request, headers, runtime)

    def modify_node_number_pre_check_with_options(
        self,
        request: starrocks_20221019_models.ModifyNodeNumberPreCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyNodeNumberPreCheckResponse:
        """
        @summary Performs a precheck before you modify the number of nodes in a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @param request: ModifyNodeNumberPreCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeNumberPreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNodeNumberPreCheck',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyNodeNumberPreCheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyNodeNumberPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_number_pre_check_with_options_async(
        self,
        request: starrocks_20221019_models.ModifyNodeNumberPreCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ModifyNodeNumberPreCheckResponse:
        """
        @summary Performs a precheck before you modify the number of nodes in a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @param request: ModifyNodeNumberPreCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeNumberPreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNodeNumberPreCheck',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/resourceChange/modifyNodeNumberPreCheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ModifyNodeNumberPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_number_pre_check(
        self,
        request: starrocks_20221019_models.ModifyNodeNumberPreCheckRequest,
    ) -> starrocks_20221019_models.ModifyNodeNumberPreCheckResponse:
        """
        @summary Performs a precheck before you modify the number of nodes in a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @param request: ModifyNodeNumberPreCheckRequest
        @return: ModifyNodeNumberPreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_node_number_pre_check_with_options(request, headers, runtime)

    async def modify_node_number_pre_check_async(
        self,
        request: starrocks_20221019_models.ModifyNodeNumberPreCheckRequest,
    ) -> starrocks_20221019_models.ModifyNodeNumberPreCheckResponse:
        """
        @summary Performs a precheck before you modify the number of nodes in a warehouse of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @param request: ModifyNodeNumberPreCheckRequest
        @return: ModifyNodeNumberPreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_node_number_pre_check_with_options_async(request, headers, runtime)

    def query_upgradable_versions_with_options(
        self,
        request: starrocks_20221019_models.QueryUpgradableVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.QueryUpgradableVersionsResponse:
        """
        @summary Queries the versions of an E-MapReduce (EMR) Serverless StarRocks instance that the versions that you can upgrade to. The versions of a StarRocks instance include the major version and minor version. You can view the major version and minor version of a StarRocks instance in the Version Information section of the Instance Details tab in the EMR console. You can call this operation to query the minor versions or major versions that the versions that you can upgrade to.
        
        @param request: QueryUpgradableVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUpgradableVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.minor):
            query['Minor'] = request.minor
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUpgradableVersions',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/starrocks/queryUpgradableVersions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.QueryUpgradableVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_upgradable_versions_with_options_async(
        self,
        request: starrocks_20221019_models.QueryUpgradableVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.QueryUpgradableVersionsResponse:
        """
        @summary Queries the versions of an E-MapReduce (EMR) Serverless StarRocks instance that the versions that you can upgrade to. The versions of a StarRocks instance include the major version and minor version. You can view the major version and minor version of a StarRocks instance in the Version Information section of the Instance Details tab in the EMR console. You can call this operation to query the minor versions or major versions that the versions that you can upgrade to.
        
        @param request: QueryUpgradableVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUpgradableVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.minor):
            query['Minor'] = request.minor
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUpgradableVersions',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/starrocks/queryUpgradableVersions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.QueryUpgradableVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_upgradable_versions(
        self,
        request: starrocks_20221019_models.QueryUpgradableVersionsRequest,
    ) -> starrocks_20221019_models.QueryUpgradableVersionsResponse:
        """
        @summary Queries the versions of an E-MapReduce (EMR) Serverless StarRocks instance that the versions that you can upgrade to. The versions of a StarRocks instance include the major version and minor version. You can view the major version and minor version of a StarRocks instance in the Version Information section of the Instance Details tab in the EMR console. You can call this operation to query the minor versions or major versions that the versions that you can upgrade to.
        
        @param request: QueryUpgradableVersionsRequest
        @return: QueryUpgradableVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_upgradable_versions_with_options(request, headers, runtime)

    async def query_upgradable_versions_async(
        self,
        request: starrocks_20221019_models.QueryUpgradableVersionsRequest,
    ) -> starrocks_20221019_models.QueryUpgradableVersionsResponse:
        """
        @summary Queries the versions of an E-MapReduce (EMR) Serverless StarRocks instance that the versions that you can upgrade to. The versions of a StarRocks instance include the major version and minor version. You can view the major version and minor version of a StarRocks instance in the Version Information section of the Instance Details tab in the EMR console. You can call this operation to query the minor versions or major versions that the versions that you can upgrade to.
        
        @param request: QueryUpgradableVersionsRequest
        @return: QueryUpgradableVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_upgradable_versions_with_options_async(request, headers, runtime)

    def release_instance_with_options(
        self,
        request: starrocks_20221019_models.ReleaseInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ReleaseInstanceResponse:
        """
        @summary Releases a pay-as-you-go E-MapReduce (EMR) Serverless StarRocks instance. To unsubscribe from a subscription instance, go to the Unsubscribe page of the Expenses and Costs console.
        
        @description *\
        *Warning:** After an instance is released, all physical resources used by the instance are recycled. Relevant data is erased and cannot be restored.
        
        @param request: ReleaseInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: starrocks_20221019_models.ReleaseInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.ReleaseInstanceResponse:
        """
        @summary Releases a pay-as-you-go E-MapReduce (EMR) Serverless StarRocks instance. To unsubscribe from a subscription instance, go to the Unsubscribe page of the Expenses and Costs console.
        
        @description *\
        *Warning:** After an instance is released, all physical resources used by the instance are recycled. Relevant data is erased and cannot be restored.
        
        @param request: ReleaseInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: starrocks_20221019_models.ReleaseInstanceRequest,
    ) -> starrocks_20221019_models.ReleaseInstanceResponse:
        """
        @summary Releases a pay-as-you-go E-MapReduce (EMR) Serverless StarRocks instance. To unsubscribe from a subscription instance, go to the Unsubscribe page of the Expenses and Costs console.
        
        @description *\
        *Warning:** After an instance is released, all physical resources used by the instance are recycled. Relevant data is erased and cannot be restored.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_instance_with_options(request, headers, runtime)

    async def release_instance_async(
        self,
        request: starrocks_20221019_models.ReleaseInstanceRequest,
    ) -> starrocks_20221019_models.ReleaseInstanceResponse:
        """
        @summary Releases a pay-as-you-go E-MapReduce (EMR) Serverless StarRocks instance. To unsubscribe from a subscription instance, go to the Unsubscribe page of the Expenses and Costs console.
        
        @description *\
        *Warning:** After an instance is released, all physical resources used by the instance are recycled. Relevant data is erased and cannot be restored.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_instance_with_options_async(request, headers, runtime)

    def restart_instance_with_options(
        self,
        request: starrocks_20221019_models.RestartInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.RestartInstanceResponse:
        """
        @summary Restarts an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description This operation is an asynchronous operation. After you call this operation to restart a StarRocks instance, the operation sets the status of the instance to Restarting and begins the restart process. When the status of the instance changes to Running, the instance is restarted.
        
        @param request: RestartInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/starrocks/restartCluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: starrocks_20221019_models.RestartInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.RestartInstanceResponse:
        """
        @summary Restarts an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description This operation is an asynchronous operation. After you call this operation to restart a StarRocks instance, the operation sets the status of the instance to Restarting and begins the restart process. When the status of the instance changes to Running, the instance is restarted.
        
        @param request: RestartInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/starrocks/restartCluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: starrocks_20221019_models.RestartInstanceRequest,
    ) -> starrocks_20221019_models.RestartInstanceResponse:
        """
        @summary Restarts an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description This operation is an asynchronous operation. After you call this operation to restart a StarRocks instance, the operation sets the status of the instance to Restarting and begins the restart process. When the status of the instance changes to Running, the instance is restarted.
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(request, headers, runtime)

    async def restart_instance_async(
        self,
        request: starrocks_20221019_models.RestartInstanceRequest,
    ) -> starrocks_20221019_models.RestartInstanceResponse:
        """
        @summary Restarts an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @description This operation is an asynchronous operation. After you call this operation to restart a StarRocks instance, the operation sets the status of the instance to Restarting and begins the restart process. When the status of the instance changes to Running, the instance is restarted.
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_instance_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: starrocks_20221019_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.TagResourcesResponse:
        """
        @summary 打标
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: starrocks_20221019_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.TagResourcesResponse:
        """
        @summary 打标
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: starrocks_20221019_models.TagResourcesRequest,
    ) -> starrocks_20221019_models.TagResourcesResponse:
        """
        @summary 打标
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: starrocks_20221019_models.TagResourcesRequest,
    ) -> starrocks_20221019_models.TagResourcesResponse:
        """
        @summary 打标
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def un_tag_resources_with_options(
        self,
        tmp_req: starrocks_20221019_models.UnTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.UnTagResourcesResponse:
        """
        @summary 删除标签
        
        @param tmp_req: UnTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = starrocks_20221019_models.UnTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        tmp_req: starrocks_20221019_models.UnTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.UnTagResourcesResponse:
        """
        @summary 删除标签
        
        @param tmp_req: UnTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = starrocks_20221019_models.UnTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: starrocks_20221019_models.UnTagResourcesRequest,
    ) -> starrocks_20221019_models.UnTagResourcesResponse:
        """
        @summary 删除标签
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_tag_resources_with_options(request, headers, runtime)

    async def un_tag_resources_async(
        self,
        request: starrocks_20221019_models.UnTagResourcesRequest,
    ) -> starrocks_20221019_models.UnTagResourcesResponse:
        """
        @summary 删除标签
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_tag_resources_with_options_async(request, headers, runtime)

    def update_instance_name_with_options(
        self,
        request: starrocks_20221019_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.UpdateInstanceNameResponse:
        """
        @summary Modifies the name of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @param request: UpdateInstanceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        request: starrocks_20221019_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.UpdateInstanceNameResponse:
        """
        @summary Modifies the name of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @param request: UpdateInstanceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        request: starrocks_20221019_models.UpdateInstanceNameRequest,
    ) -> starrocks_20221019_models.UpdateInstanceNameResponse:
        """
        @summary Modifies the name of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(request, headers, runtime)

    async def update_instance_name_async(
        self,
        request: starrocks_20221019_models.UpdateInstanceNameRequest,
    ) -> starrocks_20221019_models.UpdateInstanceNameResponse:
        """
        @summary Modifies the name of an E-MapReduce (EMR) Serverless StarRocks instance.
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_name_with_options_async(request, headers, runtime)

    def upgrade_version_with_options(
        self,
        request: starrocks_20221019_models.UpgradeVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.UpgradeVersionResponse:
        """
        @summary Upgrades the version of an E-MapReduce (EMR) Serverless StarRocks instance. The versions of a StarRocks instance include the major version and minor version. You can view the major version and minor version of a StarRocks instance in the Version Information section of the Instance Details tab in the EMR console. This operation can be used to upgrade the minor version or major version of a StarRocks instance. You can call the QueryUpgradableVersions operation to query the versions that you can upgrade to.
        
        @description The instance must be in the Running state when you call this operation.
        
        @param request: UpgradeVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.minor):
            query['Minor'] = request.minor
        if not UtilClient.is_unset(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeVersion',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/starrocks/upgradeVersion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.UpgradeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_version_with_options_async(
        self,
        request: starrocks_20221019_models.UpgradeVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> starrocks_20221019_models.UpgradeVersionResponse:
        """
        @summary Upgrades the version of an E-MapReduce (EMR) Serverless StarRocks instance. The versions of a StarRocks instance include the major version and minor version. You can view the major version and minor version of a StarRocks instance in the Version Information section of the Instance Details tab in the EMR console. This operation can be used to upgrade the minor version or major version of a StarRocks instance. You can call the QueryUpgradableVersions operation to query the versions that you can upgrade to.
        
        @description The instance must be in the Running state when you call this operation.
        
        @param request: UpgradeVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.minor):
            query['Minor'] = request.minor
        if not UtilClient.is_unset(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeVersion',
            version='2022-10-19',
            protocol='HTTPS',
            pathname=f'/webapi/starrocks/upgradeVersion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            starrocks_20221019_models.UpgradeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_version(
        self,
        request: starrocks_20221019_models.UpgradeVersionRequest,
    ) -> starrocks_20221019_models.UpgradeVersionResponse:
        """
        @summary Upgrades the version of an E-MapReduce (EMR) Serverless StarRocks instance. The versions of a StarRocks instance include the major version and minor version. You can view the major version and minor version of a StarRocks instance in the Version Information section of the Instance Details tab in the EMR console. This operation can be used to upgrade the minor version or major version of a StarRocks instance. You can call the QueryUpgradableVersions operation to query the versions that you can upgrade to.
        
        @description The instance must be in the Running state when you call this operation.
        
        @param request: UpgradeVersionRequest
        @return: UpgradeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_version_with_options(request, headers, runtime)

    async def upgrade_version_async(
        self,
        request: starrocks_20221019_models.UpgradeVersionRequest,
    ) -> starrocks_20221019_models.UpgradeVersionResponse:
        """
        @summary Upgrades the version of an E-MapReduce (EMR) Serverless StarRocks instance. The versions of a StarRocks instance include the major version and minor version. You can view the major version and minor version of a StarRocks instance in the Version Information section of the Instance Details tab in the EMR console. This operation can be used to upgrade the minor version or major version of a StarRocks instance. You can call the QueryUpgradableVersions operation to query the versions that you can upgrade to.
        
        @description The instance must be in the Running state when you call this operation.
        
        @param request: UpgradeVersionRequest
        @return: UpgradeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_version_with_options_async(request, headers, runtime)
