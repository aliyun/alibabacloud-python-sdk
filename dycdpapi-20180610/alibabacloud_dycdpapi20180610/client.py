# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dycdpapi20180610 import models as dycdpapi_20180610_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('dycdpapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_cdp_offer_with_options(
        self,
        request: dycdpapi_20180610_models.QueryCdpOfferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dycdpapi_20180610_models.QueryCdpOfferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dycdpapi_20180610_models.QueryCdpOfferResponse().from_map(
            self.do_rpcrequest('QueryCdpOffer', '2018-06-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cdp_offer_with_options_async(
        self,
        request: dycdpapi_20180610_models.QueryCdpOfferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dycdpapi_20180610_models.QueryCdpOfferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dycdpapi_20180610_models.QueryCdpOfferResponse().from_map(
            await self.do_rpcrequest_async('QueryCdpOffer', '2018-06-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cdp_offer(
        self,
        request: dycdpapi_20180610_models.QueryCdpOfferRequest,
    ) -> dycdpapi_20180610_models.QueryCdpOfferResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cdp_offer_with_options(request, runtime)

    async def query_cdp_offer_async(
        self,
        request: dycdpapi_20180610_models.QueryCdpOfferRequest,
    ) -> dycdpapi_20180610_models.QueryCdpOfferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cdp_offer_with_options_async(request, runtime)

    def query_cdp_offer_by_id_with_options(
        self,
        request: dycdpapi_20180610_models.QueryCdpOfferByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dycdpapi_20180610_models.QueryCdpOfferByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dycdpapi_20180610_models.QueryCdpOfferByIdResponse().from_map(
            self.do_rpcrequest('QueryCdpOfferById', '2018-06-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cdp_offer_by_id_with_options_async(
        self,
        request: dycdpapi_20180610_models.QueryCdpOfferByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dycdpapi_20180610_models.QueryCdpOfferByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dycdpapi_20180610_models.QueryCdpOfferByIdResponse().from_map(
            await self.do_rpcrequest_async('QueryCdpOfferById', '2018-06-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cdp_offer_by_id(
        self,
        request: dycdpapi_20180610_models.QueryCdpOfferByIdRequest,
    ) -> dycdpapi_20180610_models.QueryCdpOfferByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cdp_offer_by_id_with_options(request, runtime)

    async def query_cdp_offer_by_id_async(
        self,
        request: dycdpapi_20180610_models.QueryCdpOfferByIdRequest,
    ) -> dycdpapi_20180610_models.QueryCdpOfferByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cdp_offer_by_id_with_options_async(request, runtime)

    def query_cdp_order_with_options(
        self,
        request: dycdpapi_20180610_models.QueryCdpOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dycdpapi_20180610_models.QueryCdpOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dycdpapi_20180610_models.QueryCdpOrderResponse().from_map(
            self.do_rpcrequest('QueryCdpOrder', '2018-06-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cdp_order_with_options_async(
        self,
        request: dycdpapi_20180610_models.QueryCdpOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dycdpapi_20180610_models.QueryCdpOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dycdpapi_20180610_models.QueryCdpOrderResponse().from_map(
            await self.do_rpcrequest_async('QueryCdpOrder', '2018-06-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cdp_order(
        self,
        request: dycdpapi_20180610_models.QueryCdpOrderRequest,
    ) -> dycdpapi_20180610_models.QueryCdpOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cdp_order_with_options(request, runtime)

    async def query_cdp_order_async(
        self,
        request: dycdpapi_20180610_models.QueryCdpOrderRequest,
    ) -> dycdpapi_20180610_models.QueryCdpOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cdp_order_with_options_async(request, runtime)
