# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudgameapi20200728 import models as cloud_game_api20200728_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudgameapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_dispatch_game_slot_with_options(
        self,
        request: cloud_game_api20200728_models.BatchDispatchGameSlotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.BatchDispatchGameSlotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchDispatchGameSlotResponse(),
            self.do_rpcrequest('BatchDispatchGameSlot', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_dispatch_game_slot_with_options_async(
        self,
        request: cloud_game_api20200728_models.BatchDispatchGameSlotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.BatchDispatchGameSlotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchDispatchGameSlotResponse(),
            await self.do_rpcrequest_async('BatchDispatchGameSlot', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_dispatch_game_slot(
        self,
        request: cloud_game_api20200728_models.BatchDispatchGameSlotRequest,
    ) -> cloud_game_api20200728_models.BatchDispatchGameSlotResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_dispatch_game_slot_with_options(request, runtime)

    async def batch_dispatch_game_slot_async(
        self,
        request: cloud_game_api20200728_models.BatchDispatchGameSlotRequest,
    ) -> cloud_game_api20200728_models.BatchDispatchGameSlotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_dispatch_game_slot_with_options_async(request, runtime)

    def batch_stop_game_sessions_with_options(
        self,
        request: cloud_game_api20200728_models.BatchStopGameSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.BatchStopGameSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchStopGameSessionsResponse(),
            self.do_rpcrequest('BatchStopGameSessions', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_stop_game_sessions_with_options_async(
        self,
        request: cloud_game_api20200728_models.BatchStopGameSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.BatchStopGameSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchStopGameSessionsResponse(),
            await self.do_rpcrequest_async('BatchStopGameSessions', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_stop_game_sessions(
        self,
        request: cloud_game_api20200728_models.BatchStopGameSessionsRequest,
    ) -> cloud_game_api20200728_models.BatchStopGameSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_game_sessions_with_options(request, runtime)

    async def batch_stop_game_sessions_async(
        self,
        request: cloud_game_api20200728_models.BatchStopGameSessionsRequest,
    ) -> cloud_game_api20200728_models.BatchStopGameSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_game_sessions_with_options_async(request, runtime)

    def close_order_with_options(
        self,
        request: cloud_game_api20200728_models.CloseOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CloseOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CloseOrderResponse(),
            self.do_rpcrequest('CloseOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_order_with_options_async(
        self,
        request: cloud_game_api20200728_models.CloseOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CloseOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CloseOrderResponse(),
            await self.do_rpcrequest_async('CloseOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_order(
        self,
        request: cloud_game_api20200728_models.CloseOrderRequest,
    ) -> cloud_game_api20200728_models.CloseOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_order_with_options(request, runtime)

    async def close_order_async(
        self,
        request: cloud_game_api20200728_models.CloseOrderRequest,
    ) -> cloud_game_api20200728_models.CloseOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_order_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: cloud_game_api20200728_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateOrderResponse(),
            self.do_rpcrequest('CreateOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: cloud_game_api20200728_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateOrderResponse(),
            await self.do_rpcrequest_async('CreateOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order(
        self,
        request: cloud_game_api20200728_models.CreateOrderRequest,
    ) -> cloud_game_api20200728_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: cloud_game_api20200728_models.CreateOrderRequest,
    ) -> cloud_game_api20200728_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def create_token_with_options(
        self,
        request: cloud_game_api20200728_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateTokenResponse(),
            self.do_rpcrequest('CreateToken', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_token_with_options_async(
        self,
        request: cloud_game_api20200728_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateTokenResponse(),
            await self.do_rpcrequest_async('CreateToken', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_token(
        self,
        request: cloud_game_api20200728_models.CreateTokenRequest,
    ) -> cloud_game_api20200728_models.CreateTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    async def create_token_async(
        self,
        request: cloud_game_api20200728_models.CreateTokenRequest,
    ) -> cloud_game_api20200728_models.CreateTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_token_with_options_async(request, runtime)

    def delivery_order_with_options(
        self,
        request: cloud_game_api20200728_models.DeliveryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeliveryOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeliveryOrderResponse(),
            self.do_rpcrequest('DeliveryOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delivery_order_with_options_async(
        self,
        request: cloud_game_api20200728_models.DeliveryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeliveryOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeliveryOrderResponse(),
            await self.do_rpcrequest_async('DeliveryOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delivery_order(
        self,
        request: cloud_game_api20200728_models.DeliveryOrderRequest,
    ) -> cloud_game_api20200728_models.DeliveryOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delivery_order_with_options(request, runtime)

    async def delivery_order_async(
        self,
        request: cloud_game_api20200728_models.DeliveryOrderRequest,
    ) -> cloud_game_api20200728_models.DeliveryOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delivery_order_with_options_async(request, runtime)

    def dispatch_game_slot_with_options(
        self,
        request: cloud_game_api20200728_models.DispatchGameSlotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DispatchGameSlotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DispatchGameSlotResponse(),
            self.do_rpcrequest('DispatchGameSlot', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dispatch_game_slot_with_options_async(
        self,
        request: cloud_game_api20200728_models.DispatchGameSlotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DispatchGameSlotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DispatchGameSlotResponse(),
            await self.do_rpcrequest_async('DispatchGameSlot', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dispatch_game_slot(
        self,
        request: cloud_game_api20200728_models.DispatchGameSlotRequest,
    ) -> cloud_game_api20200728_models.DispatchGameSlotResponse:
        runtime = util_models.RuntimeOptions()
        return self.dispatch_game_slot_with_options(request, runtime)

    async def dispatch_game_slot_async(
        self,
        request: cloud_game_api20200728_models.DispatchGameSlotRequest,
    ) -> cloud_game_api20200728_models.DispatchGameSlotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dispatch_game_slot_with_options_async(request, runtime)

    def get_game_ccu_with_options(
        self,
        request: cloud_game_api20200728_models.GetGameCcuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameCcuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameCcuResponse(),
            self.do_rpcrequest('GetGameCcu', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_game_ccu_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetGameCcuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameCcuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameCcuResponse(),
            await self.do_rpcrequest_async('GetGameCcu', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_game_ccu(
        self,
        request: cloud_game_api20200728_models.GetGameCcuRequest,
    ) -> cloud_game_api20200728_models.GetGameCcuResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_game_ccu_with_options(request, runtime)

    async def get_game_ccu_async(
        self,
        request: cloud_game_api20200728_models.GetGameCcuRequest,
    ) -> cloud_game_api20200728_models.GetGameCcuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_game_ccu_with_options_async(request, runtime)

    def get_game_stock_with_options(
        self,
        request: cloud_game_api20200728_models.GetGameStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameStockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStockResponse(),
            self.do_rpcrequest('GetGameStock', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_game_stock_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetGameStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameStockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStockResponse(),
            await self.do_rpcrequest_async('GetGameStock', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_game_stock(
        self,
        request: cloud_game_api20200728_models.GetGameStockRequest,
    ) -> cloud_game_api20200728_models.GetGameStockResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_game_stock_with_options(request, runtime)

    async def get_game_stock_async(
        self,
        request: cloud_game_api20200728_models.GetGameStockRequest,
    ) -> cloud_game_api20200728_models.GetGameStockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_game_stock_with_options_async(request, runtime)

    def get_item_with_options(
        self,
        request: cloud_game_api20200728_models.GetItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetItemResponse(),
            self.do_rpcrequest('GetItem', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_item_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetItemResponse(),
            await self.do_rpcrequest_async('GetItem', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_item(
        self,
        request: cloud_game_api20200728_models.GetItemRequest,
    ) -> cloud_game_api20200728_models.GetItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_item_with_options(request, runtime)

    async def get_item_async(
        self,
        request: cloud_game_api20200728_models.GetItemRequest,
    ) -> cloud_game_api20200728_models.GetItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_item_with_options_async(request, runtime)

    def get_out_account_bind_detail_with_options(
        self,
        request: cloud_game_api20200728_models.GetOutAccountBindDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetOutAccountBindDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetOutAccountBindDetailResponse(),
            self.do_rpcrequest('GetOutAccountBindDetail', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_out_account_bind_detail_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetOutAccountBindDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetOutAccountBindDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetOutAccountBindDetailResponse(),
            await self.do_rpcrequest_async('GetOutAccountBindDetail', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_out_account_bind_detail(
        self,
        request: cloud_game_api20200728_models.GetOutAccountBindDetailRequest,
    ) -> cloud_game_api20200728_models.GetOutAccountBindDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_out_account_bind_detail_with_options(request, runtime)

    async def get_out_account_bind_detail_async(
        self,
        request: cloud_game_api20200728_models.GetOutAccountBindDetailRequest,
    ) -> cloud_game_api20200728_models.GetOutAccountBindDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_out_account_bind_detail_with_options_async(request, runtime)

    def get_session_with_options(
        self,
        request: cloud_game_api20200728_models.GetSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetSessionResponse(),
            self.do_rpcrequest('GetSession', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_session_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetSessionResponse(),
            await self.do_rpcrequest_async('GetSession', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session(
        self,
        request: cloud_game_api20200728_models.GetSessionRequest,
    ) -> cloud_game_api20200728_models.GetSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_session_with_options(request, runtime)

    async def get_session_async(
        self,
        request: cloud_game_api20200728_models.GetSessionRequest,
    ) -> cloud_game_api20200728_models.GetSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_session_with_options_async(request, runtime)

    def get_stop_game_token_with_options(
        self,
        request: cloud_game_api20200728_models.GetStopGameTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetStopGameTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetStopGameTokenResponse(),
            self.do_rpcrequest('GetStopGameToken', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stop_game_token_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetStopGameTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetStopGameTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetStopGameTokenResponse(),
            await self.do_rpcrequest_async('GetStopGameToken', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stop_game_token(
        self,
        request: cloud_game_api20200728_models.GetStopGameTokenRequest,
    ) -> cloud_game_api20200728_models.GetStopGameTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stop_game_token_with_options(request, runtime)

    async def get_stop_game_token_async(
        self,
        request: cloud_game_api20200728_models.GetStopGameTokenRequest,
    ) -> cloud_game_api20200728_models.GetStopGameTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stop_game_token_with_options_async(request, runtime)

    def list_bought_games_with_options(
        self,
        request: cloud_game_api20200728_models.ListBoughtGamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListBoughtGamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListBoughtGamesResponse(),
            self.do_rpcrequest('ListBoughtGames', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bought_games_with_options_async(
        self,
        request: cloud_game_api20200728_models.ListBoughtGamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListBoughtGamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListBoughtGamesResponse(),
            await self.do_rpcrequest_async('ListBoughtGames', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bought_games(
        self,
        request: cloud_game_api20200728_models.ListBoughtGamesRequest,
    ) -> cloud_game_api20200728_models.ListBoughtGamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bought_games_with_options(request, runtime)

    async def list_bought_games_async(
        self,
        request: cloud_game_api20200728_models.ListBoughtGamesRequest,
    ) -> cloud_game_api20200728_models.ListBoughtGamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bought_games_with_options_async(request, runtime)

    def query_game_with_options(
        self,
        request: cloud_game_api20200728_models.QueryGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryGameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryGameResponse(),
            self.do_rpcrequest('QueryGame', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_game_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryGameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryGameResponse(),
            await self.do_rpcrequest_async('QueryGame', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_game(
        self,
        request: cloud_game_api20200728_models.QueryGameRequest,
    ) -> cloud_game_api20200728_models.QueryGameResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_game_with_options(request, runtime)

    async def query_game_async(
        self,
        request: cloud_game_api20200728_models.QueryGameRequest,
    ) -> cloud_game_api20200728_models.QueryGameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_game_with_options_async(request, runtime)

    def query_items_with_options(
        self,
        request: cloud_game_api20200728_models.QueryItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryItemsResponse(),
            self.do_rpcrequest('QueryItems', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_items_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryItemsResponse(),
            await self.do_rpcrequest_async('QueryItems', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_items(
        self,
        request: cloud_game_api20200728_models.QueryItemsRequest,
    ) -> cloud_game_api20200728_models.QueryItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_items_with_options(request, runtime)

    async def query_items_async(
        self,
        request: cloud_game_api20200728_models.QueryItemsRequest,
    ) -> cloud_game_api20200728_models.QueryItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_items_with_options_async(request, runtime)

    def query_order_with_options(
        self,
        request: cloud_game_api20200728_models.QueryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOrderResponse(),
            self.do_rpcrequest('QueryOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_order_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOrderResponse(),
            await self.do_rpcrequest_async('QueryOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order(
        self,
        request: cloud_game_api20200728_models.QueryOrderRequest,
    ) -> cloud_game_api20200728_models.QueryOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_with_options(request, runtime)

    async def query_order_async(
        self,
        request: cloud_game_api20200728_models.QueryOrderRequest,
    ) -> cloud_game_api20200728_models.QueryOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_with_options_async(request, runtime)

    def query_out_account_bind_status_with_options(
        self,
        request: cloud_game_api20200728_models.QueryOutAccountBindStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryOutAccountBindStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOutAccountBindStatusResponse(),
            self.do_rpcrequest('QueryOutAccountBindStatus', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_out_account_bind_status_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryOutAccountBindStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryOutAccountBindStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOutAccountBindStatusResponse(),
            await self.do_rpcrequest_async('QueryOutAccountBindStatus', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_out_account_bind_status(
        self,
        request: cloud_game_api20200728_models.QueryOutAccountBindStatusRequest,
    ) -> cloud_game_api20200728_models.QueryOutAccountBindStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_out_account_bind_status_with_options(request, runtime)

    async def query_out_account_bind_status_async(
        self,
        request: cloud_game_api20200728_models.QueryOutAccountBindStatusRequest,
    ) -> cloud_game_api20200728_models.QueryOutAccountBindStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_out_account_bind_status_with_options_async(request, runtime)

    def query_project_with_options(
        self,
        request: cloud_game_api20200728_models.QueryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryProjectResponse(),
            self.do_rpcrequest('QueryProject', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_project_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryProjectResponse(),
            await self.do_rpcrequest_async('QueryProject', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_project(
        self,
        request: cloud_game_api20200728_models.QueryProjectRequest,
    ) -> cloud_game_api20200728_models.QueryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_project_with_options(request, runtime)

    async def query_project_async(
        self,
        request: cloud_game_api20200728_models.QueryProjectRequest,
    ) -> cloud_game_api20200728_models.QueryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_project_with_options_async(request, runtime)

    def query_tenant_with_options(
        self,
        request: cloud_game_api20200728_models.QueryTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryTenantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryTenantResponse(),
            self.do_rpcrequest('QueryTenant', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_tenant_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryTenantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryTenantResponse(),
            await self.do_rpcrequest_async('QueryTenant', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tenant(
        self,
        request: cloud_game_api20200728_models.QueryTenantRequest,
    ) -> cloud_game_api20200728_models.QueryTenantResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tenant_with_options(request, runtime)

    async def query_tenant_async(
        self,
        request: cloud_game_api20200728_models.QueryTenantRequest,
    ) -> cloud_game_api20200728_models.QueryTenantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tenant_with_options_async(request, runtime)

    def skip_trial_policy_with_options(
        self,
        request: cloud_game_api20200728_models.SkipTrialPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SkipTrialPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SkipTrialPolicyResponse(),
            self.do_rpcrequest('SkipTrialPolicy', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def skip_trial_policy_with_options_async(
        self,
        request: cloud_game_api20200728_models.SkipTrialPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SkipTrialPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SkipTrialPolicyResponse(),
            await self.do_rpcrequest_async('SkipTrialPolicy', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def skip_trial_policy(
        self,
        request: cloud_game_api20200728_models.SkipTrialPolicyRequest,
    ) -> cloud_game_api20200728_models.SkipTrialPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.skip_trial_policy_with_options(request, runtime)

    async def skip_trial_policy_async(
        self,
        request: cloud_game_api20200728_models.SkipTrialPolicyRequest,
    ) -> cloud_game_api20200728_models.SkipTrialPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.skip_trial_policy_with_options_async(request, runtime)

    def stop_game_session_with_options(
        self,
        request: cloud_game_api20200728_models.StopGameSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.StopGameSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.StopGameSessionResponse(),
            self.do_rpcrequest('StopGameSession', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_game_session_with_options_async(
        self,
        request: cloud_game_api20200728_models.StopGameSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.StopGameSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.StopGameSessionResponse(),
            await self.do_rpcrequest_async('StopGameSession', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_game_session(
        self,
        request: cloud_game_api20200728_models.StopGameSessionRequest,
    ) -> cloud_game_api20200728_models.StopGameSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_game_session_with_options(request, runtime)

    async def stop_game_session_async(
        self,
        request: cloud_game_api20200728_models.StopGameSessionRequest,
    ) -> cloud_game_api20200728_models.StopGameSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_game_session_with_options_async(request, runtime)

    def submit_internal_purchase_charge_data_with_options(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse(),
            self.do_rpcrequest('SubmitInternalPurchaseChargeData', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_internal_purchase_charge_data_with_options_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse(),
            await self.do_rpcrequest_async('SubmitInternalPurchaseChargeData', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_internal_purchase_charge_data(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataRequest,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_charge_data_with_options(request, runtime)

    async def submit_internal_purchase_charge_data_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataRequest,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_internal_purchase_charge_data_with_options_async(request, runtime)

    def submit_internal_purchase_orders_with_options(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse(),
            self.do_rpcrequest('SubmitInternalPurchaseOrders', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_internal_purchase_orders_with_options_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse(),
            await self.do_rpcrequest_async('SubmitInternalPurchaseOrders', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_internal_purchase_orders(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseOrdersRequest,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_orders_with_options(request, runtime)

    async def submit_internal_purchase_orders_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseOrdersRequest,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_internal_purchase_orders_with_options_async(request, runtime)

    def submit_internal_purchase_ready_flag_with_options(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse(),
            self.do_rpcrequest('SubmitInternalPurchaseReadyFlag', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_internal_purchase_ready_flag_with_options_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse(),
            await self.do_rpcrequest_async('SubmitInternalPurchaseReadyFlag', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_internal_purchase_ready_flag(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagRequest,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_ready_flag_with_options(request, runtime)

    async def submit_internal_purchase_ready_flag_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagRequest,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_internal_purchase_ready_flag_with_options_async(request, runtime)
