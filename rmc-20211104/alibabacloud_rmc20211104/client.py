# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rmc20211104 import models as rmc20211104_models
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
        self._endpoint = self.get_endpoint('rmc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_resource_relationships_with_options(
        self,
        request: rmc20211104_models.ListResourceRelationshipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.ListResourceRelationshipsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.source_region_id):
            query['SourceRegionId'] = request.source_region_id
        if not UtilClient.is_unset(request.source_resource_id):
            query['SourceResourceId'] = request.source_resource_id
        if not UtilClient.is_unset(request.source_resource_type):
            query['SourceResourceType'] = request.source_resource_type
        if not UtilClient.is_unset(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceRelationships',
            version='2021-11-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rmc20211104_models.ListResourceRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_relationships_with_options_async(
        self,
        request: rmc20211104_models.ListResourceRelationshipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.ListResourceRelationshipsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.source_region_id):
            query['SourceRegionId'] = request.source_region_id
        if not UtilClient.is_unset(request.source_resource_id):
            query['SourceResourceId'] = request.source_resource_id
        if not UtilClient.is_unset(request.source_resource_type):
            query['SourceResourceType'] = request.source_resource_type
        if not UtilClient.is_unset(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceRelationships',
            version='2021-11-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rmc20211104_models.ListResourceRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_relationships(
        self,
        request: rmc20211104_models.ListResourceRelationshipsRequest,
    ) -> rmc20211104_models.ListResourceRelationshipsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_relationships_with_options(request, runtime)

    async def list_resource_relationships_async(
        self,
        request: rmc20211104_models.ListResourceRelationshipsRequest,
    ) -> rmc20211104_models.ListResourceRelationshipsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_relationships_with_options_async(request, runtime)

    def search_resources_with_options(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.SearchResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchResources',
            version='2021-11-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rmc20211104_models.SearchResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_resources_with_options_async(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.SearchResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchResources',
            version='2021-11-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rmc20211104_models.SearchResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_resources(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
    ) -> rmc20211104_models.SearchResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_resources_with_options(request, runtime)

    async def search_resources_async(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
    ) -> rmc20211104_models.SearchResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_resources_with_options_async(request, runtime)
