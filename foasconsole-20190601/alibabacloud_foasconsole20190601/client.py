# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_foasconsole20190601 import models as foasconsole_20190601_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def convert_instance_with_options(
        self,
        request: foasconsole_20190601_models.ConvertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ConvertInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.convert_postpay_instance_request):
            body_flat['ConvertPostpayInstanceRequest'] = request.convert_postpay_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ConvertInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.ConvertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ConvertInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.convert_postpay_instance_request):
            body_flat['ConvertPostpayInstanceRequest'] = request.convert_postpay_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ConvertInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_instance(
        self,
        request: foasconsole_20190601_models.ConvertInstanceRequest,
    ) -> foasconsole_20190601_models.ConvertInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_instance_with_options(request, runtime)

    async def convert_instance_async(
        self,
        request: foasconsole_20190601_models.ConvertInstanceRequest,
    ) -> foasconsole_20190601_models.ConvertInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_instance_with_options_async(request, runtime)

    def convert_prepay_instance_with_options(
        self,
        request: foasconsole_20190601_models.ConvertPrepayInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ConvertPrepayInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.convert_prepay_instance_request):
            body_flat['ConvertPrepayInstanceRequest'] = request.convert_prepay_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertPrepayInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ConvertPrepayInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_prepay_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.ConvertPrepayInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ConvertPrepayInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.convert_prepay_instance_request):
            body_flat['ConvertPrepayInstanceRequest'] = request.convert_prepay_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertPrepayInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ConvertPrepayInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_prepay_instance(
        self,
        request: foasconsole_20190601_models.ConvertPrepayInstanceRequest,
    ) -> foasconsole_20190601_models.ConvertPrepayInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_prepay_instance_with_options(request, runtime)

    async def convert_prepay_instance_async(
        self,
        request: foasconsole_20190601_models.ConvertPrepayInstanceRequest,
    ) -> foasconsole_20190601_models.ConvertPrepayInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_prepay_instance_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: foasconsole_20190601_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.create_instance_request):
            body_flat['CreateInstanceRequest'] = request.create_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.create_instance_request):
            body_flat['CreateInstanceRequest'] = request.create_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: foasconsole_20190601_models.CreateInstanceRequest,
    ) -> foasconsole_20190601_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: foasconsole_20190601_models.CreateInstanceRequest,
    ) -> foasconsole_20190601_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: foasconsole_20190601_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.create_namespace_request):
            body_flat['CreateNamespaceRequest'] = request.create_namespace_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: foasconsole_20190601_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.create_namespace_request):
            body_flat['CreateNamespaceRequest'] = request.create_namespace_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: foasconsole_20190601_models.CreateNamespaceRequest,
    ) -> foasconsole_20190601_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: foasconsole_20190601_models.CreateNamespaceRequest,
    ) -> foasconsole_20190601_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: foasconsole_20190601_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.delete_instance_request):
            body_flat['DeleteInstanceRequest'] = request.delete_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.delete_instance_request):
            body_flat['DeleteInstanceRequest'] = request.delete_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: foasconsole_20190601_models.DeleteInstanceRequest,
    ) -> foasconsole_20190601_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: foasconsole_20190601_models.DeleteInstanceRequest,
    ) -> foasconsole_20190601_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: foasconsole_20190601_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.delete_namespace_request):
            body_flat['DeleteNamespaceRequest'] = request.delete_namespace_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: foasconsole_20190601_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.delete_namespace_request):
            body_flat['DeleteNamespaceRequest'] = request.delete_namespace_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: foasconsole_20190601_models.DeleteNamespaceRequest,
    ) -> foasconsole_20190601_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: foasconsole_20190601_models.DeleteNamespaceRequest,
    ) -> foasconsole_20190601_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: foasconsole_20190601_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: foasconsole_20190601_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: foasconsole_20190601_models.DescribeInstancesRequest,
    ) -> foasconsole_20190601_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: foasconsole_20190601_models.DescribeInstancesRequest,
    ) -> foasconsole_20190601_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_namespaces_with_options(
        self,
        request: foasconsole_20190601_models.DescribeNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeNamespacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespaces_with_options_async(
        self,
        request: foasconsole_20190601_models.DescribeNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeNamespacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespaces(
        self,
        request: foasconsole_20190601_models.DescribeNamespacesRequest,
    ) -> foasconsole_20190601_models.DescribeNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_namespaces_with_options(request, runtime)

    async def describe_namespaces_async(
        self,
        request: foasconsole_20190601_models.DescribeNamespacesRequest,
    ) -> foasconsole_20190601_models.DescribeNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_namespaces_with_options_async(request, runtime)

    def describe_supported_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeSupportedRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSupportedRegions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeSupportedRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_supported_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeSupportedRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSupportedRegions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeSupportedRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_supported_regions(self) -> foasconsole_20190601_models.DescribeSupportedRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_supported_regions_with_options(runtime)

    async def describe_supported_regions_async(self) -> foasconsole_20190601_models.DescribeSupportedRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_supported_regions_with_options_async(runtime)

    def describe_supported_zones_with_options(
        self,
        request: foasconsole_20190601_models.DescribeSupportedZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeSupportedZonesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportedZones',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeSupportedZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_supported_zones_with_options_async(
        self,
        request: foasconsole_20190601_models.DescribeSupportedZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeSupportedZonesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportedZones',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeSupportedZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_supported_zones(
        self,
        request: foasconsole_20190601_models.DescribeSupportedZonesRequest,
    ) -> foasconsole_20190601_models.DescribeSupportedZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_supported_zones_with_options(request, runtime)

    async def describe_supported_zones_async(
        self,
        request: foasconsole_20190601_models.DescribeSupportedZonesRequest,
    ) -> foasconsole_20190601_models.DescribeSupportedZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_supported_zones_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: foasconsole_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ListTagResourcesResponse:
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
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: foasconsole_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ListTagResourcesResponse:
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
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: foasconsole_20190601_models.ListTagResourcesRequest,
    ) -> foasconsole_20190601_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: foasconsole_20190601_models.ListTagResourcesRequest,
    ) -> foasconsole_20190601_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_prepay_instance_spec_with_options(
        self,
        request: foasconsole_20190601_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse:
        """
        @deprecated : ModifyPrepayInstanceSpec is deprecated, please use foasconsole::2019-06-01::ModifyInstanceSpec instead.
        
        @param request: ModifyPrepayInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPrepayInstanceSpecResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.modify_prepay_instance_spec_request):
            body_flat['ModifyPrepayInstanceSpecRequest'] = request.modify_prepay_instance_spec_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_prepay_instance_spec_with_options_async(
        self,
        request: foasconsole_20190601_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse:
        """
        @deprecated : ModifyPrepayInstanceSpec is deprecated, please use foasconsole::2019-06-01::ModifyInstanceSpec instead.
        
        @param request: ModifyPrepayInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPrepayInstanceSpecResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.modify_prepay_instance_spec_request):
            body_flat['ModifyPrepayInstanceSpecRequest'] = request.modify_prepay_instance_spec_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_prepay_instance_spec(
        self,
        request: foasconsole_20190601_models.ModifyPrepayInstanceSpecRequest,
    ) -> foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse:
        """
        @deprecated : ModifyPrepayInstanceSpec is deprecated, please use foasconsole::2019-06-01::ModifyInstanceSpec instead.
        
        @param request: ModifyPrepayInstanceSpecRequest
        @return: ModifyPrepayInstanceSpecResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    async def modify_prepay_instance_spec_async(
        self,
        request: foasconsole_20190601_models.ModifyPrepayInstanceSpecRequest,
    ) -> foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse:
        """
        @deprecated : ModifyPrepayInstanceSpec is deprecated, please use foasconsole::2019-06-01::ModifyInstanceSpec instead.
        
        @param request: ModifyPrepayInstanceSpecRequest
        @return: ModifyPrepayInstanceSpecResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_instance_spec_with_options_async(request, runtime)

    def modify_prepay_namespace_spec_with_options(
        self,
        request: foasconsole_20190601_models.ModifyPrepayNamespaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse:
        """
        @deprecated : ModifyPrepayNamespaceSpec is deprecated, please use foasconsole::2019-06-01::ModifyNamespaceSpec instead.
        
        @param request: ModifyPrepayNamespaceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPrepayNamespaceSpecResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.modify_prepay_namespace_spec_request):
            body_flat['ModifyPrepayNamespaceSpecRequest'] = request.modify_prepay_namespace_spec_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayNamespaceSpec',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_prepay_namespace_spec_with_options_async(
        self,
        request: foasconsole_20190601_models.ModifyPrepayNamespaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse:
        """
        @deprecated : ModifyPrepayNamespaceSpec is deprecated, please use foasconsole::2019-06-01::ModifyNamespaceSpec instead.
        
        @param request: ModifyPrepayNamespaceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPrepayNamespaceSpecResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.modify_prepay_namespace_spec_request):
            body_flat['ModifyPrepayNamespaceSpecRequest'] = request.modify_prepay_namespace_spec_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayNamespaceSpec',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_prepay_namespace_spec(
        self,
        request: foasconsole_20190601_models.ModifyPrepayNamespaceSpecRequest,
    ) -> foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse:
        """
        @deprecated : ModifyPrepayNamespaceSpec is deprecated, please use foasconsole::2019-06-01::ModifyNamespaceSpec instead.
        
        @param request: ModifyPrepayNamespaceSpecRequest
        @return: ModifyPrepayNamespaceSpecResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_namespace_spec_with_options(request, runtime)

    async def modify_prepay_namespace_spec_async(
        self,
        request: foasconsole_20190601_models.ModifyPrepayNamespaceSpecRequest,
    ) -> foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse:
        """
        @deprecated : ModifyPrepayNamespaceSpec is deprecated, please use foasconsole::2019-06-01::ModifyNamespaceSpec instead.
        
        @param request: ModifyPrepayNamespaceSpecRequest
        @return: ModifyPrepayNamespaceSpecResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_namespace_spec_with_options_async(request, runtime)

    def query_convert_instance_price_with_options(
        self,
        request: foasconsole_20190601_models.QueryConvertInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryConvertInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.convert_postpay_instance_request):
            body_flat['ConvertPostpayInstanceRequest'] = request.convert_postpay_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConvertInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryConvertInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_convert_instance_price_with_options_async(
        self,
        request: foasconsole_20190601_models.QueryConvertInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryConvertInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.convert_postpay_instance_request):
            body_flat['ConvertPostpayInstanceRequest'] = request.convert_postpay_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConvertInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryConvertInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_convert_instance_price(
        self,
        request: foasconsole_20190601_models.QueryConvertInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryConvertInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_convert_instance_price_with_options(request, runtime)

    async def query_convert_instance_price_async(
        self,
        request: foasconsole_20190601_models.QueryConvertInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryConvertInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_convert_instance_price_with_options_async(request, runtime)

    def query_convert_prepay_instance_price_with_options(
        self,
        request: foasconsole_20190601_models.QueryConvertPrepayInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryConvertPrepayInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.convert_prepay_instance_request):
            body_flat['ConvertPrepayInstanceRequest'] = request.convert_prepay_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConvertPrepayInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryConvertPrepayInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_convert_prepay_instance_price_with_options_async(
        self,
        request: foasconsole_20190601_models.QueryConvertPrepayInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryConvertPrepayInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.convert_prepay_instance_request):
            body_flat['ConvertPrepayInstanceRequest'] = request.convert_prepay_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConvertPrepayInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryConvertPrepayInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_convert_prepay_instance_price(
        self,
        request: foasconsole_20190601_models.QueryConvertPrepayInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryConvertPrepayInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_convert_prepay_instance_price_with_options(request, runtime)

    async def query_convert_prepay_instance_price_async(
        self,
        request: foasconsole_20190601_models.QueryConvertPrepayInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryConvertPrepayInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_convert_prepay_instance_price_with_options_async(request, runtime)

    def query_create_instance_price_with_options(
        self,
        request: foasconsole_20190601_models.QueryCreateInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryCreateInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.create_instance_request):
            body_flat['CreateInstanceRequest'] = request.create_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCreateInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryCreateInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_create_instance_price_with_options_async(
        self,
        request: foasconsole_20190601_models.QueryCreateInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryCreateInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.create_instance_request):
            body_flat['CreateInstanceRequest'] = request.create_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCreateInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryCreateInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_create_instance_price(
        self,
        request: foasconsole_20190601_models.QueryCreateInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryCreateInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_create_instance_price_with_options(request, runtime)

    async def query_create_instance_price_async(
        self,
        request: foasconsole_20190601_models.QueryCreateInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryCreateInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_create_instance_price_with_options_async(request, runtime)

    def query_modify_instance_price_with_options(
        self,
        request: foasconsole_20190601_models.QueryModifyInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryModifyInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.modify_prepay_instance_spec_request):
            body_flat['ModifyPrepayInstanceSpecRequest'] = request.modify_prepay_instance_spec_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryModifyInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryModifyInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_instance_price_with_options_async(
        self,
        request: foasconsole_20190601_models.QueryModifyInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryModifyInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.modify_prepay_instance_spec_request):
            body_flat['ModifyPrepayInstanceSpecRequest'] = request.modify_prepay_instance_spec_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryModifyInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryModifyInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_instance_price(
        self,
        request: foasconsole_20190601_models.QueryModifyInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryModifyInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_modify_instance_price_with_options(request, runtime)

    async def query_modify_instance_price_async(
        self,
        request: foasconsole_20190601_models.QueryModifyInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryModifyInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_modify_instance_price_with_options_async(request, runtime)

    def query_renew_instance_price_with_options(
        self,
        request: foasconsole_20190601_models.QueryRenewInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryRenewInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.renew_instance_request):
            body_flat['RenewInstanceRequest'] = request.renew_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRenewInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryRenewInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_renew_instance_price_with_options_async(
        self,
        request: foasconsole_20190601_models.QueryRenewInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryRenewInstancePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.renew_instance_request):
            body_flat['RenewInstanceRequest'] = request.renew_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRenewInstancePrice',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryRenewInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_renew_instance_price(
        self,
        request: foasconsole_20190601_models.QueryRenewInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryRenewInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_renew_instance_price_with_options(request, runtime)

    async def query_renew_instance_price_async(
        self,
        request: foasconsole_20190601_models.QueryRenewInstancePriceRequest,
    ) -> foasconsole_20190601_models.QueryRenewInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_renew_instance_price_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: foasconsole_20190601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.renew_instance_request):
            body_flat['RenewInstanceRequest'] = request.renew_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.renew_instance_request):
            body_flat['RenewInstanceRequest'] = request.renew_instance_request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: foasconsole_20190601_models.RenewInstanceRequest,
    ) -> foasconsole_20190601_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: foasconsole_20190601_models.RenewInstanceRequest,
    ) -> foasconsole_20190601_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: foasconsole_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='TagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: foasconsole_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='TagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: foasconsole_20190601_models.TagResourcesRequest,
    ) -> foasconsole_20190601_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: foasconsole_20190601_models.TagResourcesRequest,
    ) -> foasconsole_20190601_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: foasconsole_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: foasconsole_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: foasconsole_20190601_models.UntagResourcesRequest,
    ) -> foasconsole_20190601_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: foasconsole_20190601_models.UntagResourcesRequest,
    ) -> foasconsole_20190601_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
