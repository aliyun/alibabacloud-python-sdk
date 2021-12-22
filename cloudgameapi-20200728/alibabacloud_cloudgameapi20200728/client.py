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

    def adapt_game_version_with_options(
        self,
        request: cloud_game_api20200728_models.AdaptGameVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.AdaptGameVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FrameRate'] = request.frame_rate
        query['Resolution'] = request.resolution
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AdaptGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.AdaptGameVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def adapt_game_version_with_options_async(
        self,
        request: cloud_game_api20200728_models.AdaptGameVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.AdaptGameVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FrameRate'] = request.frame_rate
        query['Resolution'] = request.resolution
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AdaptGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.AdaptGameVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def adapt_game_version(
        self,
        request: cloud_game_api20200728_models.AdaptGameVersionRequest,
    ) -> cloud_game_api20200728_models.AdaptGameVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.adapt_game_version_with_options(request, runtime)

    async def adapt_game_version_async(
        self,
        request: cloud_game_api20200728_models.AdaptGameVersionRequest,
    ) -> cloud_game_api20200728_models.AdaptGameVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.adapt_game_version_with_options_async(request, runtime)

    def add_game_to_project_with_options(
        self,
        request: cloud_game_api20200728_models.AddGameToProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.AddGameToProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGameToProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.AddGameToProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_game_to_project_with_options_async(
        self,
        request: cloud_game_api20200728_models.AddGameToProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.AddGameToProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGameToProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.AddGameToProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_game_to_project(
        self,
        request: cloud_game_api20200728_models.AddGameToProjectRequest,
    ) -> cloud_game_api20200728_models.AddGameToProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_game_to_project_with_options(request, runtime)

    async def add_game_to_project_async(
        self,
        request: cloud_game_api20200728_models.AddGameToProjectRequest,
    ) -> cloud_game_api20200728_models.AddGameToProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_game_to_project_with_options_async(request, runtime)

    def batch_dispatch_game_slot_with_options(
        self,
        request: cloud_game_api20200728_models.BatchDispatchGameSlotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.BatchDispatchGameSlotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.queue_user_list):
            body['QueueUserList'] = request.queue_user_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDispatchGameSlot',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchDispatchGameSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_dispatch_game_slot_with_options_async(
        self,
        request: cloud_game_api20200728_models.BatchDispatchGameSlotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.BatchDispatchGameSlotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.queue_user_list):
            body['QueueUserList'] = request.queue_user_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDispatchGameSlot',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchDispatchGameSlotResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        query['Reason'] = request.reason
        query['Tags'] = request.tags
        query['Token'] = request.token
        query['TrackInfo'] = request.track_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopGameSessions',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchStopGameSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_game_sessions_with_options_async(
        self,
        request: cloud_game_api20200728_models.BatchStopGameSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.BatchStopGameSessionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        query['Reason'] = request.reason
        query['Tags'] = request.tags
        query['Token'] = request.token
        query['TrackInfo'] = request.track_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopGameSessions',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchStopGameSessionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CloseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_order_with_options_async(
        self,
        request: cloud_game_api20200728_models.CloseOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CloseOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CloseOrderResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_game_with_options(
        self,
        request: cloud_game_api20200728_models.CreateGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateGameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['GameName'] = request.game_name
        query['PlatformType'] = request.platform_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateGameResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_game_with_options_async(
        self,
        request: cloud_game_api20200728_models.CreateGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateGameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['GameName'] = request.game_name
        query['PlatformType'] = request.platform_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateGameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_game(
        self,
        request: cloud_game_api20200728_models.CreateGameRequest,
    ) -> cloud_game_api20200728_models.CreateGameResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_game_with_options(request, runtime)

    async def create_game_async(
        self,
        request: cloud_game_api20200728_models.CreateGameRequest,
    ) -> cloud_game_api20200728_models.CreateGameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_game_with_options_async(request, runtime)

    def create_game_deploy_workflow_with_options(
        self,
        request: cloud_game_api20200728_models.CreateGameDeployWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateGameDeployWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DownloadType'] = request.download_type
        query['FileType'] = request.file_type
        query['FrameRate'] = request.frame_rate
        query['GameId'] = request.game_id
        query['GameVersion'] = request.game_version
        query['Hash'] = request.hash
        query['Instance'] = request.instance
        query['ProjectId'] = request.project_id
        query['Resolution'] = request.resolution
        query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGameDeployWorkflow',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateGameDeployWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_game_deploy_workflow_with_options_async(
        self,
        request: cloud_game_api20200728_models.CreateGameDeployWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateGameDeployWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DownloadType'] = request.download_type
        query['FileType'] = request.file_type
        query['FrameRate'] = request.frame_rate
        query['GameId'] = request.game_id
        query['GameVersion'] = request.game_version
        query['Hash'] = request.hash
        query['Instance'] = request.instance
        query['ProjectId'] = request.project_id
        query['Resolution'] = request.resolution
        query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGameDeployWorkflow',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateGameDeployWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_game_deploy_workflow(
        self,
        request: cloud_game_api20200728_models.CreateGameDeployWorkflowRequest,
    ) -> cloud_game_api20200728_models.CreateGameDeployWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_game_deploy_workflow_with_options(request, runtime)

    async def create_game_deploy_workflow_async(
        self,
        request: cloud_game_api20200728_models.CreateGameDeployWorkflowRequest,
    ) -> cloud_game_api20200728_models.CreateGameDeployWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_game_deploy_workflow_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: cloud_game_api20200728_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['Amount'] = request.amount
        query['BuyerAccountId'] = request.buyer_account_id
        query['IdempotentCode'] = request.idempotent_code
        query['ItemId'] = request.item_id
        query['OriginPrice'] = request.origin_price
        query['SettlementPrice'] = request.settlement_price
        query['SkuId'] = request.sku_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: cloud_game_api20200728_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['Amount'] = request.amount
        query['BuyerAccountId'] = request.buyer_account_id
        query['IdempotentCode'] = request.idempotent_code
        query['ItemId'] = request.item_id
        query['OriginPrice'] = request.origin_price
        query['SettlementPrice'] = request.settlement_price
        query['SkuId'] = request.sku_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_project_with_options(
        self,
        request: cloud_game_api20200728_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: cloud_game_api20200728_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: cloud_game_api20200728_models.CreateProjectRequest,
    ) -> cloud_game_api20200728_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: cloud_game_api20200728_models.CreateProjectRequest,
    ) -> cloud_game_api20200728_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_token_with_options(
        self,
        request: cloud_game_api20200728_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['CurrentToken'] = request.current_token
        query['Session'] = request.session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_with_options_async(
        self,
        request: cloud_game_api20200728_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['CurrentToken'] = request.current_token
        query['Session'] = request.session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateTokenResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_game_with_options(
        self,
        request: cloud_game_api20200728_models.DeleteGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeleteGameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteGameResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_game_with_options_async(
        self,
        request: cloud_game_api20200728_models.DeleteGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeleteGameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteGameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_game(
        self,
        request: cloud_game_api20200728_models.DeleteGameRequest,
    ) -> cloud_game_api20200728_models.DeleteGameResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_game_with_options(request, runtime)

    async def delete_game_async(
        self,
        request: cloud_game_api20200728_models.DeleteGameRequest,
    ) -> cloud_game_api20200728_models.DeleteGameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_game_with_options_async(request, runtime)

    def delete_game_version_with_options(
        self,
        request: cloud_game_api20200728_models.DeleteGameVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeleteGameVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteGameVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_game_version_with_options_async(
        self,
        request: cloud_game_api20200728_models.DeleteGameVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeleteGameVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteGameVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_game_version(
        self,
        request: cloud_game_api20200728_models.DeleteGameVersionRequest,
    ) -> cloud_game_api20200728_models.DeleteGameVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_game_version_with_options(request, runtime)

    async def delete_game_version_async(
        self,
        request: cloud_game_api20200728_models.DeleteGameVersionRequest,
    ) -> cloud_game_api20200728_models.DeleteGameVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_game_version_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: cloud_game_api20200728_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: cloud_game_api20200728_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: cloud_game_api20200728_models.DeleteProjectRequest,
    ) -> cloud_game_api20200728_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: cloud_game_api20200728_models.DeleteProjectRequest,
    ) -> cloud_game_api20200728_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delivery_order_with_options(
        self,
        request: cloud_game_api20200728_models.DeliveryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeliveryOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeliveryOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeliveryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delivery_order_with_options_async(
        self,
        request: cloud_game_api20200728_models.DeliveryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DeliveryOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeliveryOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeliveryOrderResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.biz_param):
            body['BizParam'] = request.biz_param
        if not UtilClient.is_unset(request.cancel):
            body['Cancel'] = request.cancel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.game_command):
            body['GameCommand'] = request.game_command
        if not UtilClient.is_unset(request.game_id):
            body['GameId'] = request.game_id
        if not UtilClient.is_unset(request.game_session):
            body['GameSession'] = request.game_session
        if not UtilClient.is_unset(request.game_start_param):
            body['GameStartParam'] = request.game_start_param
        if not UtilClient.is_unset(request.reconnect):
            body['Reconnect'] = request.reconnect
        if not UtilClient.is_unset(request.region_name):
            body['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.system_info):
            body['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_level):
            body['UserLevel'] = request.user_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DispatchGameSlot',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DispatchGameSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def dispatch_game_slot_with_options_async(
        self,
        request: cloud_game_api20200728_models.DispatchGameSlotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.DispatchGameSlotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.biz_param):
            body['BizParam'] = request.biz_param
        if not UtilClient.is_unset(request.cancel):
            body['Cancel'] = request.cancel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.game_command):
            body['GameCommand'] = request.game_command
        if not UtilClient.is_unset(request.game_id):
            body['GameId'] = request.game_id
        if not UtilClient.is_unset(request.game_session):
            body['GameSession'] = request.game_session
        if not UtilClient.is_unset(request.game_start_param):
            body['GameStartParam'] = request.game_start_param
        if not UtilClient.is_unset(request.reconnect):
            body['Reconnect'] = request.reconnect
        if not UtilClient.is_unset(request.region_name):
            body['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.system_info):
            body['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_level):
            body['UserLevel'] = request.user_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DispatchGameSlot',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DispatchGameSlotResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        query['RegionName'] = request.region_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameCcu',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameCcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_game_ccu_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetGameCcuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameCcuResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        query['RegionName'] = request.region_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameCcu',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameCcuResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_game_status_with_options(
        self,
        request: cloud_game_api20200728_models.GetGameStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameSession'] = request.game_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_game_status_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetGameStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameSession'] = request.game_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_game_status(
        self,
        request: cloud_game_api20200728_models.GetGameStatusRequest,
    ) -> cloud_game_api20200728_models.GetGameStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_game_status_with_options(request, runtime)

    async def get_game_status_async(
        self,
        request: cloud_game_api20200728_models.GetGameStatusRequest,
    ) -> cloud_game_api20200728_models.GetGameStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_game_status_with_options_async(request, runtime)

    def get_game_stock_with_options(
        self,
        request: cloud_game_api20200728_models.GetGameStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameStockResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        query['UserLevel'] = request.user_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameStock',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStockResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_game_stock_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetGameStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameStockResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        query['UserLevel'] = request.user_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameStock',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStockResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_game_trial_surplus_duration_with_options(
        self,
        request: cloud_game_api20200728_models.GetGameTrialSurplusDurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameTrialSurplusDurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameTrialSurplusDuration',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameTrialSurplusDurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_game_trial_surplus_duration_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetGameTrialSurplusDurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameTrialSurplusDurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameTrialSurplusDuration',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameTrialSurplusDurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_game_trial_surplus_duration(
        self,
        request: cloud_game_api20200728_models.GetGameTrialSurplusDurationRequest,
    ) -> cloud_game_api20200728_models.GetGameTrialSurplusDurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_game_trial_surplus_duration_with_options(request, runtime)

    async def get_game_trial_surplus_duration_async(
        self,
        request: cloud_game_api20200728_models.GetGameTrialSurplusDurationRequest,
    ) -> cloud_game_api20200728_models.GetGameTrialSurplusDurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_game_trial_surplus_duration_with_options_async(request, runtime)

    def get_game_version_with_options(
        self,
        request: cloud_game_api20200728_models.GetGameVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_game_version_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetGameVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_game_version(
        self,
        request: cloud_game_api20200728_models.GetGameVersionRequest,
    ) -> cloud_game_api20200728_models.GetGameVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_game_version_with_options(request, runtime)

    async def get_game_version_async(
        self,
        request: cloud_game_api20200728_models.GetGameVersionRequest,
    ) -> cloud_game_api20200728_models.GetGameVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_game_version_with_options_async(request, runtime)

    def get_game_version_progress_with_options(
        self,
        request: cloud_game_api20200728_models.GetGameVersionProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameVersionProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameVersionProgress',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameVersionProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_game_version_progress_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetGameVersionProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetGameVersionProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameVersionProgress',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameVersionProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_game_version_progress(
        self,
        request: cloud_game_api20200728_models.GetGameVersionProgressRequest,
    ) -> cloud_game_api20200728_models.GetGameVersionProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_game_version_progress_with_options(request, runtime)

    async def get_game_version_progress_async(
        self,
        request: cloud_game_api20200728_models.GetGameVersionProgressRequest,
    ) -> cloud_game_api20200728_models.GetGameVersionProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_game_version_progress_with_options_async(request, runtime)

    def get_item_with_options(
        self,
        request: cloud_game_api20200728_models.GetItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetItemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItem',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_item_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetItemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItem',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetItemResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['OutAccountType'] = request.out_account_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOutAccountBindDetail',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetOutAccountBindDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_out_account_bind_detail_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetOutAccountBindDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetOutAccountBindDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['OutAccountType'] = request.out_account_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOutAccountBindDetail',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetOutAccountBindDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSession',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_session_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSession',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetSessionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStopGameToken',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetStopGameTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stop_game_token_with_options_async(
        self,
        request: cloud_game_api20200728_models.GetStopGameTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.GetStopGameTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStopGameToken',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetStopGameTokenResponse(),
            await self.call_api_async(params, req, runtime)
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

    def kick_player_with_options(
        self,
        request: cloud_game_api20200728_models.KickPlayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.KickPlayerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameSession'] = request.game_session
        query['KickedAccountId'] = request.kicked_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KickPlayer',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.KickPlayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def kick_player_with_options_async(
        self,
        request: cloud_game_api20200728_models.KickPlayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.KickPlayerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameSession'] = request.game_session
        query['KickedAccountId'] = request.kicked_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KickPlayer',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.KickPlayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kick_player(
        self,
        request: cloud_game_api20200728_models.KickPlayerRequest,
    ) -> cloud_game_api20200728_models.KickPlayerResponse:
        runtime = util_models.RuntimeOptions()
        return self.kick_player_with_options(request, runtime)

    async def kick_player_async(
        self,
        request: cloud_game_api20200728_models.KickPlayerRequest,
    ) -> cloud_game_api20200728_models.KickPlayerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kick_player_with_options_async(request, runtime)

    def list_bought_games_with_options(
        self,
        request: cloud_game_api20200728_models.ListBoughtGamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListBoughtGamesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBoughtGames',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListBoughtGamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bought_games_with_options_async(
        self,
        request: cloud_game_api20200728_models.ListBoughtGamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListBoughtGamesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBoughtGames',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListBoughtGamesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_container_status_with_options(
        self,
        request: cloud_game_api20200728_models.ListContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListContainerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameSessionIdList'] = request.game_session_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListContainerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_container_status_with_options_async(
        self,
        request: cloud_game_api20200728_models.ListContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListContainerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameSessionIdList'] = request.game_session_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListContainerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_container_status(
        self,
        request: cloud_game_api20200728_models.ListContainerStatusRequest,
    ) -> cloud_game_api20200728_models.ListContainerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_container_status_with_options(request, runtime)

    async def list_container_status_async(
        self,
        request: cloud_game_api20200728_models.ListContainerStatusRequest,
    ) -> cloud_game_api20200728_models.ListContainerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_container_status_with_options_async(request, runtime)

    def list_deployable_instances_with_options(
        self,
        request: cloud_game_api20200728_models.ListDeployableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListDeployableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployableInstances',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListDeployableInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployable_instances_with_options_async(
        self,
        request: cloud_game_api20200728_models.ListDeployableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListDeployableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployableInstances',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListDeployableInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployable_instances(
        self,
        request: cloud_game_api20200728_models.ListDeployableInstancesRequest,
    ) -> cloud_game_api20200728_models.ListDeployableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_deployable_instances_with_options(request, runtime)

    async def list_deployable_instances_async(
        self,
        request: cloud_game_api20200728_models.ListDeployableInstancesRequest,
    ) -> cloud_game_api20200728_models.ListDeployableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_deployable_instances_with_options_async(request, runtime)

    def list_game_versions_with_options(
        self,
        request: cloud_game_api20200728_models.ListGameVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListGameVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGameVersions',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListGameVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_game_versions_with_options_async(
        self,
        request: cloud_game_api20200728_models.ListGameVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListGameVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGameVersions',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListGameVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_game_versions(
        self,
        request: cloud_game_api20200728_models.ListGameVersionsRequest,
    ) -> cloud_game_api20200728_models.ListGameVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_game_versions_with_options(request, runtime)

    async def list_game_versions_async(
        self,
        request: cloud_game_api20200728_models.ListGameVersionsRequest,
    ) -> cloud_game_api20200728_models.ListGameVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_game_versions_with_options_async(request, runtime)

    def list_games_with_options(
        self,
        request: cloud_game_api20200728_models.ListGamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListGamesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGames',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListGamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_games_with_options_async(
        self,
        request: cloud_game_api20200728_models.ListGamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListGamesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGames',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListGamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_games(
        self,
        request: cloud_game_api20200728_models.ListGamesRequest,
    ) -> cloud_game_api20200728_models.ListGamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_games_with_options(request, runtime)

    async def list_games_async(
        self,
        request: cloud_game_api20200728_models.ListGamesRequest,
    ) -> cloud_game_api20200728_models.ListGamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_games_with_options_async(request, runtime)

    def list_history_container_status_with_options(
        self,
        request: cloud_game_api20200728_models.ListHistoryContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListHistoryContainerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['LastGameSessionId'] = request.last_game_session_id
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHistoryContainerStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListHistoryContainerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_history_container_status_with_options_async(
        self,
        request: cloud_game_api20200728_models.ListHistoryContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListHistoryContainerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['LastGameSessionId'] = request.last_game_session_id
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHistoryContainerStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListHistoryContainerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_history_container_status(
        self,
        request: cloud_game_api20200728_models.ListHistoryContainerStatusRequest,
    ) -> cloud_game_api20200728_models.ListHistoryContainerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_history_container_status_with_options(request, runtime)

    async def list_history_container_status_async(
        self,
        request: cloud_game_api20200728_models.ListHistoryContainerStatusRequest,
    ) -> cloud_game_api20200728_models.ListHistoryContainerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_history_container_status_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: cloud_game_api20200728_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: cloud_game_api20200728_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: cloud_game_api20200728_models.ListProjectsRequest,
    ) -> cloud_game_api20200728_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: cloud_game_api20200728_models.ListProjectsRequest,
    ) -> cloud_game_api20200728_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def query_game_with_options(
        self,
        request: cloud_game_api20200728_models.QueryGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryGameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryGameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_game_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryGameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryGameResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItems',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_items_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItems',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryItemsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOrderResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOutAccountBindStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOutAccountBindStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_out_account_bind_status_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryOutAccountBindStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryOutAccountBindStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOutAccountBindStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOutAccountBindStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_project_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTenant',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tenant_with_options_async(
        self,
        request: cloud_game_api20200728_models.QueryTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.QueryTenantResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTenant',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryTenantResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_game_from_project_with_options(
        self,
        request: cloud_game_api20200728_models.RemoveGameFromProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.RemoveGameFromProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveGameFromProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.RemoveGameFromProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_game_from_project_with_options_async(
        self,
        request: cloud_game_api20200728_models.RemoveGameFromProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.RemoveGameFromProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveGameFromProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.RemoveGameFromProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_game_from_project(
        self,
        request: cloud_game_api20200728_models.RemoveGameFromProjectRequest,
    ) -> cloud_game_api20200728_models.RemoveGameFromProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_game_from_project_with_options(request, runtime)

    async def remove_game_from_project_async(
        self,
        request: cloud_game_api20200728_models.RemoveGameFromProjectRequest,
    ) -> cloud_game_api20200728_models.RemoveGameFromProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_game_from_project_with_options_async(request, runtime)

    def skip_trial_policy_with_options(
        self,
        request: cloud_game_api20200728_models.SkipTrialPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SkipTrialPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameSessionId'] = request.game_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipTrialPolicy',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SkipTrialPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_trial_policy_with_options_async(
        self,
        request: cloud_game_api20200728_models.SkipTrialPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SkipTrialPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GameSessionId'] = request.game_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipTrialPolicy',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SkipTrialPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.biz_param):
            body['BizParam'] = request.biz_param
        if not UtilClient.is_unset(request.game_id):
            body['GameId'] = request.game_id
        if not UtilClient.is_unset(request.game_session):
            body['GameSession'] = request.game_session
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopGameSession',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.StopGameSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_game_session_with_options_async(
        self,
        request: cloud_game_api20200728_models.StopGameSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.StopGameSessionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.biz_param):
            body['BizParam'] = request.biz_param
        if not UtilClient.is_unset(request.game_id):
            body['GameId'] = request.game_id
        if not UtilClient.is_unset(request.game_session):
            body['GameSession'] = request.game_session
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopGameSession',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.StopGameSessionResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_deployment_with_options(
        self,
        request: cloud_game_api20200728_models.SubmitDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitDeploymentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CloudGameInstanceIds'] = request.cloud_game_instance_ids
        query['GameId'] = request.game_id
        query['OperationType'] = request.operation_type
        query['ProjectId'] = request.project_id
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDeployment',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_deployment_with_options_async(
        self,
        request: cloud_game_api20200728_models.SubmitDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitDeploymentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CloudGameInstanceIds'] = request.cloud_game_instance_ids
        query['GameId'] = request.game_id
        query['OperationType'] = request.operation_type
        query['ProjectId'] = request.project_id
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDeployment',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_deployment(
        self,
        request: cloud_game_api20200728_models.SubmitDeploymentRequest,
    ) -> cloud_game_api20200728_models.SubmitDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_deployment_with_options(request, runtime)

    async def submit_deployment_async(
        self,
        request: cloud_game_api20200728_models.SubmitDeploymentRequest,
    ) -> cloud_game_api20200728_models.SubmitDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_deployment_with_options_async(request, runtime)

    def submit_internal_purchase_charge_data_with_options(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActiveUserRetentionRateOneDay'] = request.active_user_retention_rate_one_day
        query['ActiveUserRetentionRateSevenDay'] = request.active_user_retention_rate_seven_day
        query['ActiveUserRetentionRateThirtyDay'] = request.active_user_retention_rate_thirty_day
        query['Arpu'] = request.arpu
        query['ChargeDate'] = request.charge_date
        query['Dau'] = request.dau
        query['GameId'] = request.game_id
        query['Mau'] = request.mau
        query['NewUserRetentionRateOneDay'] = request.new_user_retention_rate_one_day
        query['NewUserRetentionRateSevenDay'] = request.new_user_retention_rate_seven_day
        query['NewUserRetentionRateThirtyDay'] = request.new_user_retention_rate_thirty_day
        query['PaymentConversionRate'] = request.payment_conversion_rate
        query['PlayTimeAverageOneDay'] = request.play_time_average_one_day
        query['PlayTimeAverageThirtyDay'] = request.play_time_average_thirty_day
        query['PlayTimeNinetyPointsOneDay'] = request.play_time_ninety_points_one_day
        query['PlayTimeNinetyPointsThirtyDay'] = request.play_time_ninety_points_thirty_day
        query['PlayTimeRangeOneDay'] = request.play_time_range_one_day
        query['PlayTimeRangeThirtyDay'] = request.play_time_range_thirty_day
        query['UserActivationRate'] = request.user_activation_rate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseChargeData',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_internal_purchase_charge_data_with_options_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActiveUserRetentionRateOneDay'] = request.active_user_retention_rate_one_day
        query['ActiveUserRetentionRateSevenDay'] = request.active_user_retention_rate_seven_day
        query['ActiveUserRetentionRateThirtyDay'] = request.active_user_retention_rate_thirty_day
        query['Arpu'] = request.arpu
        query['ChargeDate'] = request.charge_date
        query['Dau'] = request.dau
        query['GameId'] = request.game_id
        query['Mau'] = request.mau
        query['NewUserRetentionRateOneDay'] = request.new_user_retention_rate_one_day
        query['NewUserRetentionRateSevenDay'] = request.new_user_retention_rate_seven_day
        query['NewUserRetentionRateThirtyDay'] = request.new_user_retention_rate_thirty_day
        query['PaymentConversionRate'] = request.payment_conversion_rate
        query['PlayTimeAverageOneDay'] = request.play_time_average_one_day
        query['PlayTimeAverageThirtyDay'] = request.play_time_average_thirty_day
        query['PlayTimeNinetyPointsOneDay'] = request.play_time_ninety_points_one_day
        query['PlayTimeNinetyPointsThirtyDay'] = request.play_time_ninety_points_thirty_day
        query['PlayTimeRangeOneDay'] = request.play_time_range_one_day
        query['PlayTimeRangeThirtyDay'] = request.play_time_range_thirty_day
        query['UserActivationRate'] = request.user_activation_rate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseChargeData',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OrderList'] = request.order_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseOrders',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_internal_purchase_orders_with_options_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OrderList'] = request.order_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseOrders',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['BatchInfoList'] = request.batch_info_list
        query['ChargeDate'] = request.charge_date
        query['GameId'] = request.game_id
        query['OrderTotalCount'] = request.order_total_count
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseReadyFlag',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_internal_purchase_ready_flag_with_options_async(
        self,
        request: cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BatchInfoList'] = request.batch_info_list
        query['ChargeDate'] = request.charge_date
        query['GameId'] = request.game_id
        query['OrderTotalCount'] = request.order_total_count
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseReadyFlag',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse(),
            await self.call_api_async(params, req, runtime)
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

    def upload_game_version_by_download_with_options(
        self,
        request: cloud_game_api20200728_models.UploadGameVersionByDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.UploadGameVersionByDownloadResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DownloadType'] = request.download_type
        query['FileType'] = request.file_type
        query['GameId'] = request.game_id
        query['GameVersion'] = request.game_version
        query['Hash'] = request.hash
        query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadGameVersionByDownload',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.UploadGameVersionByDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_game_version_by_download_with_options_async(
        self,
        request: cloud_game_api20200728_models.UploadGameVersionByDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_game_api20200728_models.UploadGameVersionByDownloadResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DownloadType'] = request.download_type
        query['FileType'] = request.file_type
        query['GameId'] = request.game_id
        query['GameVersion'] = request.game_version
        query['Hash'] = request.hash
        query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadGameVersionByDownload',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.UploadGameVersionByDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_game_version_by_download(
        self,
        request: cloud_game_api20200728_models.UploadGameVersionByDownloadRequest,
    ) -> cloud_game_api20200728_models.UploadGameVersionByDownloadResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_game_version_by_download_with_options(request, runtime)

    async def upload_game_version_by_download_async(
        self,
        request: cloud_game_api20200728_models.UploadGameVersionByDownloadRequest,
    ) -> cloud_game_api20200728_models.UploadGameVersionByDownloadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_game_version_by_download_with_options_async(request, runtime)
