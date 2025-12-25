# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_workorder20210610 import models as main_models
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
        body = {}
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseTicket',
            version = '2021-06-10',
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
        body = {}
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseTicket',
            version = '2021-06-10',
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
        tmp_req: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        tmp_req.validate()
        request = main_models.CreateTicketShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_name_list):
            request.file_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_name_list, 'FileNameList', 'simple')
        if not DaraCore.is_null(tmp_req.secret_info):
            request.secret_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.secret_info, 'SecretInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.secret_info_shrink):
            query['SecretInfo'] = request.secret_info_shrink
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.file_name_list_shrink):
            body['FileNameList'] = request.file_name_list_shrink
        if not DaraCore.is_null(request.severity):
            body['Severity'] = request.severity
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2021-06-10',
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
        tmp_req: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        tmp_req.validate()
        request = main_models.CreateTicketShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_name_list):
            request.file_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_name_list, 'FileNameList', 'simple')
        if not DaraCore.is_null(tmp_req.secret_info):
            request.secret_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.secret_info, 'SecretInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.secret_info_shrink):
            query['SecretInfo'] = request.secret_info_shrink
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.file_name_list_shrink):
            body['FileNameList'] = request.file_name_list_shrink
        if not DaraCore.is_null(request.severity):
            body['Severity'] = request.severity
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2021-06-10',
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

    def evaluate_ticket_with_options(
        self,
        request: main_models.EvaluateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EvaluateTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.score):
            body['Score'] = request.score
        if not DaraCore.is_null(request.solved):
            body['Solved'] = request.solved
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EvaluateTicket',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvaluateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_ticket_with_options_async(
        self,
        request: main_models.EvaluateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EvaluateTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.score):
            body['Score'] = request.score
        if not DaraCore.is_null(request.solved):
            body['Solved'] = request.solved
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EvaluateTicket',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvaluateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_ticket(
        self,
        request: main_models.EvaluateTicketRequest,
    ) -> main_models.EvaluateTicketResponse:
        runtime = RuntimeOptions()
        return self.evaluate_ticket_with_options(request, runtime)

    async def evaluate_ticket_async(
        self,
        request: main_models.EvaluateTicketRequest,
    ) -> main_models.EvaluateTicketResponse:
        runtime = RuntimeOptions()
        return await self.evaluate_ticket_with_options_async(request, runtime)

    def get_attachment_upload_url_with_options(
        self,
        request: main_models.GetAttachmentUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAttachmentUploadUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAttachmentUploadUrl',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAttachmentUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_attachment_upload_url_with_options_async(
        self,
        request: main_models.GetAttachmentUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAttachmentUploadUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAttachmentUploadUrl',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAttachmentUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_attachment_upload_url(
        self,
        request: main_models.GetAttachmentUploadUrlRequest,
    ) -> main_models.GetAttachmentUploadUrlResponse:
        runtime = RuntimeOptions()
        return self.get_attachment_upload_url_with_options(request, runtime)

    async def get_attachment_upload_url_async(
        self,
        request: main_models.GetAttachmentUploadUrlRequest,
    ) -> main_models.GetAttachmentUploadUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_attachment_upload_url_with_options_async(request, runtime)

    def get_mq_consumer_tag_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetMqConsumerTagResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetMqConsumerTag',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMqConsumerTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mq_consumer_tag_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetMqConsumerTagResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetMqConsumerTag',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMqConsumerTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mq_consumer_tag(self) -> main_models.GetMqConsumerTagResponse:
        runtime = RuntimeOptions()
        return self.get_mq_consumer_tag_with_options(runtime)

    async def get_mq_consumer_tag_async(self) -> main_models.GetMqConsumerTagResponse:
        runtime = RuntimeOptions()
        return await self.get_mq_consumer_tag_with_options_async(runtime)

    def get_ticket_with_options(
        self,
        request: main_models.GetTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTicket',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ticket_with_options_async(
        self,
        request: main_models.GetTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTicket',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ticket(
        self,
        request: main_models.GetTicketRequest,
    ) -> main_models.GetTicketResponse:
        runtime = RuntimeOptions()
        return self.get_ticket_with_options(request, runtime)

    async def get_ticket_async(
        self,
        request: main_models.GetTicketRequest,
    ) -> main_models.GetTicketResponse:
        runtime = RuntimeOptions()
        return await self.get_ticket_with_options_async(request, runtime)

    def list_categories_with_options(
        self,
        request: main_models.ListCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2021-06-10',
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
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2021-06-10',
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
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2021-06-10',
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
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2021-06-10',
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
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTicketNotes',
            version = '2021-06-10',
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
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTicketNotes',
            version = '2021-06-10',
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
        tmp_req: main_models.ListTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketsResponse:
        tmp_req.validate()
        request = main_models.ListTicketsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ticket_id_list):
            request.ticket_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ticket_id_list, 'TicketIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.status_list):
            body['StatusList'] = request.status_list
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.ticket_id_list_shrink):
            body['TicketIdList'] = request.ticket_id_list_shrink
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = '2021-06-10',
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
        tmp_req: main_models.ListTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketsResponse:
        tmp_req.validate()
        request = main_models.ListTicketsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ticket_id_list):
            request.ticket_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ticket_id_list, 'TicketIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.status_list):
            body['StatusList'] = request.status_list
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.ticket_id_list_shrink):
            body['TicketIdList'] = request.ticket_id_list_shrink
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = '2021-06-10',
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

    def reopen_ticket_with_options(
        self,
        request: main_models.ReopenTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReopenTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReopenTicket',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReopenTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def reopen_ticket_with_options_async(
        self,
        request: main_models.ReopenTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReopenTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReopenTicket',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReopenTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reopen_ticket(
        self,
        request: main_models.ReopenTicketRequest,
    ) -> main_models.ReopenTicketResponse:
        runtime = RuntimeOptions()
        return self.reopen_ticket_with_options(request, runtime)

    async def reopen_ticket_async(
        self,
        request: main_models.ReopenTicketRequest,
    ) -> main_models.ReopenTicketResponse:
        runtime = RuntimeOptions()
        return await self.reopen_ticket_with_options_async(request, runtime)

    def reply_ticket_with_options(
        self,
        tmp_req: main_models.ReplyTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplyTicketResponse:
        tmp_req.validate()
        request = main_models.ReplyTicketShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_name_list):
            request.file_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_name_list, 'FileNameList', 'simple')
        query = {}
        if not DaraCore.is_null(request.file_name_list_shrink):
            query['FileNameList'] = request.file_name_list_shrink
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.encrypt):
            body['Encrypt'] = request.encrypt
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplyTicket',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplyTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def reply_ticket_with_options_async(
        self,
        tmp_req: main_models.ReplyTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplyTicketResponse:
        tmp_req.validate()
        request = main_models.ReplyTicketShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_name_list):
            request.file_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_name_list, 'FileNameList', 'simple')
        query = {}
        if not DaraCore.is_null(request.file_name_list_shrink):
            query['FileNameList'] = request.file_name_list_shrink
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.encrypt):
            body['Encrypt'] = request.encrypt
        if not DaraCore.is_null(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.uid):
            body['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplyTicket',
            version = '2021-06-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplyTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reply_ticket(
        self,
        request: main_models.ReplyTicketRequest,
    ) -> main_models.ReplyTicketResponse:
        runtime = RuntimeOptions()
        return self.reply_ticket_with_options(request, runtime)

    async def reply_ticket_async(
        self,
        request: main_models.ReplyTicketRequest,
    ) -> main_models.ReplyTicketResponse:
        runtime = RuntimeOptions()
        return await self.reply_ticket_with_options_async(request, runtime)
