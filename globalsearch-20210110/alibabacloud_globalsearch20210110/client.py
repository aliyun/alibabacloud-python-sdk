# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_globalsearch20210110 import models as global_search_20210110_models
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
        self._endpoint = self.get_endpoint('globalsearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def count_product_resources_with_options(
        self,
        request: global_search_20210110_models.CountProductResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.CountProductResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.released):
            query['Released'] = request.released
        if not UtilClient.is_unset(request.request):
            query['Request'] = request.request
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountProductResources',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.CountProductResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_product_resources_with_options_async(
        self,
        request: global_search_20210110_models.CountProductResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.CountProductResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.released):
            query['Released'] = request.released
        if not UtilClient.is_unset(request.request):
            query['Request'] = request.request
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountProductResources',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.CountProductResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_product_resources(
        self,
        request: global_search_20210110_models.CountProductResourcesRequest,
    ) -> global_search_20210110_models.CountProductResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_product_resources_with_options(request, runtime)

    async def count_product_resources_async(
        self,
        request: global_search_20210110_models.CountProductResourcesRequest,
    ) -> global_search_20210110_models.CountProductResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_product_resources_with_options_async(request, runtime)

    def describe_released_resources_with_options(
        self,
        request: global_search_20210110_models.DescribeReleasedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeReleasedResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail_attribute_names):
            query['DetailAttributeNames'] = request.detail_attribute_names
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReleasedResources',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeReleasedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_released_resources_with_options_async(
        self,
        request: global_search_20210110_models.DescribeReleasedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeReleasedResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail_attribute_names):
            query['DetailAttributeNames'] = request.detail_attribute_names
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReleasedResources',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeReleasedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_released_resources(
        self,
        request: global_search_20210110_models.DescribeReleasedResourcesRequest,
    ) -> global_search_20210110_models.DescribeReleasedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_released_resources_with_options(request, runtime)

    async def describe_released_resources_async(
        self,
        request: global_search_20210110_models.DescribeReleasedResourcesRequest,
    ) -> global_search_20210110_models.DescribeReleasedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_released_resources_with_options_async(request, runtime)

    def describe_resource_aggregations_with_options(
        self,
        request: global_search_20210110_models.DescribeResourceAggregationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeResourceAggregationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agg_action):
            query['AggAction'] = request.agg_action
        if not UtilClient.is_unset(request.aggregators):
            query['Aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceAggregations',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeResourceAggregationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_aggregations_with_options_async(
        self,
        request: global_search_20210110_models.DescribeResourceAggregationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeResourceAggregationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agg_action):
            query['AggAction'] = request.agg_action
        if not UtilClient.is_unset(request.aggregators):
            query['Aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceAggregations',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeResourceAggregationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_aggregations(
        self,
        request: global_search_20210110_models.DescribeResourceAggregationsRequest,
    ) -> global_search_20210110_models.DescribeResourceAggregationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_aggregations_with_options(request, runtime)

    async def describe_resource_aggregations_async(
        self,
        request: global_search_20210110_models.DescribeResourceAggregationsRequest,
    ) -> global_search_20210110_models.DescribeResourceAggregationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_aggregations_with_options_async(request, runtime)

    def describe_resource_filter_attributes_with_options(
        self,
        request: global_search_20210110_models.DescribeResourceFilterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeResourceFilterAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceFilterAttributes',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeResourceFilterAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_filter_attributes_with_options_async(
        self,
        request: global_search_20210110_models.DescribeResourceFilterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeResourceFilterAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceFilterAttributes',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeResourceFilterAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_filter_attributes(
        self,
        request: global_search_20210110_models.DescribeResourceFilterAttributesRequest,
    ) -> global_search_20210110_models.DescribeResourceFilterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_filter_attributes_with_options(request, runtime)

    async def describe_resource_filter_attributes_async(
        self,
        request: global_search_20210110_models.DescribeResourceFilterAttributesRequest,
    ) -> global_search_20210110_models.DescribeResourceFilterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_filter_attributes_with_options_async(request, runtime)

    def describe_resource_recommend_filters_with_options(
        self,
        request: global_search_20210110_models.DescribeResourceRecommendFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeResourceRecommendFiltersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceRecommendFilters',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeResourceRecommendFiltersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_recommend_filters_with_options_async(
        self,
        request: global_search_20210110_models.DescribeResourceRecommendFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeResourceRecommendFiltersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceRecommendFilters',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeResourceRecommendFiltersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_recommend_filters(
        self,
        request: global_search_20210110_models.DescribeResourceRecommendFiltersRequest,
    ) -> global_search_20210110_models.DescribeResourceRecommendFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_recommend_filters_with_options(request, runtime)

    async def describe_resource_recommend_filters_async(
        self,
        request: global_search_20210110_models.DescribeResourceRecommendFiltersRequest,
    ) -> global_search_20210110_models.DescribeResourceRecommendFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_recommend_filters_with_options_async(request, runtime)

    def describe_resources_with_options(
        self,
        request: global_search_20210110_models.DescribeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.detail_attribute_names):
            query['DetailAttributeNames'] = request.detail_attribute_names
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResources',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resources_with_options_async(
        self,
        request: global_search_20210110_models.DescribeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.detail_attribute_names):
            query['DetailAttributeNames'] = request.detail_attribute_names
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResources',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resources(
        self,
        request: global_search_20210110_models.DescribeResourcesRequest,
    ) -> global_search_20210110_models.DescribeResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resources_with_options(request, runtime)

    async def describe_resources_async(
        self,
        request: global_search_20210110_models.DescribeResourcesRequest,
    ) -> global_search_20210110_models.DescribeResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resources_with_options_async(request, runtime)

    def describe_supported_products_with_options(
        self,
        request: global_search_20210110_models.DescribeSupportedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeSupportedProductsResponse:
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportedProducts',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeSupportedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_supported_products_with_options_async(
        self,
        request: global_search_20210110_models.DescribeSupportedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> global_search_20210110_models.DescribeSupportedProductsResponse:
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportedProducts',
            version='2021-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            global_search_20210110_models.DescribeSupportedProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_supported_products(
        self,
        request: global_search_20210110_models.DescribeSupportedProductsRequest,
    ) -> global_search_20210110_models.DescribeSupportedProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_supported_products_with_options(request, runtime)

    async def describe_supported_products_async(
        self,
        request: global_search_20210110_models.DescribeSupportedProductsRequest,
    ) -> global_search_20210110_models.DescribeSupportedProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_supported_products_with_options_async(request, runtime)
