# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_domain20180208 import models as domain_20180208_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_demand_with_options(
        self,
        request: domain_20180208_models.AcceptDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.AcceptDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.AcceptDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_demand_with_options_async(
        self,
        request: domain_20180208_models.AcceptDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.AcceptDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.AcceptDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_demand(
        self,
        request: domain_20180208_models.AcceptDemandRequest,
    ) -> domain_20180208_models.AcceptDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_demand_with_options(request, runtime)

    async def accept_demand_async(
        self,
        request: domain_20180208_models.AcceptDemandRequest,
    ) -> domain_20180208_models.AcceptDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_demand_with_options_async(request, runtime)

    def bid_domain_with_options(
        self,
        request: domain_20180208_models.BidDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.BidDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.max_bid):
            body['MaxBid'] = request.max_bid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BidDomain',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.BidDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def bid_domain_with_options_async(
        self,
        request: domain_20180208_models.BidDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.BidDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.max_bid):
            body['MaxBid'] = request.max_bid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BidDomain',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.BidDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bid_domain(
        self,
        request: domain_20180208_models.BidDomainRequest,
    ) -> domain_20180208_models.BidDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.bid_domain_with_options(request, runtime)

    async def bid_domain_async(
        self,
        request: domain_20180208_models.BidDomainRequest,
    ) -> domain_20180208_models.BidDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bid_domain_with_options_async(request, runtime)

    def change_auction_with_options(
        self,
        request: domain_20180208_models.ChangeAuctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.ChangeAuctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_list):
            body['AuctionList'] = request.auction_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeAuction',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.ChangeAuctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_auction_with_options_async(
        self,
        request: domain_20180208_models.ChangeAuctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.ChangeAuctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_list):
            body['AuctionList'] = request.auction_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeAuction',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.ChangeAuctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_auction(
        self,
        request: domain_20180208_models.ChangeAuctionRequest,
    ) -> domain_20180208_models.ChangeAuctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_auction_with_options(request, runtime)

    async def change_auction_async(
        self,
        request: domain_20180208_models.ChangeAuctionRequest,
    ) -> domain_20180208_models.ChangeAuctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_auction_with_options_async(request, runtime)

    def check_domain_status_with_options(
        self,
        request: domain_20180208_models.CheckDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.CheckDomainStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomainStatus',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.CheckDomainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_status_with_options_async(
        self,
        request: domain_20180208_models.CheckDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.CheckDomainStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomainStatus',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.CheckDomainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain_status(
        self,
        request: domain_20180208_models.CheckDomainStatusRequest,
    ) -> domain_20180208_models.CheckDomainStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_domain_status_with_options(request, runtime)

    async def check_domain_status_async(
        self,
        request: domain_20180208_models.CheckDomainStatusRequest,
    ) -> domain_20180208_models.CheckDomainStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_status_with_options_async(request, runtime)

    def check_selected_domain_status_with_options(
        self,
        request: domain_20180208_models.CheckSelectedDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.CheckSelectedDomainStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSelectedDomainStatus',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.CheckSelectedDomainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_selected_domain_status_with_options_async(
        self,
        request: domain_20180208_models.CheckSelectedDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.CheckSelectedDomainStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSelectedDomainStatus',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.CheckSelectedDomainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_selected_domain_status(
        self,
        request: domain_20180208_models.CheckSelectedDomainStatusRequest,
    ) -> domain_20180208_models.CheckSelectedDomainStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_selected_domain_status_with_options(request, runtime)

    async def check_selected_domain_status_async(
        self,
        request: domain_20180208_models.CheckSelectedDomainStatusRequest,
    ) -> domain_20180208_models.CheckSelectedDomainStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_selected_domain_status_with_options_async(request, runtime)

    def create_fixed_price_demand_order_with_options(
        self,
        request: domain_20180208_models.CreateFixedPriceDemandOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.CreateFixedPriceDemandOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFixedPriceDemandOrder',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.CreateFixedPriceDemandOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fixed_price_demand_order_with_options_async(
        self,
        request: domain_20180208_models.CreateFixedPriceDemandOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.CreateFixedPriceDemandOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFixedPriceDemandOrder',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.CreateFixedPriceDemandOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fixed_price_demand_order(
        self,
        request: domain_20180208_models.CreateFixedPriceDemandOrderRequest,
    ) -> domain_20180208_models.CreateFixedPriceDemandOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fixed_price_demand_order_with_options(request, runtime)

    async def create_fixed_price_demand_order_async(
        self,
        request: domain_20180208_models.CreateFixedPriceDemandOrderRequest,
    ) -> domain_20180208_models.CreateFixedPriceDemandOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fixed_price_demand_order_with_options_async(request, runtime)

    def create_fixed_price_selected_order_with_options(
        self,
        request: domain_20180208_models.CreateFixedPriceSelectedOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.CreateFixedPriceSelectedOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.expected_price):
            query['ExpectedPrice'] = request.expected_price
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFixedPriceSelectedOrder',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.CreateFixedPriceSelectedOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fixed_price_selected_order_with_options_async(
        self,
        request: domain_20180208_models.CreateFixedPriceSelectedOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.CreateFixedPriceSelectedOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.expected_price):
            query['ExpectedPrice'] = request.expected_price
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFixedPriceSelectedOrder',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.CreateFixedPriceSelectedOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fixed_price_selected_order(
        self,
        request: domain_20180208_models.CreateFixedPriceSelectedOrderRequest,
    ) -> domain_20180208_models.CreateFixedPriceSelectedOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fixed_price_selected_order_with_options(request, runtime)

    async def create_fixed_price_selected_order_async(
        self,
        request: domain_20180208_models.CreateFixedPriceSelectedOrderRequest,
    ) -> domain_20180208_models.CreateFixedPriceSelectedOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fixed_price_selected_order_with_options_async(request, runtime)

    def fail_demand_with_options(
        self,
        request: domain_20180208_models.FailDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.FailDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.FailDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def fail_demand_with_options_async(
        self,
        request: domain_20180208_models.FailDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.FailDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.FailDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fail_demand(
        self,
        request: domain_20180208_models.FailDemandRequest,
    ) -> domain_20180208_models.FailDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.fail_demand_with_options(request, runtime)

    async def fail_demand_async(
        self,
        request: domain_20180208_models.FailDemandRequest,
    ) -> domain_20180208_models.FailDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fail_demand_with_options_async(request, runtime)

    def finish_demand_with_options(
        self,
        request: domain_20180208_models.FinishDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.FinishDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FinishDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.FinishDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_demand_with_options_async(
        self,
        request: domain_20180208_models.FinishDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.FinishDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FinishDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.FinishDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_demand(
        self,
        request: domain_20180208_models.FinishDemandRequest,
    ) -> domain_20180208_models.FinishDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.finish_demand_with_options(request, runtime)

    async def finish_demand_async(
        self,
        request: domain_20180208_models.FinishDemandRequest,
    ) -> domain_20180208_models.FinishDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.finish_demand_with_options_async(request, runtime)

    def get_intl_domain_download_url_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.GetIntlDomainDownloadUrlResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetIntlDomainDownloadUrl',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.GetIntlDomainDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intl_domain_download_url_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.GetIntlDomainDownloadUrlResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetIntlDomainDownloadUrl',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.GetIntlDomainDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intl_domain_download_url(self) -> domain_20180208_models.GetIntlDomainDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_intl_domain_download_url_with_options(runtime)

    async def get_intl_domain_download_url_async(self) -> domain_20180208_models.GetIntlDomainDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_intl_domain_download_url_with_options_async(runtime)

    def get_reserve_domain_url_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.GetReserveDomainUrlResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetReserveDomainUrl',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.GetReserveDomainUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reserve_domain_url_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.GetReserveDomainUrlResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetReserveDomainUrl',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.GetReserveDomainUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reserve_domain_url(self) -> domain_20180208_models.GetReserveDomainUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_reserve_domain_url_with_options(runtime)

    async def get_reserve_domain_url_async(self) -> domain_20180208_models.GetReserveDomainUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_reserve_domain_url_with_options_async(runtime)

    def purchase_intl_domain_with_options(
        self,
        request: domain_20180208_models.PurchaseIntlDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.PurchaseIntlDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.price):
            body['Price'] = request.price
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PurchaseIntlDomain',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.PurchaseIntlDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def purchase_intl_domain_with_options_async(
        self,
        request: domain_20180208_models.PurchaseIntlDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.PurchaseIntlDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.price):
            body['Price'] = request.price
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PurchaseIntlDomain',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.PurchaseIntlDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purchase_intl_domain(
        self,
        request: domain_20180208_models.PurchaseIntlDomainRequest,
    ) -> domain_20180208_models.PurchaseIntlDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_intl_domain_with_options(request, runtime)

    async def purchase_intl_domain_async(
        self,
        request: domain_20180208_models.PurchaseIntlDomainRequest,
    ) -> domain_20180208_models.PurchaseIntlDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_intl_domain_with_options_async(request, runtime)

    def query_auction_detail_with_options(
        self,
        request: domain_20180208_models.QueryAuctionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryAuctionDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_id):
            body['AuctionId'] = request.auction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAuctionDetail',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryAuctionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_auction_detail_with_options_async(
        self,
        request: domain_20180208_models.QueryAuctionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryAuctionDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_id):
            body['AuctionId'] = request.auction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAuctionDetail',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryAuctionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_auction_detail(
        self,
        request: domain_20180208_models.QueryAuctionDetailRequest,
    ) -> domain_20180208_models.QueryAuctionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_auction_detail_with_options(request, runtime)

    async def query_auction_detail_async(
        self,
        request: domain_20180208_models.QueryAuctionDetailRequest,
    ) -> domain_20180208_models.QueryAuctionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_auction_detail_with_options_async(request, runtime)

    def query_auctions_with_options(
        self,
        request: domain_20180208_models.QueryAuctionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryAuctionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAuctions',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryAuctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_auctions_with_options_async(
        self,
        request: domain_20180208_models.QueryAuctionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryAuctionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAuctions',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryAuctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_auctions(
        self,
        request: domain_20180208_models.QueryAuctionsRequest,
    ) -> domain_20180208_models.QueryAuctionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_auctions_with_options(request, runtime)

    async def query_auctions_async(
        self,
        request: domain_20180208_models.QueryAuctionsRequest,
    ) -> domain_20180208_models.QueryAuctionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_auctions_with_options_async(request, runtime)

    def query_bid_records_with_options(
        self,
        request: domain_20180208_models.QueryBidRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryBidRecordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBidRecords',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryBidRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bid_records_with_options_async(
        self,
        request: domain_20180208_models.QueryBidRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryBidRecordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auction_id):
            body['AuctionId'] = request.auction_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBidRecords',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryBidRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bid_records(
        self,
        request: domain_20180208_models.QueryBidRecordsRequest,
    ) -> domain_20180208_models.QueryBidRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_bid_records_with_options(request, runtime)

    async def query_bid_records_async(
        self,
        request: domain_20180208_models.QueryBidRecordsRequest,
    ) -> domain_20180208_models.QueryBidRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_bid_records_with_options_async(request, runtime)

    def query_booking_domain_info_with_options(
        self,
        request: domain_20180208_models.QueryBookingDomainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryBookingDomainInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBookingDomainInfo',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryBookingDomainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_booking_domain_info_with_options_async(
        self,
        request: domain_20180208_models.QueryBookingDomainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryBookingDomainInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBookingDomainInfo',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryBookingDomainInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_booking_domain_info(
        self,
        request: domain_20180208_models.QueryBookingDomainInfoRequest,
    ) -> domain_20180208_models.QueryBookingDomainInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_booking_domain_info_with_options(request, runtime)

    async def query_booking_domain_info_async(
        self,
        request: domain_20180208_models.QueryBookingDomainInfoRequest,
    ) -> domain_20180208_models.QueryBookingDomainInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_booking_domain_info_with_options_async(request, runtime)

    def query_broker_demand_with_options(
        self,
        request: domain_20180208_models.QueryBrokerDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryBrokerDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBrokerDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryBrokerDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_broker_demand_with_options_async(
        self,
        request: domain_20180208_models.QueryBrokerDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryBrokerDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBrokerDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryBrokerDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_broker_demand(
        self,
        request: domain_20180208_models.QueryBrokerDemandRequest,
    ) -> domain_20180208_models.QueryBrokerDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_broker_demand_with_options(request, runtime)

    async def query_broker_demand_async(
        self,
        request: domain_20180208_models.QueryBrokerDemandRequest,
    ) -> domain_20180208_models.QueryBrokerDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_broker_demand_with_options_async(request, runtime)

    def query_broker_demand_record_with_options(
        self,
        request: domain_20180208_models.QueryBrokerDemandRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryBrokerDemandRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBrokerDemandRecord',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryBrokerDemandRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_broker_demand_record_with_options_async(
        self,
        request: domain_20180208_models.QueryBrokerDemandRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryBrokerDemandRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBrokerDemandRecord',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryBrokerDemandRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_broker_demand_record(
        self,
        request: domain_20180208_models.QueryBrokerDemandRecordRequest,
    ) -> domain_20180208_models.QueryBrokerDemandRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_broker_demand_record_with_options(request, runtime)

    async def query_broker_demand_record_async(
        self,
        request: domain_20180208_models.QueryBrokerDemandRecordRequest,
    ) -> domain_20180208_models.QueryBrokerDemandRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_broker_demand_record_with_options_async(request, runtime)

    def query_domain_transfer_status_with_options(
        self,
        request: domain_20180208_models.QueryDomainTransferStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryDomainTransferStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDomainTransferStatus',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryDomainTransferStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_transfer_status_with_options_async(
        self,
        request: domain_20180208_models.QueryDomainTransferStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryDomainTransferStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDomainTransferStatus',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryDomainTransferStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_transfer_status(
        self,
        request: domain_20180208_models.QueryDomainTransferStatusRequest,
    ) -> domain_20180208_models.QueryDomainTransferStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_domain_transfer_status_with_options(request, runtime)

    async def query_domain_transfer_status_async(
        self,
        request: domain_20180208_models.QueryDomainTransferStatusRequest,
    ) -> domain_20180208_models.QueryDomainTransferStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_transfer_status_with_options_async(request, runtime)

    def query_purchased_domains_with_options(
        self,
        request: domain_20180208_models.QueryPurchasedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryPurchasedDomainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_operation_time):
            body['EndOperationTime'] = request.end_operation_time
        if not UtilClient.is_unset(request.op_time_order):
            body['OpTimeOrder'] = request.op_time_order
        if not UtilClient.is_unset(request.operation_status):
            body['OperationStatus'] = request.operation_status
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.start_operation_time):
            body['StartOperationTime'] = request.start_operation_time
        if not UtilClient.is_unset(request.update_time_order):
            body['UpdateTimeOrder'] = request.update_time_order
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPurchasedDomains',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryPurchasedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_purchased_domains_with_options_async(
        self,
        request: domain_20180208_models.QueryPurchasedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.QueryPurchasedDomainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_operation_time):
            body['EndOperationTime'] = request.end_operation_time
        if not UtilClient.is_unset(request.op_time_order):
            body['OpTimeOrder'] = request.op_time_order
        if not UtilClient.is_unset(request.operation_status):
            body['OperationStatus'] = request.operation_status
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.start_operation_time):
            body['StartOperationTime'] = request.start_operation_time
        if not UtilClient.is_unset(request.update_time_order):
            body['UpdateTimeOrder'] = request.update_time_order
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPurchasedDomains',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.QueryPurchasedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_purchased_domains(
        self,
        request: domain_20180208_models.QueryPurchasedDomainsRequest,
    ) -> domain_20180208_models.QueryPurchasedDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_purchased_domains_with_options(request, runtime)

    async def query_purchased_domains_async(
        self,
        request: domain_20180208_models.QueryPurchasedDomainsRequest,
    ) -> domain_20180208_models.QueryPurchasedDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_purchased_domains_with_options_async(request, runtime)

    def record_demand_with_options(
        self,
        request: domain_20180208_models.RecordDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.RecordDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.RecordDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_demand_with_options_async(
        self,
        request: domain_20180208_models.RecordDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.RecordDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.RecordDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_demand(
        self,
        request: domain_20180208_models.RecordDemandRequest,
    ) -> domain_20180208_models.RecordDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.record_demand_with_options(request, runtime)

    async def record_demand_async(
        self,
        request: domain_20180208_models.RecordDemandRequest,
    ) -> domain_20180208_models.RecordDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.record_demand_with_options_async(request, runtime)

    def refuse_demand_with_options(
        self,
        request: domain_20180208_models.RefuseDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.RefuseDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefuseDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.RefuseDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def refuse_demand_with_options_async(
        self,
        request: domain_20180208_models.RefuseDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.RefuseDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefuseDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.RefuseDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refuse_demand(
        self,
        request: domain_20180208_models.RefuseDemandRequest,
    ) -> domain_20180208_models.RefuseDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.refuse_demand_with_options(request, runtime)

    async def refuse_demand_async(
        self,
        request: domain_20180208_models.RefuseDemandRequest,
    ) -> domain_20180208_models.RefuseDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refuse_demand_with_options_async(request, runtime)

    def request_pay_demand_with_options(
        self,
        request: domain_20180208_models.RequestPayDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.RequestPayDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.price):
            query['Price'] = request.price
        if not UtilClient.is_unset(request.produce_type):
            query['ProduceType'] = request.produce_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestPayDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.RequestPayDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_pay_demand_with_options_async(
        self,
        request: domain_20180208_models.RequestPayDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.RequestPayDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.price):
            query['Price'] = request.price
        if not UtilClient.is_unset(request.produce_type):
            query['ProduceType'] = request.produce_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestPayDemand',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.RequestPayDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_pay_demand(
        self,
        request: domain_20180208_models.RequestPayDemandRequest,
    ) -> domain_20180208_models.RequestPayDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_pay_demand_with_options(request, runtime)

    async def request_pay_demand_async(
        self,
        request: domain_20180208_models.RequestPayDemandRequest,
    ) -> domain_20180208_models.RequestPayDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_pay_demand_with_options_async(request, runtime)

    def reserve_domain_with_options(
        self,
        request: domain_20180208_models.ReserveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.ReserveDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channels):
            body['Channels'] = request.channels
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReserveDomain',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.ReserveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def reserve_domain_with_options_async(
        self,
        request: domain_20180208_models.ReserveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.ReserveDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channels):
            body['Channels'] = request.channels
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReserveDomain',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.ReserveDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reserve_domain(
        self,
        request: domain_20180208_models.ReserveDomainRequest,
    ) -> domain_20180208_models.ReserveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.reserve_domain_with_options(request, runtime)

    async def reserve_domain_async(
        self,
        request: domain_20180208_models.ReserveDomainRequest,
    ) -> domain_20180208_models.ReserveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reserve_domain_with_options_async(request, runtime)

    def reserve_intl_domain_with_options(
        self,
        request: domain_20180208_models.ReserveIntlDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.ReserveIntlDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReserveIntlDomain',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.ReserveIntlDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def reserve_intl_domain_with_options_async(
        self,
        request: domain_20180208_models.ReserveIntlDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.ReserveIntlDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReserveIntlDomain',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.ReserveIntlDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reserve_intl_domain(
        self,
        request: domain_20180208_models.ReserveIntlDomainRequest,
    ) -> domain_20180208_models.ReserveIntlDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.reserve_intl_domain_with_options(request, runtime)

    async def reserve_intl_domain_async(
        self,
        request: domain_20180208_models.ReserveIntlDomainRequest,
    ) -> domain_20180208_models.ReserveIntlDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reserve_intl_domain_with_options_async(request, runtime)

    def selected_domain_list_with_options(
        self,
        request: domain_20180208_models.SelectedDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.SelectedDomainListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.list_date):
            query['ListDate'] = request.list_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectedDomainList',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.SelectedDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def selected_domain_list_with_options_async(
        self,
        request: domain_20180208_models.SelectedDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.SelectedDomainListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.list_date):
            query['ListDate'] = request.list_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectedDomainList',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.SelectedDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def selected_domain_list(
        self,
        request: domain_20180208_models.SelectedDomainListRequest,
    ) -> domain_20180208_models.SelectedDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return self.selected_domain_list_with_options(request, runtime)

    async def selected_domain_list_async(
        self,
        request: domain_20180208_models.SelectedDomainListRequest,
    ) -> domain_20180208_models.SelectedDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.selected_domain_list_with_options_async(request, runtime)

    def submit_purchase_info_with_options(
        self,
        request: domain_20180208_models.SubmitPurchaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.SubmitPurchaseInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.purchase_currency):
            body['PurchaseCurrency'] = request.purchase_currency
        if not UtilClient.is_unset(request.purchase_price):
            body['PurchasePrice'] = request.purchase_price
        if not UtilClient.is_unset(request.purchase_proofs):
            body['PurchaseProofs'] = request.purchase_proofs
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitPurchaseInfo',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.SubmitPurchaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_purchase_info_with_options_async(
        self,
        request: domain_20180208_models.SubmitPurchaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.SubmitPurchaseInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.purchase_currency):
            body['PurchaseCurrency'] = request.purchase_currency
        if not UtilClient.is_unset(request.purchase_price):
            body['PurchasePrice'] = request.purchase_price
        if not UtilClient.is_unset(request.purchase_proofs):
            body['PurchaseProofs'] = request.purchase_proofs
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitPurchaseInfo',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.SubmitPurchaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_purchase_info(
        self,
        request: domain_20180208_models.SubmitPurchaseInfoRequest,
    ) -> domain_20180208_models.SubmitPurchaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_purchase_info_with_options(request, runtime)

    async def submit_purchase_info_async(
        self,
        request: domain_20180208_models.SubmitPurchaseInfoRequest,
    ) -> domain_20180208_models.SubmitPurchaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_purchase_info_with_options_async(request, runtime)

    def update_partner_reserve_price_with_options(
        self,
        request: domain_20180208_models.UpdatePartnerReservePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.UpdatePartnerReservePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bidding_id):
            body['BiddingId'] = request.bidding_id
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.partner_type):
            body['PartnerType'] = request.partner_type
        if not UtilClient.is_unset(request.reserve_price):
            body['ReservePrice'] = request.reserve_price
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePartnerReservePrice',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.UpdatePartnerReservePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_partner_reserve_price_with_options_async(
        self,
        request: domain_20180208_models.UpdatePartnerReservePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180208_models.UpdatePartnerReservePriceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bidding_id):
            body['BiddingId'] = request.bidding_id
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.partner_type):
            body['PartnerType'] = request.partner_type
        if not UtilClient.is_unset(request.reserve_price):
            body['ReservePrice'] = request.reserve_price
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePartnerReservePrice',
            version='2018-02-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180208_models.UpdatePartnerReservePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_partner_reserve_price(
        self,
        request: domain_20180208_models.UpdatePartnerReservePriceRequest,
    ) -> domain_20180208_models.UpdatePartnerReservePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_partner_reserve_price_with_options(request, runtime)

    async def update_partner_reserve_price_async(
        self,
        request: domain_20180208_models.UpdatePartnerReservePriceRequest,
    ) -> domain_20180208_models.UpdatePartnerReservePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_partner_reserve_price_with_options_async(request, runtime)
