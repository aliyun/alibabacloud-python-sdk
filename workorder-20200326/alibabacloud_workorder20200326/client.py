# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_workorder20200326 import models as workorder_20200326_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-northeast-1': 'workorder.ap-northeast-1.aliyuncs.com',
            'ap-southeast-1': 'workorder.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('workorder', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def close_ticket_with_options(
        self,
        request: workorder_20200326_models.CloseTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.CloseTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.CloseTicketResponse().from_map(
            self.do_rpcrequest('CloseTicket', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_ticket_with_options_async(
        self,
        request: workorder_20200326_models.CloseTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.CloseTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.CloseTicketResponse().from_map(
            await self.do_rpcrequest_async('CloseTicket', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_ticket(
        self,
        request: workorder_20200326_models.CloseTicketRequest,
    ) -> workorder_20200326_models.CloseTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_ticket_with_options(request, runtime)

    async def close_ticket_async(
        self,
        request: workorder_20200326_models.CloseTicketRequest,
    ) -> workorder_20200326_models.CloseTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_ticket_with_options_async(request, runtime)

    def create_ticket_with_options(
        self,
        request: workorder_20200326_models.CreateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.CreateTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.CreateTicketResponse().from_map(
            self.do_rpcrequest('CreateTicket', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: workorder_20200326_models.CreateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.CreateTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.CreateTicketResponse().from_map(
            await self.do_rpcrequest_async('CreateTicket', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ticket(
        self,
        request: workorder_20200326_models.CreateTicketRequest,
    ) -> workorder_20200326_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    async def create_ticket_async(
        self,
        request: workorder_20200326_models.CreateTicketRequest,
    ) -> workorder_20200326_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ticket_with_options_async(request, runtime)

    def list_categories_with_options(
        self,
        request: workorder_20200326_models.ListCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ListCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ListCategoriesResponse().from_map(
            self.do_rpcrequest('ListCategories', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_categories_with_options_async(
        self,
        request: workorder_20200326_models.ListCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ListCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ListCategoriesResponse().from_map(
            await self.do_rpcrequest_async('ListCategories', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_categories(
        self,
        request: workorder_20200326_models.ListCategoriesRequest,
    ) -> workorder_20200326_models.ListCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_categories_with_options(request, runtime)

    async def list_categories_async(
        self,
        request: workorder_20200326_models.ListCategoriesRequest,
    ) -> workorder_20200326_models.ListCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_categories_with_options_async(request, runtime)

    def list_products_with_options(
        self,
        request: workorder_20200326_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ListProductsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ListProductsResponse().from_map(
            self.do_rpcrequest('ListProducts', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: workorder_20200326_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ListProductsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ListProductsResponse().from_map(
            await self.do_rpcrequest_async('ListProducts', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_products(
        self,
        request: workorder_20200326_models.ListProductsRequest,
    ) -> workorder_20200326_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: workorder_20200326_models.ListProductsRequest,
    ) -> workorder_20200326_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def list_ticket_notes_with_options(
        self,
        request: workorder_20200326_models.ListTicketNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ListTicketNotesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ListTicketNotesResponse().from_map(
            self.do_rpcrequest('ListTicketNotes', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ticket_notes_with_options_async(
        self,
        request: workorder_20200326_models.ListTicketNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ListTicketNotesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ListTicketNotesResponse().from_map(
            await self.do_rpcrequest_async('ListTicketNotes', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ticket_notes(
        self,
        request: workorder_20200326_models.ListTicketNotesRequest,
    ) -> workorder_20200326_models.ListTicketNotesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ticket_notes_with_options(request, runtime)

    async def list_ticket_notes_async(
        self,
        request: workorder_20200326_models.ListTicketNotesRequest,
    ) -> workorder_20200326_models.ListTicketNotesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ticket_notes_with_options_async(request, runtime)

    def list_tickets_with_options(
        self,
        request: workorder_20200326_models.ListTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ListTicketsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ListTicketsResponse().from_map(
            self.do_rpcrequest('ListTickets', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tickets_with_options_async(
        self,
        request: workorder_20200326_models.ListTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ListTicketsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ListTicketsResponse().from_map(
            await self.do_rpcrequest_async('ListTickets', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tickets(
        self,
        request: workorder_20200326_models.ListTicketsRequest,
    ) -> workorder_20200326_models.ListTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tickets_with_options(request, runtime)

    async def list_tickets_async(
        self,
        request: workorder_20200326_models.ListTicketsRequest,
    ) -> workorder_20200326_models.ListTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tickets_with_options_async(request, runtime)

    def reply_ticket_with_options(
        self,
        request: workorder_20200326_models.ReplyTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ReplyTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ReplyTicketResponse().from_map(
            self.do_rpcrequest('ReplyTicket', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reply_ticket_with_options_async(
        self,
        request: workorder_20200326_models.ReplyTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> workorder_20200326_models.ReplyTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return workorder_20200326_models.ReplyTicketResponse().from_map(
            await self.do_rpcrequest_async('ReplyTicket', '2020-03-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reply_ticket(
        self,
        request: workorder_20200326_models.ReplyTicketRequest,
    ) -> workorder_20200326_models.ReplyTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.reply_ticket_with_options(request, runtime)

    async def reply_ticket_async(
        self,
        request: workorder_20200326_models.ReplyTicketRequest,
    ) -> workorder_20200326_models.ReplyTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reply_ticket_with_options_async(request, runtime)
