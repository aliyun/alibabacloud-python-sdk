# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_workorder20200326 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def close_ticket_with_options(
        self,
        request: main_models.CloseTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseTicket',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_ticket_with_options_async(
        self,
        request: main_models.CloseTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseTicket',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_ticket(
        self,
        request: main_models.CloseTicketRequest,
    ) -> main_models.CloseTicketResponse:
        runtime = RuntimeOptions()
        return self.close_ticket_with_options(request, runtime)

    async def close_ticket_async(
        self,
        request: main_models.CloseTicketRequest,
    ) -> main_models.CloseTicketResponse:
        runtime = RuntimeOptions()
        return await self.close_ticket_with_options_async(request, runtime)

    def create_ticket_with_options(
        self,
        request: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.notify_time_range):
            query['NotifyTimeRange'] = request.notify_time_range
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.secret_content):
            query['SecretContent'] = request.secret_content
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.notify_time_range):
            query['NotifyTimeRange'] = request.notify_time_range
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.secret_content):
            query['SecretContent'] = request.secret_content
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    async def create_ticket_async(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        return await self.create_ticket_with_options_async(request, runtime)

    def list_categories_with_options(
        self,
        request: main_models.ListCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_categories_with_options_async(
        self,
        request: main_models.ListCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_categories(
        self,
        request: main_models.ListCategoriesRequest,
    ) -> main_models.ListCategoriesResponse:
        runtime = RuntimeOptions()
        return self.list_categories_with_options(request, runtime)

    async def list_categories_async(
        self,
        request: main_models.ListCategoriesRequest,
    ) -> main_models.ListCategoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_categories_with_options_async(request, runtime)

    def list_products_with_options(
        self,
        request: main_models.ListProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: main_models.ListProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def list_ticket_notes_with_options(
        self,
        request: main_models.ListTicketNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketNotesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTicketNotes',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketNotesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ticket_notes_with_options_async(
        self,
        request: main_models.ListTicketNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketNotesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTicketNotes',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketNotesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ticket_notes(
        self,
        request: main_models.ListTicketNotesRequest,
    ) -> main_models.ListTicketNotesResponse:
        runtime = RuntimeOptions()
        return self.list_ticket_notes_with_options(request, runtime)

    async def list_ticket_notes_async(
        self,
        request: main_models.ListTicketNotesRequest,
    ) -> main_models.ListTicketNotesResponse:
        runtime = RuntimeOptions()
        return await self.list_ticket_notes_with_options_async(request, runtime)

    def list_tickets_with_options(
        self,
        request: main_models.ListTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.created_after_time):
            query['CreatedAfterTime'] = request.created_after_time
        if not DaraCore.is_null(request.created_before_time):
            query['CreatedBeforeTime'] = request.created_before_time
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_start):
            query['PageStart'] = request.page_start
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not DaraCore.is_null(request.ticket_status):
            query['TicketStatus'] = request.ticket_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tickets_with_options_async(
        self,
        request: main_models.ListTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.created_after_time):
            query['CreatedAfterTime'] = request.created_after_time
        if not DaraCore.is_null(request.created_before_time):
            query['CreatedBeforeTime'] = request.created_before_time
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_start):
            query['PageStart'] = request.page_start
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not DaraCore.is_null(request.ticket_status):
            query['TicketStatus'] = request.ticket_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = '2020-03-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tickets(
        self,
        request: main_models.ListTicketsRequest,
    ) -> main_models.ListTicketsResponse:
        runtime = RuntimeOptions()
        return self.list_tickets_with_options(request, runtime)

    async def list_tickets_async(
        self,
        request: main_models.ListTicketsRequest,
    ) -> main_models.ListTicketsResponse:
        runtime = RuntimeOptions()
        return await self.list_tickets_with_options_async(request, runtime)
