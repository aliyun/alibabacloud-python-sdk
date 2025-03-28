# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_dbaudit20191209 import models as yundun_dbaudit_20191209_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-dbaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def clear_instance_storage_with_options(
        self,
        request: yundun_dbaudit_20191209_models.ClearInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.ClearInstanceStorageResponse:
        """
        @summary 清理SLS存储空间
        
        @param request: ClearInstanceStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearInstanceStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_category):
            query['StorageCategory'] = request.storage_category
        if not UtilClient.is_unset(request.storage_space):
            query['StorageSpace'] = request.storage_space
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearInstanceStorage',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.ClearInstanceStorageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.ClearInstanceStorageResponse(),
                self.execute(params, req, runtime)
            )

    async def clear_instance_storage_with_options_async(
        self,
        request: yundun_dbaudit_20191209_models.ClearInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.ClearInstanceStorageResponse:
        """
        @summary 清理SLS存储空间
        
        @param request: ClearInstanceStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearInstanceStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_category):
            query['StorageCategory'] = request.storage_category
        if not UtilClient.is_unset(request.storage_space):
            query['StorageSpace'] = request.storage_space
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearInstanceStorage',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.ClearInstanceStorageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.ClearInstanceStorageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def clear_instance_storage(
        self,
        request: yundun_dbaudit_20191209_models.ClearInstanceStorageRequest,
    ) -> yundun_dbaudit_20191209_models.ClearInstanceStorageResponse:
        """
        @summary 清理SLS存储空间
        
        @param request: ClearInstanceStorageRequest
        @return: ClearInstanceStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clear_instance_storage_with_options(request, runtime)

    async def clear_instance_storage_async(
        self,
        request: yundun_dbaudit_20191209_models.ClearInstanceStorageRequest,
    ) -> yundun_dbaudit_20191209_models.ClearInstanceStorageResponse:
        """
        @summary 清理SLS存储空间
        
        @param request: ClearInstanceStorageRequest
        @return: ClearInstanceStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.clear_instance_storage_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse:
        """
        @summary 获取实例属性
        
        @param request: DescribeInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAttribute',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse:
        """
        @summary 获取实例属性
        
        @param request: DescribeInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAttribute',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_attribute(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstanceAttributeRequest,
    ) -> yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse:
        """
        @summary 获取实例属性
        
        @param request: DescribeInstanceAttributeRequest
        @return: DescribeInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstanceAttributeRequest,
    ) -> yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse:
        """
        @summary 获取实例属性
        
        @param request: DescribeInstanceAttributeRequest
        @return: DescribeInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instance_storage_with_options(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse:
        """
        @summary 获取存储大小
        
        @param request: DescribeInstanceStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStorage',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_storage_with_options_async(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse:
        """
        @summary 获取存储大小
        
        @param request: DescribeInstanceStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStorage',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_storage(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstanceStorageRequest,
    ) -> yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse:
        """
        @summary 获取存储大小
        
        @param request: DescribeInstanceStorageRequest
        @return: DescribeInstanceStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_storage_with_options(request, runtime)

    async def describe_instance_storage_async(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstanceStorageRequest,
    ) -> yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse:
        """
        @summary 获取存储大小
        
        @param request: DescribeInstanceStorageRequest
        @return: DescribeInstanceStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_storage_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.DescribeInstancesResponse:
        """
        @summary 获取实例列表
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.get_center_instance):
            query['GetCenterInstance'] = request.get_center_instance
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.DescribeInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.DescribeInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instances_with_options_async(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.DescribeInstancesResponse:
        """
        @summary 获取实例列表
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.get_center_instance):
            query['GetCenterInstance'] = request.get_center_instance
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.DescribeInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.DescribeInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instances(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstancesRequest,
    ) -> yundun_dbaudit_20191209_models.DescribeInstancesResponse:
        """
        @summary 获取实例列表
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: yundun_dbaudit_20191209_models.DescribeInstancesRequest,
    ) -> yundun_dbaudit_20191209_models.DescribeInstancesResponse:
        """
        @summary 获取实例列表
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: yundun_dbaudit_20191209_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20191209_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20191209_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-12-09',
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
                yundun_dbaudit_20191209_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                yundun_dbaudit_20191209_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: yundun_dbaudit_20191209_models.ListTagResourcesRequest,
    ) -> yundun_dbaudit_20191209_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: yundun_dbaudit_20191209_models.ListTagResourcesRequest,
    ) -> yundun_dbaudit_20191209_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)
