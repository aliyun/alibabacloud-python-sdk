# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_opt20210730 import models as opt_20210730_models
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
        self._endpoint = self.get_endpoint('opt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_open_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> opt_20210730_models.GetOpenStatusResponse:
        """
        @param request: GetOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpenStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOpenStatus',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            opt_20210730_models.GetOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_open_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> opt_20210730_models.GetOpenStatusResponse:
        """
        @param request: GetOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpenStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOpenStatus',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            opt_20210730_models.GetOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_open_status(self) -> opt_20210730_models.GetOpenStatusResponse:
        """
        @return: GetOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_open_status_with_options(runtime)

    async def get_open_status_async(self) -> opt_20210730_models.GetOpenStatusResponse:
        """
        @return: GetOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_open_status_with_options_async(runtime)

    def get_order_info_with_options(
        self,
        request: opt_20210730_models.GetOrderInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> opt_20210730_models.GetOrderInfoResponse:
        """
        @param request: GetOrderInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrderInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.list_released):
            query['ListReleased'] = request.list_released
        if not UtilClient.is_unset(request.rel_service):
            query['RelService'] = request.rel_service
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderInfo',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            opt_20210730_models.GetOrderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_info_with_options_async(
        self,
        request: opt_20210730_models.GetOrderInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> opt_20210730_models.GetOrderInfoResponse:
        """
        @param request: GetOrderInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrderInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.list_released):
            query['ListReleased'] = request.list_released
        if not UtilClient.is_unset(request.rel_service):
            query['RelService'] = request.rel_service
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderInfo',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            opt_20210730_models.GetOrderInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order_info(
        self,
        request: opt_20210730_models.GetOrderInfoRequest,
    ) -> opt_20210730_models.GetOrderInfoResponse:
        """
        @param request: GetOrderInfoRequest
        @return: GetOrderInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_order_info_with_options(request, runtime)

    async def get_order_info_async(
        self,
        request: opt_20210730_models.GetOrderInfoRequest,
    ) -> opt_20210730_models.GetOrderInfoResponse:
        """
        @param request: GetOrderInfoRequest
        @return: GetOrderInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_order_info_with_options_async(request, runtime)

    def get_order_usage_with_options(
        self,
        request: opt_20210730_models.GetOrderUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> opt_20210730_models.GetOrderUsageResponse:
        """
        @param request: GetOrderUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrderUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.license_key):
            query['LicenseKey'] = request.license_key
        if not UtilClient.is_unset(request.rel_service):
            query['RelService'] = request.rel_service
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderUsage',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            opt_20210730_models.GetOrderUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_usage_with_options_async(
        self,
        request: opt_20210730_models.GetOrderUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> opt_20210730_models.GetOrderUsageResponse:
        """
        @param request: GetOrderUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrderUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.license_key):
            query['LicenseKey'] = request.license_key
        if not UtilClient.is_unset(request.rel_service):
            query['RelService'] = request.rel_service
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderUsage',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            opt_20210730_models.GetOrderUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order_usage(
        self,
        request: opt_20210730_models.GetOrderUsageRequest,
    ) -> opt_20210730_models.GetOrderUsageResponse:
        """
        @param request: GetOrderUsageRequest
        @return: GetOrderUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_order_usage_with_options(request, runtime)

    async def get_order_usage_async(
        self,
        request: opt_20210730_models.GetOrderUsageRequest,
    ) -> opt_20210730_models.GetOrderUsageResponse:
        """
        @param request: GetOrderUsageRequest
        @return: GetOrderUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_order_usage_with_options_async(request, runtime)
