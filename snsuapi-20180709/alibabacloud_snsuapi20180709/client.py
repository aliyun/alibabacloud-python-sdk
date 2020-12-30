# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_snsuapi20180709 import models as snsuapi_20180709_models
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
        self._endpoint = self.get_endpoint('snsuapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def band_offer_order_with_options(
        self,
        request: snsuapi_20180709_models.BandOfferOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandOfferOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandOfferOrderResponse().from_map(
            self.do_rpcrequest('BandOfferOrder', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def band_offer_order_with_options_async(
        self,
        request: snsuapi_20180709_models.BandOfferOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandOfferOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandOfferOrderResponse().from_map(
            await self.do_rpcrequest_async('BandOfferOrder', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def band_offer_order(
        self,
        request: snsuapi_20180709_models.BandOfferOrderRequest,
    ) -> snsuapi_20180709_models.BandOfferOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.band_offer_order_with_options(request, runtime)

    async def band_offer_order_async(
        self,
        request: snsuapi_20180709_models.BandOfferOrderRequest,
    ) -> snsuapi_20180709_models.BandOfferOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.band_offer_order_with_options_async(request, runtime)

    def band_precheck_with_options(
        self,
        request: snsuapi_20180709_models.BandPrecheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandPrecheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandPrecheckResponse().from_map(
            self.do_rpcrequest('BandPrecheck', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def band_precheck_with_options_async(
        self,
        request: snsuapi_20180709_models.BandPrecheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandPrecheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandPrecheckResponse().from_map(
            await self.do_rpcrequest_async('BandPrecheck', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def band_precheck(
        self,
        request: snsuapi_20180709_models.BandPrecheckRequest,
    ) -> snsuapi_20180709_models.BandPrecheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.band_precheck_with_options(request, runtime)

    async def band_precheck_async(
        self,
        request: snsuapi_20180709_models.BandPrecheckRequest,
    ) -> snsuapi_20180709_models.BandPrecheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.band_precheck_with_options_async(request, runtime)

    def band_start_speed_up_with_options(
        self,
        request: snsuapi_20180709_models.BandStartSpeedUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandStartSpeedUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandStartSpeedUpResponse().from_map(
            self.do_rpcrequest('BandStartSpeedUp', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def band_start_speed_up_with_options_async(
        self,
        request: snsuapi_20180709_models.BandStartSpeedUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandStartSpeedUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandStartSpeedUpResponse().from_map(
            await self.do_rpcrequest_async('BandStartSpeedUp', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def band_start_speed_up(
        self,
        request: snsuapi_20180709_models.BandStartSpeedUpRequest,
    ) -> snsuapi_20180709_models.BandStartSpeedUpResponse:
        runtime = util_models.RuntimeOptions()
        return self.band_start_speed_up_with_options(request, runtime)

    async def band_start_speed_up_async(
        self,
        request: snsuapi_20180709_models.BandStartSpeedUpRequest,
    ) -> snsuapi_20180709_models.BandStartSpeedUpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.band_start_speed_up_with_options_async(request, runtime)

    def band_status_query_with_options(
        self,
        request: snsuapi_20180709_models.BandStatusQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandStatusQueryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandStatusQueryResponse().from_map(
            self.do_rpcrequest('BandStatusQuery', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def band_status_query_with_options_async(
        self,
        request: snsuapi_20180709_models.BandStatusQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandStatusQueryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandStatusQueryResponse().from_map(
            await self.do_rpcrequest_async('BandStatusQuery', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def band_status_query(
        self,
        request: snsuapi_20180709_models.BandStatusQueryRequest,
    ) -> snsuapi_20180709_models.BandStatusQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.band_status_query_with_options(request, runtime)

    async def band_status_query_async(
        self,
        request: snsuapi_20180709_models.BandStatusQueryRequest,
    ) -> snsuapi_20180709_models.BandStatusQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.band_status_query_with_options_async(request, runtime)

    def band_stop_speed_up_with_options(
        self,
        request: snsuapi_20180709_models.BandStopSpeedUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandStopSpeedUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandStopSpeedUpResponse().from_map(
            self.do_rpcrequest('BandStopSpeedUp', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def band_stop_speed_up_with_options_async(
        self,
        request: snsuapi_20180709_models.BandStopSpeedUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.BandStopSpeedUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.BandStopSpeedUpResponse().from_map(
            await self.do_rpcrequest_async('BandStopSpeedUp', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def band_stop_speed_up(
        self,
        request: snsuapi_20180709_models.BandStopSpeedUpRequest,
    ) -> snsuapi_20180709_models.BandStopSpeedUpResponse:
        runtime = util_models.RuntimeOptions()
        return self.band_stop_speed_up_with_options(request, runtime)

    async def band_stop_speed_up_async(
        self,
        request: snsuapi_20180709_models.BandStopSpeedUpRequest,
    ) -> snsuapi_20180709_models.BandStopSpeedUpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.band_stop_speed_up_with_options_async(request, runtime)

    def mobile_start_speed_up_with_options(
        self,
        request: snsuapi_20180709_models.MobileStartSpeedUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.MobileStartSpeedUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.MobileStartSpeedUpResponse().from_map(
            self.do_rpcrequest('MobileStartSpeedUp', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mobile_start_speed_up_with_options_async(
        self,
        request: snsuapi_20180709_models.MobileStartSpeedUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.MobileStartSpeedUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.MobileStartSpeedUpResponse().from_map(
            await self.do_rpcrequest_async('MobileStartSpeedUp', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mobile_start_speed_up(
        self,
        request: snsuapi_20180709_models.MobileStartSpeedUpRequest,
    ) -> snsuapi_20180709_models.MobileStartSpeedUpResponse:
        runtime = util_models.RuntimeOptions()
        return self.mobile_start_speed_up_with_options(request, runtime)

    async def mobile_start_speed_up_async(
        self,
        request: snsuapi_20180709_models.MobileStartSpeedUpRequest,
    ) -> snsuapi_20180709_models.MobileStartSpeedUpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mobile_start_speed_up_with_options_async(request, runtime)

    def mobile_status_query_with_options(
        self,
        request: snsuapi_20180709_models.MobileStatusQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.MobileStatusQueryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.MobileStatusQueryResponse().from_map(
            self.do_rpcrequest('MobileStatusQuery', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mobile_status_query_with_options_async(
        self,
        request: snsuapi_20180709_models.MobileStatusQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.MobileStatusQueryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.MobileStatusQueryResponse().from_map(
            await self.do_rpcrequest_async('MobileStatusQuery', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mobile_status_query(
        self,
        request: snsuapi_20180709_models.MobileStatusQueryRequest,
    ) -> snsuapi_20180709_models.MobileStatusQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.mobile_status_query_with_options(request, runtime)

    async def mobile_status_query_async(
        self,
        request: snsuapi_20180709_models.MobileStatusQueryRequest,
    ) -> snsuapi_20180709_models.MobileStatusQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mobile_status_query_with_options_async(request, runtime)

    def mobile_stop_speed_up_with_options(
        self,
        request: snsuapi_20180709_models.MobileStopSpeedUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.MobileStopSpeedUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.MobileStopSpeedUpResponse().from_map(
            self.do_rpcrequest('MobileStopSpeedUp', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mobile_stop_speed_up_with_options_async(
        self,
        request: snsuapi_20180709_models.MobileStopSpeedUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> snsuapi_20180709_models.MobileStopSpeedUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return snsuapi_20180709_models.MobileStopSpeedUpResponse().from_map(
            await self.do_rpcrequest_async('MobileStopSpeedUp', '2018-07-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mobile_stop_speed_up(
        self,
        request: snsuapi_20180709_models.MobileStopSpeedUpRequest,
    ) -> snsuapi_20180709_models.MobileStopSpeedUpResponse:
        runtime = util_models.RuntimeOptions()
        return self.mobile_stop_speed_up_with_options(request, runtime)

    async def mobile_stop_speed_up_async(
        self,
        request: snsuapi_20180709_models.MobileStopSpeedUpRequest,
    ) -> snsuapi_20180709_models.MobileStopSpeedUpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mobile_stop_speed_up_with_options_async(request, runtime)
