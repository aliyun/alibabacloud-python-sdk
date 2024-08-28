# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_milvus20231012 import models as milvus_20231012_models
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
        self._endpoint = self.get_endpoint('milvus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_access_control_list_with_options(
        self,
        request: milvus_20231012_models.DescribeAccessControlListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DescribeAccessControlListResponse:
        """
        @summary 获取Milvus公网访问ACL信息
        
        @param request: DescribeAccessControlListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessControlListResponse
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
            action='DescribeAccessControlList',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/milvus/describe_access_control_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DescribeAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_list_with_options_async(
        self,
        request: milvus_20231012_models.DescribeAccessControlListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DescribeAccessControlListResponse:
        """
        @summary 获取Milvus公网访问ACL信息
        
        @param request: DescribeAccessControlListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessControlListResponse
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
            action='DescribeAccessControlList',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/milvus/describe_access_control_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DescribeAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_control_list(
        self,
        request: milvus_20231012_models.DescribeAccessControlListRequest,
    ) -> milvus_20231012_models.DescribeAccessControlListResponse:
        """
        @summary 获取Milvus公网访问ACL信息
        
        @param request: DescribeAccessControlListRequest
        @return: DescribeAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_access_control_list_with_options(request, headers, runtime)

    async def describe_access_control_list_async(
        self,
        request: milvus_20231012_models.DescribeAccessControlListRequest,
    ) -> milvus_20231012_models.DescribeAccessControlListResponse:
        """
        @summary 获取Milvus公网访问ACL信息
        
        @param request: DescribeAccessControlListRequest
        @return: DescribeAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_access_control_list_with_options_async(request, headers, runtime)

    def describe_instance_configs_with_options(
        self,
        request: milvus_20231012_models.DescribeInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DescribeInstanceConfigsResponse:
        """
        @summary 查询实例用户配置
        
        @param request: DescribeInstanceConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceConfigsResponse
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
            action='DescribeInstanceConfigs',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/config/describe_milvus_user_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DescribeInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_configs_with_options_async(
        self,
        request: milvus_20231012_models.DescribeInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DescribeInstanceConfigsResponse:
        """
        @summary 查询实例用户配置
        
        @param request: DescribeInstanceConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceConfigsResponse
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
            action='DescribeInstanceConfigs',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/config/describe_milvus_user_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DescribeInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_configs(
        self,
        request: milvus_20231012_models.DescribeInstanceConfigsRequest,
    ) -> milvus_20231012_models.DescribeInstanceConfigsResponse:
        """
        @summary 查询实例用户配置
        
        @param request: DescribeInstanceConfigsRequest
        @return: DescribeInstanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_configs_with_options(request, headers, runtime)

    async def describe_instance_configs_async(
        self,
        request: milvus_20231012_models.DescribeInstanceConfigsRequest,
    ) -> milvus_20231012_models.DescribeInstanceConfigsResponse:
        """
        @summary 查询实例用户配置
        
        @param request: DescribeInstanceConfigsRequest
        @return: DescribeInstanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_configs_with_options_async(request, headers, runtime)

    def get_instance_detail_with_options(
        self,
        request: milvus_20231012_models.GetInstanceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.GetInstanceDetailResponse:
        """
        @summary 根据集群ID获取集群的详细信息
        
        @param request: GetInstanceDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceDetailResponse
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
            action='GetInstanceDetail',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.GetInstanceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_detail_with_options_async(
        self,
        request: milvus_20231012_models.GetInstanceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.GetInstanceDetailResponse:
        """
        @summary 根据集群ID获取集群的详细信息
        
        @param request: GetInstanceDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceDetailResponse
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
            action='GetInstanceDetail',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.GetInstanceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_detail(
        self,
        request: milvus_20231012_models.GetInstanceDetailRequest,
    ) -> milvus_20231012_models.GetInstanceDetailResponse:
        """
        @summary 根据集群ID获取集群的详细信息
        
        @param request: GetInstanceDetailRequest
        @return: GetInstanceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_detail_with_options(request, headers, runtime)

    async def get_instance_detail_async(
        self,
        request: milvus_20231012_models.GetInstanceDetailRequest,
    ) -> milvus_20231012_models.GetInstanceDetailResponse:
        """
        @summary 根据集群ID获取集群的详细信息
        
        @param request: GetInstanceDetailRequest
        @return: GetInstanceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_detail_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: milvus_20231012_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ListInstancesResponse:
        """
        @summary 根据集群ID或者名称等信息过滤集群
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/order/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: milvus_20231012_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ListInstancesResponse:
        """
        @summary 根据集群ID或者名称等信息过滤集群
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/order/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: milvus_20231012_models.ListInstancesRequest,
    ) -> milvus_20231012_models.ListInstancesResponse:
        """
        @summary 根据集群ID或者名称等信息过滤集群
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: milvus_20231012_models.ListInstancesRequest,
    ) -> milvus_20231012_models.ListInstancesResponse:
        """
        @summary 根据集群ID或者名称等信息过滤集群
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def modify_instance_config_with_options(
        self,
        request: milvus_20231012_models.ModifyInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyInstanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/config/modify_milvus_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: milvus_20231012_models.ModifyInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyInstanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/config/modify_milvus_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: milvus_20231012_models.ModifyInstanceConfigRequest,
    ) -> milvus_20231012_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_instance_config_with_options(request, headers, runtime)

    async def modify_instance_config_async(
        self,
        request: milvus_20231012_models.ModifyInstanceConfigRequest,
    ) -> milvus_20231012_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_instance_config_with_options_async(request, headers, runtime)

    def update_access_control_list_with_options(
        self,
        request: milvus_20231012_models.UpdateAccessControlListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateAccessControlListResponse:
        """
        @summary 更新Milvus公网访问ACL信息
        
        @param request: UpdateAccessControlListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccessControlListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessControlList',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/milvus/update_access_control_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_access_control_list_with_options_async(
        self,
        request: milvus_20231012_models.UpdateAccessControlListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateAccessControlListResponse:
        """
        @summary 更新Milvus公网访问ACL信息
        
        @param request: UpdateAccessControlListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccessControlListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessControlList',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/milvus/update_access_control_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_access_control_list(
        self,
        request: milvus_20231012_models.UpdateAccessControlListRequest,
    ) -> milvus_20231012_models.UpdateAccessControlListResponse:
        """
        @summary 更新Milvus公网访问ACL信息
        
        @param request: UpdateAccessControlListRequest
        @return: UpdateAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_access_control_list_with_options(request, headers, runtime)

    async def update_access_control_list_async(
        self,
        request: milvus_20231012_models.UpdateAccessControlListRequest,
    ) -> milvus_20231012_models.UpdateAccessControlListResponse:
        """
        @summary 更新Milvus公网访问ACL信息
        
        @param request: UpdateAccessControlListRequest
        @return: UpdateAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_access_control_list_with_options_async(request, headers, runtime)

    def update_instance_name_with_options(
        self,
        request: milvus_20231012_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateInstanceNameResponse:
        """
        @summary 修改集群名称
        
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
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        request: milvus_20231012_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateInstanceNameResponse:
        """
        @summary 修改集群名称
        
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
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        request: milvus_20231012_models.UpdateInstanceNameRequest,
    ) -> milvus_20231012_models.UpdateInstanceNameResponse:
        """
        @summary 修改集群名称
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(request, headers, runtime)

    async def update_instance_name_async(
        self,
        request: milvus_20231012_models.UpdateInstanceNameRequest,
    ) -> milvus_20231012_models.UpdateInstanceNameResponse:
        """
        @summary 修改集群名称
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_name_with_options_async(request, headers, runtime)

    def update_public_network_status_with_options(
        self,
        request: milvus_20231012_models.UpdatePublicNetworkStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdatePublicNetworkStatusResponse:
        """
        @summary 该接口用于开通/关闭 Proxy的公网SLB。
        
        @param request: UpdatePublicNetworkStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicNetworkStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicNetworkStatus',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/network/updatePublicNetworkStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdatePublicNetworkStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_network_status_with_options_async(
        self,
        request: milvus_20231012_models.UpdatePublicNetworkStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdatePublicNetworkStatusResponse:
        """
        @summary 该接口用于开通/关闭 Proxy的公网SLB。
        
        @param request: UpdatePublicNetworkStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicNetworkStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicNetworkStatus',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/network/updatePublicNetworkStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdatePublicNetworkStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_network_status(
        self,
        request: milvus_20231012_models.UpdatePublicNetworkStatusRequest,
    ) -> milvus_20231012_models.UpdatePublicNetworkStatusResponse:
        """
        @summary 该接口用于开通/关闭 Proxy的公网SLB。
        
        @param request: UpdatePublicNetworkStatusRequest
        @return: UpdatePublicNetworkStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_network_status_with_options(request, headers, runtime)

    async def update_public_network_status_async(
        self,
        request: milvus_20231012_models.UpdatePublicNetworkStatusRequest,
    ) -> milvus_20231012_models.UpdatePublicNetworkStatusResponse:
        """
        @summary 该接口用于开通/关闭 Proxy的公网SLB。
        
        @param request: UpdatePublicNetworkStatusRequest
        @return: UpdatePublicNetworkStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_public_network_status_with_options_async(request, headers, runtime)
