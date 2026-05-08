# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_marketing_event20210101 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('marketing_event', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_sum_record_flow_pop_with_options(
        self,
        request: main_models.AddSumRecordFlowPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSumRecordFlowPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.conference_name):
            query['ConferenceName'] = request.conference_name
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.entry_name):
            query['EntryName'] = request.entry_name
        if not DaraCore.is_null(request.idcard):
            query['Idcard'] = request.idcard
        if not DaraCore.is_null(request.sign_time):
            query['SignTime'] = request.sign_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSumRecordFlowPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSumRecordFlowPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sum_record_flow_pop_with_options_async(
        self,
        request: main_models.AddSumRecordFlowPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSumRecordFlowPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.conference_name):
            query['ConferenceName'] = request.conference_name
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.entry_name):
            query['EntryName'] = request.entry_name
        if not DaraCore.is_null(request.idcard):
            query['Idcard'] = request.idcard
        if not DaraCore.is_null(request.sign_time):
            query['SignTime'] = request.sign_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSumRecordFlowPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSumRecordFlowPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sum_record_flow_pop(
        self,
        request: main_models.AddSumRecordFlowPopRequest,
    ) -> main_models.AddSumRecordFlowPopResponse:
        runtime = RuntimeOptions()
        return self.add_sum_record_flow_pop_with_options(request, runtime)

    async def add_sum_record_flow_pop_async(
        self,
        request: main_models.AddSumRecordFlowPopRequest,
    ) -> main_models.AddSumRecordFlowPopResponse:
        runtime = RuntimeOptions()
        return await self.add_sum_record_flow_pop_with_options_async(request, runtime)

    def bind_exhibitor_rfid_pop_with_options(
        self,
        request: main_models.BindExhibitorRfidPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindExhibitorRfidPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not DaraCore.is_null(request.guest_ticket_record_id):
            query['GuestTicketRecordId'] = request.guest_ticket_record_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.rfid):
            query['Rfid'] = request.rfid
        if not DaraCore.is_null(request.ticket_code):
            query['TicketCode'] = request.ticket_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindExhibitorRfidPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindExhibitorRfidPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_exhibitor_rfid_pop_with_options_async(
        self,
        request: main_models.BindExhibitorRfidPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindExhibitorRfidPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not DaraCore.is_null(request.guest_ticket_record_id):
            query['GuestTicketRecordId'] = request.guest_ticket_record_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.rfid):
            query['Rfid'] = request.rfid
        if not DaraCore.is_null(request.ticket_code):
            query['TicketCode'] = request.ticket_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindExhibitorRfidPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindExhibitorRfidPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_exhibitor_rfid_pop(
        self,
        request: main_models.BindExhibitorRfidPopRequest,
    ) -> main_models.BindExhibitorRfidPopResponse:
        runtime = RuntimeOptions()
        return self.bind_exhibitor_rfid_pop_with_options(request, runtime)

    async def bind_exhibitor_rfid_pop_async(
        self,
        request: main_models.BindExhibitorRfidPopRequest,
    ) -> main_models.BindExhibitorRfidPopResponse:
        runtime = RuntimeOptions()
        return await self.bind_exhibitor_rfid_pop_with_options_async(request, runtime)

    def bind_guest_rfid_pop_with_options(
        self,
        request: main_models.BindGuestRfidPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindGuestRfidPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not DaraCore.is_null(request.guest_ticket_record_id):
            query['GuestTicketRecordId'] = request.guest_ticket_record_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.rfid):
            query['Rfid'] = request.rfid
        if not DaraCore.is_null(request.ticket_code):
            query['TicketCode'] = request.ticket_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindGuestRfidPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindGuestRfidPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_guest_rfid_pop_with_options_async(
        self,
        request: main_models.BindGuestRfidPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindGuestRfidPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not DaraCore.is_null(request.guest_ticket_record_id):
            query['GuestTicketRecordId'] = request.guest_ticket_record_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.rfid):
            query['Rfid'] = request.rfid
        if not DaraCore.is_null(request.ticket_code):
            query['TicketCode'] = request.ticket_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindGuestRfidPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindGuestRfidPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_guest_rfid_pop(
        self,
        request: main_models.BindGuestRfidPopRequest,
    ) -> main_models.BindGuestRfidPopResponse:
        runtime = RuntimeOptions()
        return self.bind_guest_rfid_pop_with_options(request, runtime)

    async def bind_guest_rfid_pop_async(
        self,
        request: main_models.BindGuestRfidPopRequest,
    ) -> main_models.BindGuestRfidPopResponse:
        runtime = RuntimeOptions()
        return await self.bind_guest_rfid_pop_with_options_async(request, runtime)

    def check_nfcbind_pop_with_options(
        self,
        request: main_models.CheckNFCBindPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckNFCBindPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckNFCBindPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckNFCBindPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_nfcbind_pop_with_options_async(
        self,
        request: main_models.CheckNFCBindPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckNFCBindPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckNFCBindPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckNFCBindPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_nfcbind_pop(
        self,
        request: main_models.CheckNFCBindPopRequest,
    ) -> main_models.CheckNFCBindPopResponse:
        runtime = RuntimeOptions()
        return self.check_nfcbind_pop_with_options(request, runtime)

    async def check_nfcbind_pop_async(
        self,
        request: main_models.CheckNFCBindPopRequest,
    ) -> main_models.CheckNFCBindPopResponse:
        runtime = RuntimeOptions()
        return await self.check_nfcbind_pop_with_options_async(request, runtime)

    def find_guest_credentials_record_with_options(
        self,
        request: main_models.FindGuestCredentialsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindGuestCredentialsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.date_time_string):
            query['DateTimeString'] = request.date_time_string
        if not DaraCore.is_null(request.end_date_time):
            query['EndDateTime'] = request.end_date_time
        if not DaraCore.is_null(request.start_date_time):
            query['StartDateTime'] = request.start_date_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindGuestCredentialsRecord',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindGuestCredentialsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_guest_credentials_record_with_options_async(
        self,
        request: main_models.FindGuestCredentialsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindGuestCredentialsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.date_time_string):
            query['DateTimeString'] = request.date_time_string
        if not DaraCore.is_null(request.end_date_time):
            query['EndDateTime'] = request.end_date_time
        if not DaraCore.is_null(request.start_date_time):
            query['StartDateTime'] = request.start_date_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindGuestCredentialsRecord',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindGuestCredentialsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_guest_credentials_record(
        self,
        request: main_models.FindGuestCredentialsRecordRequest,
    ) -> main_models.FindGuestCredentialsRecordResponse:
        runtime = RuntimeOptions()
        return self.find_guest_credentials_record_with_options(request, runtime)

    async def find_guest_credentials_record_async(
        self,
        request: main_models.FindGuestCredentialsRecordRequest,
    ) -> main_models.FindGuestCredentialsRecordResponse:
        runtime = RuntimeOptions()
        return await self.find_guest_credentials_record_with_options_async(request, runtime)

    def find_guest_ticket_record_with_options(
        self,
        request: main_models.FindGuestTicketRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindGuestTicketRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.date_time_string):
            query['DateTimeString'] = request.date_time_string
        if not DaraCore.is_null(request.end_date_time):
            query['EndDateTime'] = request.end_date_time
        if not DaraCore.is_null(request.start_date_time):
            query['StartDateTime'] = request.start_date_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindGuestTicketRecord',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindGuestTicketRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_guest_ticket_record_with_options_async(
        self,
        request: main_models.FindGuestTicketRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindGuestTicketRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.date_time_string):
            query['DateTimeString'] = request.date_time_string
        if not DaraCore.is_null(request.end_date_time):
            query['EndDateTime'] = request.end_date_time
        if not DaraCore.is_null(request.start_date_time):
            query['StartDateTime'] = request.start_date_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindGuestTicketRecord',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindGuestTicketRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_guest_ticket_record(
        self,
        request: main_models.FindGuestTicketRecordRequest,
    ) -> main_models.FindGuestTicketRecordResponse:
        runtime = RuntimeOptions()
        return self.find_guest_ticket_record_with_options(request, runtime)

    async def find_guest_ticket_record_async(
        self,
        request: main_models.FindGuestTicketRecordRequest,
    ) -> main_models.FindGuestTicketRecordResponse:
        runtime = RuntimeOptions()
        return await self.find_guest_ticket_record_with_options_async(request, runtime)

    def query_all_activity_info_with_options(
        self,
        request: main_models.QueryAllActivityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAllActivityInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAllActivityInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAllActivityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_all_activity_info_with_options_async(
        self,
        request: main_models.QueryAllActivityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAllActivityInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAllActivityInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAllActivityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_all_activity_info(
        self,
        request: main_models.QueryAllActivityInfoRequest,
    ) -> main_models.QueryAllActivityInfoResponse:
        runtime = RuntimeOptions()
        return self.query_all_activity_info_with_options(request, runtime)

    async def query_all_activity_info_async(
        self,
        request: main_models.QueryAllActivityInfoRequest,
    ) -> main_models.QueryAllActivityInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_all_activity_info_with_options_async(request, runtime)

    def query_order_session_list_pop_with_options(
        self,
        request: main_models.QueryOrderSessionListPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrderSessionListPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrderSessionListPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrderSessionListPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_session_list_pop_with_options_async(
        self,
        request: main_models.QueryOrderSessionListPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrderSessionListPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrderSessionListPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrderSessionListPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_session_list_pop(
        self,
        request: main_models.QueryOrderSessionListPopRequest,
    ) -> main_models.QueryOrderSessionListPopResponse:
        runtime = RuntimeOptions()
        return self.query_order_session_list_pop_with_options(request, runtime)

    async def query_order_session_list_pop_async(
        self,
        request: main_models.QueryOrderSessionListPopRequest,
    ) -> main_models.QueryOrderSessionListPopResponse:
        runtime = RuntimeOptions()
        return await self.query_order_session_list_pop_with_options_async(request, runtime)

    def query_qwen_conference_sg_ticket_pop_with_options(
        self,
        request: main_models.QueryQwenConferenceSgTicketPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryQwenConferenceSgTicketPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket_token):
            query['TicketToken'] = request.ticket_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryQwenConferenceSgTicketPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQwenConferenceSgTicketPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_qwen_conference_sg_ticket_pop_with_options_async(
        self,
        request: main_models.QueryQwenConferenceSgTicketPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryQwenConferenceSgTicketPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket_token):
            query['TicketToken'] = request.ticket_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryQwenConferenceSgTicketPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQwenConferenceSgTicketPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_qwen_conference_sg_ticket_pop(
        self,
        request: main_models.QueryQwenConferenceSgTicketPopRequest,
    ) -> main_models.QueryQwenConferenceSgTicketPopResponse:
        runtime = RuntimeOptions()
        return self.query_qwen_conference_sg_ticket_pop_with_options(request, runtime)

    async def query_qwen_conference_sg_ticket_pop_async(
        self,
        request: main_models.QueryQwenConferenceSgTicketPopRequest,
    ) -> main_models.QueryQwenConferenceSgTicketPopResponse:
        runtime = RuntimeOptions()
        return await self.query_qwen_conference_sg_ticket_pop_with_options_async(request, runtime)

    def query_qwen_conference_sg_ticket_search_pop_with_options(
        self,
        request: main_models.QueryQwenConferenceSgTicketSearchPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryQwenConferenceSgTicketSearchPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryQwenConferenceSgTicketSearchPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQwenConferenceSgTicketSearchPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_qwen_conference_sg_ticket_search_pop_with_options_async(
        self,
        request: main_models.QueryQwenConferenceSgTicketSearchPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryQwenConferenceSgTicketSearchPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryQwenConferenceSgTicketSearchPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQwenConferenceSgTicketSearchPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_qwen_conference_sg_ticket_search_pop(
        self,
        request: main_models.QueryQwenConferenceSgTicketSearchPopRequest,
    ) -> main_models.QueryQwenConferenceSgTicketSearchPopResponse:
        runtime = RuntimeOptions()
        return self.query_qwen_conference_sg_ticket_search_pop_with_options(request, runtime)

    async def query_qwen_conference_sg_ticket_search_pop_async(
        self,
        request: main_models.QueryQwenConferenceSgTicketSearchPopRequest,
    ) -> main_models.QueryQwenConferenceSgTicketSearchPopResponse:
        runtime = RuntimeOptions()
        return await self.query_qwen_conference_sg_ticket_search_pop_with_options_async(request, runtime)

    def query_session_by_activity_id_pop_with_options(
        self,
        request: main_models.QuerySessionByActivityIdPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySessionByActivityIdPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySessionByActivityIdPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySessionByActivityIdPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_session_by_activity_id_pop_with_options_async(
        self,
        request: main_models.QuerySessionByActivityIdPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySessionByActivityIdPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySessionByActivityIdPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySessionByActivityIdPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_session_by_activity_id_pop(
        self,
        request: main_models.QuerySessionByActivityIdPopRequest,
    ) -> main_models.QuerySessionByActivityIdPopResponse:
        runtime = RuntimeOptions()
        return self.query_session_by_activity_id_pop_with_options(request, runtime)

    async def query_session_by_activity_id_pop_async(
        self,
        request: main_models.QuerySessionByActivityIdPopRequest,
    ) -> main_models.QuerySessionByActivityIdPopResponse:
        runtime = RuntimeOptions()
        return await self.query_session_by_activity_id_pop_with_options_async(request, runtime)

    def query_session_list_pop_with_options(
        self,
        request: main_models.QuerySessionListPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySessionListPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySessionListPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySessionListPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_session_list_pop_with_options_async(
        self,
        request: main_models.QuerySessionListPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySessionListPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySessionListPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySessionListPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_session_list_pop(
        self,
        request: main_models.QuerySessionListPopRequest,
    ) -> main_models.QuerySessionListPopResponse:
        runtime = RuntimeOptions()
        return self.query_session_list_pop_with_options(request, runtime)

    async def query_session_list_pop_async(
        self,
        request: main_models.QuerySessionListPopRequest,
    ) -> main_models.QuerySessionListPopResponse:
        runtime = RuntimeOptions()
        return await self.query_session_list_pop_with_options_async(request, runtime)

    def query_sign_in_record_pop_with_options(
        self,
        request: main_models.QuerySignInRecordPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySignInRecordPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySignInRecordPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySignInRecordPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sign_in_record_pop_with_options_async(
        self,
        request: main_models.QuerySignInRecordPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySignInRecordPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySignInRecordPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySignInRecordPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sign_in_record_pop(
        self,
        request: main_models.QuerySignInRecordPopRequest,
    ) -> main_models.QuerySignInRecordPopResponse:
        runtime = RuntimeOptions()
        return self.query_sign_in_record_pop_with_options(request, runtime)

    async def query_sign_in_record_pop_async(
        self,
        request: main_models.QuerySignInRecordPopRequest,
    ) -> main_models.QuerySignInRecordPopResponse:
        runtime = RuntimeOptions()
        return await self.query_sign_in_record_pop_with_options_async(request, runtime)

    def query_single_activity_info_with_options(
        self,
        request: main_models.QuerySingleActivityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySingleActivityInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySingleActivityInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySingleActivityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_single_activity_info_with_options_async(
        self,
        request: main_models.QuerySingleActivityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySingleActivityInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySingleActivityInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySingleActivityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_single_activity_info(
        self,
        request: main_models.QuerySingleActivityInfoRequest,
    ) -> main_models.QuerySingleActivityInfoResponse:
        runtime = RuntimeOptions()
        return self.query_single_activity_info_with_options(request, runtime)

    async def query_single_activity_info_async(
        self,
        request: main_models.QuerySingleActivityInfoRequest,
    ) -> main_models.QuerySingleActivityInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_single_activity_info_with_options_async(request, runtime)

    def sync_sign_in_info_with_options(
        self,
        request: main_models.SyncSignInInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncSignInInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncSignInInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncSignInInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_sign_in_info_with_options_async(
        self,
        request: main_models.SyncSignInInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncSignInInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncSignInInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncSignInInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_sign_in_info(
        self,
        request: main_models.SyncSignInInfoRequest,
    ) -> main_models.SyncSignInInfoResponse:
        runtime = RuntimeOptions()
        return self.sync_sign_in_info_with_options(request, runtime)

    async def sync_sign_in_info_async(
        self,
        request: main_models.SyncSignInInfoRequest,
    ) -> main_models.SyncSignInInfoResponse:
        runtime = RuntimeOptions()
        return await self.sync_sign_in_info_with_options_async(request, runtime)

    def ticket_or_credentials_sign_in_pop_with_options(
        self,
        request: main_models.TicketOrCredentialsSignInPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TicketOrCredentialsSignInPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.conference_name):
            query['ConferenceName'] = request.conference_name
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.entry_name):
            query['EntryName'] = request.entry_name
        if not DaraCore.is_null(request.idcard):
            query['Idcard'] = request.idcard
        if not DaraCore.is_null(request.sign_time):
            query['SignTime'] = request.sign_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TicketOrCredentialsSignInPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketOrCredentialsSignInPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_or_credentials_sign_in_pop_with_options_async(
        self,
        request: main_models.TicketOrCredentialsSignInPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TicketOrCredentialsSignInPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.conference_name):
            query['ConferenceName'] = request.conference_name
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.entry_name):
            query['EntryName'] = request.entry_name
        if not DaraCore.is_null(request.idcard):
            query['Idcard'] = request.idcard
        if not DaraCore.is_null(request.sign_time):
            query['SignTime'] = request.sign_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TicketOrCredentialsSignInPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketOrCredentialsSignInPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_or_credentials_sign_in_pop(
        self,
        request: main_models.TicketOrCredentialsSignInPopRequest,
    ) -> main_models.TicketOrCredentialsSignInPopResponse:
        runtime = RuntimeOptions()
        return self.ticket_or_credentials_sign_in_pop_with_options(request, runtime)

    async def ticket_or_credentials_sign_in_pop_async(
        self,
        request: main_models.TicketOrCredentialsSignInPopRequest,
    ) -> main_models.TicketOrCredentialsSignInPopResponse:
        runtime = RuntimeOptions()
        return await self.ticket_or_credentials_sign_in_pop_with_options_async(request, runtime)

    def update_credentials_status_pop_with_options(
        self,
        request: main_models.UpdateCredentialsStatusPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialsStatusPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.proxy_recipient_name):
            query['ProxyRecipientName'] = request.proxy_recipient_name
        if not DaraCore.is_null(request.proxy_recipient_phone_number):
            query['ProxyRecipientPhoneNumber'] = request.proxy_recipient_phone_number
        if not DaraCore.is_null(request.receipt_location):
            query['ReceiptLocation'] = request.receipt_location
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredentialsStatusPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialsStatusPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_credentials_status_pop_with_options_async(
        self,
        request: main_models.UpdateCredentialsStatusPopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialsStatusPopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.proxy_recipient_name):
            query['ProxyRecipientName'] = request.proxy_recipient_name
        if not DaraCore.is_null(request.proxy_recipient_phone_number):
            query['ProxyRecipientPhoneNumber'] = request.proxy_recipient_phone_number
        if not DaraCore.is_null(request.receipt_location):
            query['ReceiptLocation'] = request.receipt_location
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredentialsStatusPop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialsStatusPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_credentials_status_pop(
        self,
        request: main_models.UpdateCredentialsStatusPopRequest,
    ) -> main_models.UpdateCredentialsStatusPopResponse:
        runtime = RuntimeOptions()
        return self.update_credentials_status_pop_with_options(request, runtime)

    async def update_credentials_status_pop_async(
        self,
        request: main_models.UpdateCredentialsStatusPopRequest,
    ) -> main_models.UpdateCredentialsStatusPopResponse:
        runtime = RuntimeOptions()
        return await self.update_credentials_status_pop_with_options_async(request, runtime)

    def update_ticket_record_byticket_code_pop_with_options(
        self,
        request: main_models.UpdateTicketRecordByticketCodePopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTicketRecordByticketCodePopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agenda_id):
            query['AgendaId'] = request.agenda_id
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.event):
            query['Event'] = request.event
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTicketRecordByticketCodePop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTicketRecordByticketCodePopResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ticket_record_byticket_code_pop_with_options_async(
        self,
        request: main_models.UpdateTicketRecordByticketCodePopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTicketRecordByticketCodePopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agenda_id):
            query['AgendaId'] = request.agenda_id
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.event):
            query['Event'] = request.event
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTicketRecordByticketCodePop',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTicketRecordByticketCodePopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ticket_record_byticket_code_pop(
        self,
        request: main_models.UpdateTicketRecordByticketCodePopRequest,
    ) -> main_models.UpdateTicketRecordByticketCodePopResponse:
        runtime = RuntimeOptions()
        return self.update_ticket_record_byticket_code_pop_with_options(request, runtime)

    async def update_ticket_record_byticket_code_pop_async(
        self,
        request: main_models.UpdateTicketRecordByticketCodePopRequest,
    ) -> main_models.UpdateTicketRecordByticketCodePopResponse:
        runtime = RuntimeOptions()
        return await self.update_ticket_record_byticket_code_pop_with_options_async(request, runtime)
