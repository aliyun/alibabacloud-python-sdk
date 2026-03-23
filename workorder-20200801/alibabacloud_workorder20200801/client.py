# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_workorder20200801 import models as main_models
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

    def create_ticket_with_options(
        self,
        request: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.common_question_id):
            query['CommonQuestionId'] = request.common_question_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.file_name_list):
            query['FileNameList'] = request.file_name_list
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
            version = '2020-08-01',
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
        if not DaraCore.is_null(request.common_question_id):
            query['CommonQuestionId'] = request.common_question_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.file_name_list):
            query['FileNameList'] = request.file_name_list
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
            version = '2020-08-01',
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

    def get_attachment_upload_url_with_options(
        self,
        request: main_models.GetAttachmentUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAttachmentUploadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAttachmentUploadUrl',
            version = '2020-08-01',
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
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAttachmentUploadUrl',
            version = '2020-08-01',
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

    def get_attachment_url_with_options(
        self,
        request: main_models.GetAttachmentUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAttachmentUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_name):
            query['AttachName'] = request.attach_name
        if not DaraCore.is_null(request.note_id):
            query['NoteId'] = request.note_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAttachmentUrl',
            version = '2020-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAttachmentUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_attachment_url_with_options_async(
        self,
        request: main_models.GetAttachmentUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAttachmentUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_name):
            query['AttachName'] = request.attach_name
        if not DaraCore.is_null(request.note_id):
            query['NoteId'] = request.note_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAttachmentUrl',
            version = '2020-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAttachmentUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_attachment_url(
        self,
        request: main_models.GetAttachmentUrlRequest,
    ) -> main_models.GetAttachmentUrlResponse:
        runtime = RuntimeOptions()
        return self.get_attachment_url_with_options(request, runtime)

    async def get_attachment_url_async(
        self,
        request: main_models.GetAttachmentUrlRequest,
    ) -> main_models.GetAttachmentUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_attachment_url_with_options_async(request, runtime)

    def get_ticket_with_options(
        self,
        request: main_models.GetTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicket',
            version = '2020-08-01',
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
        query = {}
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicket',
            version = '2020-08-01',
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
        if not DaraCore.is_null(request.extra_condition_list):
            query['ExtraConditionList'] = request.extra_condition_list
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_start):
            query['PageStart'] = request.page_start
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.ticket_status):
            query['TicketStatus'] = request.ticket_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = '2020-08-01',
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
        if not DaraCore.is_null(request.extra_condition_list):
            query['ExtraConditionList'] = request.extra_condition_list
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_start):
            query['PageStart'] = request.page_start
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.ticket_status):
            query['TicketStatus'] = request.ticket_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = '2020-08-01',
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
