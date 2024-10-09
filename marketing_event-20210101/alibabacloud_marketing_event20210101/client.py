# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_marketing_event20210101 import models as marketing_event_20210101_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_sum_record_flow_pop_with_options(
        self,
        request: marketing_event_20210101_models.AddSumRecordFlowPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.AddSumRecordFlowPopResponse:
        """
        @param request: AddSumRecordFlowPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSumRecordFlowPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.conference_name):
            query['ConferenceName'] = request.conference_name
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.entry_name):
            query['EntryName'] = request.entry_name
        if not UtilClient.is_unset(request.idcard):
            query['Idcard'] = request.idcard
        if not UtilClient.is_unset(request.sign_time):
            query['SignTime'] = request.sign_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSumRecordFlowPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.AddSumRecordFlowPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sum_record_flow_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.AddSumRecordFlowPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.AddSumRecordFlowPopResponse:
        """
        @param request: AddSumRecordFlowPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSumRecordFlowPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.conference_name):
            query['ConferenceName'] = request.conference_name
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.entry_name):
            query['EntryName'] = request.entry_name
        if not UtilClient.is_unset(request.idcard):
            query['Idcard'] = request.idcard
        if not UtilClient.is_unset(request.sign_time):
            query['SignTime'] = request.sign_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSumRecordFlowPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.AddSumRecordFlowPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sum_record_flow_pop(
        self,
        request: marketing_event_20210101_models.AddSumRecordFlowPopRequest,
    ) -> marketing_event_20210101_models.AddSumRecordFlowPopResponse:
        """
        @param request: AddSumRecordFlowPopRequest
        @return: AddSumRecordFlowPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_sum_record_flow_pop_with_options(request, runtime)

    async def add_sum_record_flow_pop_async(
        self,
        request: marketing_event_20210101_models.AddSumRecordFlowPopRequest,
    ) -> marketing_event_20210101_models.AddSumRecordFlowPopResponse:
        """
        @param request: AddSumRecordFlowPopRequest
        @return: AddSumRecordFlowPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_sum_record_flow_pop_with_options_async(request, runtime)

    def bind_exhibitor_rfid_pop_with_options(
        self,
        request: marketing_event_20210101_models.BindExhibitorRfidPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.BindExhibitorRfidPopResponse:
        """
        @param request: BindExhibitorRfidPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindExhibitorRfidPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.guest_ticket_record_id):
            query['GuestTicketRecordId'] = request.guest_ticket_record_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.rfid):
            query['Rfid'] = request.rfid
        if not UtilClient.is_unset(request.ticket_code):
            query['TicketCode'] = request.ticket_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindExhibitorRfidPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.BindExhibitorRfidPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_exhibitor_rfid_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.BindExhibitorRfidPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.BindExhibitorRfidPopResponse:
        """
        @param request: BindExhibitorRfidPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindExhibitorRfidPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.guest_ticket_record_id):
            query['GuestTicketRecordId'] = request.guest_ticket_record_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.rfid):
            query['Rfid'] = request.rfid
        if not UtilClient.is_unset(request.ticket_code):
            query['TicketCode'] = request.ticket_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindExhibitorRfidPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.BindExhibitorRfidPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_exhibitor_rfid_pop(
        self,
        request: marketing_event_20210101_models.BindExhibitorRfidPopRequest,
    ) -> marketing_event_20210101_models.BindExhibitorRfidPopResponse:
        """
        @param request: BindExhibitorRfidPopRequest
        @return: BindExhibitorRfidPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_exhibitor_rfid_pop_with_options(request, runtime)

    async def bind_exhibitor_rfid_pop_async(
        self,
        request: marketing_event_20210101_models.BindExhibitorRfidPopRequest,
    ) -> marketing_event_20210101_models.BindExhibitorRfidPopResponse:
        """
        @param request: BindExhibitorRfidPopRequest
        @return: BindExhibitorRfidPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_exhibitor_rfid_pop_with_options_async(request, runtime)

    def bind_guest_rfid_pop_with_options(
        self,
        request: marketing_event_20210101_models.BindGuestRfidPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.BindGuestRfidPopResponse:
        """
        @param request: BindGuestRfidPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindGuestRfidPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.guest_ticket_record_id):
            query['GuestTicketRecordId'] = request.guest_ticket_record_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.rfid):
            query['Rfid'] = request.rfid
        if not UtilClient.is_unset(request.ticket_code):
            query['TicketCode'] = request.ticket_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindGuestRfidPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.BindGuestRfidPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_guest_rfid_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.BindGuestRfidPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.BindGuestRfidPopResponse:
        """
        @param request: BindGuestRfidPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindGuestRfidPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.guest_ticket_record_id):
            query['GuestTicketRecordId'] = request.guest_ticket_record_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.rfid):
            query['Rfid'] = request.rfid
        if not UtilClient.is_unset(request.ticket_code):
            query['TicketCode'] = request.ticket_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindGuestRfidPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.BindGuestRfidPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_guest_rfid_pop(
        self,
        request: marketing_event_20210101_models.BindGuestRfidPopRequest,
    ) -> marketing_event_20210101_models.BindGuestRfidPopResponse:
        """
        @param request: BindGuestRfidPopRequest
        @return: BindGuestRfidPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_guest_rfid_pop_with_options(request, runtime)

    async def bind_guest_rfid_pop_async(
        self,
        request: marketing_event_20210101_models.BindGuestRfidPopRequest,
    ) -> marketing_event_20210101_models.BindGuestRfidPopResponse:
        """
        @param request: BindGuestRfidPopRequest
        @return: BindGuestRfidPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_guest_rfid_pop_with_options_async(request, runtime)

    def check_nfcbind_pop_with_options(
        self,
        request: marketing_event_20210101_models.CheckNFCBindPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.CheckNFCBindPopResponse:
        """
        @param request: CheckNFCBindPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckNFCBindPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckNFCBindPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.CheckNFCBindPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_nfcbind_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.CheckNFCBindPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.CheckNFCBindPopResponse:
        """
        @param request: CheckNFCBindPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckNFCBindPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckNFCBindPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.CheckNFCBindPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_nfcbind_pop(
        self,
        request: marketing_event_20210101_models.CheckNFCBindPopRequest,
    ) -> marketing_event_20210101_models.CheckNFCBindPopResponse:
        """
        @param request: CheckNFCBindPopRequest
        @return: CheckNFCBindPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_nfcbind_pop_with_options(request, runtime)

    async def check_nfcbind_pop_async(
        self,
        request: marketing_event_20210101_models.CheckNFCBindPopRequest,
    ) -> marketing_event_20210101_models.CheckNFCBindPopResponse:
        """
        @param request: CheckNFCBindPopRequest
        @return: CheckNFCBindPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_nfcbind_pop_with_options_async(request, runtime)

    def find_guest_credentials_record_with_options(
        self,
        request: marketing_event_20210101_models.FindGuestCredentialsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.FindGuestCredentialsRecordResponse:
        """
        @summary 拉取领证人员记录
        
        @param request: FindGuestCredentialsRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindGuestCredentialsRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.date_time_string):
            query['DateTimeString'] = request.date_time_string
        if not UtilClient.is_unset(request.end_date_time):
            query['EndDateTime'] = request.end_date_time
        if not UtilClient.is_unset(request.start_date_time):
            query['StartDateTime'] = request.start_date_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindGuestCredentialsRecord',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.FindGuestCredentialsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_guest_credentials_record_with_options_async(
        self,
        request: marketing_event_20210101_models.FindGuestCredentialsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.FindGuestCredentialsRecordResponse:
        """
        @summary 拉取领证人员记录
        
        @param request: FindGuestCredentialsRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindGuestCredentialsRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.date_time_string):
            query['DateTimeString'] = request.date_time_string
        if not UtilClient.is_unset(request.end_date_time):
            query['EndDateTime'] = request.end_date_time
        if not UtilClient.is_unset(request.start_date_time):
            query['StartDateTime'] = request.start_date_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindGuestCredentialsRecord',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.FindGuestCredentialsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_guest_credentials_record(
        self,
        request: marketing_event_20210101_models.FindGuestCredentialsRecordRequest,
    ) -> marketing_event_20210101_models.FindGuestCredentialsRecordResponse:
        """
        @summary 拉取领证人员记录
        
        @param request: FindGuestCredentialsRecordRequest
        @return: FindGuestCredentialsRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_guest_credentials_record_with_options(request, runtime)

    async def find_guest_credentials_record_async(
        self,
        request: marketing_event_20210101_models.FindGuestCredentialsRecordRequest,
    ) -> marketing_event_20210101_models.FindGuestCredentialsRecordResponse:
        """
        @summary 拉取领证人员记录
        
        @param request: FindGuestCredentialsRecordRequest
        @return: FindGuestCredentialsRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_guest_credentials_record_with_options_async(request, runtime)

    def find_guest_ticket_record_with_options(
        self,
        request: marketing_event_20210101_models.FindGuestTicketRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.FindGuestTicketRecordResponse:
        """
        @summary 云栖大会获取取票人信息list接口
        
        @param request: FindGuestTicketRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindGuestTicketRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.date_time_string):
            query['DateTimeString'] = request.date_time_string
        if not UtilClient.is_unset(request.end_date_time):
            query['EndDateTime'] = request.end_date_time
        if not UtilClient.is_unset(request.start_date_time):
            query['StartDateTime'] = request.start_date_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindGuestTicketRecord',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.FindGuestTicketRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_guest_ticket_record_with_options_async(
        self,
        request: marketing_event_20210101_models.FindGuestTicketRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.FindGuestTicketRecordResponse:
        """
        @summary 云栖大会获取取票人信息list接口
        
        @param request: FindGuestTicketRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindGuestTicketRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.date_time_string):
            query['DateTimeString'] = request.date_time_string
        if not UtilClient.is_unset(request.end_date_time):
            query['EndDateTime'] = request.end_date_time
        if not UtilClient.is_unset(request.start_date_time):
            query['StartDateTime'] = request.start_date_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindGuestTicketRecord',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.FindGuestTicketRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_guest_ticket_record(
        self,
        request: marketing_event_20210101_models.FindGuestTicketRecordRequest,
    ) -> marketing_event_20210101_models.FindGuestTicketRecordResponse:
        """
        @summary 云栖大会获取取票人信息list接口
        
        @param request: FindGuestTicketRecordRequest
        @return: FindGuestTicketRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_guest_ticket_record_with_options(request, runtime)

    async def find_guest_ticket_record_async(
        self,
        request: marketing_event_20210101_models.FindGuestTicketRecordRequest,
    ) -> marketing_event_20210101_models.FindGuestTicketRecordResponse:
        """
        @summary 云栖大会获取取票人信息list接口
        
        @param request: FindGuestTicketRecordRequest
        @return: FindGuestTicketRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_guest_ticket_record_with_options_async(request, runtime)

    def query_all_activity_info_with_options(
        self,
        request: marketing_event_20210101_models.QueryAllActivityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QueryAllActivityInfoResponse:
        """
        @param request: QueryAllActivityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAllActivityInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAllActivityInfo',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QueryAllActivityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_all_activity_info_with_options_async(
        self,
        request: marketing_event_20210101_models.QueryAllActivityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QueryAllActivityInfoResponse:
        """
        @param request: QueryAllActivityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAllActivityInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAllActivityInfo',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QueryAllActivityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_all_activity_info(
        self,
        request: marketing_event_20210101_models.QueryAllActivityInfoRequest,
    ) -> marketing_event_20210101_models.QueryAllActivityInfoResponse:
        """
        @param request: QueryAllActivityInfoRequest
        @return: QueryAllActivityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_all_activity_info_with_options(request, runtime)

    async def query_all_activity_info_async(
        self,
        request: marketing_event_20210101_models.QueryAllActivityInfoRequest,
    ) -> marketing_event_20210101_models.QueryAllActivityInfoResponse:
        """
        @param request: QueryAllActivityInfoRequest
        @return: QueryAllActivityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_all_activity_info_with_options_async(request, runtime)

    def query_order_session_list_pop_with_options(
        self,
        request: marketing_event_20210101_models.QueryOrderSessionListPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QueryOrderSessionListPopResponse:
        """
        @param request: QueryOrderSessionListPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrderSessionListPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderSessionListPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QueryOrderSessionListPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_session_list_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.QueryOrderSessionListPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QueryOrderSessionListPopResponse:
        """
        @param request: QueryOrderSessionListPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrderSessionListPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderSessionListPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QueryOrderSessionListPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_session_list_pop(
        self,
        request: marketing_event_20210101_models.QueryOrderSessionListPopRequest,
    ) -> marketing_event_20210101_models.QueryOrderSessionListPopResponse:
        """
        @param request: QueryOrderSessionListPopRequest
        @return: QueryOrderSessionListPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_order_session_list_pop_with_options(request, runtime)

    async def query_order_session_list_pop_async(
        self,
        request: marketing_event_20210101_models.QueryOrderSessionListPopRequest,
    ) -> marketing_event_20210101_models.QueryOrderSessionListPopResponse:
        """
        @param request: QueryOrderSessionListPopRequest
        @return: QueryOrderSessionListPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_order_session_list_pop_with_options_async(request, runtime)

    def query_session_by_activity_id_pop_with_options(
        self,
        request: marketing_event_20210101_models.QuerySessionByActivityIdPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QuerySessionByActivityIdPopResponse:
        """
        @param request: QuerySessionByActivityIdPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySessionByActivityIdPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionByActivityIdPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QuerySessionByActivityIdPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_session_by_activity_id_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.QuerySessionByActivityIdPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QuerySessionByActivityIdPopResponse:
        """
        @param request: QuerySessionByActivityIdPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySessionByActivityIdPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionByActivityIdPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QuerySessionByActivityIdPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_session_by_activity_id_pop(
        self,
        request: marketing_event_20210101_models.QuerySessionByActivityIdPopRequest,
    ) -> marketing_event_20210101_models.QuerySessionByActivityIdPopResponse:
        """
        @param request: QuerySessionByActivityIdPopRequest
        @return: QuerySessionByActivityIdPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_session_by_activity_id_pop_with_options(request, runtime)

    async def query_session_by_activity_id_pop_async(
        self,
        request: marketing_event_20210101_models.QuerySessionByActivityIdPopRequest,
    ) -> marketing_event_20210101_models.QuerySessionByActivityIdPopResponse:
        """
        @param request: QuerySessionByActivityIdPopRequest
        @return: QuerySessionByActivityIdPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_session_by_activity_id_pop_with_options_async(request, runtime)

    def query_session_list_pop_with_options(
        self,
        request: marketing_event_20210101_models.QuerySessionListPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QuerySessionListPopResponse:
        """
        @param request: QuerySessionListPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySessionListPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionListPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QuerySessionListPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_session_list_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.QuerySessionListPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QuerySessionListPopResponse:
        """
        @param request: QuerySessionListPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySessionListPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.nfc_id):
            query['NfcId'] = request.nfc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionListPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QuerySessionListPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_session_list_pop(
        self,
        request: marketing_event_20210101_models.QuerySessionListPopRequest,
    ) -> marketing_event_20210101_models.QuerySessionListPopResponse:
        """
        @param request: QuerySessionListPopRequest
        @return: QuerySessionListPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_session_list_pop_with_options(request, runtime)

    async def query_session_list_pop_async(
        self,
        request: marketing_event_20210101_models.QuerySessionListPopRequest,
    ) -> marketing_event_20210101_models.QuerySessionListPopResponse:
        """
        @param request: QuerySessionListPopRequest
        @return: QuerySessionListPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_session_list_pop_with_options_async(request, runtime)

    def query_sign_in_record_pop_with_options(
        self,
        request: marketing_event_20210101_models.QuerySignInRecordPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QuerySignInRecordPopResponse:
        """
        @param request: QuerySignInRecordPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySignInRecordPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySignInRecordPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QuerySignInRecordPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sign_in_record_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.QuerySignInRecordPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QuerySignInRecordPopResponse:
        """
        @param request: QuerySignInRecordPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySignInRecordPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySignInRecordPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QuerySignInRecordPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sign_in_record_pop(
        self,
        request: marketing_event_20210101_models.QuerySignInRecordPopRequest,
    ) -> marketing_event_20210101_models.QuerySignInRecordPopResponse:
        """
        @param request: QuerySignInRecordPopRequest
        @return: QuerySignInRecordPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sign_in_record_pop_with_options(request, runtime)

    async def query_sign_in_record_pop_async(
        self,
        request: marketing_event_20210101_models.QuerySignInRecordPopRequest,
    ) -> marketing_event_20210101_models.QuerySignInRecordPopResponse:
        """
        @param request: QuerySignInRecordPopRequest
        @return: QuerySignInRecordPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sign_in_record_pop_with_options_async(request, runtime)

    def query_single_activity_info_with_options(
        self,
        request: marketing_event_20210101_models.QuerySingleActivityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QuerySingleActivityInfoResponse:
        """
        @param request: QuerySingleActivityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySingleActivityInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySingleActivityInfo',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QuerySingleActivityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_single_activity_info_with_options_async(
        self,
        request: marketing_event_20210101_models.QuerySingleActivityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.QuerySingleActivityInfoResponse:
        """
        @param request: QuerySingleActivityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySingleActivityInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySingleActivityInfo',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.QuerySingleActivityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_single_activity_info(
        self,
        request: marketing_event_20210101_models.QuerySingleActivityInfoRequest,
    ) -> marketing_event_20210101_models.QuerySingleActivityInfoResponse:
        """
        @param request: QuerySingleActivityInfoRequest
        @return: QuerySingleActivityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_single_activity_info_with_options(request, runtime)

    async def query_single_activity_info_async(
        self,
        request: marketing_event_20210101_models.QuerySingleActivityInfoRequest,
    ) -> marketing_event_20210101_models.QuerySingleActivityInfoResponse:
        """
        @param request: QuerySingleActivityInfoRequest
        @return: QuerySingleActivityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_single_activity_info_with_options_async(request, runtime)

    def sync_sign_in_info_with_options(
        self,
        request: marketing_event_20210101_models.SyncSignInInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.SyncSignInInfoResponse:
        """
        @param request: SyncSignInInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncSignInInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncSignInInfo',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.SyncSignInInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_sign_in_info_with_options_async(
        self,
        request: marketing_event_20210101_models.SyncSignInInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.SyncSignInInfoResponse:
        """
        @param request: SyncSignInInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncSignInInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncSignInInfo',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.SyncSignInInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_sign_in_info(
        self,
        request: marketing_event_20210101_models.SyncSignInInfoRequest,
    ) -> marketing_event_20210101_models.SyncSignInInfoResponse:
        """
        @param request: SyncSignInInfoRequest
        @return: SyncSignInInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_sign_in_info_with_options(request, runtime)

    async def sync_sign_in_info_async(
        self,
        request: marketing_event_20210101_models.SyncSignInInfoRequest,
    ) -> marketing_event_20210101_models.SyncSignInInfoResponse:
        """
        @param request: SyncSignInInfoRequest
        @return: SyncSignInInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_sign_in_info_with_options_async(request, runtime)

    def ticket_or_credentials_sign_in_pop_with_options(
        self,
        request: marketing_event_20210101_models.TicketOrCredentialsSignInPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.TicketOrCredentialsSignInPopResponse:
        """
        @param request: TicketOrCredentialsSignInPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TicketOrCredentialsSignInPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.conference_name):
            query['ConferenceName'] = request.conference_name
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.entry_name):
            query['EntryName'] = request.entry_name
        if not UtilClient.is_unset(request.idcard):
            query['Idcard'] = request.idcard
        if not UtilClient.is_unset(request.sign_time):
            query['SignTime'] = request.sign_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketOrCredentialsSignInPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.TicketOrCredentialsSignInPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_or_credentials_sign_in_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.TicketOrCredentialsSignInPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.TicketOrCredentialsSignInPopResponse:
        """
        @param request: TicketOrCredentialsSignInPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TicketOrCredentialsSignInPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.conference_name):
            query['ConferenceName'] = request.conference_name
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.entry_name):
            query['EntryName'] = request.entry_name
        if not UtilClient.is_unset(request.idcard):
            query['Idcard'] = request.idcard
        if not UtilClient.is_unset(request.sign_time):
            query['SignTime'] = request.sign_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TicketOrCredentialsSignInPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.TicketOrCredentialsSignInPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_or_credentials_sign_in_pop(
        self,
        request: marketing_event_20210101_models.TicketOrCredentialsSignInPopRequest,
    ) -> marketing_event_20210101_models.TicketOrCredentialsSignInPopResponse:
        """
        @param request: TicketOrCredentialsSignInPopRequest
        @return: TicketOrCredentialsSignInPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ticket_or_credentials_sign_in_pop_with_options(request, runtime)

    async def ticket_or_credentials_sign_in_pop_async(
        self,
        request: marketing_event_20210101_models.TicketOrCredentialsSignInPopRequest,
    ) -> marketing_event_20210101_models.TicketOrCredentialsSignInPopResponse:
        """
        @param request: TicketOrCredentialsSignInPopRequest
        @return: TicketOrCredentialsSignInPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ticket_or_credentials_sign_in_pop_with_options_async(request, runtime)

    def update_credentials_status_pop_with_options(
        self,
        request: marketing_event_20210101_models.UpdateCredentialsStatusPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.UpdateCredentialsStatusPopResponse:
        """
        @param request: UpdateCredentialsStatusPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCredentialsStatusPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.proxy_recipient_name):
            query['ProxyRecipientName'] = request.proxy_recipient_name
        if not UtilClient.is_unset(request.proxy_recipient_phone_number):
            query['ProxyRecipientPhoneNumber'] = request.proxy_recipient_phone_number
        if not UtilClient.is_unset(request.receipt_location):
            query['ReceiptLocation'] = request.receipt_location
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCredentialsStatusPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.UpdateCredentialsStatusPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_credentials_status_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.UpdateCredentialsStatusPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.UpdateCredentialsStatusPopResponse:
        """
        @param request: UpdateCredentialsStatusPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCredentialsStatusPopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.proxy_recipient_name):
            query['ProxyRecipientName'] = request.proxy_recipient_name
        if not UtilClient.is_unset(request.proxy_recipient_phone_number):
            query['ProxyRecipientPhoneNumber'] = request.proxy_recipient_phone_number
        if not UtilClient.is_unset(request.receipt_location):
            query['ReceiptLocation'] = request.receipt_location
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCredentialsStatusPop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.UpdateCredentialsStatusPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_credentials_status_pop(
        self,
        request: marketing_event_20210101_models.UpdateCredentialsStatusPopRequest,
    ) -> marketing_event_20210101_models.UpdateCredentialsStatusPopResponse:
        """
        @param request: UpdateCredentialsStatusPopRequest
        @return: UpdateCredentialsStatusPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_credentials_status_pop_with_options(request, runtime)

    async def update_credentials_status_pop_async(
        self,
        request: marketing_event_20210101_models.UpdateCredentialsStatusPopRequest,
    ) -> marketing_event_20210101_models.UpdateCredentialsStatusPopResponse:
        """
        @param request: UpdateCredentialsStatusPopRequest
        @return: UpdateCredentialsStatusPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_credentials_status_pop_with_options_async(request, runtime)

    def update_ticket_record_byticket_code_pop_with_options(
        self,
        request: marketing_event_20210101_models.UpdateTicketRecordByticketCodePopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.UpdateTicketRecordByticketCodePopResponse:
        """
        @param request: UpdateTicketRecordByticketCodePopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTicketRecordByticketCodePopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agenda_id):
            query['AgendaId'] = request.agenda_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.event):
            query['Event'] = request.event
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTicketRecordByticketCodePop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.UpdateTicketRecordByticketCodePopResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ticket_record_byticket_code_pop_with_options_async(
        self,
        request: marketing_event_20210101_models.UpdateTicketRecordByticketCodePopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketing_event_20210101_models.UpdateTicketRecordByticketCodePopResponse:
        """
        @param request: UpdateTicketRecordByticketCodePopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTicketRecordByticketCodePopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agenda_id):
            query['AgendaId'] = request.agenda_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.event):
            query['Event'] = request.event
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTicketRecordByticketCodePop',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            marketing_event_20210101_models.UpdateTicketRecordByticketCodePopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ticket_record_byticket_code_pop(
        self,
        request: marketing_event_20210101_models.UpdateTicketRecordByticketCodePopRequest,
    ) -> marketing_event_20210101_models.UpdateTicketRecordByticketCodePopResponse:
        """
        @param request: UpdateTicketRecordByticketCodePopRequest
        @return: UpdateTicketRecordByticketCodePopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ticket_record_byticket_code_pop_with_options(request, runtime)

    async def update_ticket_record_byticket_code_pop_async(
        self,
        request: marketing_event_20210101_models.UpdateTicketRecordByticketCodePopRequest,
    ) -> marketing_event_20210101_models.UpdateTicketRecordByticketCodePopResponse:
        """
        @param request: UpdateTicketRecordByticketCodePopRequest
        @return: UpdateTicketRecordByticketCodePopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ticket_record_byticket_code_pop_with_options_async(request, runtime)
