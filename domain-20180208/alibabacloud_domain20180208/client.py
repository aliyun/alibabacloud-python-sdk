# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_domain20180208 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('domain', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_demand_with_options(
        self,
        request: main_models.AcceptDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_demand_with_options_async(
        self,
        request: main_models.AcceptDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_demand(
        self,
        request: main_models.AcceptDemandRequest,
    ) -> main_models.AcceptDemandResponse:
        runtime = RuntimeOptions()
        return self.accept_demand_with_options(request, runtime)

    async def accept_demand_async(
        self,
        request: main_models.AcceptDemandRequest,
    ) -> main_models.AcceptDemandResponse:
        runtime = RuntimeOptions()
        return await self.accept_demand_with_options_async(request, runtime)

    def batch_intrude_domains_with_options(
        self,
        tmp_req: main_models.BatchIntrudeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchIntrudeDomainsResponse:
        tmp_req.validate()
        request = main_models.BatchIntrudeDomainsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domain_names):
            request.domain_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_names, 'DomainNames', 'json')
        query = {}
        if not DaraCore.is_null(request.domain_names_shrink):
            query['DomainNames'] = request.domain_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchIntrudeDomains',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchIntrudeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_intrude_domains_with_options_async(
        self,
        tmp_req: main_models.BatchIntrudeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchIntrudeDomainsResponse:
        tmp_req.validate()
        request = main_models.BatchIntrudeDomainsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domain_names):
            request.domain_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_names, 'DomainNames', 'json')
        query = {}
        if not DaraCore.is_null(request.domain_names_shrink):
            query['DomainNames'] = request.domain_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchIntrudeDomains',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchIntrudeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_intrude_domains(
        self,
        request: main_models.BatchIntrudeDomainsRequest,
    ) -> main_models.BatchIntrudeDomainsResponse:
        runtime = RuntimeOptions()
        return self.batch_intrude_domains_with_options(request, runtime)

    async def batch_intrude_domains_async(
        self,
        request: main_models.BatchIntrudeDomainsRequest,
    ) -> main_models.BatchIntrudeDomainsResponse:
        runtime = RuntimeOptions()
        return await self.batch_intrude_domains_with_options_async(request, runtime)

    def batch_query_push_status_with_options(
        self,
        tmp_req: main_models.BatchQueryPushStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryPushStatusResponse:
        tmp_req.validate()
        request = main_models.BatchQueryPushStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.out_biz_ids):
            request.out_biz_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.out_biz_ids, 'OutBizIds', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.out_biz_ids_shrink):
            query['OutBizIds'] = request.out_biz_ids_shrink
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryPushStatus',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryPushStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_push_status_with_options_async(
        self,
        tmp_req: main_models.BatchQueryPushStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryPushStatusResponse:
        tmp_req.validate()
        request = main_models.BatchQueryPushStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.out_biz_ids):
            request.out_biz_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.out_biz_ids, 'OutBizIds', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.out_biz_ids_shrink):
            query['OutBizIds'] = request.out_biz_ids_shrink
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryPushStatus',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryPushStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_push_status(
        self,
        request: main_models.BatchQueryPushStatusRequest,
    ) -> main_models.BatchQueryPushStatusResponse:
        runtime = RuntimeOptions()
        return self.batch_query_push_status_with_options(request, runtime)

    async def batch_query_push_status_async(
        self,
        request: main_models.BatchQueryPushStatusRequest,
    ) -> main_models.BatchQueryPushStatusResponse:
        runtime = RuntimeOptions()
        return await self.batch_query_push_status_with_options_async(request, runtime)

    def batch_recall_push_with_options(
        self,
        tmp_req: main_models.BatchRecallPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchRecallPushResponse:
        tmp_req.validate()
        request = main_models.BatchRecallPushShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.out_biz_ids):
            request.out_biz_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.out_biz_ids, 'OutBizIds', 'json')
        query = {}
        if not DaraCore.is_null(request.out_biz_ids_shrink):
            query['OutBizIds'] = request.out_biz_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchRecallPush',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRecallPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_recall_push_with_options_async(
        self,
        tmp_req: main_models.BatchRecallPushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchRecallPushResponse:
        tmp_req.validate()
        request = main_models.BatchRecallPushShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.out_biz_ids):
            request.out_biz_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.out_biz_ids, 'OutBizIds', 'json')
        query = {}
        if not DaraCore.is_null(request.out_biz_ids_shrink):
            query['OutBizIds'] = request.out_biz_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchRecallPush',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRecallPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_recall_push(
        self,
        request: main_models.BatchRecallPushRequest,
    ) -> main_models.BatchRecallPushResponse:
        runtime = RuntimeOptions()
        return self.batch_recall_push_with_options(request, runtime)

    async def batch_recall_push_async(
        self,
        request: main_models.BatchRecallPushRequest,
    ) -> main_models.BatchRecallPushResponse:
        runtime = RuntimeOptions()
        return await self.batch_recall_push_with_options_async(request, runtime)

    def bid_domain_with_options(
        self,
        request: main_models.BidDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BidDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.max_bid):
            body['MaxBid'] = request.max_bid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BidDomain',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BidDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def bid_domain_with_options_async(
        self,
        request: main_models.BidDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BidDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.max_bid):
            body['MaxBid'] = request.max_bid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BidDomain',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BidDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bid_domain(
        self,
        request: main_models.BidDomainRequest,
    ) -> main_models.BidDomainResponse:
        runtime = RuntimeOptions()
        return self.bid_domain_with_options(request, runtime)

    async def bid_domain_async(
        self,
        request: main_models.BidDomainRequest,
    ) -> main_models.BidDomainResponse:
        runtime = RuntimeOptions()
        return await self.bid_domain_with_options_async(request, runtime)

    def change_auction_with_options(
        self,
        request: main_models.ChangeAuctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAuctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_list):
            body['AuctionList'] = request.auction_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAuction',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAuctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_auction_with_options_async(
        self,
        request: main_models.ChangeAuctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAuctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_list):
            body['AuctionList'] = request.auction_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAuction',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAuctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_auction(
        self,
        request: main_models.ChangeAuctionRequest,
    ) -> main_models.ChangeAuctionResponse:
        runtime = RuntimeOptions()
        return self.change_auction_with_options(request, runtime)

    async def change_auction_async(
        self,
        request: main_models.ChangeAuctionRequest,
    ) -> main_models.ChangeAuctionResponse:
        runtime = RuntimeOptions()
        return await self.change_auction_with_options_async(request, runtime)

    def check_domain_status_with_options(
        self,
        request: main_models.CheckDomainStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomainStatus',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_status_with_options_async(
        self,
        request: main_models.CheckDomainStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomainStatus',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain_status(
        self,
        request: main_models.CheckDomainStatusRequest,
    ) -> main_models.CheckDomainStatusResponse:
        runtime = RuntimeOptions()
        return self.check_domain_status_with_options(request, runtime)

    async def check_domain_status_async(
        self,
        request: main_models.CheckDomainStatusRequest,
    ) -> main_models.CheckDomainStatusResponse:
        runtime = RuntimeOptions()
        return await self.check_domain_status_with_options_async(request, runtime)

    def check_push_receiver_with_options(
        self,
        request: main_models.CheckPushReceiverRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckPushReceiverResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.receiver_account):
            query['ReceiverAccount'] = request.receiver_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckPushReceiver',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckPushReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_push_receiver_with_options_async(
        self,
        request: main_models.CheckPushReceiverRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckPushReceiverResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.receiver_account):
            query['ReceiverAccount'] = request.receiver_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckPushReceiver',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckPushReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_push_receiver(
        self,
        request: main_models.CheckPushReceiverRequest,
    ) -> main_models.CheckPushReceiverResponse:
        runtime = RuntimeOptions()
        return self.check_push_receiver_with_options(request, runtime)

    async def check_push_receiver_async(
        self,
        request: main_models.CheckPushReceiverRequest,
    ) -> main_models.CheckPushReceiverResponse:
        runtime = RuntimeOptions()
        return await self.check_push_receiver_with_options_async(request, runtime)

    def check_selected_domain_status_with_options(
        self,
        request: main_models.CheckSelectedDomainStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSelectedDomainStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckSelectedDomainStatus',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSelectedDomainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_selected_domain_status_with_options_async(
        self,
        request: main_models.CheckSelectedDomainStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSelectedDomainStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckSelectedDomainStatus',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSelectedDomainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_selected_domain_status(
        self,
        request: main_models.CheckSelectedDomainStatusRequest,
    ) -> main_models.CheckSelectedDomainStatusResponse:
        runtime = RuntimeOptions()
        return self.check_selected_domain_status_with_options(request, runtime)

    async def check_selected_domain_status_async(
        self,
        request: main_models.CheckSelectedDomainStatusRequest,
    ) -> main_models.CheckSelectedDomainStatusResponse:
        runtime = RuntimeOptions()
        return await self.check_selected_domain_status_with_options_async(request, runtime)

    def create_fixed_price_demand_order_with_options(
        self,
        request: main_models.CreateFixedPriceDemandOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFixedPriceDemandOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFixedPriceDemandOrder',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFixedPriceDemandOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fixed_price_demand_order_with_options_async(
        self,
        request: main_models.CreateFixedPriceDemandOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFixedPriceDemandOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFixedPriceDemandOrder',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFixedPriceDemandOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fixed_price_demand_order(
        self,
        request: main_models.CreateFixedPriceDemandOrderRequest,
    ) -> main_models.CreateFixedPriceDemandOrderResponse:
        runtime = RuntimeOptions()
        return self.create_fixed_price_demand_order_with_options(request, runtime)

    async def create_fixed_price_demand_order_async(
        self,
        request: main_models.CreateFixedPriceDemandOrderRequest,
    ) -> main_models.CreateFixedPriceDemandOrderResponse:
        runtime = RuntimeOptions()
        return await self.create_fixed_price_demand_order_with_options_async(request, runtime)

    def create_fixed_price_selected_order_with_options(
        self,
        request: main_models.CreateFixedPriceSelectedOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFixedPriceSelectedOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.expected_price):
            query['ExpectedPrice'] = request.expected_price
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFixedPriceSelectedOrder',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFixedPriceSelectedOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fixed_price_selected_order_with_options_async(
        self,
        request: main_models.CreateFixedPriceSelectedOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFixedPriceSelectedOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.expected_price):
            query['ExpectedPrice'] = request.expected_price
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFixedPriceSelectedOrder',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFixedPriceSelectedOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fixed_price_selected_order(
        self,
        request: main_models.CreateFixedPriceSelectedOrderRequest,
    ) -> main_models.CreateFixedPriceSelectedOrderResponse:
        runtime = RuntimeOptions()
        return self.create_fixed_price_selected_order_with_options(request, runtime)

    async def create_fixed_price_selected_order_async(
        self,
        request: main_models.CreateFixedPriceSelectedOrderRequest,
    ) -> main_models.CreateFixedPriceSelectedOrderResponse:
        runtime = RuntimeOptions()
        return await self.create_fixed_price_selected_order_with_options_async(request, runtime)

    def fail_demand_with_options(
        self,
        request: main_models.FailDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FailDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FailDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FailDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def fail_demand_with_options_async(
        self,
        request: main_models.FailDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FailDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FailDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FailDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fail_demand(
        self,
        request: main_models.FailDemandRequest,
    ) -> main_models.FailDemandResponse:
        runtime = RuntimeOptions()
        return self.fail_demand_with_options(request, runtime)

    async def fail_demand_async(
        self,
        request: main_models.FailDemandRequest,
    ) -> main_models.FailDemandResponse:
        runtime = RuntimeOptions()
        return await self.fail_demand_with_options_async(request, runtime)

    def finish_demand_with_options(
        self,
        request: main_models.FinishDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FinishDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FinishDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_demand_with_options_async(
        self,
        request: main_models.FinishDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FinishDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FinishDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_demand(
        self,
        request: main_models.FinishDemandRequest,
    ) -> main_models.FinishDemandResponse:
        runtime = RuntimeOptions()
        return self.finish_demand_with_options(request, runtime)

    async def finish_demand_async(
        self,
        request: main_models.FinishDemandRequest,
    ) -> main_models.FinishDemandResponse:
        runtime = RuntimeOptions()
        return await self.finish_demand_with_options_async(request, runtime)

    def get_intl_domain_download_url_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntlDomainDownloadUrlResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetIntlDomainDownloadUrl',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntlDomainDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intl_domain_download_url_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntlDomainDownloadUrlResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetIntlDomainDownloadUrl',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntlDomainDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intl_domain_download_url(self) -> main_models.GetIntlDomainDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.get_intl_domain_download_url_with_options(runtime)

    async def get_intl_domain_download_url_async(self) -> main_models.GetIntlDomainDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_intl_domain_download_url_with_options_async(runtime)

    def get_reserve_domain_url_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetReserveDomainUrlResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetReserveDomainUrl',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReserveDomainUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reserve_domain_url_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetReserveDomainUrlResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetReserveDomainUrl',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReserveDomainUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reserve_domain_url(self) -> main_models.GetReserveDomainUrlResponse:
        runtime = RuntimeOptions()
        return self.get_reserve_domain_url_with_options(runtime)

    async def get_reserve_domain_url_async(self) -> main_models.GetReserveDomainUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_reserve_domain_url_with_options_async(runtime)

    def purchase_intl_domain_with_options(
        self,
        request: main_models.PurchaseIntlDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PurchaseIntlDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.price):
            body['Price'] = request.price
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PurchaseIntlDomain',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PurchaseIntlDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def purchase_intl_domain_with_options_async(
        self,
        request: main_models.PurchaseIntlDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PurchaseIntlDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.price):
            body['Price'] = request.price
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PurchaseIntlDomain',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PurchaseIntlDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purchase_intl_domain(
        self,
        request: main_models.PurchaseIntlDomainRequest,
    ) -> main_models.PurchaseIntlDomainResponse:
        runtime = RuntimeOptions()
        return self.purchase_intl_domain_with_options(request, runtime)

    async def purchase_intl_domain_async(
        self,
        request: main_models.PurchaseIntlDomainRequest,
    ) -> main_models.PurchaseIntlDomainResponse:
        runtime = RuntimeOptions()
        return await self.purchase_intl_domain_with_options_async(request, runtime)

    def push_domains_with_options(
        self,
        tmp_req: main_models.PushDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushDomainsResponse:
        tmp_req.validate()
        request = main_models.PushDomainsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domain_list):
            request.domain_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_list, 'DomainList', 'json')
        query = {}
        if not DaraCore.is_null(request.domain_list_shrink):
            query['DomainList'] = request.domain_list_shrink
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.publish_remark):
            query['PublishRemark'] = request.publish_remark
        if not DaraCore.is_null(request.receiver_account):
            query['ReceiverAccount'] = request.receiver_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushDomains',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_domains_with_options_async(
        self,
        tmp_req: main_models.PushDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushDomainsResponse:
        tmp_req.validate()
        request = main_models.PushDomainsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domain_list):
            request.domain_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_list, 'DomainList', 'json')
        query = {}
        if not DaraCore.is_null(request.domain_list_shrink):
            query['DomainList'] = request.domain_list_shrink
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.publish_remark):
            query['PublishRemark'] = request.publish_remark
        if not DaraCore.is_null(request.receiver_account):
            query['ReceiverAccount'] = request.receiver_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushDomains',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_domains(
        self,
        request: main_models.PushDomainsRequest,
    ) -> main_models.PushDomainsResponse:
        runtime = RuntimeOptions()
        return self.push_domains_with_options(request, runtime)

    async def push_domains_async(
        self,
        request: main_models.PushDomainsRequest,
    ) -> main_models.PushDomainsResponse:
        runtime = RuntimeOptions()
        return await self.push_domains_with_options_async(request, runtime)

    def query_auction_detail_with_options(
        self,
        request: main_models.QueryAuctionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuctionDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_id):
            body['AuctionId'] = request.auction_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuctionDetail',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuctionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_auction_detail_with_options_async(
        self,
        request: main_models.QueryAuctionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuctionDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_id):
            body['AuctionId'] = request.auction_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuctionDetail',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuctionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_auction_detail(
        self,
        request: main_models.QueryAuctionDetailRequest,
    ) -> main_models.QueryAuctionDetailResponse:
        runtime = RuntimeOptions()
        return self.query_auction_detail_with_options(request, runtime)

    async def query_auction_detail_async(
        self,
        request: main_models.QueryAuctionDetailRequest,
    ) -> main_models.QueryAuctionDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_auction_detail_with_options_async(request, runtime)

    def query_auctions_with_options(
        self,
        request: main_models.QueryAuctionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuctionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_end_time_order):
            body['AuctionEndTimeOrder'] = request.auction_end_time_order
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.statuses):
            body['Statuses'] = request.statuses
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuctions',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_auctions_with_options_async(
        self,
        request: main_models.QueryAuctionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuctionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_end_time_order):
            body['AuctionEndTimeOrder'] = request.auction_end_time_order
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.statuses):
            body['Statuses'] = request.statuses
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuctions',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_auctions(
        self,
        request: main_models.QueryAuctionsRequest,
    ) -> main_models.QueryAuctionsResponse:
        runtime = RuntimeOptions()
        return self.query_auctions_with_options(request, runtime)

    async def query_auctions_async(
        self,
        request: main_models.QueryAuctionsRequest,
    ) -> main_models.QueryAuctionsResponse:
        runtime = RuntimeOptions()
        return await self.query_auctions_with_options_async(request, runtime)

    def query_bid_records_with_options(
        self,
        request: main_models.QueryBidRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBidRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryBidRecords',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBidRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bid_records_with_options_async(
        self,
        request: main_models.QueryBidRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBidRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryBidRecords',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBidRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bid_records(
        self,
        request: main_models.QueryBidRecordsRequest,
    ) -> main_models.QueryBidRecordsResponse:
        runtime = RuntimeOptions()
        return self.query_bid_records_with_options(request, runtime)

    async def query_bid_records_async(
        self,
        request: main_models.QueryBidRecordsRequest,
    ) -> main_models.QueryBidRecordsResponse:
        runtime = RuntimeOptions()
        return await self.query_bid_records_with_options_async(request, runtime)

    def query_booking_domain_info_with_options(
        self,
        request: main_models.QueryBookingDomainInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBookingDomainInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryBookingDomainInfo',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBookingDomainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_booking_domain_info_with_options_async(
        self,
        request: main_models.QueryBookingDomainInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBookingDomainInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryBookingDomainInfo',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBookingDomainInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_booking_domain_info(
        self,
        request: main_models.QueryBookingDomainInfoRequest,
    ) -> main_models.QueryBookingDomainInfoResponse:
        runtime = RuntimeOptions()
        return self.query_booking_domain_info_with_options(request, runtime)

    async def query_booking_domain_info_async(
        self,
        request: main_models.QueryBookingDomainInfoRequest,
    ) -> main_models.QueryBookingDomainInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_booking_domain_info_with_options_async(request, runtime)

    def query_broker_demand_with_options(
        self,
        request: main_models.QueryBrokerDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBrokerDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBrokerDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBrokerDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_broker_demand_with_options_async(
        self,
        request: main_models.QueryBrokerDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBrokerDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBrokerDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBrokerDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_broker_demand(
        self,
        request: main_models.QueryBrokerDemandRequest,
    ) -> main_models.QueryBrokerDemandResponse:
        runtime = RuntimeOptions()
        return self.query_broker_demand_with_options(request, runtime)

    async def query_broker_demand_async(
        self,
        request: main_models.QueryBrokerDemandRequest,
    ) -> main_models.QueryBrokerDemandResponse:
        runtime = RuntimeOptions()
        return await self.query_broker_demand_with_options_async(request, runtime)

    def query_broker_demand_record_with_options(
        self,
        request: main_models.QueryBrokerDemandRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBrokerDemandRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBrokerDemandRecord',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBrokerDemandRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_broker_demand_record_with_options_async(
        self,
        request: main_models.QueryBrokerDemandRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBrokerDemandRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBrokerDemandRecord',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBrokerDemandRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_broker_demand_record(
        self,
        request: main_models.QueryBrokerDemandRecordRequest,
    ) -> main_models.QueryBrokerDemandRecordResponse:
        runtime = RuntimeOptions()
        return self.query_broker_demand_record_with_options(request, runtime)

    async def query_broker_demand_record_async(
        self,
        request: main_models.QueryBrokerDemandRecordRequest,
    ) -> main_models.QueryBrokerDemandRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_broker_demand_record_with_options_async(request, runtime)

    def query_buyer_domain_trade_records_with_options(
        self,
        tmp_req: main_models.QueryBuyerDomainTradeRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBuyerDomainTradeRecordsResponse:
        tmp_req.validate()
        request = main_models.QueryBuyerDomainTradeRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_id_list):
            request.biz_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_id_list, 'BizIdList', 'json')
        if not DaraCore.is_null(tmp_req.domain_name_list):
            request.domain_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        if not DaraCore.is_null(tmp_req.suffix_list):
            request.suffix_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.suffix_list, 'SuffixList', 'json')
        if not DaraCore.is_null(tmp_req.trade_type_list):
            request.trade_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.trade_type_list, 'TradeTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id_list_shrink):
            query['BizIdList'] = request.biz_id_list_shrink
        if not DaraCore.is_null(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.end_price):
            query['EndPrice'] = request.end_price
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sorter):
            query['Sorter'] = request.sorter
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.start_price):
            query['StartPrice'] = request.start_price
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.suffix_list_shrink):
            query['SuffixList'] = request.suffix_list_shrink
        if not DaraCore.is_null(request.trade_type_list_shrink):
            query['TradeTypeList'] = request.trade_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBuyerDomainTradeRecords',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBuyerDomainTradeRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_buyer_domain_trade_records_with_options_async(
        self,
        tmp_req: main_models.QueryBuyerDomainTradeRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBuyerDomainTradeRecordsResponse:
        tmp_req.validate()
        request = main_models.QueryBuyerDomainTradeRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_id_list):
            request.biz_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_id_list, 'BizIdList', 'json')
        if not DaraCore.is_null(tmp_req.domain_name_list):
            request.domain_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        if not DaraCore.is_null(tmp_req.suffix_list):
            request.suffix_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.suffix_list, 'SuffixList', 'json')
        if not DaraCore.is_null(tmp_req.trade_type_list):
            request.trade_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.trade_type_list, 'TradeTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id_list_shrink):
            query['BizIdList'] = request.biz_id_list_shrink
        if not DaraCore.is_null(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.end_price):
            query['EndPrice'] = request.end_price
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sorter):
            query['Sorter'] = request.sorter
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.start_price):
            query['StartPrice'] = request.start_price
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not DaraCore.is_null(request.suffix_list_shrink):
            query['SuffixList'] = request.suffix_list_shrink
        if not DaraCore.is_null(request.trade_type_list_shrink):
            query['TradeTypeList'] = request.trade_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBuyerDomainTradeRecords',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBuyerDomainTradeRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_buyer_domain_trade_records(
        self,
        request: main_models.QueryBuyerDomainTradeRecordsRequest,
    ) -> main_models.QueryBuyerDomainTradeRecordsResponse:
        runtime = RuntimeOptions()
        return self.query_buyer_domain_trade_records_with_options(request, runtime)

    async def query_buyer_domain_trade_records_async(
        self,
        request: main_models.QueryBuyerDomainTradeRecordsRequest,
    ) -> main_models.QueryBuyerDomainTradeRecordsResponse:
        runtime = RuntimeOptions()
        return await self.query_buyer_domain_trade_records_with_options_async(request, runtime)

    def query_domain_transfer_status_with_options(
        self,
        request: main_models.QueryDomainTransferStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainTransferStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainTransferStatus',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainTransferStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_transfer_status_with_options_async(
        self,
        request: main_models.QueryDomainTransferStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainTransferStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainTransferStatus',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainTransferStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_transfer_status(
        self,
        request: main_models.QueryDomainTransferStatusRequest,
    ) -> main_models.QueryDomainTransferStatusResponse:
        runtime = RuntimeOptions()
        return self.query_domain_transfer_status_with_options(request, runtime)

    async def query_domain_transfer_status_async(
        self,
        request: main_models.QueryDomainTransferStatusRequest,
    ) -> main_models.QueryDomainTransferStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_transfer_status_with_options_async(request, runtime)

    def query_exchange_rate_with_options(
        self,
        request: main_models.QueryExchangeRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryExchangeRateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_currency):
            query['FromCurrency'] = request.from_currency
        if not DaraCore.is_null(request.to_currency):
            query['ToCurrency'] = request.to_currency
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryExchangeRate',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryExchangeRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_exchange_rate_with_options_async(
        self,
        request: main_models.QueryExchangeRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryExchangeRateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_currency):
            query['FromCurrency'] = request.from_currency
        if not DaraCore.is_null(request.to_currency):
            query['ToCurrency'] = request.to_currency
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryExchangeRate',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryExchangeRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_exchange_rate(
        self,
        request: main_models.QueryExchangeRateRequest,
    ) -> main_models.QueryExchangeRateResponse:
        runtime = RuntimeOptions()
        return self.query_exchange_rate_with_options(request, runtime)

    async def query_exchange_rate_async(
        self,
        request: main_models.QueryExchangeRateRequest,
    ) -> main_models.QueryExchangeRateResponse:
        runtime = RuntimeOptions()
        return await self.query_exchange_rate_with_options_async(request, runtime)

    def query_export_auction_detail_with_options(
        self,
        request: main_models.QueryExportAuctionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryExportAuctionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auction_id):
            query['AuctionId'] = request.auction_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryExportAuctionDetail',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryExportAuctionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_export_auction_detail_with_options_async(
        self,
        request: main_models.QueryExportAuctionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryExportAuctionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auction_id):
            query['AuctionId'] = request.auction_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryExportAuctionDetail',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryExportAuctionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_export_auction_detail(
        self,
        request: main_models.QueryExportAuctionDetailRequest,
    ) -> main_models.QueryExportAuctionDetailResponse:
        runtime = RuntimeOptions()
        return self.query_export_auction_detail_with_options(request, runtime)

    async def query_export_auction_detail_async(
        self,
        request: main_models.QueryExportAuctionDetailRequest,
    ) -> main_models.QueryExportAuctionDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_export_auction_detail_with_options_async(request, runtime)

    def query_export_domain_expire_snatchs_with_options(
        self,
        request: main_models.QueryExportDomainExpireSnatchsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryExportDomainExpireSnatchsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_id):
            query['CurrentId'] = request.current_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryExportDomainExpireSnatchs',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryExportDomainExpireSnatchsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_export_domain_expire_snatchs_with_options_async(
        self,
        request: main_models.QueryExportDomainExpireSnatchsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryExportDomainExpireSnatchsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_id):
            query['CurrentId'] = request.current_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryExportDomainExpireSnatchs',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryExportDomainExpireSnatchsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_export_domain_expire_snatchs(
        self,
        request: main_models.QueryExportDomainExpireSnatchsRequest,
    ) -> main_models.QueryExportDomainExpireSnatchsResponse:
        runtime = RuntimeOptions()
        return self.query_export_domain_expire_snatchs_with_options(request, runtime)

    async def query_export_domain_expire_snatchs_async(
        self,
        request: main_models.QueryExportDomainExpireSnatchsRequest,
    ) -> main_models.QueryExportDomainExpireSnatchsResponse:
        runtime = RuntimeOptions()
        return await self.query_export_domain_expire_snatchs_with_options_async(request, runtime)

    def query_purchased_domains_with_options(
        self,
        request: main_models.QueryPurchasedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPurchasedDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_operation_time):
            body['EndOperationTime'] = request.end_operation_time
        if not DaraCore.is_null(request.op_time_order):
            body['OpTimeOrder'] = request.op_time_order
        if not DaraCore.is_null(request.operation_status):
            body['OperationStatus'] = request.operation_status
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.start_operation_time):
            body['StartOperationTime'] = request.start_operation_time
        if not DaraCore.is_null(request.update_time_order):
            body['UpdateTimeOrder'] = request.update_time_order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPurchasedDomains',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPurchasedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_purchased_domains_with_options_async(
        self,
        request: main_models.QueryPurchasedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPurchasedDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_operation_time):
            body['EndOperationTime'] = request.end_operation_time
        if not DaraCore.is_null(request.op_time_order):
            body['OpTimeOrder'] = request.op_time_order
        if not DaraCore.is_null(request.operation_status):
            body['OperationStatus'] = request.operation_status
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.start_operation_time):
            body['StartOperationTime'] = request.start_operation_time
        if not DaraCore.is_null(request.update_time_order):
            body['UpdateTimeOrder'] = request.update_time_order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPurchasedDomains',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPurchasedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_purchased_domains(
        self,
        request: main_models.QueryPurchasedDomainsRequest,
    ) -> main_models.QueryPurchasedDomainsResponse:
        runtime = RuntimeOptions()
        return self.query_purchased_domains_with_options(request, runtime)

    async def query_purchased_domains_async(
        self,
        request: main_models.QueryPurchasedDomainsRequest,
    ) -> main_models.QueryPurchasedDomainsResponse:
        runtime = RuntimeOptions()
        return await self.query_purchased_domains_with_options_async(request, runtime)

    def record_demand_with_options(
        self,
        request: main_models.RecordDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_demand_with_options_async(
        self,
        request: main_models.RecordDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_demand(
        self,
        request: main_models.RecordDemandRequest,
    ) -> main_models.RecordDemandResponse:
        runtime = RuntimeOptions()
        return self.record_demand_with_options(request, runtime)

    async def record_demand_async(
        self,
        request: main_models.RecordDemandRequest,
    ) -> main_models.RecordDemandResponse:
        runtime = RuntimeOptions()
        return await self.record_demand_with_options_async(request, runtime)

    def refuse_demand_with_options(
        self,
        request: main_models.RefuseDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefuseDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefuseDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefuseDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def refuse_demand_with_options_async(
        self,
        request: main_models.RefuseDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefuseDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefuseDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefuseDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refuse_demand(
        self,
        request: main_models.RefuseDemandRequest,
    ) -> main_models.RefuseDemandResponse:
        runtime = RuntimeOptions()
        return self.refuse_demand_with_options(request, runtime)

    async def refuse_demand_async(
        self,
        request: main_models.RefuseDemandRequest,
    ) -> main_models.RefuseDemandResponse:
        runtime = RuntimeOptions()
        return await self.refuse_demand_with_options_async(request, runtime)

    def request_pay_demand_with_options(
        self,
        request: main_models.RequestPayDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequestPayDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.price):
            query['Price'] = request.price
        if not DaraCore.is_null(request.produce_type):
            query['ProduceType'] = request.produce_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RequestPayDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequestPayDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_pay_demand_with_options_async(
        self,
        request: main_models.RequestPayDemandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequestPayDemandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.price):
            query['Price'] = request.price
        if not DaraCore.is_null(request.produce_type):
            query['ProduceType'] = request.produce_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RequestPayDemand',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequestPayDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_pay_demand(
        self,
        request: main_models.RequestPayDemandRequest,
    ) -> main_models.RequestPayDemandResponse:
        runtime = RuntimeOptions()
        return self.request_pay_demand_with_options(request, runtime)

    async def request_pay_demand_async(
        self,
        request: main_models.RequestPayDemandRequest,
    ) -> main_models.RequestPayDemandResponse:
        runtime = RuntimeOptions()
        return await self.request_pay_demand_with_options_async(request, runtime)

    def reserve_domain_with_options(
        self,
        request: main_models.ReserveDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReserveDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channels):
            body['Channels'] = request.channels
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReserveDomain',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReserveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def reserve_domain_with_options_async(
        self,
        request: main_models.ReserveDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReserveDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channels):
            body['Channels'] = request.channels
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReserveDomain',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReserveDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reserve_domain(
        self,
        request: main_models.ReserveDomainRequest,
    ) -> main_models.ReserveDomainResponse:
        runtime = RuntimeOptions()
        return self.reserve_domain_with_options(request, runtime)

    async def reserve_domain_async(
        self,
        request: main_models.ReserveDomainRequest,
    ) -> main_models.ReserveDomainResponse:
        runtime = RuntimeOptions()
        return await self.reserve_domain_with_options_async(request, runtime)

    def reserve_intl_domain_with_options(
        self,
        request: main_models.ReserveIntlDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReserveIntlDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReserveIntlDomain',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReserveIntlDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def reserve_intl_domain_with_options_async(
        self,
        request: main_models.ReserveIntlDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReserveIntlDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReserveIntlDomain',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReserveIntlDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reserve_intl_domain(
        self,
        request: main_models.ReserveIntlDomainRequest,
    ) -> main_models.ReserveIntlDomainResponse:
        runtime = RuntimeOptions()
        return self.reserve_intl_domain_with_options(request, runtime)

    async def reserve_intl_domain_async(
        self,
        request: main_models.ReserveIntlDomainRequest,
    ) -> main_models.ReserveIntlDomainResponse:
        runtime = RuntimeOptions()
        return await self.reserve_intl_domain_with_options_async(request, runtime)

    def selected_domain_list_with_options(
        self,
        request: main_models.SelectedDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SelectedDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.list_date):
            query['ListDate'] = request.list_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SelectedDomainList',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectedDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def selected_domain_list_with_options_async(
        self,
        request: main_models.SelectedDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SelectedDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.list_date):
            query['ListDate'] = request.list_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SelectedDomainList',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectedDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def selected_domain_list(
        self,
        request: main_models.SelectedDomainListRequest,
    ) -> main_models.SelectedDomainListResponse:
        runtime = RuntimeOptions()
        return self.selected_domain_list_with_options(request, runtime)

    async def selected_domain_list_async(
        self,
        request: main_models.SelectedDomainListRequest,
    ) -> main_models.SelectedDomainListResponse:
        runtime = RuntimeOptions()
        return await self.selected_domain_list_with_options_async(request, runtime)

    def submit_purchase_info_with_options(
        self,
        request: main_models.SubmitPurchaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitPurchaseInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.purchase_currency):
            body['PurchaseCurrency'] = request.purchase_currency
        if not DaraCore.is_null(request.purchase_price):
            body['PurchasePrice'] = request.purchase_price
        if not DaraCore.is_null(request.purchase_proofs):
            body['PurchaseProofs'] = request.purchase_proofs
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitPurchaseInfo',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitPurchaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_purchase_info_with_options_async(
        self,
        request: main_models.SubmitPurchaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitPurchaseInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.purchase_currency):
            body['PurchaseCurrency'] = request.purchase_currency
        if not DaraCore.is_null(request.purchase_price):
            body['PurchasePrice'] = request.purchase_price
        if not DaraCore.is_null(request.purchase_proofs):
            body['PurchaseProofs'] = request.purchase_proofs
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitPurchaseInfo',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitPurchaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_purchase_info(
        self,
        request: main_models.SubmitPurchaseInfoRequest,
    ) -> main_models.SubmitPurchaseInfoResponse:
        runtime = RuntimeOptions()
        return self.submit_purchase_info_with_options(request, runtime)

    async def submit_purchase_info_async(
        self,
        request: main_models.SubmitPurchaseInfoRequest,
    ) -> main_models.SubmitPurchaseInfoResponse:
        runtime = RuntimeOptions()
        return await self.submit_purchase_info_with_options_async(request, runtime)

    def update_partner_reserve_price_with_options(
        self,
        request: main_models.UpdatePartnerReservePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePartnerReservePriceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bidding_id):
            body['BiddingId'] = request.bidding_id
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.partner_type):
            body['PartnerType'] = request.partner_type
        if not DaraCore.is_null(request.reserve_price):
            body['ReservePrice'] = request.reserve_price
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePartnerReservePrice',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePartnerReservePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_partner_reserve_price_with_options_async(
        self,
        request: main_models.UpdatePartnerReservePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePartnerReservePriceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bidding_id):
            body['BiddingId'] = request.bidding_id
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.partner_type):
            body['PartnerType'] = request.partner_type
        if not DaraCore.is_null(request.reserve_price):
            body['ReservePrice'] = request.reserve_price
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePartnerReservePrice',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePartnerReservePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_partner_reserve_price(
        self,
        request: main_models.UpdatePartnerReservePriceRequest,
    ) -> main_models.UpdatePartnerReservePriceResponse:
        runtime = RuntimeOptions()
        return self.update_partner_reserve_price_with_options(request, runtime)

    async def update_partner_reserve_price_async(
        self,
        request: main_models.UpdatePartnerReservePriceRequest,
    ) -> main_models.UpdatePartnerReservePriceResponse:
        runtime = RuntimeOptions()
        return await self.update_partner_reserve_price_with_options_async(request, runtime)

    def website_add_dns_record_with_options(
        self,
        request: main_models.WebsiteAddDnsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WebsiteAddDnsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.website_no):
            query['WebsiteNo'] = request.website_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WebsiteAddDnsRecord',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WebsiteAddDnsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def website_add_dns_record_with_options_async(
        self,
        request: main_models.WebsiteAddDnsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WebsiteAddDnsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.website_no):
            query['WebsiteNo'] = request.website_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WebsiteAddDnsRecord',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WebsiteAddDnsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def website_add_dns_record(
        self,
        request: main_models.WebsiteAddDnsRecordRequest,
    ) -> main_models.WebsiteAddDnsRecordResponse:
        runtime = RuntimeOptions()
        return self.website_add_dns_record_with_options(request, runtime)

    async def website_add_dns_record_async(
        self,
        request: main_models.WebsiteAddDnsRecordRequest,
    ) -> main_models.WebsiteAddDnsRecordResponse:
        runtime = RuntimeOptions()
        return await self.website_add_dns_record_with_options_async(request, runtime)

    def website_delete_dns_record_with_options(
        self,
        request: main_models.WebsiteDeleteDnsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WebsiteDeleteDnsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.website_no):
            query['WebsiteNo'] = request.website_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WebsiteDeleteDnsRecord',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WebsiteDeleteDnsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def website_delete_dns_record_with_options_async(
        self,
        request: main_models.WebsiteDeleteDnsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WebsiteDeleteDnsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.website_no):
            query['WebsiteNo'] = request.website_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WebsiteDeleteDnsRecord',
            version = '2018-02-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WebsiteDeleteDnsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def website_delete_dns_record(
        self,
        request: main_models.WebsiteDeleteDnsRecordRequest,
    ) -> main_models.WebsiteDeleteDnsRecordResponse:
        runtime = RuntimeOptions()
        return self.website_delete_dns_record_with_options(request, runtime)

    async def website_delete_dns_record_async(
        self,
        request: main_models.WebsiteDeleteDnsRecordRequest,
    ) -> main_models.WebsiteDeleteDnsRecordResponse:
        runtime = RuntimeOptions()
        return await self.website_delete_dns_record_with_options_async(request, runtime)
