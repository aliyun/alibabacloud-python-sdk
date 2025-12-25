# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_foasconsole20190601 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('foasconsole', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def convert_instance_with_options(
        self,
        request: main_models.ConvertInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.convert_postpay_instance_request):
            body_flat['ConvertPostpayInstanceRequest'] = request.convert_postpay_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConvertInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_instance_with_options_async(
        self,
        request: main_models.ConvertInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.convert_postpay_instance_request):
            body_flat['ConvertPostpayInstanceRequest'] = request.convert_postpay_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConvertInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_instance(
        self,
        request: main_models.ConvertInstanceRequest,
    ) -> main_models.ConvertInstanceResponse:
        runtime = RuntimeOptions()
        return self.convert_instance_with_options(request, runtime)

    async def convert_instance_async(
        self,
        request: main_models.ConvertInstanceRequest,
    ) -> main_models.ConvertInstanceResponse:
        runtime = RuntimeOptions()
        return await self.convert_instance_with_options_async(request, runtime)

    def convert_prepay_instance_with_options(
        self,
        request: main_models.ConvertPrepayInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertPrepayInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.convert_prepay_instance_request):
            body_flat['ConvertPrepayInstanceRequest'] = request.convert_prepay_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConvertPrepayInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertPrepayInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_prepay_instance_with_options_async(
        self,
        request: main_models.ConvertPrepayInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertPrepayInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.convert_prepay_instance_request):
            body_flat['ConvertPrepayInstanceRequest'] = request.convert_prepay_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConvertPrepayInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertPrepayInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_prepay_instance(
        self,
        request: main_models.ConvertPrepayInstanceRequest,
    ) -> main_models.ConvertPrepayInstanceResponse:
        runtime = RuntimeOptions()
        return self.convert_prepay_instance_with_options(request, runtime)

    async def convert_prepay_instance_async(
        self,
        request: main_models.ConvertPrepayInstanceRequest,
    ) -> main_models.ConvertPrepayInstanceResponse:
        runtime = RuntimeOptions()
        return await self.convert_prepay_instance_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.create_instance_request):
            body_flat['CreateInstanceRequest'] = request.create_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.create_instance_request):
            body_flat['CreateInstanceRequest'] = request.create_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.create_namespace_request):
            body_flat['CreateNamespaceRequest'] = request.create_namespace_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.create_namespace_request):
            body_flat['CreateNamespaceRequest'] = request.create_namespace_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.delete_instance_request):
            body_flat['DeleteInstanceRequest'] = request.delete_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.delete_instance_request):
            body_flat['DeleteInstanceRequest'] = request.delete_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.delete_namespace_request):
            body_flat['DeleteNamespaceRequest'] = request.delete_namespace_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.delete_namespace_request):
            body_flat['DeleteNamespaceRequest'] = request.delete_namespace_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_namespaces_with_options(
        self,
        request: main_models.DescribeNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespacesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespaces',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespaces_with_options_async(
        self,
        request: main_models.DescribeNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespacesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespaces',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespaces(
        self,
        request: main_models.DescribeNamespacesRequest,
    ) -> main_models.DescribeNamespacesResponse:
        runtime = RuntimeOptions()
        return self.describe_namespaces_with_options(request, runtime)

    async def describe_namespaces_async(
        self,
        request: main_models.DescribeNamespacesRequest,
    ) -> main_models.DescribeNamespacesResponse:
        runtime = RuntimeOptions()
        return await self.describe_namespaces_with_options_async(request, runtime)

    def describe_supported_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportedRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSupportedRegions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportedRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_supported_regions_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportedRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSupportedRegions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportedRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_supported_regions(self) -> main_models.DescribeSupportedRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_supported_regions_with_options(runtime)

    async def describe_supported_regions_async(self) -> main_models.DescribeSupportedRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_supported_regions_with_options_async(runtime)

    def describe_supported_zones_with_options(
        self,
        request: main_models.DescribeSupportedZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportedZonesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSupportedZones',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportedZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_supported_zones_with_options_async(
        self,
        request: main_models.DescribeSupportedZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportedZonesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSupportedZones',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportedZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_supported_zones(
        self,
        request: main_models.DescribeSupportedZonesRequest,
    ) -> main_models.DescribeSupportedZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_supported_zones_with_options(request, runtime)

    async def describe_supported_zones_async(
        self,
        request: main_models.DescribeSupportedZonesRequest,
    ) -> main_models.DescribeSupportedZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_supported_zones_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-06-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-06-01',
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

    def modify_prepay_instance_spec_with_options(
        self,
        request: main_models.ModifyPrepayInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPrepayInstanceSpecResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.modify_prepay_instance_spec_request):
            body_flat['ModifyPrepayInstanceSpecRequest'] = request.modify_prepay_instance_spec_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPrepayInstanceSpec',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPrepayInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_prepay_instance_spec_with_options_async(
        self,
        request: main_models.ModifyPrepayInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPrepayInstanceSpecResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.modify_prepay_instance_spec_request):
            body_flat['ModifyPrepayInstanceSpecRequest'] = request.modify_prepay_instance_spec_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPrepayInstanceSpec',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPrepayInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_prepay_instance_spec(
        self,
        request: main_models.ModifyPrepayInstanceSpecRequest,
    ) -> main_models.ModifyPrepayInstanceSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    async def modify_prepay_instance_spec_async(
        self,
        request: main_models.ModifyPrepayInstanceSpecRequest,
    ) -> main_models.ModifyPrepayInstanceSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_prepay_instance_spec_with_options_async(request, runtime)

    def modify_prepay_namespace_spec_with_options(
        self,
        request: main_models.ModifyPrepayNamespaceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPrepayNamespaceSpecResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.modify_prepay_namespace_spec_request):
            body_flat['ModifyPrepayNamespaceSpecRequest'] = request.modify_prepay_namespace_spec_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPrepayNamespaceSpec',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPrepayNamespaceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_prepay_namespace_spec_with_options_async(
        self,
        request: main_models.ModifyPrepayNamespaceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPrepayNamespaceSpecResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.modify_prepay_namespace_spec_request):
            body_flat['ModifyPrepayNamespaceSpecRequest'] = request.modify_prepay_namespace_spec_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPrepayNamespaceSpec',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPrepayNamespaceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_prepay_namespace_spec(
        self,
        request: main_models.ModifyPrepayNamespaceSpecRequest,
    ) -> main_models.ModifyPrepayNamespaceSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_prepay_namespace_spec_with_options(request, runtime)

    async def modify_prepay_namespace_spec_async(
        self,
        request: main_models.ModifyPrepayNamespaceSpecRequest,
    ) -> main_models.ModifyPrepayNamespaceSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_prepay_namespace_spec_with_options_async(request, runtime)

    def query_convert_instance_price_with_options(
        self,
        request: main_models.QueryConvertInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConvertInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.convert_postpay_instance_request):
            body_flat['ConvertPostpayInstanceRequest'] = request.convert_postpay_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryConvertInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConvertInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_convert_instance_price_with_options_async(
        self,
        request: main_models.QueryConvertInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConvertInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.convert_postpay_instance_request):
            body_flat['ConvertPostpayInstanceRequest'] = request.convert_postpay_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryConvertInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConvertInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_convert_instance_price(
        self,
        request: main_models.QueryConvertInstancePriceRequest,
    ) -> main_models.QueryConvertInstancePriceResponse:
        runtime = RuntimeOptions()
        return self.query_convert_instance_price_with_options(request, runtime)

    async def query_convert_instance_price_async(
        self,
        request: main_models.QueryConvertInstancePriceRequest,
    ) -> main_models.QueryConvertInstancePriceResponse:
        runtime = RuntimeOptions()
        return await self.query_convert_instance_price_with_options_async(request, runtime)

    def query_convert_prepay_instance_price_with_options(
        self,
        request: main_models.QueryConvertPrepayInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConvertPrepayInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.convert_prepay_instance_request):
            body_flat['ConvertPrepayInstanceRequest'] = request.convert_prepay_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryConvertPrepayInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConvertPrepayInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_convert_prepay_instance_price_with_options_async(
        self,
        request: main_models.QueryConvertPrepayInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConvertPrepayInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.convert_prepay_instance_request):
            body_flat['ConvertPrepayInstanceRequest'] = request.convert_prepay_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryConvertPrepayInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConvertPrepayInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_convert_prepay_instance_price(
        self,
        request: main_models.QueryConvertPrepayInstancePriceRequest,
    ) -> main_models.QueryConvertPrepayInstancePriceResponse:
        runtime = RuntimeOptions()
        return self.query_convert_prepay_instance_price_with_options(request, runtime)

    async def query_convert_prepay_instance_price_async(
        self,
        request: main_models.QueryConvertPrepayInstancePriceRequest,
    ) -> main_models.QueryConvertPrepayInstancePriceResponse:
        runtime = RuntimeOptions()
        return await self.query_convert_prepay_instance_price_with_options_async(request, runtime)

    def query_create_instance_price_with_options(
        self,
        request: main_models.QueryCreateInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCreateInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.create_instance_request):
            body_flat['CreateInstanceRequest'] = request.create_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCreateInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCreateInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_create_instance_price_with_options_async(
        self,
        request: main_models.QueryCreateInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCreateInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.create_instance_request):
            body_flat['CreateInstanceRequest'] = request.create_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCreateInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCreateInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_create_instance_price(
        self,
        request: main_models.QueryCreateInstancePriceRequest,
    ) -> main_models.QueryCreateInstancePriceResponse:
        runtime = RuntimeOptions()
        return self.query_create_instance_price_with_options(request, runtime)

    async def query_create_instance_price_async(
        self,
        request: main_models.QueryCreateInstancePriceRequest,
    ) -> main_models.QueryCreateInstancePriceResponse:
        runtime = RuntimeOptions()
        return await self.query_create_instance_price_with_options_async(request, runtime)

    def query_modify_instance_price_with_options(
        self,
        request: main_models.QueryModifyInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.modify_prepay_instance_spec_request):
            body_flat['ModifyPrepayInstanceSpecRequest'] = request.modify_prepay_instance_spec_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_instance_price_with_options_async(
        self,
        request: main_models.QueryModifyInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.modify_prepay_instance_spec_request):
            body_flat['ModifyPrepayInstanceSpecRequest'] = request.modify_prepay_instance_spec_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_instance_price(
        self,
        request: main_models.QueryModifyInstancePriceRequest,
    ) -> main_models.QueryModifyInstancePriceResponse:
        runtime = RuntimeOptions()
        return self.query_modify_instance_price_with_options(request, runtime)

    async def query_modify_instance_price_async(
        self,
        request: main_models.QueryModifyInstancePriceRequest,
    ) -> main_models.QueryModifyInstancePriceResponse:
        runtime = RuntimeOptions()
        return await self.query_modify_instance_price_with_options_async(request, runtime)

    def query_renew_instance_price_with_options(
        self,
        request: main_models.QueryRenewInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRenewInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.renew_instance_request):
            body_flat['RenewInstanceRequest'] = request.renew_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryRenewInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRenewInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_renew_instance_price_with_options_async(
        self,
        request: main_models.QueryRenewInstancePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRenewInstancePriceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.renew_instance_request):
            body_flat['RenewInstanceRequest'] = request.renew_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryRenewInstancePrice',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRenewInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_renew_instance_price(
        self,
        request: main_models.QueryRenewInstancePriceRequest,
    ) -> main_models.QueryRenewInstancePriceResponse:
        runtime = RuntimeOptions()
        return self.query_renew_instance_price_with_options(request, runtime)

    async def query_renew_instance_price_async(
        self,
        request: main_models.QueryRenewInstancePriceRequest,
    ) -> main_models.QueryRenewInstancePriceResponse:
        runtime = RuntimeOptions()
        return await self.query_renew_instance_price_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.renew_instance_request):
            body_flat['RenewInstanceRequest'] = request.renew_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.renew_instance_request):
            body_flat['RenewInstanceRequest'] = request.renew_instance_request
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-06-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-06-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-06-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-06-01',
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
