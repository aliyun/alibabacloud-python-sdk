# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_consolecs20160406 import models as consolecs_20160406_models
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
        self._endpoint = self.get_endpoint('consolecs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_open_api_list_with_options(
        self,
        request: consolecs_20160406_models.GetOpenApiListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> consolecs_20160406_models.GetOpenApiListResponse:
        """
        @param request: GetOpenApiListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpenApiListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpenApiList',
            version='2016-04-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            consolecs_20160406_models.GetOpenApiListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_open_api_list_with_options_async(
        self,
        request: consolecs_20160406_models.GetOpenApiListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> consolecs_20160406_models.GetOpenApiListResponse:
        """
        @param request: GetOpenApiListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpenApiListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpenApiList',
            version='2016-04-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            consolecs_20160406_models.GetOpenApiListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_open_api_list(
        self,
        request: consolecs_20160406_models.GetOpenApiListRequest,
    ) -> consolecs_20160406_models.GetOpenApiListResponse:
        """
        @param request: GetOpenApiListRequest
        @return: GetOpenApiListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_open_api_list_with_options(request, runtime)

    async def get_open_api_list_async(
        self,
        request: consolecs_20160406_models.GetOpenApiListRequest,
    ) -> consolecs_20160406_models.GetOpenApiListResponse:
        """
        @param request: GetOpenApiListRequest
        @return: GetOpenApiListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_open_api_list_with_options_async(request, runtime)

    def list_console_product_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> consolecs_20160406_models.ListConsoleProductResponse:
        """
        @param request: ListConsoleProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsoleProductResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListConsoleProduct',
            version='2016-04-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            consolecs_20160406_models.ListConsoleProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_console_product_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> consolecs_20160406_models.ListConsoleProductResponse:
        """
        @param request: ListConsoleProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsoleProductResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListConsoleProduct',
            version='2016-04-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            consolecs_20160406_models.ListConsoleProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_console_product(self) -> consolecs_20160406_models.ListConsoleProductResponse:
        """
        @return: ListConsoleProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_console_product_with_options(runtime)

    async def list_console_product_async(self) -> consolecs_20160406_models.ListConsoleProductResponse:
        """
        @return: ListConsoleProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_console_product_with_options_async(runtime)
