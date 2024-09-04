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
