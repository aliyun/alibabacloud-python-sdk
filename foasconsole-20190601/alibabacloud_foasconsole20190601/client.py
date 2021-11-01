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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ConvertInstanceResponse(),
            self.do_rpcrequest('ConvertInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def convert_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.ConvertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ConvertInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ConvertInstanceResponse(),
            await self.do_rpcrequest_async('ConvertInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_instance_with_options(
        self,
        request: foasconsole_20190601_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateInstanceResponse(),
            await self.do_rpcrequest_async('CreateInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateNamespaceResponse(),
            self.do_rpcrequest('CreateNamespace', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: foasconsole_20190601_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateNamespaceResponse(),
            await self.do_rpcrequest_async('CreateNamespace', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteInstanceResponse(),
            await self.do_rpcrequest_async('DeleteInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteNamespaceResponse(),
            self.do_rpcrequest('DeleteNamespace', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: foasconsole_20190601_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteNamespaceResponse(),
            await self.do_rpcrequest_async('DeleteNamespace', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2019-06-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: foasconsole_20190601_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeInstancesResponse(),
            await self.do_rpcrequest_async('DescribeInstances', '2019-06-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeNamespacesResponse(),
            self.do_rpcrequest('DescribeNamespaces', '2019-06-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_namespaces_with_options_async(
        self,
        request: foasconsole_20190601_models.DescribeNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.DescribeNamespacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeNamespacesResponse(),
            await self.do_rpcrequest_async('DescribeNamespaces', '2019-06-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def modify_prepay_instance_spec_with_options(
        self,
        request: foasconsole_20190601_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse(),
            self.do_rpcrequest('ModifyPrepayInstanceSpec', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_prepay_instance_spec_with_options_async(
        self,
        request: foasconsole_20190601_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse(),
            await self.do_rpcrequest_async('ModifyPrepayInstanceSpec', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_prepay_instance_spec(
        self,
        request: foasconsole_20190601_models.ModifyPrepayInstanceSpecRequest,
    ) -> foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    async def modify_prepay_instance_spec_async(
        self,
        request: foasconsole_20190601_models.ModifyPrepayInstanceSpecRequest,
    ) -> foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_instance_spec_with_options_async(request, runtime)

    def modify_prepay_namespace_spec_with_options(
        self,
        request: foasconsole_20190601_models.ModifyPrepayNamespaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse(),
            self.do_rpcrequest('ModifyPrepayNamespaceSpec', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_prepay_namespace_spec_with_options_async(
        self,
        request: foasconsole_20190601_models.ModifyPrepayNamespaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse(),
            await self.do_rpcrequest_async('ModifyPrepayNamespaceSpec', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_prepay_namespace_spec(
        self,
        request: foasconsole_20190601_models.ModifyPrepayNamespaceSpecRequest,
    ) -> foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_namespace_spec_with_options(request, runtime)

    async def modify_prepay_namespace_spec_async(
        self,
        request: foasconsole_20190601_models.ModifyPrepayNamespaceSpecRequest,
    ) -> foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_namespace_spec_with_options_async(request, runtime)

    def query_convert_instance_price_with_options(
        self,
        request: foasconsole_20190601_models.QueryConvertInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryConvertInstancePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryConvertInstancePriceResponse(),
            self.do_rpcrequest('QueryConvertInstancePrice', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_convert_instance_price_with_options_async(
        self,
        request: foasconsole_20190601_models.QueryConvertInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.QueryConvertInstancePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryConvertInstancePriceResponse(),
            await self.do_rpcrequest_async('QueryConvertInstancePrice', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def renew_instance_with_options(
        self,
        request: foasconsole_20190601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.RenewInstanceResponse(),
            self.do_rpcrequest('RenewInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: foasconsole_20190601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20190601_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.RenewInstanceResponse(),
            await self.do_rpcrequest_async('RenewInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
