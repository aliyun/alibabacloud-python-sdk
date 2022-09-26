# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_api_workbench20201120 import models as api_workbench_20201120_models
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
        self._endpoint = self.get_endpoint('api-workbench', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_api_meta(
        self,
        request: api_workbench_20201120_models.GetApiMetaRequest,
    ) -> api_workbench_20201120_models.GetApiMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_api_meta_with_options(request, headers, runtime)

    async def get_api_meta_async(
        self,
        request: api_workbench_20201120_models.GetApiMetaRequest,
    ) -> api_workbench_20201120_models.GetApiMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_api_meta_with_options_async(request, headers, runtime)

    def get_api_meta_with_options(
        self,
        request: api_workbench_20201120_models.GetApiMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> api_workbench_20201120_models.GetApiMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['apiName'] = request.api_name
        if not UtilClient.is_unset(request.product_name):
            query['productName'] = request.product_name
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiMeta',
            version='2020-11-20',
            protocol='HTTPS',
            pathname=f'/openapi/product/apiInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            api_workbench_20201120_models.GetApiMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_meta_with_options_async(
        self,
        request: api_workbench_20201120_models.GetApiMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> api_workbench_20201120_models.GetApiMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['apiName'] = request.api_name
        if not UtilClient.is_unset(request.product_name):
            query['productName'] = request.product_name
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiMeta',
            version='2020-11-20',
            protocol='HTTPS',
            pathname=f'/openapi/product/apiInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            api_workbench_20201120_models.GetApiMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_code(
        self,
        request: api_workbench_20201120_models.MakeCodeRequest,
    ) -> api_workbench_20201120_models.MakeCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.make_code_with_options(request, headers, runtime)

    async def make_code_async(
        self,
        request: api_workbench_20201120_models.MakeCodeRequest,
    ) -> api_workbench_20201120_models.MakeCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.make_code_with_options_async(request, headers, runtime)

    def make_code_with_options(
        self,
        request: api_workbench_20201120_models.MakeCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> api_workbench_20201120_models.MakeCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['apiName'] = request.api_name
        if not UtilClient.is_unset(request.api_style):
            body['apiStyle'] = request.api_style
        if not UtilClient.is_unset(request.api_version):
            body['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.endpoint):
            body['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.meta):
            body['meta'] = request.meta
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.product):
            body['product'] = request.product
        if not UtilClient.is_unset(request.sdk_type):
            body['sdkType'] = request.sdk_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MakeCode',
            version='2020-11-20',
            protocol='HTTPS',
            pathname=f'/openapi/product/makeCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            api_workbench_20201120_models.MakeCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_code_with_options_async(
        self,
        request: api_workbench_20201120_models.MakeCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> api_workbench_20201120_models.MakeCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['apiName'] = request.api_name
        if not UtilClient.is_unset(request.api_style):
            body['apiStyle'] = request.api_style
        if not UtilClient.is_unset(request.api_version):
            body['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.endpoint):
            body['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.meta):
            body['meta'] = request.meta
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.product):
            body['product'] = request.product
        if not UtilClient.is_unset(request.sdk_type):
            body['sdkType'] = request.sdk_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MakeCode',
            version='2020-11-20',
            protocol='HTTPS',
            pathname=f'/openapi/product/makeCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            api_workbench_20201120_models.MakeCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_product(
        self,
        request: api_workbench_20201120_models.SearchProductRequest,
    ) -> api_workbench_20201120_models.SearchProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_product_with_options(request, headers, runtime)

    async def search_product_async(
        self,
        request: api_workbench_20201120_models.SearchProductRequest,
    ) -> api_workbench_20201120_models.SearchProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_product_with_options_async(request, headers, runtime)

    def search_product_with_options(
        self,
        request: api_workbench_20201120_models.SearchProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> api_workbench_20201120_models.SearchProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchProduct',
            version='2020-11-20',
            protocol='HTTPS',
            pathname=f'/openapi/product/search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            api_workbench_20201120_models.SearchProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_product_with_options_async(
        self,
        request: api_workbench_20201120_models.SearchProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> api_workbench_20201120_models.SearchProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchProduct',
            version='2020-11-20',
            protocol='HTTPS',
            pathname=f'/openapi/product/search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            api_workbench_20201120_models.SearchProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_open_api_request(
        self,
        request: api_workbench_20201120_models.TestOpenApiRequestRequest,
    ) -> api_workbench_20201120_models.TestOpenApiRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.test_open_api_request_with_options(request, headers, runtime)

    async def test_open_api_request_async(
        self,
        request: api_workbench_20201120_models.TestOpenApiRequestRequest,
    ) -> api_workbench_20201120_models.TestOpenApiRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.test_open_api_request_with_options_async(request, headers, runtime)

    def test_open_api_request_with_options(
        self,
        request: api_workbench_20201120_models.TestOpenApiRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> api_workbench_20201120_models.TestOpenApiRequestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['apiName'] = request.api_name
        if not UtilClient.is_unset(request.api_version):
            body['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.meta):
            body['meta'] = request.meta
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.product):
            body['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestOpenApiRequest',
            version='2020-11-20',
            protocol='HTTPS',
            pathname=f'/openapi/product/openApiRequest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            api_workbench_20201120_models.TestOpenApiRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_open_api_request_with_options_async(
        self,
        request: api_workbench_20201120_models.TestOpenApiRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> api_workbench_20201120_models.TestOpenApiRequestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['apiName'] = request.api_name
        if not UtilClient.is_unset(request.api_version):
            body['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.meta):
            body['meta'] = request.meta
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.product):
            body['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestOpenApiRequest',
            version='2020-11-20',
            protocol='HTTPS',
            pathname=f'/openapi/product/openApiRequest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            api_workbench_20201120_models.TestOpenApiRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )
