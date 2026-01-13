# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_iqs20241121 import models as main_models
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
        self._endpoint = self.get_endpoint('iqs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_formal_service_with_options(
        self,
        request: main_models.ApplyFormalServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyFormalServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyFormalService',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/services/commands/applyFormalService',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyFormalServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_formal_service_with_options_async(
        self,
        request: main_models.ApplyFormalServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyFormalServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyFormalService',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/services/commands/applyFormalService',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyFormalServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_formal_service(
        self,
        request: main_models.ApplyFormalServiceRequest,
    ) -> main_models.ApplyFormalServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.apply_formal_service_with_options(request, headers, runtime)

    async def apply_formal_service_async(
        self,
        request: main_models.ApplyFormalServiceRequest,
    ) -> main_models.ApplyFormalServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.apply_formal_service_with_options_async(request, headers, runtime)

    def check_account_type_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckAccountTypeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CheckAccountType',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/openService/v1/account/commands/checkAccountType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAccountTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_account_type_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckAccountTypeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CheckAccountType',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/openService/v1/account/commands/checkAccountType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAccountTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_account_type(self) -> main_models.CheckAccountTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_account_type_with_options(headers, runtime)

    async def check_account_type_async(self) -> main_models.CheckAccountTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_account_type_with_options_async(headers, runtime)

    def download_api_call_daily_detail_with_options(
        self,
        request: main_models.DownloadApiCallDailyDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadApiCallDailyDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'DownloadApiCallDailyDetail',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/downloadApiCallDailyDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadApiCallDailyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_api_call_daily_detail_with_options_async(
        self,
        request: main_models.DownloadApiCallDailyDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadApiCallDailyDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'DownloadApiCallDailyDetail',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/downloadApiCallDailyDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadApiCallDailyDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_api_call_daily_detail(
        self,
        request: main_models.DownloadApiCallDailyDetailRequest,
    ) -> main_models.DownloadApiCallDailyDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.download_api_call_daily_detail_with_options(request, headers, runtime)

    async def download_api_call_daily_detail_async(
        self,
        request: main_models.DownloadApiCallDailyDetailRequest,
    ) -> main_models.DownloadApiCallDailyDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.download_api_call_daily_detail_with_options_async(request, headers, runtime)

    def download_metering_daily_detail_with_options(
        self,
        request: main_models.DownloadMeteringDailyDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadMeteringDailyDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'DownloadMeteringDailyDetail',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/downloadMeteringDailyDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadMeteringDailyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_metering_daily_detail_with_options_async(
        self,
        request: main_models.DownloadMeteringDailyDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadMeteringDailyDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'DownloadMeteringDailyDetail',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/downloadMeteringDailyDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadMeteringDailyDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_metering_daily_detail(
        self,
        request: main_models.DownloadMeteringDailyDetailRequest,
    ) -> main_models.DownloadMeteringDailyDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.download_metering_daily_detail_with_options(request, headers, runtime)

    async def download_metering_daily_detail_async(
        self,
        request: main_models.DownloadMeteringDailyDetailRequest,
    ) -> main_models.DownloadMeteringDailyDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.download_metering_daily_detail_with_options_async(request, headers, runtime)

    def expand_search_expired_time_with_options(
        self,
        request: main_models.ExpandSearchExpiredTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExpandSearchExpiredTimeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ExpandSearchExpiredTime',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/openService/v1/account/commands/expendExpiredTime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpandSearchExpiredTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def expand_search_expired_time_with_options_async(
        self,
        request: main_models.ExpandSearchExpiredTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExpandSearchExpiredTimeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ExpandSearchExpiredTime',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/openService/v1/account/commands/expendExpiredTime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpandSearchExpiredTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expand_search_expired_time(
        self,
        request: main_models.ExpandSearchExpiredTimeRequest,
    ) -> main_models.ExpandSearchExpiredTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.expand_search_expired_time_with_options(request, headers, runtime)

    async def expand_search_expired_time_async(
        self,
        request: main_models.ExpandSearchExpiredTimeRequest,
    ) -> main_models.ExpandSearchExpiredTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.expand_search_expired_time_with_options_async(request, headers, runtime)

    def get_account_config_info_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountConfigInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAccountConfigInfo',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/openService/v1/account/command/accountConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountConfigInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_config_info_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountConfigInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAccountConfigInfo',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/openService/v1/account/command/accountConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountConfigInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_config_info(self) -> main_models.GetAccountConfigInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_account_config_info_with_options(headers, runtime)

    async def get_account_config_info_async(self) -> main_models.GetAccountConfigInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_account_config_info_with_options_async(headers, runtime)

    def get_account_review_record_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountReviewRecordResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAccountReviewRecord',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/services/commands/reviewRecord',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountReviewRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_review_record_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountReviewRecordResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAccountReviewRecord',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/services/commands/reviewRecord',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountReviewRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_review_record(self) -> main_models.GetAccountReviewRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_account_review_record_with_options(headers, runtime)

    async def get_account_review_record_async(self) -> main_models.GetAccountReviewRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_account_review_record_with_options_async(headers, runtime)

    def get_metering_summary_with_options(
        self,
        request: main_models.GetMeteringSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMeteringSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_period):
            query['billPeriod'] = request.bill_period
        if not DaraCore.is_null(request.billing_item):
            query['billingItem'] = request.billing_item
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.sub_account_id):
            query['subAccountId'] = request.sub_account_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMeteringSummary',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/metering/summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMeteringSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_metering_summary_with_options_async(
        self,
        request: main_models.GetMeteringSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMeteringSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_period):
            query['billPeriod'] = request.bill_period
        if not DaraCore.is_null(request.billing_item):
            query['billingItem'] = request.billing_item
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.sub_account_id):
            query['subAccountId'] = request.sub_account_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMeteringSummary',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/metering/summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMeteringSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_metering_summary(
        self,
        request: main_models.GetMeteringSummaryRequest,
    ) -> main_models.GetMeteringSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_metering_summary_with_options(request, headers, runtime)

    async def get_metering_summary_async(
        self,
        request: main_models.GetMeteringSummaryRequest,
    ) -> main_models.GetMeteringSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_metering_summary_with_options_async(request, headers, runtime)

    def get_service_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceConfig',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/services/commands/serviceConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceConfig',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/services/commands/serviceConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_config(self) -> main_models.GetServiceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_config_with_options(headers, runtime)

    async def get_service_config_async(self) -> main_models.GetServiceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_config_with_options_async(headers, runtime)

    def list_api_call_daily_detail_with_options(
        self,
        request: main_models.ListApiCallDailyDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiCallDailyDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['apiName'] = request.api_name
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.engine_type):
            query['engineType'] = request.engine_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiCallDailyDetail',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/apiCall/dailyDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiCallDailyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_call_daily_detail_with_options_async(
        self,
        request: main_models.ListApiCallDailyDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiCallDailyDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['apiName'] = request.api_name
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.engine_type):
            query['engineType'] = request.engine_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiCallDailyDetail',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/apiCall/dailyDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiCallDailyDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_call_daily_detail(
        self,
        request: main_models.ListApiCallDailyDetailRequest,
    ) -> main_models.ListApiCallDailyDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_api_call_daily_detail_with_options(request, headers, runtime)

    async def list_api_call_daily_detail_async(
        self,
        request: main_models.ListApiCallDailyDetailRequest,
    ) -> main_models.ListApiCallDailyDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_api_call_daily_detail_with_options_async(request, headers, runtime)

    def list_api_names_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiNamesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListApiNames',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/apiNames',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_names_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiNamesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListApiNames',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/apiNames',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_names(self) -> main_models.ListApiNamesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_api_names_with_options(headers, runtime)

    async def list_api_names_async(self) -> main_models.ListApiNamesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_api_names_with_options_async(headers, runtime)

    def list_metering_daily_detail_with_options(
        self,
        request: main_models.ListMeteringDailyDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMeteringDailyDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_period):
            query['billPeriod'] = request.bill_period
        if not DaraCore.is_null(request.billing_item):
            query['billingItem'] = request.billing_item
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.sub_account_id):
            query['subAccountId'] = request.sub_account_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMeteringDailyDetail',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/metering/dailyDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMeteringDailyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_metering_daily_detail_with_options_async(
        self,
        request: main_models.ListMeteringDailyDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMeteringDailyDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_period):
            query['billPeriod'] = request.bill_period
        if not DaraCore.is_null(request.billing_item):
            query['billingItem'] = request.billing_item
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.sub_account_id):
            query['subAccountId'] = request.sub_account_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMeteringDailyDetail',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/metering/dailyDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMeteringDailyDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_metering_daily_detail(
        self,
        request: main_models.ListMeteringDailyDetailRequest,
    ) -> main_models.ListMeteringDailyDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_metering_daily_detail_with_options(request, headers, runtime)

    async def list_metering_daily_detail_async(
        self,
        request: main_models.ListMeteringDailyDetailRequest,
    ) -> main_models.ListMeteringDailyDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_metering_daily_detail_with_options_async(request, headers, runtime)

    def list_sub_account_info_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubAccountInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSubAccountInfo',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/subAccountInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_account_info_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubAccountInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSubAccountInfo',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/console/v1/monitors/commands/subAccountInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_account_info(self) -> main_models.ListSubAccountInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sub_account_info_with_options(headers, runtime)

    async def list_sub_account_info_async(self) -> main_models.ListSubAccountInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sub_account_info_with_options_async(headers, runtime)

    def manage_search_account_info_with_options(
        self,
        request: main_models.ManageSearchAccountInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ManageSearchAccountInfoResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ManageSearchAccountInfo',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/openService/v1/account/commands/manage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageSearchAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_search_account_info_with_options_async(
        self,
        request: main_models.ManageSearchAccountInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ManageSearchAccountInfoResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ManageSearchAccountInfo',
            version = '2024-11-21',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/openService/v1/account/commands/manage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageSearchAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_search_account_info(
        self,
        request: main_models.ManageSearchAccountInfoRequest,
    ) -> main_models.ManageSearchAccountInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.manage_search_account_info_with_options(request, headers, runtime)

    async def manage_search_account_info_async(
        self,
        request: main_models.ManageSearchAccountInfoRequest,
    ) -> main_models.ManageSearchAccountInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.manage_search_account_info_with_options_async(request, headers, runtime)
