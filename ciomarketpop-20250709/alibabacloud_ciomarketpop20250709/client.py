# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ciomarketpop20250709 import models as cio_market_pop_20250709_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('ciomarketpop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_every_one_sells_form_list_with_options(
        self,
        request: cio_market_pop_20250709_models.GetEveryOneSellsFormListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cio_market_pop_20250709_models.GetEveryOneSellsFormListResponse:
        """
        @summary 全员营销
        
        @param request: GetEveryOneSellsFormListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEveryOneSellsFormListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEveryOneSellsFormList',
            version='2025-07-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='array'
        )
        return TeaCore.from_map(
            cio_market_pop_20250709_models.GetEveryOneSellsFormListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_every_one_sells_form_list_with_options_async(
        self,
        request: cio_market_pop_20250709_models.GetEveryOneSellsFormListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cio_market_pop_20250709_models.GetEveryOneSellsFormListResponse:
        """
        @summary 全员营销
        
        @param request: GetEveryOneSellsFormListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEveryOneSellsFormListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEveryOneSellsFormList',
            version='2025-07-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='array'
        )
        return TeaCore.from_map(
            cio_market_pop_20250709_models.GetEveryOneSellsFormListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_every_one_sells_form_list(
        self,
        request: cio_market_pop_20250709_models.GetEveryOneSellsFormListRequest,
    ) -> cio_market_pop_20250709_models.GetEveryOneSellsFormListResponse:
        """
        @summary 全员营销
        
        @param request: GetEveryOneSellsFormListRequest
        @return: GetEveryOneSellsFormListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_every_one_sells_form_list_with_options(request, runtime)

    async def get_every_one_sells_form_list_async(
        self,
        request: cio_market_pop_20250709_models.GetEveryOneSellsFormListRequest,
    ) -> cio_market_pop_20250709_models.GetEveryOneSellsFormListResponse:
        """
        @summary 全员营销
        
        @param request: GetEveryOneSellsFormListRequest
        @return: GetEveryOneSellsFormListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_every_one_sells_form_list_with_options_async(request, runtime)

    def push_every_one_sell_msg_with_options(
        self,
        tmp_req: cio_market_pop_20250709_models.PushEveryOneSellMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cio_market_pop_20250709_models.PushEveryOneSellMsgResponse:
        """
        @summary 推送钉钉消息
        
        @param tmp_req: PushEveryOneSellMsgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushEveryOneSellMsgResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cio_market_pop_20250709_models.PushEveryOneSellMsgShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ding_id_list):
            request.ding_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ding_id_list, 'DingIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.ding_id_list_shrink):
            body['DingIdList'] = request.ding_id_list_shrink
        if not UtilClient.is_unset(request.push_msg):
            body['PushMsg'] = request.push_msg
        if not UtilClient.is_unset(request.push_type):
            body['PushType'] = request.push_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushEveryOneSellMsg',
            version='2025-07-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='string'
        )
        return TeaCore.from_map(
            cio_market_pop_20250709_models.PushEveryOneSellMsgResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_every_one_sell_msg_with_options_async(
        self,
        tmp_req: cio_market_pop_20250709_models.PushEveryOneSellMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cio_market_pop_20250709_models.PushEveryOneSellMsgResponse:
        """
        @summary 推送钉钉消息
        
        @param tmp_req: PushEveryOneSellMsgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushEveryOneSellMsgResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cio_market_pop_20250709_models.PushEveryOneSellMsgShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ding_id_list):
            request.ding_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ding_id_list, 'DingIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.ding_id_list_shrink):
            body['DingIdList'] = request.ding_id_list_shrink
        if not UtilClient.is_unset(request.push_msg):
            body['PushMsg'] = request.push_msg
        if not UtilClient.is_unset(request.push_type):
            body['PushType'] = request.push_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushEveryOneSellMsg',
            version='2025-07-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='string'
        )
        return TeaCore.from_map(
            cio_market_pop_20250709_models.PushEveryOneSellMsgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_every_one_sell_msg(
        self,
        request: cio_market_pop_20250709_models.PushEveryOneSellMsgRequest,
    ) -> cio_market_pop_20250709_models.PushEveryOneSellMsgResponse:
        """
        @summary 推送钉钉消息
        
        @param request: PushEveryOneSellMsgRequest
        @return: PushEveryOneSellMsgResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_every_one_sell_msg_with_options(request, runtime)

    async def push_every_one_sell_msg_async(
        self,
        request: cio_market_pop_20250709_models.PushEveryOneSellMsgRequest,
    ) -> cio_market_pop_20250709_models.PushEveryOneSellMsgResponse:
        """
        @summary 推送钉钉消息
        
        @param request: PushEveryOneSellMsgRequest
        @return: PushEveryOneSellMsgResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_every_one_sell_msg_with_options_async(request, runtime)
