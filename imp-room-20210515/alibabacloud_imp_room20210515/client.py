# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imp_room20210515 import models as imp_room_20210515_models
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
        self._endpoint = self.get_endpoint('imp-room', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_login_token_with_options(
        self,
        tmp_req: imp_room_20210515_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_room_20210515_models.GetLoginTokenResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_room_20210515_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_room_20210515_models.GetLoginTokenResponse(),
            self.do_rpcrequest('GetLoginToken', '2021-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_login_token_with_options_async(
        self,
        tmp_req: imp_room_20210515_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_room_20210515_models.GetLoginTokenResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_room_20210515_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_room_20210515_models.GetLoginTokenResponse(),
            await self.do_rpcrequest_async('GetLoginToken', '2021-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_token(
        self,
        request: imp_room_20210515_models.GetLoginTokenRequest,
    ) -> imp_room_20210515_models.GetLoginTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_token_with_options(request, runtime)

    async def get_login_token_async(
        self,
        request: imp_room_20210515_models.GetLoginTokenRequest,
    ) -> imp_room_20210515_models.GetLoginTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_token_with_options_async(request, runtime)

    def create_room_with_options(
        self,
        request: imp_room_20210515_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_room_20210515_models.CreateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_room_20210515_models.CreateRoomResponse(),
            self.do_rpcrequest('CreateRoom', '2021-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_room_with_options_async(
        self,
        request: imp_room_20210515_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_room_20210515_models.CreateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_room_20210515_models.CreateRoomResponse(),
            await self.do_rpcrequest_async('CreateRoom', '2021-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_room(
        self,
        request: imp_room_20210515_models.CreateRoomRequest,
    ) -> imp_room_20210515_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    async def create_room_async(
        self,
        request: imp_room_20210515_models.CreateRoomRequest,
    ) -> imp_room_20210515_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_room_with_options_async(request, runtime)
