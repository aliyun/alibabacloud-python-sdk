# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_airticketopen20230117 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('airticketopen', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def account_flow_list_with_options(
        self,
        request: main_models.AccountFlowListRequest,
        headers: main_models.AccountFlowListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AccountFlowListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.day_num):
            query['day_num'] = request.day_num
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.utc_begin_time):
            query['utc_begin_time'] = request.utc_begin_time
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AccountFlowList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/account/flow-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountFlowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def account_flow_list_with_options_async(
        self,
        request: main_models.AccountFlowListRequest,
        headers: main_models.AccountFlowListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AccountFlowListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.day_num):
            query['day_num'] = request.day_num
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.utc_begin_time):
            query['utc_begin_time'] = request.utc_begin_time
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AccountFlowList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/account/flow-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountFlowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def account_flow_list(
        self,
        request: main_models.AccountFlowListRequest,
    ) -> main_models.AccountFlowListResponse:
        runtime = RuntimeOptions()
        headers = main_models.AccountFlowListHeaders()
        return self.account_flow_list_with_options(request, headers, runtime)

    async def account_flow_list_async(
        self,
        request: main_models.AccountFlowListRequest,
    ) -> main_models.AccountFlowListResponse:
        runtime = RuntimeOptions()
        headers = main_models.AccountFlowListHeaders()
        return await self.account_flow_list_with_options_async(request, headers, runtime)

    def ancillary_suggest_with_options(
        self,
        request: main_models.AncillarySuggestRequest,
        headers: main_models.AncillarySuggestHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AncillarySuggestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AncillarySuggest',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/ancillary/action-suggest',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AncillarySuggestResponse(),
            self.call_api(params, req, runtime)
        )

    async def ancillary_suggest_with_options_async(
        self,
        request: main_models.AncillarySuggestRequest,
        headers: main_models.AncillarySuggestHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AncillarySuggestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AncillarySuggest',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/ancillary/action-suggest',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AncillarySuggestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ancillary_suggest(
        self,
        request: main_models.AncillarySuggestRequest,
    ) -> main_models.AncillarySuggestResponse:
        runtime = RuntimeOptions()
        headers = main_models.AncillarySuggestHeaders()
        return self.ancillary_suggest_with_options(request, headers, runtime)

    async def ancillary_suggest_async(
        self,
        request: main_models.AncillarySuggestRequest,
    ) -> main_models.AncillarySuggestResponse:
        runtime = RuntimeOptions()
        headers = main_models.AncillarySuggestHeaders()
        return await self.ancillary_suggest_with_options_async(request, headers, runtime)

    def book_with_options(
        self,
        tmp_req: main_models.BookRequest,
        headers: main_models.BookHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.BookResponse:
        tmp_req.validate()
        request = main_models.BookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        if not DaraCore.is_null(tmp_req.passenger_ancillary_purchase_map_list):
            request.passenger_ancillary_purchase_map_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.passenger_ancillary_purchase_map_list, 'passenger_ancillary_purchase_map_list', 'json')
        if not DaraCore.is_null(tmp_req.passenger_list):
            request.passenger_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.passenger_list, 'passenger_list', 'json')
        body = {}
        if not DaraCore.is_null(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not DaraCore.is_null(request.out_order_num):
            body['out_order_num'] = request.out_order_num
        if not DaraCore.is_null(request.passenger_ancillary_purchase_map_list_shrink):
            body['passenger_ancillary_purchase_map_list'] = request.passenger_ancillary_purchase_map_list_shrink
        if not DaraCore.is_null(request.passenger_list_shrink):
            body['passenger_list'] = request.passenger_list_shrink
        if not DaraCore.is_null(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Book',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-book',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BookResponse(),
            self.call_api(params, req, runtime)
        )

    async def book_with_options_async(
        self,
        tmp_req: main_models.BookRequest,
        headers: main_models.BookHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.BookResponse:
        tmp_req.validate()
        request = main_models.BookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        if not DaraCore.is_null(tmp_req.passenger_ancillary_purchase_map_list):
            request.passenger_ancillary_purchase_map_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.passenger_ancillary_purchase_map_list, 'passenger_ancillary_purchase_map_list', 'json')
        if not DaraCore.is_null(tmp_req.passenger_list):
            request.passenger_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.passenger_list, 'passenger_list', 'json')
        body = {}
        if not DaraCore.is_null(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not DaraCore.is_null(request.out_order_num):
            body['out_order_num'] = request.out_order_num
        if not DaraCore.is_null(request.passenger_ancillary_purchase_map_list_shrink):
            body['passenger_ancillary_purchase_map_list'] = request.passenger_ancillary_purchase_map_list_shrink
        if not DaraCore.is_null(request.passenger_list_shrink):
            body['passenger_list'] = request.passenger_list_shrink
        if not DaraCore.is_null(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Book',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-book',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def book(
        self,
        request: main_models.BookRequest,
    ) -> main_models.BookResponse:
        runtime = RuntimeOptions()
        headers = main_models.BookHeaders()
        return self.book_with_options(request, headers, runtime)

    async def book_async(
        self,
        request: main_models.BookRequest,
    ) -> main_models.BookResponse:
        runtime = RuntimeOptions()
        headers = main_models.BookHeaders()
        return await self.book_with_options_async(request, headers, runtime)

    def cancel_with_options(
        self,
        request: main_models.CancelRequest,
        headers: main_models.CancelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CancelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Cancel',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_with_options_async(
        self,
        request: main_models.CancelRequest,
        headers: main_models.CancelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CancelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Cancel',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel(
        self,
        request: main_models.CancelRequest,
    ) -> main_models.CancelResponse:
        runtime = RuntimeOptions()
        headers = main_models.CancelHeaders()
        return self.cancel_with_options(request, headers, runtime)

    async def cancel_async(
        self,
        request: main_models.CancelRequest,
    ) -> main_models.CancelResponse:
        runtime = RuntimeOptions()
        headers = main_models.CancelHeaders()
        return await self.cancel_with_options_async(request, headers, runtime)

    def change_apply_with_options(
        self,
        tmp_req: main_models.ChangeApplyRequest,
        headers: main_models.ChangeApplyHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeApplyResponse:
        tmp_req.validate()
        request = main_models.ChangeApplyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.change_passenger_list):
            request.change_passenger_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.change_passenger_list, 'change_passenger_list', 'json')
        if not DaraCore.is_null(tmp_req.changed_journeys):
            request.changed_journeys_shrink = Utils.array_to_string_with_specified_style(tmp_req.changed_journeys, 'changed_journeys', 'json')
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        body = {}
        if not DaraCore.is_null(request.change_passenger_list_shrink):
            body['change_passenger_list'] = request.change_passenger_list_shrink
        if not DaraCore.is_null(request.changed_journeys_shrink):
            body['changed_journeys'] = request.changed_journeys_shrink
        if not DaraCore.is_null(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeApply',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/action-apply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_apply_with_options_async(
        self,
        tmp_req: main_models.ChangeApplyRequest,
        headers: main_models.ChangeApplyHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeApplyResponse:
        tmp_req.validate()
        request = main_models.ChangeApplyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.change_passenger_list):
            request.change_passenger_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.change_passenger_list, 'change_passenger_list', 'json')
        if not DaraCore.is_null(tmp_req.changed_journeys):
            request.changed_journeys_shrink = Utils.array_to_string_with_specified_style(tmp_req.changed_journeys, 'changed_journeys', 'json')
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        body = {}
        if not DaraCore.is_null(request.change_passenger_list_shrink):
            body['change_passenger_list'] = request.change_passenger_list_shrink
        if not DaraCore.is_null(request.changed_journeys_shrink):
            body['changed_journeys'] = request.changed_journeys_shrink
        if not DaraCore.is_null(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeApply',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/action-apply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_apply(
        self,
        request: main_models.ChangeApplyRequest,
    ) -> main_models.ChangeApplyResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeApplyHeaders()
        return self.change_apply_with_options(request, headers, runtime)

    async def change_apply_async(
        self,
        request: main_models.ChangeApplyRequest,
    ) -> main_models.ChangeApplyResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeApplyHeaders()
        return await self.change_apply_with_options_async(request, headers, runtime)

    def change_cancel_with_options(
        self,
        request: main_models.ChangeCancelRequest,
        headers: main_models.ChangeCancelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeCancelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeCancel',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/action-cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_cancel_with_options_async(
        self,
        request: main_models.ChangeCancelRequest,
        headers: main_models.ChangeCancelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeCancelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeCancel',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/action-cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_cancel(
        self,
        request: main_models.ChangeCancelRequest,
    ) -> main_models.ChangeCancelResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeCancelHeaders()
        return self.change_cancel_with_options(request, headers, runtime)

    async def change_cancel_async(
        self,
        request: main_models.ChangeCancelRequest,
    ) -> main_models.ChangeCancelResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeCancelHeaders()
        return await self.change_cancel_with_options_async(request, headers, runtime)

    def change_confirm_with_options(
        self,
        request: main_models.ChangeConfirmRequest,
        headers: main_models.ChangeConfirmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeConfirmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeConfirm',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/action-confirm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_confirm_with_options_async(
        self,
        request: main_models.ChangeConfirmRequest,
        headers: main_models.ChangeConfirmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeConfirmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeConfirm',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/action-confirm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeConfirmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_confirm(
        self,
        request: main_models.ChangeConfirmRequest,
    ) -> main_models.ChangeConfirmResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeConfirmHeaders()
        return self.change_confirm_with_options(request, headers, runtime)

    async def change_confirm_async(
        self,
        request: main_models.ChangeConfirmRequest,
    ) -> main_models.ChangeConfirmResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeConfirmHeaders()
        return await self.change_confirm_with_options_async(request, headers, runtime)

    def change_detail_with_options(
        self,
        request: main_models.ChangeDetailRequest,
        headers: main_models.ChangeDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_num):
            query['change_order_num'] = request.change_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_detail_with_options_async(
        self,
        request: main_models.ChangeDetailRequest,
        headers: main_models.ChangeDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_num):
            query['change_order_num'] = request.change_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_detail(
        self,
        request: main_models.ChangeDetailRequest,
    ) -> main_models.ChangeDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeDetailHeaders()
        return self.change_detail_with_options(request, headers, runtime)

    async def change_detail_async(
        self,
        request: main_models.ChangeDetailRequest,
    ) -> main_models.ChangeDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeDetailHeaders()
        return await self.change_detail_with_options_async(request, headers, runtime)

    def change_detail_list_of_buyer_with_options(
        self,
        request: main_models.ChangeDetailListOfBuyerRequest,
        headers: main_models.ChangeDetailListOfBuyerHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDetailListOfBuyerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.utc_create_begin):
            query['utc_create_begin'] = request.utc_create_begin
        if not DaraCore.is_null(request.utc_create_end):
            query['utc_create_end'] = request.utc_create_end
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDetailListOfBuyer',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/buyer/detail-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDetailListOfBuyerResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_detail_list_of_buyer_with_options_async(
        self,
        request: main_models.ChangeDetailListOfBuyerRequest,
        headers: main_models.ChangeDetailListOfBuyerHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDetailListOfBuyerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.utc_create_begin):
            query['utc_create_begin'] = request.utc_create_begin
        if not DaraCore.is_null(request.utc_create_end):
            query['utc_create_end'] = request.utc_create_end
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDetailListOfBuyer',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/buyer/detail-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDetailListOfBuyerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_detail_list_of_buyer(
        self,
        request: main_models.ChangeDetailListOfBuyerRequest,
    ) -> main_models.ChangeDetailListOfBuyerResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeDetailListOfBuyerHeaders()
        return self.change_detail_list_of_buyer_with_options(request, headers, runtime)

    async def change_detail_list_of_buyer_async(
        self,
        request: main_models.ChangeDetailListOfBuyerRequest,
    ) -> main_models.ChangeDetailListOfBuyerResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeDetailListOfBuyerHeaders()
        return await self.change_detail_list_of_buyer_with_options_async(request, headers, runtime)

    def change_detail_list_of_order_num_with_options(
        self,
        request: main_models.ChangeDetailListOfOrderNumRequest,
        headers: main_models.ChangeDetailListOfOrderNumHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDetailListOfOrderNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_num):
            query['order_num'] = request.order_num
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDetailListOfOrderNum',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/order-num/detail-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDetailListOfOrderNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_detail_list_of_order_num_with_options_async(
        self,
        request: main_models.ChangeDetailListOfOrderNumRequest,
        headers: main_models.ChangeDetailListOfOrderNumHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDetailListOfOrderNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_num):
            query['order_num'] = request.order_num
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDetailListOfOrderNum',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/change/order-num/detail-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDetailListOfOrderNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_detail_list_of_order_num(
        self,
        request: main_models.ChangeDetailListOfOrderNumRequest,
    ) -> main_models.ChangeDetailListOfOrderNumResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeDetailListOfOrderNumHeaders()
        return self.change_detail_list_of_order_num_with_options(request, headers, runtime)

    async def change_detail_list_of_order_num_async(
        self,
        request: main_models.ChangeDetailListOfOrderNumRequest,
    ) -> main_models.ChangeDetailListOfOrderNumResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChangeDetailListOfOrderNumHeaders()
        return await self.change_detail_list_of_order_num_with_options_async(request, headers, runtime)

    def collect_flight_lowest_price_with_options(
        self,
        tmp_req: main_models.CollectFlightLowestPriceRequest,
        headers: main_models.CollectFlightLowestPriceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CollectFlightLowestPriceResponse:
        tmp_req.validate()
        request = main_models.CollectFlightLowestPriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lowest_price_flight_info_list):
            request.lowest_price_flight_info_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.lowest_price_flight_info_list, 'lowest_price_flight_info_list', 'json')
        body = {}
        if not DaraCore.is_null(request.lowest_price_flight_info_list_shrink):
            body['lowest_price_flight_info_list'] = request.lowest_price_flight_info_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CollectFlightLowestPrice',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/data-collect/flight-lowest-price',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CollectFlightLowestPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def collect_flight_lowest_price_with_options_async(
        self,
        tmp_req: main_models.CollectFlightLowestPriceRequest,
        headers: main_models.CollectFlightLowestPriceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CollectFlightLowestPriceResponse:
        tmp_req.validate()
        request = main_models.CollectFlightLowestPriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lowest_price_flight_info_list):
            request.lowest_price_flight_info_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.lowest_price_flight_info_list, 'lowest_price_flight_info_list', 'json')
        body = {}
        if not DaraCore.is_null(request.lowest_price_flight_info_list_shrink):
            body['lowest_price_flight_info_list'] = request.lowest_price_flight_info_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CollectFlightLowestPrice',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/data-collect/flight-lowest-price',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CollectFlightLowestPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def collect_flight_lowest_price(
        self,
        request: main_models.CollectFlightLowestPriceRequest,
    ) -> main_models.CollectFlightLowestPriceResponse:
        runtime = RuntimeOptions()
        headers = main_models.CollectFlightLowestPriceHeaders()
        return self.collect_flight_lowest_price_with_options(request, headers, runtime)

    async def collect_flight_lowest_price_async(
        self,
        request: main_models.CollectFlightLowestPriceRequest,
    ) -> main_models.CollectFlightLowestPriceResponse:
        runtime = RuntimeOptions()
        headers = main_models.CollectFlightLowestPriceHeaders()
        return await self.collect_flight_lowest_price_with_options_async(request, headers, runtime)

    def enrich_with_options(
        self,
        tmp_req: main_models.EnrichRequest,
        headers: main_models.EnrichHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.EnrichResponse:
        tmp_req.validate()
        request = main_models.EnrichShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.journey_param_list):
            request.journey_param_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.journey_param_list, 'journey_param_list', 'json')
        body = {}
        if not DaraCore.is_null(request.adults):
            body['adults'] = request.adults
        if not DaraCore.is_null(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not DaraCore.is_null(request.children):
            body['children'] = request.children
        if not DaraCore.is_null(request.infants):
            body['infants'] = request.infants
        if not DaraCore.is_null(request.journey_param_list_shrink):
            body['journey_param_list'] = request.journey_param_list_shrink
        if not DaraCore.is_null(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Enrich',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-enrich',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnrichResponse(),
            self.call_api(params, req, runtime)
        )

    async def enrich_with_options_async(
        self,
        tmp_req: main_models.EnrichRequest,
        headers: main_models.EnrichHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.EnrichResponse:
        tmp_req.validate()
        request = main_models.EnrichShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.journey_param_list):
            request.journey_param_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.journey_param_list, 'journey_param_list', 'json')
        body = {}
        if not DaraCore.is_null(request.adults):
            body['adults'] = request.adults
        if not DaraCore.is_null(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not DaraCore.is_null(request.children):
            body['children'] = request.children
        if not DaraCore.is_null(request.infants):
            body['infants'] = request.infants
        if not DaraCore.is_null(request.journey_param_list_shrink):
            body['journey_param_list'] = request.journey_param_list_shrink
        if not DaraCore.is_null(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Enrich',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-enrich',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnrichResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enrich(
        self,
        request: main_models.EnrichRequest,
    ) -> main_models.EnrichResponse:
        runtime = RuntimeOptions()
        headers = main_models.EnrichHeaders()
        return self.enrich_with_options(request, headers, runtime)

    async def enrich_async(
        self,
        request: main_models.EnrichRequest,
    ) -> main_models.EnrichResponse:
        runtime = RuntimeOptions()
        headers = main_models.EnrichHeaders()
        return await self.enrich_with_options_async(request, headers, runtime)

    def file_upload_with_options(
        self,
        request: main_models.FileUploadRequest,
        headers: main_models.FileUploadHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FileUploadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_content):
            body['file_content'] = request.file_content
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileUpload',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/attachment/action-upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def file_upload_with_options_async(
        self,
        request: main_models.FileUploadRequest,
        headers: main_models.FileUploadHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FileUploadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_content):
            body['file_content'] = request.file_content
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileUpload',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/attachment/action-upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def file_upload(
        self,
        request: main_models.FileUploadRequest,
    ) -> main_models.FileUploadResponse:
        runtime = RuntimeOptions()
        headers = main_models.FileUploadHeaders()
        return self.file_upload_with_options(request, headers, runtime)

    async def file_upload_async(
        self,
        request: main_models.FileUploadRequest,
    ) -> main_models.FileUploadResponse:
        runtime = RuntimeOptions()
        headers = main_models.FileUploadHeaders()
        return await self.file_upload_with_options_async(request, headers, runtime)

    def flight_change_of_order_with_options(
        self,
        request: main_models.FlightChangeOfOrderRequest,
        headers: main_models.FlightChangeOfOrderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FlightChangeOfOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_num):
            query['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlightChangeOfOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/flightchange/of-order',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlightChangeOfOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_change_of_order_with_options_async(
        self,
        request: main_models.FlightChangeOfOrderRequest,
        headers: main_models.FlightChangeOfOrderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FlightChangeOfOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_num):
            query['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlightChangeOfOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/flightchange/of-order',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlightChangeOfOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_change_of_order(
        self,
        request: main_models.FlightChangeOfOrderRequest,
    ) -> main_models.FlightChangeOfOrderResponse:
        runtime = RuntimeOptions()
        headers = main_models.FlightChangeOfOrderHeaders()
        return self.flight_change_of_order_with_options(request, headers, runtime)

    async def flight_change_of_order_async(
        self,
        request: main_models.FlightChangeOfOrderRequest,
    ) -> main_models.FlightChangeOfOrderResponse:
        runtime = RuntimeOptions()
        headers = main_models.FlightChangeOfOrderHeaders()
        return await self.flight_change_of_order_with_options_async(request, headers, runtime)

    def get_token_with_options(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['app_key'] = request.app_key
        if not DaraCore.is_null(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['app_key'] = request.app_key
        if not DaraCore.is_null(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def luggage_direct_with_options(
        self,
        tmp_req: main_models.LuggageDirectRequest,
        headers: main_models.LuggageDirectHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.LuggageDirectResponse:
        tmp_req.validate()
        request = main_models.LuggageDirectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.flight_segment_param_list):
            request.flight_segment_param_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.flight_segment_param_list, 'flight_segment_param_list', 'json')
        query = {}
        if not DaraCore.is_null(request.flight_segment_param_list_shrink):
            query['flight_segment_param_list'] = request.flight_segment_param_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LuggageDirect',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/flight-data/luggage-direct',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LuggageDirectResponse(),
            self.call_api(params, req, runtime)
        )

    async def luggage_direct_with_options_async(
        self,
        tmp_req: main_models.LuggageDirectRequest,
        headers: main_models.LuggageDirectHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.LuggageDirectResponse:
        tmp_req.validate()
        request = main_models.LuggageDirectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.flight_segment_param_list):
            request.flight_segment_param_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.flight_segment_param_list, 'flight_segment_param_list', 'json')
        query = {}
        if not DaraCore.is_null(request.flight_segment_param_list_shrink):
            query['flight_segment_param_list'] = request.flight_segment_param_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LuggageDirect',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/flight-data/luggage-direct',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LuggageDirectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def luggage_direct(
        self,
        request: main_models.LuggageDirectRequest,
    ) -> main_models.LuggageDirectResponse:
        runtime = RuntimeOptions()
        headers = main_models.LuggageDirectHeaders()
        return self.luggage_direct_with_options(request, headers, runtime)

    async def luggage_direct_async(
        self,
        request: main_models.LuggageDirectRequest,
    ) -> main_models.LuggageDirectResponse:
        runtime = RuntimeOptions()
        headers = main_models.LuggageDirectHeaders()
        return await self.luggage_direct_with_options_async(request, headers, runtime)

    def order_detail_with_options(
        self,
        request: main_models.OrderDetailRequest,
        headers: main_models.OrderDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.OrderDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_num):
            query['order_num'] = request.order_num
        if not DaraCore.is_null(request.out_order_num):
            query['out_order_num'] = request.out_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OrderDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/order-detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_detail_with_options_async(
        self,
        request: main_models.OrderDetailRequest,
        headers: main_models.OrderDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.OrderDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_num):
            query['order_num'] = request.order_num
        if not DaraCore.is_null(request.out_order_num):
            query['out_order_num'] = request.out_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OrderDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/order-detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_detail(
        self,
        request: main_models.OrderDetailRequest,
    ) -> main_models.OrderDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.OrderDetailHeaders()
        return self.order_detail_with_options(request, headers, runtime)

    async def order_detail_async(
        self,
        request: main_models.OrderDetailRequest,
    ) -> main_models.OrderDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.OrderDetailHeaders()
        return await self.order_detail_with_options_async(request, headers, runtime)

    def order_list_with_options(
        self,
        request: main_models.OrderListRequest,
        headers: main_models.OrderListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.OrderListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.book_time_end):
            query['book_time_end'] = request.book_time_end
        if not DaraCore.is_null(request.book_time_start):
            query['book_time_start'] = request.book_time_start
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OrderList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/order-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_list_with_options_async(
        self,
        request: main_models.OrderListRequest,
        headers: main_models.OrderListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.OrderListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.book_time_end):
            query['book_time_end'] = request.book_time_end
        if not DaraCore.is_null(request.book_time_start):
            query['book_time_start'] = request.book_time_start
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OrderList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/order-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_list(
        self,
        request: main_models.OrderListRequest,
    ) -> main_models.OrderListResponse:
        runtime = RuntimeOptions()
        headers = main_models.OrderListHeaders()
        return self.order_list_with_options(request, headers, runtime)

    async def order_list_async(
        self,
        request: main_models.OrderListRequest,
    ) -> main_models.OrderListResponse:
        runtime = RuntimeOptions()
        headers = main_models.OrderListHeaders()
        return await self.order_list_with_options_async(request, headers, runtime)

    def pricing_with_options(
        self,
        request: main_models.PricingRequest,
        headers: main_models.PricingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PricingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Pricing',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-pricing',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PricingResponse(),
            self.call_api(params, req, runtime)
        )

    async def pricing_with_options_async(
        self,
        request: main_models.PricingRequest,
        headers: main_models.PricingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PricingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Pricing',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-pricing',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PricingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pricing(
        self,
        request: main_models.PricingRequest,
    ) -> main_models.PricingResponse:
        runtime = RuntimeOptions()
        headers = main_models.PricingHeaders()
        return self.pricing_with_options(request, headers, runtime)

    async def pricing_async(
        self,
        request: main_models.PricingRequest,
    ) -> main_models.PricingResponse:
        runtime = RuntimeOptions()
        headers = main_models.PricingHeaders()
        return await self.pricing_with_options_async(request, headers, runtime)

    def refund_apply_with_options(
        self,
        tmp_req: main_models.RefundApplyRequest,
        headers: main_models.RefundApplyHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RefundApplyResponse:
        tmp_req.validate()
        request = main_models.RefundApplyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.refund_journeys):
            request.refund_journeys_shrink = Utils.array_to_string_with_specified_style(tmp_req.refund_journeys, 'refund_journeys', 'json')
        if not DaraCore.is_null(tmp_req.refund_passenger_list):
            request.refund_passenger_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.refund_passenger_list, 'refund_passenger_list', 'json')
        if not DaraCore.is_null(tmp_req.refund_type):
            request.refund_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.refund_type, 'refund_type', 'json')
        body = {}
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        if not DaraCore.is_null(request.refund_journeys_shrink):
            body['refund_journeys'] = request.refund_journeys_shrink
        if not DaraCore.is_null(request.refund_passenger_list_shrink):
            body['refund_passenger_list'] = request.refund_passenger_list_shrink
        if not DaraCore.is_null(request.refund_type_shrink):
            body['refund_type'] = request.refund_type_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefundApply',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/refund/action-apply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_apply_with_options_async(
        self,
        tmp_req: main_models.RefundApplyRequest,
        headers: main_models.RefundApplyHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RefundApplyResponse:
        tmp_req.validate()
        request = main_models.RefundApplyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.refund_journeys):
            request.refund_journeys_shrink = Utils.array_to_string_with_specified_style(tmp_req.refund_journeys, 'refund_journeys', 'json')
        if not DaraCore.is_null(tmp_req.refund_passenger_list):
            request.refund_passenger_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.refund_passenger_list, 'refund_passenger_list', 'json')
        if not DaraCore.is_null(tmp_req.refund_type):
            request.refund_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.refund_type, 'refund_type', 'json')
        body = {}
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        if not DaraCore.is_null(request.refund_journeys_shrink):
            body['refund_journeys'] = request.refund_journeys_shrink
        if not DaraCore.is_null(request.refund_passenger_list_shrink):
            body['refund_passenger_list'] = request.refund_passenger_list_shrink
        if not DaraCore.is_null(request.refund_type_shrink):
            body['refund_type'] = request.refund_type_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefundApply',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/refund/action-apply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_apply(
        self,
        request: main_models.RefundApplyRequest,
    ) -> main_models.RefundApplyResponse:
        runtime = RuntimeOptions()
        headers = main_models.RefundApplyHeaders()
        return self.refund_apply_with_options(request, headers, runtime)

    async def refund_apply_async(
        self,
        request: main_models.RefundApplyRequest,
    ) -> main_models.RefundApplyResponse:
        runtime = RuntimeOptions()
        headers = main_models.RefundApplyHeaders()
        return await self.refund_apply_with_options_async(request, headers, runtime)

    def refund_detail_with_options(
        self,
        request: main_models.RefundDetailRequest,
        headers: main_models.RefundDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RefundDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.refund_order_num):
            query['refund_order_num'] = request.refund_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/refund/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_detail_with_options_async(
        self,
        request: main_models.RefundDetailRequest,
        headers: main_models.RefundDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RefundDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.refund_order_num):
            query['refund_order_num'] = request.refund_order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/refund/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_detail(
        self,
        request: main_models.RefundDetailRequest,
    ) -> main_models.RefundDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.RefundDetailHeaders()
        return self.refund_detail_with_options(request, headers, runtime)

    async def refund_detail_async(
        self,
        request: main_models.RefundDetailRequest,
    ) -> main_models.RefundDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.RefundDetailHeaders()
        return await self.refund_detail_with_options_async(request, headers, runtime)

    def refund_detail_list_with_options(
        self,
        request: main_models.RefundDetailListRequest,
        headers: main_models.RefundDetailListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RefundDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_num):
            query['order_num'] = request.order_num
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.refund_create_begin_time):
            query['refund_create_begin_time'] = request.refund_create_begin_time
        if not DaraCore.is_null(request.refund_create_end_time):
            query['refund_create_end_time'] = request.refund_create_end_time
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundDetailList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/refund/detail-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_detail_list_with_options_async(
        self,
        request: main_models.RefundDetailListRequest,
        headers: main_models.RefundDetailListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RefundDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_num):
            query['order_num'] = request.order_num
        if not DaraCore.is_null(request.page_index):
            query['page_index'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.refund_create_begin_time):
            query['refund_create_begin_time'] = request.refund_create_begin_time
        if not DaraCore.is_null(request.refund_create_end_time):
            query['refund_create_end_time'] = request.refund_create_end_time
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundDetailList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/refund/detail-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_detail_list(
        self,
        request: main_models.RefundDetailListRequest,
    ) -> main_models.RefundDetailListResponse:
        runtime = RuntimeOptions()
        headers = main_models.RefundDetailListHeaders()
        return self.refund_detail_list_with_options(request, headers, runtime)

    async def refund_detail_list_async(
        self,
        request: main_models.RefundDetailListRequest,
    ) -> main_models.RefundDetailListResponse:
        runtime = RuntimeOptions()
        headers = main_models.RefundDetailListHeaders()
        return await self.refund_detail_list_with_options_async(request, headers, runtime)

    def search_with_options(
        self,
        tmp_req: main_models.SearchRequest,
        headers: main_models.SearchHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SearchResponse:
        tmp_req.validate()
        request = main_models.SearchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.air_legs):
            request.air_legs_shrink = Utils.array_to_string_with_specified_style(tmp_req.air_legs, 'air_legs', 'json')
        if not DaraCore.is_null(tmp_req.search_control_options):
            request.search_control_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_control_options, 'search_control_options', 'json')
        body = {}
        if not DaraCore.is_null(request.adults):
            body['adults'] = request.adults
        if not DaraCore.is_null(request.air_legs_shrink):
            body['air_legs'] = request.air_legs_shrink
        if not DaraCore.is_null(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not DaraCore.is_null(request.children):
            body['children'] = request.children
        if not DaraCore.is_null(request.infants):
            body['infants'] = request.infants
        if not DaraCore.is_null(request.search_control_options_shrink):
            body['search_control_options'] = request.search_control_options_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Search',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_with_options_async(
        self,
        tmp_req: main_models.SearchRequest,
        headers: main_models.SearchHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SearchResponse:
        tmp_req.validate()
        request = main_models.SearchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.air_legs):
            request.air_legs_shrink = Utils.array_to_string_with_specified_style(tmp_req.air_legs, 'air_legs', 'json')
        if not DaraCore.is_null(tmp_req.search_control_options):
            request.search_control_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_control_options, 'search_control_options', 'json')
        body = {}
        if not DaraCore.is_null(request.adults):
            body['adults'] = request.adults
        if not DaraCore.is_null(request.air_legs_shrink):
            body['air_legs'] = request.air_legs_shrink
        if not DaraCore.is_null(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not DaraCore.is_null(request.children):
            body['children'] = request.children
        if not DaraCore.is_null(request.infants):
            body['infants'] = request.infants
        if not DaraCore.is_null(request.search_control_options_shrink):
            body['search_control_options'] = request.search_control_options_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Search',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search(
        self,
        request: main_models.SearchRequest,
    ) -> main_models.SearchResponse:
        runtime = RuntimeOptions()
        headers = main_models.SearchHeaders()
        return self.search_with_options(request, headers, runtime)

    async def search_async(
        self,
        request: main_models.SearchRequest,
    ) -> main_models.SearchResponse:
        runtime = RuntimeOptions()
        headers = main_models.SearchHeaders()
        return await self.search_with_options_async(request, headers, runtime)

    def standard_search_with_options(
        self,
        tmp_req: main_models.StandardSearchRequest,
        headers: main_models.StandardSearchHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StandardSearchResponse:
        tmp_req.validate()
        request = main_models.StandardSearchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.air_legs):
            request.air_legs_shrink = Utils.array_to_string_with_specified_style(tmp_req.air_legs, 'air_legs', 'json')
        if not DaraCore.is_null(tmp_req.search_control_options):
            request.search_control_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_control_options, 'search_control_options', 'json')
        body = {}
        if not DaraCore.is_null(request.adults):
            body['adults'] = request.adults
        if not DaraCore.is_null(request.air_legs_shrink):
            body['air_legs'] = request.air_legs_shrink
        if not DaraCore.is_null(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not DaraCore.is_null(request.children):
            body['children'] = request.children
        if not DaraCore.is_null(request.infants):
            body['infants'] = request.infants
        if not DaraCore.is_null(request.search_control_options_shrink):
            body['search_control_options'] = request.search_control_options_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StandardSearch',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-standardsearch',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StandardSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def standard_search_with_options_async(
        self,
        tmp_req: main_models.StandardSearchRequest,
        headers: main_models.StandardSearchHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StandardSearchResponse:
        tmp_req.validate()
        request = main_models.StandardSearchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.air_legs):
            request.air_legs_shrink = Utils.array_to_string_with_specified_style(tmp_req.air_legs, 'air_legs', 'json')
        if not DaraCore.is_null(tmp_req.search_control_options):
            request.search_control_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_control_options, 'search_control_options', 'json')
        body = {}
        if not DaraCore.is_null(request.adults):
            body['adults'] = request.adults
        if not DaraCore.is_null(request.air_legs_shrink):
            body['air_legs'] = request.air_legs_shrink
        if not DaraCore.is_null(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not DaraCore.is_null(request.children):
            body['children'] = request.children
        if not DaraCore.is_null(request.infants):
            body['infants'] = request.infants
        if not DaraCore.is_null(request.search_control_options_shrink):
            body['search_control_options'] = request.search_control_options_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StandardSearch',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-standardsearch',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StandardSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def standard_search(
        self,
        request: main_models.StandardSearchRequest,
    ) -> main_models.StandardSearchResponse:
        runtime = RuntimeOptions()
        headers = main_models.StandardSearchHeaders()
        return self.standard_search_with_options(request, headers, runtime)

    async def standard_search_async(
        self,
        request: main_models.StandardSearchRequest,
    ) -> main_models.StandardSearchResponse:
        runtime = RuntimeOptions()
        headers = main_models.StandardSearchHeaders()
        return await self.standard_search_with_options_async(request, headers, runtime)

    def ticket_apply_refund_with_options(
        self,
        request: main_models.TicketApplyRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketApplyRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        if not DaraCore.is_null(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.refund_remark):
            body['RefundRemark'] = request.refund_remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketApplyRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketApplyRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketApplyRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_apply_refund_with_options_async(
        self,
        request: main_models.TicketApplyRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketApplyRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        if not DaraCore.is_null(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.refund_remark):
            body['RefundRemark'] = request.refund_remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketApplyRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketApplyRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketApplyRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_apply_refund(
        self,
        request: main_models.TicketApplyRefundRequest,
    ) -> main_models.TicketApplyRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_apply_refund_with_options(request, headers, runtime)

    async def ticket_apply_refund_async(
        self,
        request: main_models.TicketApplyRefundRequest,
    ) -> main_models.TicketApplyRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_apply_refund_with_options_async(request, headers, runtime)

    def ticket_cancel_order_with_options(
        self,
        request: main_models.TicketCancelOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketCancelOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketCancelOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketCancelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketCancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_cancel_order_with_options_async(
        self,
        request: main_models.TicketCancelOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketCancelOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketCancelOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketCancelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketCancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_cancel_order(
        self,
        request: main_models.TicketCancelOrderRequest,
    ) -> main_models.TicketCancelOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_cancel_order_with_options(request, headers, runtime)

    async def ticket_cancel_order_async(
        self,
        request: main_models.TicketCancelOrderRequest,
    ) -> main_models.TicketCancelOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_cancel_order_with_options_async(request, headers, runtime)

    def ticket_check_refund_with_options(
        self,
        request: main_models.TicketCheckRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketCheckRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        if not DaraCore.is_null(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.refund_remark):
            body['RefundRemark'] = request.refund_remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketCheckRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketCheckRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketCheckRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_check_refund_with_options_async(
        self,
        request: main_models.TicketCheckRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketCheckRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        if not DaraCore.is_null(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.refund_remark):
            body['RefundRemark'] = request.refund_remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketCheckRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketCheckRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketCheckRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_check_refund(
        self,
        request: main_models.TicketCheckRefundRequest,
    ) -> main_models.TicketCheckRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_check_refund_with_options(request, headers, runtime)

    async def ticket_check_refund_async(
        self,
        request: main_models.TicketCheckRefundRequest,
    ) -> main_models.TicketCheckRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_check_refund_with_options_async(request, headers, runtime)

    def ticket_create_order_with_options(
        self,
        tmp_req: main_models.TicketCreateOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketCreateOrderResponse:
        tmp_req.validate()
        request = main_models.TicketCreateOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.order_product):
            request.order_product_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_product, 'OrderProduct', 'json')
        if not DaraCore.is_null(tmp_req.total_distribution_price):
            request.total_distribution_price_shrink = Utils.array_to_string_with_specified_style(tmp_req.total_distribution_price, 'TotalDistributionPrice', 'json')
        if not DaraCore.is_null(tmp_req.travelers):
            request.travelers_shrink = Utils.array_to_string_with_specified_style(tmp_req.travelers, 'Travelers', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        if not DaraCore.is_null(request.order_product_shrink):
            body['OrderProduct'] = request.order_product_shrink
        if not DaraCore.is_null(request.quantity):
            body['Quantity'] = request.quantity
        if not DaraCore.is_null(request.total_distribution_price_shrink):
            body['TotalDistributionPrice'] = request.total_distribution_price_shrink
        if not DaraCore.is_null(request.travelers_shrink):
            body['Travelers'] = request.travelers_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketCreateOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketCreateOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketCreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_create_order_with_options_async(
        self,
        tmp_req: main_models.TicketCreateOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketCreateOrderResponse:
        tmp_req.validate()
        request = main_models.TicketCreateOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.order_product):
            request.order_product_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_product, 'OrderProduct', 'json')
        if not DaraCore.is_null(tmp_req.total_distribution_price):
            request.total_distribution_price_shrink = Utils.array_to_string_with_specified_style(tmp_req.total_distribution_price, 'TotalDistributionPrice', 'json')
        if not DaraCore.is_null(tmp_req.travelers):
            request.travelers_shrink = Utils.array_to_string_with_specified_style(tmp_req.travelers, 'Travelers', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        if not DaraCore.is_null(request.order_product_shrink):
            body['OrderProduct'] = request.order_product_shrink
        if not DaraCore.is_null(request.quantity):
            body['Quantity'] = request.quantity
        if not DaraCore.is_null(request.total_distribution_price_shrink):
            body['TotalDistributionPrice'] = request.total_distribution_price_shrink
        if not DaraCore.is_null(request.travelers_shrink):
            body['Travelers'] = request.travelers_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketCreateOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketCreateOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketCreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_create_order(
        self,
        request: main_models.TicketCreateOrderRequest,
    ) -> main_models.TicketCreateOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_create_order_with_options(request, headers, runtime)

    async def ticket_create_order_async(
        self,
        request: main_models.TicketCreateOrderRequest,
    ) -> main_models.TicketCreateOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_create_order_with_options_async(request, headers, runtime)

    def ticket_page_query_product_with_options(
        self,
        request: main_models.TicketPageQueryProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketPageQueryProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scenic_id):
            body['ScenicId'] = request.scenic_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketPageQueryProduct',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketPageQueryProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketPageQueryProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_page_query_product_with_options_async(
        self,
        request: main_models.TicketPageQueryProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketPageQueryProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scenic_id):
            body['ScenicId'] = request.scenic_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketPageQueryProduct',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketPageQueryProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketPageQueryProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_page_query_product(
        self,
        request: main_models.TicketPageQueryProductRequest,
    ) -> main_models.TicketPageQueryProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_page_query_product_with_options(request, headers, runtime)

    async def ticket_page_query_product_async(
        self,
        request: main_models.TicketPageQueryProductRequest,
    ) -> main_models.TicketPageQueryProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_page_query_product_with_options_async(request, headers, runtime)

    def ticket_page_query_scenic_with_options(
        self,
        request: main_models.TicketPageQueryScenicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketPageQueryScenicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketPageQueryScenic',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketPageQueryScenic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketPageQueryScenicResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_page_query_scenic_with_options_async(
        self,
        request: main_models.TicketPageQueryScenicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketPageQueryScenicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketPageQueryScenic',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketPageQueryScenic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketPageQueryScenicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_page_query_scenic(
        self,
        request: main_models.TicketPageQueryScenicRequest,
    ) -> main_models.TicketPageQueryScenicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_page_query_scenic_with_options(request, headers, runtime)

    async def ticket_page_query_scenic_async(
        self,
        request: main_models.TicketPageQueryScenicRequest,
    ) -> main_models.TicketPageQueryScenicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_page_query_scenic_with_options_async(request, headers, runtime)

    def ticket_pay_order_with_options(
        self,
        request: main_models.TicketPayOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketPayOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketPayOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketPayOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_pay_order_with_options_async(
        self,
        request: main_models.TicketPayOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketPayOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketPayOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketPayOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_pay_order(
        self,
        request: main_models.TicketPayOrderRequest,
    ) -> main_models.TicketPayOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_pay_order_with_options(request, headers, runtime)

    async def ticket_pay_order_async(
        self,
        request: main_models.TicketPayOrderRequest,
    ) -> main_models.TicketPayOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_pay_order_with_options_async(request, headers, runtime)

    def ticket_query_order_with_options(
        self,
        request: main_models.TicketQueryOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_query_order_with_options_async(
        self,
        request: main_models.TicketQueryOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_query_order(
        self,
        request: main_models.TicketQueryOrderRequest,
    ) -> main_models.TicketQueryOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_query_order_with_options(request, headers, runtime)

    async def ticket_query_order_async(
        self,
        request: main_models.TicketQueryOrderRequest,
    ) -> main_models.TicketQueryOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_query_order_with_options_async(request, headers, runtime)

    def ticket_query_price_stock_with_options(
        self,
        request: main_models.TicketQueryPriceStockRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryPriceStockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryPriceStock',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryPriceStock',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryPriceStockResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_query_price_stock_with_options_async(
        self,
        request: main_models.TicketQueryPriceStockRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryPriceStockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryPriceStock',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryPriceStock',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryPriceStockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_query_price_stock(
        self,
        request: main_models.TicketQueryPriceStockRequest,
    ) -> main_models.TicketQueryPriceStockResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_query_price_stock_with_options(request, headers, runtime)

    async def ticket_query_price_stock_async(
        self,
        request: main_models.TicketQueryPriceStockRequest,
    ) -> main_models.TicketQueryPriceStockResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_query_price_stock_with_options_async(request, headers, runtime)

    def ticket_query_product_with_options(
        self,
        request: main_models.TicketQueryProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryProduct',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_query_product_with_options_async(
        self,
        request: main_models.TicketQueryProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryProduct',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_query_product(
        self,
        request: main_models.TicketQueryProductRequest,
    ) -> main_models.TicketQueryProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_query_product_with_options(request, headers, runtime)

    async def ticket_query_product_async(
        self,
        request: main_models.TicketQueryProductRequest,
    ) -> main_models.TicketQueryProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_query_product_with_options_async(request, headers, runtime)

    def ticket_query_refund_order_with_options(
        self,
        request: main_models.TicketQueryRefundOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryRefundOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryRefundOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryRefundOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_query_refund_order_with_options_async(
        self,
        request: main_models.TicketQueryRefundOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryRefundOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.distributor_order_id):
            body['DistributorOrderId'] = request.distributor_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryRefundOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryRefundOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_query_refund_order(
        self,
        request: main_models.TicketQueryRefundOrderRequest,
    ) -> main_models.TicketQueryRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_query_refund_order_with_options(request, headers, runtime)

    async def ticket_query_refund_order_async(
        self,
        request: main_models.TicketQueryRefundOrderRequest,
    ) -> main_models.TicketQueryRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_query_refund_order_with_options_async(request, headers, runtime)

    def ticket_query_scenic_with_options(
        self,
        request: main_models.TicketQueryScenicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryScenicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.scenic_id):
            body['ScenicId'] = request.scenic_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryScenic',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryScenic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryScenicResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_query_scenic_with_options_async(
        self,
        request: main_models.TicketQueryScenicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryScenicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.scenic_id):
            body['ScenicId'] = request.scenic_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryScenic',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryScenic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryScenicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_query_scenic(
        self,
        request: main_models.TicketQueryScenicRequest,
    ) -> main_models.TicketQueryScenicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_query_scenic_with_options(request, headers, runtime)

    async def ticket_query_scenic_async(
        self,
        request: main_models.TicketQueryScenicRequest,
    ) -> main_models.TicketQueryScenicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_query_scenic_with_options_async(request, headers, runtime)

    def ticket_query_shelf_with_options(
        self,
        request: main_models.TicketQueryShelfRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryShelfResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.scenic_id):
            body['ScenicId'] = request.scenic_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryShelf',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryShelf',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryShelfResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticket_query_shelf_with_options_async(
        self,
        request: main_models.TicketQueryShelfRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TicketQueryShelfResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.scenic_id):
            body['ScenicId'] = request.scenic_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketQueryShelf',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/TicketQueryShelf',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketQueryShelfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticket_query_shelf(
        self,
        request: main_models.TicketQueryShelfRequest,
    ) -> main_models.TicketQueryShelfResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ticket_query_shelf_with_options(request, headers, runtime)

    async def ticket_query_shelf_async(
        self,
        request: main_models.TicketQueryShelfRequest,
    ) -> main_models.TicketQueryShelfResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ticket_query_shelf_with_options_async(request, headers, runtime)

    def ticketing_with_options(
        self,
        request: main_models.TicketingRequest,
        headers: main_models.TicketingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.TicketingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Ticketing',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-ticketing',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketingResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticketing_with_options_async(
        self,
        request: main_models.TicketingRequest,
        headers: main_models.TicketingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.TicketingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Ticketing',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-ticketing',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticketing(
        self,
        request: main_models.TicketingRequest,
    ) -> main_models.TicketingResponse:
        runtime = RuntimeOptions()
        headers = main_models.TicketingHeaders()
        return self.ticketing_with_options(request, headers, runtime)

    async def ticketing_async(
        self,
        request: main_models.TicketingRequest,
    ) -> main_models.TicketingResponse:
        runtime = RuntimeOptions()
        headers = main_models.TicketingHeaders()
        return await self.ticketing_with_options_async(request, headers, runtime)

    def ticketing_check_with_options(
        self,
        request: main_models.TicketingCheckRequest,
        headers: main_models.TicketingCheckHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.TicketingCheckResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketingCheck',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-ticketing-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketingCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticketing_check_with_options_async(
        self,
        request: main_models.TicketingCheckRequest,
        headers: main_models.TicketingCheckHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.TicketingCheckResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TicketingCheck',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/trade/action-ticketing-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TicketingCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticketing_check(
        self,
        request: main_models.TicketingCheckRequest,
    ) -> main_models.TicketingCheckResponse:
        runtime = RuntimeOptions()
        headers = main_models.TicketingCheckHeaders()
        return self.ticketing_check_with_options(request, headers, runtime)

    async def ticketing_check_async(
        self,
        request: main_models.TicketingCheckRequest,
    ) -> main_models.TicketingCheckResponse:
        runtime = RuntimeOptions()
        headers = main_models.TicketingCheckHeaders()
        return await self.ticketing_check_with_options_async(request, headers, runtime)

    def transit_visa_with_options(
        self,
        tmp_req: main_models.TransitVisaRequest,
        headers: main_models.TransitVisaHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.TransitVisaResponse:
        tmp_req.validate()
        request = main_models.TransitVisaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.flight_segment_param_list):
            request.flight_segment_param_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.flight_segment_param_list, 'flight_segment_param_list', 'json')
        query = {}
        if not DaraCore.is_null(request.flight_segment_param_list_shrink):
            query['flight_segment_param_list'] = request.flight_segment_param_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransitVisa',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/flight-data/transit-visa',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransitVisaResponse(),
            self.call_api(params, req, runtime)
        )

    async def transit_visa_with_options_async(
        self,
        tmp_req: main_models.TransitVisaRequest,
        headers: main_models.TransitVisaHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.TransitVisaResponse:
        tmp_req.validate()
        request = main_models.TransitVisaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.flight_segment_param_list):
            request.flight_segment_param_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.flight_segment_param_list, 'flight_segment_param_list', 'json')
        query = {}
        if not DaraCore.is_null(request.flight_segment_param_list_shrink):
            query['flight_segment_param_list'] = request.flight_segment_param_list_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = str(headers.x_acs_airticket_access_token)
        if not DaraCore.is_null(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = str(headers.x_acs_airticket_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransitVisa',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/airticket/v1/flight-data/transit-visa',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransitVisaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transit_visa(
        self,
        request: main_models.TransitVisaRequest,
    ) -> main_models.TransitVisaResponse:
        runtime = RuntimeOptions()
        headers = main_models.TransitVisaHeaders()
        return self.transit_visa_with_options(request, headers, runtime)

    async def transit_visa_async(
        self,
        request: main_models.TransitVisaRequest,
    ) -> main_models.TransitVisaResponse:
        runtime = RuntimeOptions()
        headers = main_models.TransitVisaHeaders()
        return await self.transit_visa_with_options_async(request, headers, runtime)

    def apply_refund_with_options(
        self,
        request: main_models.ApplyRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'applyRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/applyRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_refund_with_options_async(
        self,
        request: main_models.ApplyRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'applyRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/applyRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_refund(
        self,
        request: main_models.ApplyRefundRequest,
    ) -> main_models.ApplyRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.apply_refund_with_options(request, headers, runtime)

    async def apply_refund_async(
        self,
        request: main_models.ApplyRefundRequest,
    ) -> main_models.ApplyRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.apply_refund_with_options_async(request, headers, runtime)

    def batch_get_hotel_detail_with_options(
        self,
        tmp_req: main_models.BatchGetHotelDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetHotelDetailResponse:
        tmp_req.validate()
        request = main_models.BatchGetHotelDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'batchGetHotelDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/batchGetHotelDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetHotelDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_hotel_detail_with_options_async(
        self,
        tmp_req: main_models.BatchGetHotelDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetHotelDetailResponse:
        tmp_req.validate()
        request = main_models.BatchGetHotelDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'batchGetHotelDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/batchGetHotelDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetHotelDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_hotel_detail(
        self,
        request: main_models.BatchGetHotelDetailRequest,
    ) -> main_models.BatchGetHotelDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_get_hotel_detail_with_options(request, headers, runtime)

    async def batch_get_hotel_detail_async(
        self,
        request: main_models.BatchGetHotelDetailRequest,
    ) -> main_models.BatchGetHotelDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_get_hotel_detail_with_options_async(request, headers, runtime)

    def cancel_or_refund_with_options(
        self,
        request: main_models.CancelOrRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'cancelOrRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/cancelOrRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_or_refund_with_options_async(
        self,
        request: main_models.CancelOrRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'cancelOrRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/cancelOrRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_or_refund(
        self,
        request: main_models.CancelOrRefundRequest,
    ) -> main_models.CancelOrRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_or_refund_with_options(request, headers, runtime)

    async def cancel_or_refund_async(
        self,
        request: main_models.CancelOrRefundRequest,
    ) -> main_models.CancelOrRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_or_refund_with_options_async(request, headers, runtime)

    def cancel_order_with_options(
        self,
        request: main_models.CancelOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'cancelOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/cancelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: main_models.CancelOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'cancelOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/cancelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order(
        self,
        request: main_models.CancelOrderRequest,
    ) -> main_models.CancelOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_order_with_options(request, headers, runtime)

    async def cancel_order_async(
        self,
        request: main_models.CancelOrderRequest,
    ) -> main_models.CancelOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_order_with_options_async(request, headers, runtime)

    def create_and_pay_with_options(
        self,
        tmp_req: main_models.CreateAndPayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndPayResponse:
        tmp_req.validate()
        request = main_models.CreateAndPayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.guests):
            request.guests_shrink = Utils.array_to_string_with_specified_style(tmp_req.guests, 'Guests', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.guests_shrink):
            body['Guests'] = request.guests_shrink
        if not DaraCore.is_null(request.item_offer_id):
            body['ItemOfferId'] = request.item_offer_id
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'createAndPay',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/createAndPay',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndPayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_pay_with_options_async(
        self,
        tmp_req: main_models.CreateAndPayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndPayResponse:
        tmp_req.validate()
        request = main_models.CreateAndPayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.guests):
            request.guests_shrink = Utils.array_to_string_with_specified_style(tmp_req.guests, 'Guests', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.guests_shrink):
            body['Guests'] = request.guests_shrink
        if not DaraCore.is_null(request.item_offer_id):
            body['ItemOfferId'] = request.item_offer_id
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'createAndPay',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/createAndPay',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndPayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_pay(
        self,
        request: main_models.CreateAndPayRequest,
    ) -> main_models.CreateAndPayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_and_pay_with_options(request, headers, runtime)

    async def create_and_pay_async(
        self,
        request: main_models.CreateAndPayRequest,
    ) -> main_models.CreateAndPayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_and_pay_with_options_async(request, headers, runtime)

    def create_order_with_options(
        self,
        tmp_req: main_models.CreateOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrderResponse:
        tmp_req.validate()
        request = main_models.CreateOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.guests):
            request.guests_shrink = Utils.array_to_string_with_specified_style(tmp_req.guests, 'Guests', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.guests_shrink):
            body['Guests'] = request.guests_shrink
        if not DaraCore.is_null(request.item_offer_id):
            body['ItemOfferId'] = request.item_offer_id
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'createOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/createOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        tmp_req: main_models.CreateOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrderResponse:
        tmp_req.validate()
        request = main_models.CreateOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.guests):
            request.guests_shrink = Utils.array_to_string_with_specified_style(tmp_req.guests, 'Guests', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.guests_shrink):
            body['Guests'] = request.guests_shrink
        if not DaraCore.is_null(request.item_offer_id):
            body['ItemOfferId'] = request.item_offer_id
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'createOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/createOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order(
        self,
        request: main_models.CreateOrderRequest,
    ) -> main_models.CreateOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_order_with_options(request, headers, runtime)

    async def create_order_async(
        self,
        request: main_models.CreateOrderRequest,
    ) -> main_models.CreateOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_order_with_options_async(request, headers, runtime)

    def global_hotel_apply_refund_with_options(
        self,
        request: main_models.GlobalHotelApplyRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelApplyRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelApplyRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelApplyRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelApplyRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_apply_refund_with_options_async(
        self,
        request: main_models.GlobalHotelApplyRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelApplyRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelApplyRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelApplyRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelApplyRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_apply_refund(
        self,
        request: main_models.GlobalHotelApplyRefundRequest,
    ) -> main_models.GlobalHotelApplyRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_apply_refund_with_options(request, headers, runtime)

    async def global_hotel_apply_refund_async(
        self,
        request: main_models.GlobalHotelApplyRefundRequest,
    ) -> main_models.GlobalHotelApplyRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_apply_refund_with_options_async(request, headers, runtime)

    def global_hotel_batch_get_hotel_detail_with_options(
        self,
        tmp_req: main_models.GlobalHotelBatchGetHotelDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelBatchGetHotelDetailResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelBatchGetHotelDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelBatchGetHotelDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelBatchGetHotelDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelBatchGetHotelDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_batch_get_hotel_detail_with_options_async(
        self,
        tmp_req: main_models.GlobalHotelBatchGetHotelDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelBatchGetHotelDetailResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelBatchGetHotelDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelBatchGetHotelDetail',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelBatchGetHotelDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelBatchGetHotelDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_batch_get_hotel_detail(
        self,
        request: main_models.GlobalHotelBatchGetHotelDetailRequest,
    ) -> main_models.GlobalHotelBatchGetHotelDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_batch_get_hotel_detail_with_options(request, headers, runtime)

    async def global_hotel_batch_get_hotel_detail_async(
        self,
        request: main_models.GlobalHotelBatchGetHotelDetailRequest,
    ) -> main_models.GlobalHotelBatchGetHotelDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_batch_get_hotel_detail_with_options_async(request, headers, runtime)

    def global_hotel_cancel_or_refund_with_options(
        self,
        request: main_models.GlobalHotelCancelOrRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelCancelOrRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelCancelOrRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelCancelOrRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelCancelOrRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_cancel_or_refund_with_options_async(
        self,
        request: main_models.GlobalHotelCancelOrRefundRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelCancelOrRefundResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelCancelOrRefund',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelCancelOrRefund',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelCancelOrRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_cancel_or_refund(
        self,
        request: main_models.GlobalHotelCancelOrRefundRequest,
    ) -> main_models.GlobalHotelCancelOrRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_cancel_or_refund_with_options(request, headers, runtime)

    async def global_hotel_cancel_or_refund_async(
        self,
        request: main_models.GlobalHotelCancelOrRefundRequest,
    ) -> main_models.GlobalHotelCancelOrRefundResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_cancel_or_refund_with_options_async(request, headers, runtime)

    def global_hotel_cancel_order_with_options(
        self,
        request: main_models.GlobalHotelCancelOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelCancelOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelCancelOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelCancelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelCancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_cancel_order_with_options_async(
        self,
        request: main_models.GlobalHotelCancelOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelCancelOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelCancelOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelCancelOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelCancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_cancel_order(
        self,
        request: main_models.GlobalHotelCancelOrderRequest,
    ) -> main_models.GlobalHotelCancelOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_cancel_order_with_options(request, headers, runtime)

    async def global_hotel_cancel_order_async(
        self,
        request: main_models.GlobalHotelCancelOrderRequest,
    ) -> main_models.GlobalHotelCancelOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_cancel_order_with_options_async(request, headers, runtime)

    def global_hotel_create_and_pay_with_options(
        self,
        tmp_req: main_models.GlobalHotelCreateAndPayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelCreateAndPayResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelCreateAndPayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.guests):
            request.guests_shrink = Utils.array_to_string_with_specified_style(tmp_req.guests, 'Guests', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.guests_shrink):
            body['Guests'] = request.guests_shrink
        if not DaraCore.is_null(request.item_offer_id):
            body['ItemOfferId'] = request.item_offer_id
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelCreateAndPay',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelCreateAndPay',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelCreateAndPayResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_create_and_pay_with_options_async(
        self,
        tmp_req: main_models.GlobalHotelCreateAndPayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelCreateAndPayResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelCreateAndPayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.guests):
            request.guests_shrink = Utils.array_to_string_with_specified_style(tmp_req.guests, 'Guests', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.guests_shrink):
            body['Guests'] = request.guests_shrink
        if not DaraCore.is_null(request.item_offer_id):
            body['ItemOfferId'] = request.item_offer_id
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelCreateAndPay',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelCreateAndPay',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelCreateAndPayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_create_and_pay(
        self,
        request: main_models.GlobalHotelCreateAndPayRequest,
    ) -> main_models.GlobalHotelCreateAndPayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_create_and_pay_with_options(request, headers, runtime)

    async def global_hotel_create_and_pay_async(
        self,
        request: main_models.GlobalHotelCreateAndPayRequest,
    ) -> main_models.GlobalHotelCreateAndPayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_create_and_pay_with_options_async(request, headers, runtime)

    def global_hotel_create_order_with_options(
        self,
        tmp_req: main_models.GlobalHotelCreateOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelCreateOrderResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelCreateOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.guests):
            request.guests_shrink = Utils.array_to_string_with_specified_style(tmp_req.guests, 'Guests', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.guests_shrink):
            body['Guests'] = request.guests_shrink
        if not DaraCore.is_null(request.item_offer_id):
            body['ItemOfferId'] = request.item_offer_id
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelCreateOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelCreateOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelCreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_create_order_with_options_async(
        self,
        tmp_req: main_models.GlobalHotelCreateOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelCreateOrderResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelCreateOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact):
            request.contact_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact, 'Contact', 'json')
        if not DaraCore.is_null(tmp_req.guests):
            request.guests_shrink = Utils.array_to_string_with_specified_style(tmp_req.guests, 'Guests', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.contact_shrink):
            body['Contact'] = request.contact_shrink
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.guests_shrink):
            body['Guests'] = request.guests_shrink
        if not DaraCore.is_null(request.item_offer_id):
            body['ItemOfferId'] = request.item_offer_id
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelCreateOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelCreateOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelCreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_create_order(
        self,
        request: main_models.GlobalHotelCreateOrderRequest,
    ) -> main_models.GlobalHotelCreateOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_create_order_with_options(request, headers, runtime)

    async def global_hotel_create_order_async(
        self,
        request: main_models.GlobalHotelCreateOrderRequest,
    ) -> main_models.GlobalHotelCreateOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_create_order_with_options_async(request, headers, runtime)

    def global_hotel_pay_with_options(
        self,
        request: main_models.GlobalHotelPayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelPayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelPay',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelPay',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelPayResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_pay_with_options_async(
        self,
        request: main_models.GlobalHotelPayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelPayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelPay',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelPay',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelPayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_pay(
        self,
        request: main_models.GlobalHotelPayRequest,
    ) -> main_models.GlobalHotelPayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_pay_with_options(request, headers, runtime)

    async def global_hotel_pay_async(
        self,
        request: main_models.GlobalHotelPayRequest,
    ) -> main_models.GlobalHotelPayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_pay_with_options_async(request, headers, runtime)

    def global_hotel_query_availability_with_options(
        self,
        tmp_req: main_models.GlobalHotelQueryAvailabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelQueryAvailabilityResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelQueryAvailabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adult_count):
            body['AdultCount'] = request.adult_count
        if not DaraCore.is_null(request.check_in_date):
            body['CheckInDate'] = request.check_in_date
        if not DaraCore.is_null(request.check_out_date):
            body['CheckOutDate'] = request.check_out_date
        if not DaraCore.is_null(request.child_count):
            body['ChildCount'] = request.child_count
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelQueryAvailability',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelQueryAvailability',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelQueryAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_query_availability_with_options_async(
        self,
        tmp_req: main_models.GlobalHotelQueryAvailabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelQueryAvailabilityResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelQueryAvailabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adult_count):
            body['AdultCount'] = request.adult_count
        if not DaraCore.is_null(request.check_in_date):
            body['CheckInDate'] = request.check_in_date
        if not DaraCore.is_null(request.check_out_date):
            body['CheckOutDate'] = request.check_out_date
        if not DaraCore.is_null(request.child_count):
            body['ChildCount'] = request.child_count
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelQueryAvailability',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelQueryAvailability',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelQueryAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_query_availability(
        self,
        request: main_models.GlobalHotelQueryAvailabilityRequest,
    ) -> main_models.GlobalHotelQueryAvailabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_query_availability_with_options(request, headers, runtime)

    async def global_hotel_query_availability_async(
        self,
        request: main_models.GlobalHotelQueryAvailabilityRequest,
    ) -> main_models.GlobalHotelQueryAvailabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_query_availability_with_options_async(request, headers, runtime)

    def global_hotel_query_calendar_availability_with_options(
        self,
        tmp_req: main_models.GlobalHotelQueryCalendarAvailabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelQueryCalendarAvailabilityResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelQueryCalendarAvailabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adult_count):
            body['AdultCount'] = request.adult_count
        if not DaraCore.is_null(request.check_in_date_end):
            body['CheckInDateEnd'] = request.check_in_date_end
        if not DaraCore.is_null(request.check_in_date_start):
            body['CheckInDateStart'] = request.check_in_date_start
        if not DaraCore.is_null(request.child_count):
            body['ChildCount'] = request.child_count
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelQueryCalendarAvailability',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelQueryCalendarAvailability',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelQueryCalendarAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_query_calendar_availability_with_options_async(
        self,
        tmp_req: main_models.GlobalHotelQueryCalendarAvailabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelQueryCalendarAvailabilityResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelQueryCalendarAvailabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adult_count):
            body['AdultCount'] = request.adult_count
        if not DaraCore.is_null(request.check_in_date_end):
            body['CheckInDateEnd'] = request.check_in_date_end
        if not DaraCore.is_null(request.check_in_date_start):
            body['CheckInDateStart'] = request.check_in_date_start
        if not DaraCore.is_null(request.child_count):
            body['ChildCount'] = request.child_count
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelQueryCalendarAvailability',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelQueryCalendarAvailability',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelQueryCalendarAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_query_calendar_availability(
        self,
        request: main_models.GlobalHotelQueryCalendarAvailabilityRequest,
    ) -> main_models.GlobalHotelQueryCalendarAvailabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_query_calendar_availability_with_options(request, headers, runtime)

    async def global_hotel_query_calendar_availability_async(
        self,
        request: main_models.GlobalHotelQueryCalendarAvailabilityRequest,
    ) -> main_models.GlobalHotelQueryCalendarAvailabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_query_calendar_availability_with_options_async(request, headers, runtime)

    def global_hotel_query_order_with_options(
        self,
        request: main_models.GlobalHotelQueryOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelQueryOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelQueryOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelQueryOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelQueryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_query_order_with_options_async(
        self,
        request: main_models.GlobalHotelQueryOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelQueryOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelQueryOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelQueryOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelQueryOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_query_order(
        self,
        request: main_models.GlobalHotelQueryOrderRequest,
    ) -> main_models.GlobalHotelQueryOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_query_order_with_options(request, headers, runtime)

    async def global_hotel_query_order_async(
        self,
        request: main_models.GlobalHotelQueryOrderRequest,
    ) -> main_models.GlobalHotelQueryOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_query_order_with_options_async(request, headers, runtime)

    def global_hotel_search_city_page_with_options(
        self,
        request: main_models.GlobalHotelSearchCityPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelSearchCityPageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.count):
            body['Count'] = request.count
        if not DaraCore.is_null(request.country_code):
            body['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelSearchCityPage',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelSearchCityPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelSearchCityPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_search_city_page_with_options_async(
        self,
        request: main_models.GlobalHotelSearchCityPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelSearchCityPageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.count):
            body['Count'] = request.count
        if not DaraCore.is_null(request.country_code):
            body['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelSearchCityPage',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelSearchCityPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelSearchCityPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_search_city_page(
        self,
        request: main_models.GlobalHotelSearchCityPageRequest,
    ) -> main_models.GlobalHotelSearchCityPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_search_city_page_with_options(request, headers, runtime)

    async def global_hotel_search_city_page_async(
        self,
        request: main_models.GlobalHotelSearchCityPageRequest,
    ) -> main_models.GlobalHotelSearchCityPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_search_city_page_with_options_async(request, headers, runtime)

    def global_hotel_search_hotel_list_with_options(
        self,
        request: main_models.GlobalHotelSearchHotelListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelSearchHotelListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.city_code):
            body['CityCode'] = request.city_code
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelSearchHotelList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelSearchHotelList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelSearchHotelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_search_hotel_list_with_options_async(
        self,
        request: main_models.GlobalHotelSearchHotelListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelSearchHotelListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.city_code):
            body['CityCode'] = request.city_code
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelSearchHotelList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelSearchHotelList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelSearchHotelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_search_hotel_list(
        self,
        request: main_models.GlobalHotelSearchHotelListRequest,
    ) -> main_models.GlobalHotelSearchHotelListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_search_hotel_list_with_options(request, headers, runtime)

    async def global_hotel_search_hotel_list_async(
        self,
        request: main_models.GlobalHotelSearchHotelListRequest,
    ) -> main_models.GlobalHotelSearchHotelListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_search_hotel_list_with_options_async(request, headers, runtime)

    def global_hotel_validate_price_with_options(
        self,
        tmp_req: main_models.GlobalHotelValidatePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelValidatePriceResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelValidatePriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adults):
            body['Adults'] = request.adults
        if not DaraCore.is_null(request.children):
            body['Children'] = request.children
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.item_offer_key):
            body['ItemOfferKey'] = request.item_offer_key
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelValidatePrice',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelValidatePrice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelValidatePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_hotel_validate_price_with_options_async(
        self,
        tmp_req: main_models.GlobalHotelValidatePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalHotelValidatePriceResponse:
        tmp_req.validate()
        request = main_models.GlobalHotelValidatePriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adults):
            body['Adults'] = request.adults
        if not DaraCore.is_null(request.children):
            body['Children'] = request.children
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.item_offer_key):
            body['ItemOfferKey'] = request.item_offer_key
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'globalHotelValidatePrice',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotelValidatePrice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalHotelValidatePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_hotel_validate_price(
        self,
        request: main_models.GlobalHotelValidatePriceRequest,
    ) -> main_models.GlobalHotelValidatePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_hotel_validate_price_with_options(request, headers, runtime)

    async def global_hotel_validate_price_async(
        self,
        request: main_models.GlobalHotelValidatePriceRequest,
    ) -> main_models.GlobalHotelValidatePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_hotel_validate_price_with_options_async(request, headers, runtime)

    def pay_with_options(
        self,
        request: main_models.PayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'pay',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/pay',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PayResponse(),
            self.call_api(params, req, runtime)
        )

    async def pay_with_options_async(
        self,
        request: main_models.PayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'pay',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/pay',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pay(
        self,
        request: main_models.PayRequest,
    ) -> main_models.PayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.pay_with_options(request, headers, runtime)

    async def pay_async(
        self,
        request: main_models.PayRequest,
    ) -> main_models.PayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.pay_with_options_async(request, headers, runtime)

    def query_availability_with_options(
        self,
        tmp_req: main_models.QueryAvailabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailabilityResponse:
        tmp_req.validate()
        request = main_models.QueryAvailabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adult_count):
            body['AdultCount'] = request.adult_count
        if not DaraCore.is_null(request.check_in_date):
            body['CheckInDate'] = request.check_in_date
        if not DaraCore.is_null(request.check_out_date):
            body['CheckOutDate'] = request.check_out_date
        if not DaraCore.is_null(request.child_count):
            body['ChildCount'] = request.child_count
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'queryAvailability',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/queryAvailability',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_availability_with_options_async(
        self,
        tmp_req: main_models.QueryAvailabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailabilityResponse:
        tmp_req.validate()
        request = main_models.QueryAvailabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adult_count):
            body['AdultCount'] = request.adult_count
        if not DaraCore.is_null(request.check_in_date):
            body['CheckInDate'] = request.check_in_date
        if not DaraCore.is_null(request.check_out_date):
            body['CheckOutDate'] = request.check_out_date
        if not DaraCore.is_null(request.child_count):
            body['ChildCount'] = request.child_count
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'queryAvailability',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/queryAvailability',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_availability(
        self,
        request: main_models.QueryAvailabilityRequest,
    ) -> main_models.QueryAvailabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_availability_with_options(request, headers, runtime)

    async def query_availability_async(
        self,
        request: main_models.QueryAvailabilityRequest,
    ) -> main_models.QueryAvailabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_availability_with_options_async(request, headers, runtime)

    def query_calendar_availability_with_options(
        self,
        tmp_req: main_models.QueryCalendarAvailabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryCalendarAvailabilityResponse:
        tmp_req.validate()
        request = main_models.QueryCalendarAvailabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adult_count):
            body['AdultCount'] = request.adult_count
        if not DaraCore.is_null(request.check_in_date_end):
            body['CheckInDateEnd'] = request.check_in_date_end
        if not DaraCore.is_null(request.check_in_date_start):
            body['CheckInDateStart'] = request.check_in_date_start
        if not DaraCore.is_null(request.child_count):
            body['ChildCount'] = request.child_count
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'queryCalendarAvailability',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/queryCalendarAvailability',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCalendarAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_calendar_availability_with_options_async(
        self,
        tmp_req: main_models.QueryCalendarAvailabilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryCalendarAvailabilityResponse:
        tmp_req.validate()
        request = main_models.QueryCalendarAvailabilityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        if not DaraCore.is_null(tmp_req.standard_hotel_ids):
            request.standard_hotel_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_hotel_ids, 'StandardHotelIds', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adult_count):
            body['AdultCount'] = request.adult_count
        if not DaraCore.is_null(request.check_in_date_end):
            body['CheckInDateEnd'] = request.check_in_date_end
        if not DaraCore.is_null(request.check_in_date_start):
            body['CheckInDateStart'] = request.check_in_date_start
        if not DaraCore.is_null(request.child_count):
            body['ChildCount'] = request.child_count
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.standard_hotel_ids_shrink):
            body['StandardHotelIds'] = request.standard_hotel_ids_shrink
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'queryCalendarAvailability',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/queryCalendarAvailability',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCalendarAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_calendar_availability(
        self,
        request: main_models.QueryCalendarAvailabilityRequest,
    ) -> main_models.QueryCalendarAvailabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_calendar_availability_with_options(request, headers, runtime)

    async def query_calendar_availability_async(
        self,
        request: main_models.QueryCalendarAvailabilityRequest,
    ) -> main_models.QueryCalendarAvailabilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_calendar_availability_with_options_async(request, headers, runtime)

    def query_order_with_options(
        self,
        request: main_models.QueryOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'queryOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/queryOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_with_options_async(
        self,
        request: main_models.QueryOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.external_order_no):
            body['ExternalOrderNo'] = request.external_order_no
        if not DaraCore.is_null(request.order_no):
            body['OrderNo'] = request.order_no
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'queryOrder',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/queryOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order(
        self,
        request: main_models.QueryOrderRequest,
    ) -> main_models.QueryOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_order_with_options(request, headers, runtime)

    async def query_order_async(
        self,
        request: main_models.QueryOrderRequest,
    ) -> main_models.QueryOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_order_with_options_async(request, headers, runtime)

    def search_city_page_with_options(
        self,
        request: main_models.SearchCityPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchCityPageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.count):
            body['Count'] = request.count
        if not DaraCore.is_null(request.country_code):
            body['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'searchCityPage',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/searchCityPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCityPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_city_page_with_options_async(
        self,
        request: main_models.SearchCityPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchCityPageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.count):
            body['Count'] = request.count
        if not DaraCore.is_null(request.country_code):
            body['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'searchCityPage',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/searchCityPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCityPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_city_page(
        self,
        request: main_models.SearchCityPageRequest,
    ) -> main_models.SearchCityPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_city_page_with_options(request, headers, runtime)

    async def search_city_page_async(
        self,
        request: main_models.SearchCityPageRequest,
    ) -> main_models.SearchCityPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_city_page_with_options_async(request, headers, runtime)

    def search_hotel_list_with_options(
        self,
        request: main_models.SearchHotelListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchHotelListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.city_code):
            body['CityCode'] = request.city_code
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'searchHotelList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotel/searchHotelList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchHotelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_hotel_list_with_options_async(
        self,
        request: main_models.SearchHotelListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchHotelListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.city_code):
            body['CityCode'] = request.city_code
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'searchHotelList',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/globalHotel/searchHotelList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchHotelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_hotel_list(
        self,
        request: main_models.SearchHotelListRequest,
    ) -> main_models.SearchHotelListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_hotel_list_with_options(request, headers, runtime)

    async def search_hotel_list_async(
        self,
        request: main_models.SearchHotelListRequest,
    ) -> main_models.SearchHotelListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_hotel_list_with_options_async(request, headers, runtime)

    def validate_price_with_options(
        self,
        tmp_req: main_models.ValidatePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidatePriceResponse:
        tmp_req.validate()
        request = main_models.ValidatePriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adults):
            body['Adults'] = request.adults
        if not DaraCore.is_null(request.children):
            body['Children'] = request.children
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.item_offer_key):
            body['ItemOfferKey'] = request.item_offer_key
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'validatePrice',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/validatePrice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidatePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_price_with_options_async(
        self,
        tmp_req: main_models.ValidatePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidatePriceResponse:
        tmp_req.validate()
        request = main_models.ValidatePriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.children_ages):
            request.children_ages_shrink = Utils.array_to_string_with_specified_style(tmp_req.children_ages, 'ChildrenAges', 'json')
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.adults):
            body['Adults'] = request.adults
        if not DaraCore.is_null(request.children):
            body['Children'] = request.children
        if not DaraCore.is_null(request.children_ages_shrink):
            body['ChildrenAges'] = request.children_ages_shrink
        if not DaraCore.is_null(request.item_offer_key):
            body['ItemOfferKey'] = request.item_offer_key
        if not DaraCore.is_null(request.room_count):
            body['RoomCount'] = request.room_count
        if not DaraCore.is_null(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'validatePrice',
            version = '2023-01-17',
            protocol = 'HTTPS',
            pathname = f'/validatePrice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidatePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_price(
        self,
        request: main_models.ValidatePriceRequest,
    ) -> main_models.ValidatePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_price_with_options(request, headers, runtime)

    async def validate_price_async(
        self,
        request: main_models.ValidatePriceRequest,
    ) -> main_models.ValidatePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_price_with_options_async(request, headers, runtime)
