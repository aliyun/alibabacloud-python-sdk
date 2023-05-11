# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_airticketopen20230117 import models as airticket_open_20230117_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def account_flow_list_with_options(
        self,
        request: airticket_open_20230117_models.AccountFlowListRequest,
        headers: airticket_open_20230117_models.AccountFlowListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.AccountFlowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.day_num):
            query['day_num'] = request.day_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.utc_begin_time):
            query['utc_begin_time'] = request.utc_begin_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccountFlowList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/account/flow-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.AccountFlowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def account_flow_list_with_options_async(
        self,
        request: airticket_open_20230117_models.AccountFlowListRequest,
        headers: airticket_open_20230117_models.AccountFlowListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.AccountFlowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.day_num):
            query['day_num'] = request.day_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.utc_begin_time):
            query['utc_begin_time'] = request.utc_begin_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccountFlowList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/account/flow-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.AccountFlowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def account_flow_list(
        self,
        request: airticket_open_20230117_models.AccountFlowListRequest,
    ) -> airticket_open_20230117_models.AccountFlowListResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.AccountFlowListHeaders()
        return self.account_flow_list_with_options(request, headers, runtime)

    async def account_flow_list_async(
        self,
        request: airticket_open_20230117_models.AccountFlowListRequest,
    ) -> airticket_open_20230117_models.AccountFlowListResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.AccountFlowListHeaders()
        return await self.account_flow_list_with_options_async(request, headers, runtime)

    def ancillary_suggest_with_options(
        self,
        request: airticket_open_20230117_models.AncillarySuggestRequest,
        headers: airticket_open_20230117_models.AncillarySuggestHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.AncillarySuggestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AncillarySuggest',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/ancillary/action-suggest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.AncillarySuggestResponse(),
            self.call_api(params, req, runtime)
        )

    async def ancillary_suggest_with_options_async(
        self,
        request: airticket_open_20230117_models.AncillarySuggestRequest,
        headers: airticket_open_20230117_models.AncillarySuggestHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.AncillarySuggestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AncillarySuggest',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/ancillary/action-suggest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.AncillarySuggestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ancillary_suggest(
        self,
        request: airticket_open_20230117_models.AncillarySuggestRequest,
    ) -> airticket_open_20230117_models.AncillarySuggestResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.AncillarySuggestHeaders()
        return self.ancillary_suggest_with_options(request, headers, runtime)

    async def ancillary_suggest_async(
        self,
        request: airticket_open_20230117_models.AncillarySuggestRequest,
    ) -> airticket_open_20230117_models.AncillarySuggestResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.AncillarySuggestHeaders()
        return await self.ancillary_suggest_with_options_async(request, headers, runtime)

    def book_with_options(
        self,
        tmp_req: airticket_open_20230117_models.BookRequest,
        headers: airticket_open_20230117_models.BookHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.BookResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.BookShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact):
            request.contact_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        if not UtilClient.is_unset(tmp_req.passenger_ancillary_purchase_map_list):
            request.passenger_ancillary_purchase_map_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_ancillary_purchase_map_list, 'passenger_ancillary_purchase_map_list', 'json')
        if not UtilClient.is_unset(tmp_req.passenger_list):
            request.passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_list, 'passenger_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not UtilClient.is_unset(request.out_order_num):
            body['out_order_num'] = request.out_order_num
        if not UtilClient.is_unset(request.passenger_ancillary_purchase_map_list_shrink):
            body['passenger_ancillary_purchase_map_list'] = request.passenger_ancillary_purchase_map_list_shrink
        if not UtilClient.is_unset(request.passenger_list_shrink):
            body['passenger_list'] = request.passenger_list_shrink
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Book',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-book',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.BookResponse(),
            self.call_api(params, req, runtime)
        )

    async def book_with_options_async(
        self,
        tmp_req: airticket_open_20230117_models.BookRequest,
        headers: airticket_open_20230117_models.BookHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.BookResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.BookShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact):
            request.contact_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        if not UtilClient.is_unset(tmp_req.passenger_ancillary_purchase_map_list):
            request.passenger_ancillary_purchase_map_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_ancillary_purchase_map_list, 'passenger_ancillary_purchase_map_list', 'json')
        if not UtilClient.is_unset(tmp_req.passenger_list):
            request.passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_list, 'passenger_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not UtilClient.is_unset(request.out_order_num):
            body['out_order_num'] = request.out_order_num
        if not UtilClient.is_unset(request.passenger_ancillary_purchase_map_list_shrink):
            body['passenger_ancillary_purchase_map_list'] = request.passenger_ancillary_purchase_map_list_shrink
        if not UtilClient.is_unset(request.passenger_list_shrink):
            body['passenger_list'] = request.passenger_list_shrink
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Book',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-book',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.BookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def book(
        self,
        request: airticket_open_20230117_models.BookRequest,
    ) -> airticket_open_20230117_models.BookResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.BookHeaders()
        return self.book_with_options(request, headers, runtime)

    async def book_async(
        self,
        request: airticket_open_20230117_models.BookRequest,
    ) -> airticket_open_20230117_models.BookResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.BookHeaders()
        return await self.book_with_options_async(request, headers, runtime)

    def cancel_with_options(
        self,
        request: airticket_open_20230117_models.CancelRequest,
        headers: airticket_open_20230117_models.CancelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.CancelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Cancel',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.CancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_with_options_async(
        self,
        request: airticket_open_20230117_models.CancelRequest,
        headers: airticket_open_20230117_models.CancelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.CancelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Cancel',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.CancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel(
        self,
        request: airticket_open_20230117_models.CancelRequest,
    ) -> airticket_open_20230117_models.CancelResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.CancelHeaders()
        return self.cancel_with_options(request, headers, runtime)

    async def cancel_async(
        self,
        request: airticket_open_20230117_models.CancelRequest,
    ) -> airticket_open_20230117_models.CancelResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.CancelHeaders()
        return await self.cancel_with_options_async(request, headers, runtime)

    def change_apply_with_options(
        self,
        tmp_req: airticket_open_20230117_models.ChangeApplyRequest,
        headers: airticket_open_20230117_models.ChangeApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeApplyResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.ChangeApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.change_passenger_list):
            request.change_passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.change_passenger_list, 'change_passenger_list', 'json')
        if not UtilClient.is_unset(tmp_req.changed_journeys):
            request.changed_journeys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.changed_journeys, 'changed_journeys', 'json')
        if not UtilClient.is_unset(tmp_req.contact):
            request.contact_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        body = {}
        if not UtilClient.is_unset(request.change_passenger_list_shrink):
            body['change_passenger_list'] = request.change_passenger_list_shrink
        if not UtilClient.is_unset(request.changed_journeys_shrink):
            body['changed_journeys'] = request.changed_journeys_shrink
        if not UtilClient.is_unset(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeApply',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/action-apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_apply_with_options_async(
        self,
        tmp_req: airticket_open_20230117_models.ChangeApplyRequest,
        headers: airticket_open_20230117_models.ChangeApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeApplyResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.ChangeApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.change_passenger_list):
            request.change_passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.change_passenger_list, 'change_passenger_list', 'json')
        if not UtilClient.is_unset(tmp_req.changed_journeys):
            request.changed_journeys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.changed_journeys, 'changed_journeys', 'json')
        if not UtilClient.is_unset(tmp_req.contact):
            request.contact_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        body = {}
        if not UtilClient.is_unset(request.change_passenger_list_shrink):
            body['change_passenger_list'] = request.change_passenger_list_shrink
        if not UtilClient.is_unset(request.changed_journeys_shrink):
            body['changed_journeys'] = request.changed_journeys_shrink
        if not UtilClient.is_unset(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeApply',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/action-apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_apply(
        self,
        request: airticket_open_20230117_models.ChangeApplyRequest,
    ) -> airticket_open_20230117_models.ChangeApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeApplyHeaders()
        return self.change_apply_with_options(request, headers, runtime)

    async def change_apply_async(
        self,
        request: airticket_open_20230117_models.ChangeApplyRequest,
    ) -> airticket_open_20230117_models.ChangeApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeApplyHeaders()
        return await self.change_apply_with_options_async(request, headers, runtime)

    def change_cancel_with_options(
        self,
        request: airticket_open_20230117_models.ChangeCancelRequest,
        headers: airticket_open_20230117_models.ChangeCancelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeCancelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeCancel',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/action-cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_cancel_with_options_async(
        self,
        request: airticket_open_20230117_models.ChangeCancelRequest,
        headers: airticket_open_20230117_models.ChangeCancelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeCancelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeCancel',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/action-cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_cancel(
        self,
        request: airticket_open_20230117_models.ChangeCancelRequest,
    ) -> airticket_open_20230117_models.ChangeCancelResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeCancelHeaders()
        return self.change_cancel_with_options(request, headers, runtime)

    async def change_cancel_async(
        self,
        request: airticket_open_20230117_models.ChangeCancelRequest,
    ) -> airticket_open_20230117_models.ChangeCancelResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeCancelHeaders()
        return await self.change_cancel_with_options_async(request, headers, runtime)

    def change_confirm_with_options(
        self,
        request: airticket_open_20230117_models.ChangeConfirmRequest,
        headers: airticket_open_20230117_models.ChangeConfirmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeConfirmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeConfirm',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/action-confirm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_confirm_with_options_async(
        self,
        request: airticket_open_20230117_models.ChangeConfirmRequest,
        headers: airticket_open_20230117_models.ChangeConfirmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeConfirmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeConfirm',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/action-confirm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeConfirmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_confirm(
        self,
        request: airticket_open_20230117_models.ChangeConfirmRequest,
    ) -> airticket_open_20230117_models.ChangeConfirmResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeConfirmHeaders()
        return self.change_confirm_with_options(request, headers, runtime)

    async def change_confirm_async(
        self,
        request: airticket_open_20230117_models.ChangeConfirmRequest,
    ) -> airticket_open_20230117_models.ChangeConfirmResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeConfirmHeaders()
        return await self.change_confirm_with_options_async(request, headers, runtime)

    def change_detail_with_options(
        self,
        request: airticket_open_20230117_models.ChangeDetailRequest,
        headers: airticket_open_20230117_models.ChangeDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_num):
            query['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_detail_with_options_async(
        self,
        request: airticket_open_20230117_models.ChangeDetailRequest,
        headers: airticket_open_20230117_models.ChangeDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_num):
            query['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_detail(
        self,
        request: airticket_open_20230117_models.ChangeDetailRequest,
    ) -> airticket_open_20230117_models.ChangeDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailHeaders()
        return self.change_detail_with_options(request, headers, runtime)

    async def change_detail_async(
        self,
        request: airticket_open_20230117_models.ChangeDetailRequest,
    ) -> airticket_open_20230117_models.ChangeDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailHeaders()
        return await self.change_detail_with_options_async(request, headers, runtime)

    def change_detail_list_of_buyer_with_options(
        self,
        request: airticket_open_20230117_models.ChangeDetailListOfBuyerRequest,
        headers: airticket_open_20230117_models.ChangeDetailListOfBuyerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeDetailListOfBuyerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.utc_create_begin):
            query['utc_create_begin'] = request.utc_create_begin
        if not UtilClient.is_unset(request.utc_create_end):
            query['utc_create_end'] = request.utc_create_end
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetailListOfBuyer',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/buyer/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailListOfBuyerResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_detail_list_of_buyer_with_options_async(
        self,
        request: airticket_open_20230117_models.ChangeDetailListOfBuyerRequest,
        headers: airticket_open_20230117_models.ChangeDetailListOfBuyerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeDetailListOfBuyerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.utc_create_begin):
            query['utc_create_begin'] = request.utc_create_begin
        if not UtilClient.is_unset(request.utc_create_end):
            query['utc_create_end'] = request.utc_create_end
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetailListOfBuyer',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/buyer/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailListOfBuyerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_detail_list_of_buyer(
        self,
        request: airticket_open_20230117_models.ChangeDetailListOfBuyerRequest,
    ) -> airticket_open_20230117_models.ChangeDetailListOfBuyerResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailListOfBuyerHeaders()
        return self.change_detail_list_of_buyer_with_options(request, headers, runtime)

    async def change_detail_list_of_buyer_async(
        self,
        request: airticket_open_20230117_models.ChangeDetailListOfBuyerRequest,
    ) -> airticket_open_20230117_models.ChangeDetailListOfBuyerResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailListOfBuyerHeaders()
        return await self.change_detail_list_of_buyer_with_options_async(request, headers, runtime)

    def change_detail_list_of_order_num_with_options(
        self,
        request: airticket_open_20230117_models.ChangeDetailListOfOrderNumRequest,
        headers: airticket_open_20230117_models.ChangeDetailListOfOrderNumHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeDetailListOfOrderNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetailListOfOrderNum',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/order-num/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailListOfOrderNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_detail_list_of_order_num_with_options_async(
        self,
        request: airticket_open_20230117_models.ChangeDetailListOfOrderNumRequest,
        headers: airticket_open_20230117_models.ChangeDetailListOfOrderNumHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.ChangeDetailListOfOrderNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetailListOfOrderNum',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/change/order-num/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailListOfOrderNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_detail_list_of_order_num(
        self,
        request: airticket_open_20230117_models.ChangeDetailListOfOrderNumRequest,
    ) -> airticket_open_20230117_models.ChangeDetailListOfOrderNumResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailListOfOrderNumHeaders()
        return self.change_detail_list_of_order_num_with_options(request, headers, runtime)

    async def change_detail_list_of_order_num_async(
        self,
        request: airticket_open_20230117_models.ChangeDetailListOfOrderNumRequest,
    ) -> airticket_open_20230117_models.ChangeDetailListOfOrderNumResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailListOfOrderNumHeaders()
        return await self.change_detail_list_of_order_num_with_options_async(request, headers, runtime)

    def enrich_with_options(
        self,
        tmp_req: airticket_open_20230117_models.EnrichRequest,
        headers: airticket_open_20230117_models.EnrichHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.EnrichResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.EnrichShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.journey_param_list):
            request.journey_param_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.journey_param_list, 'journey_param_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.adults):
            body['adults'] = request.adults
        if not UtilClient.is_unset(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.children):
            body['children'] = request.children
        if not UtilClient.is_unset(request.infants):
            body['infants'] = request.infants
        if not UtilClient.is_unset(request.journey_param_list_shrink):
            body['journey_param_list'] = request.journey_param_list_shrink
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Enrich',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-enrich',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.EnrichResponse(),
            self.call_api(params, req, runtime)
        )

    async def enrich_with_options_async(
        self,
        tmp_req: airticket_open_20230117_models.EnrichRequest,
        headers: airticket_open_20230117_models.EnrichHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.EnrichResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.EnrichShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.journey_param_list):
            request.journey_param_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.journey_param_list, 'journey_param_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.adults):
            body['adults'] = request.adults
        if not UtilClient.is_unset(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.children):
            body['children'] = request.children
        if not UtilClient.is_unset(request.infants):
            body['infants'] = request.infants
        if not UtilClient.is_unset(request.journey_param_list_shrink):
            body['journey_param_list'] = request.journey_param_list_shrink
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Enrich',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-enrich',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.EnrichResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enrich(
        self,
        request: airticket_open_20230117_models.EnrichRequest,
    ) -> airticket_open_20230117_models.EnrichResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.EnrichHeaders()
        return self.enrich_with_options(request, headers, runtime)

    async def enrich_async(
        self,
        request: airticket_open_20230117_models.EnrichRequest,
    ) -> airticket_open_20230117_models.EnrichResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.EnrichHeaders()
        return await self.enrich_with_options_async(request, headers, runtime)

    def file_upload_with_options(
        self,
        request: airticket_open_20230117_models.FileUploadRequest,
        headers: airticket_open_20230117_models.FileUploadHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.FileUploadResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_content):
            body['file_content'] = request.file_content
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileUpload',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/attachment/action-upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.FileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def file_upload_with_options_async(
        self,
        request: airticket_open_20230117_models.FileUploadRequest,
        headers: airticket_open_20230117_models.FileUploadHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.FileUploadResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_content):
            body['file_content'] = request.file_content
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileUpload',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/attachment/action-upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.FileUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def file_upload(
        self,
        request: airticket_open_20230117_models.FileUploadRequest,
    ) -> airticket_open_20230117_models.FileUploadResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.FileUploadHeaders()
        return self.file_upload_with_options(request, headers, runtime)

    async def file_upload_async(
        self,
        request: airticket_open_20230117_models.FileUploadRequest,
    ) -> airticket_open_20230117_models.FileUploadResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.FileUploadHeaders()
        return await self.file_upload_with_options_async(request, headers, runtime)

    def flight_change_of_order_with_options(
        self,
        request: airticket_open_20230117_models.FlightChangeOfOrderRequest,
        headers: airticket_open_20230117_models.FlightChangeOfOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.FlightChangeOfOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightChangeOfOrder',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/flightchange/of-order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.FlightChangeOfOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def flight_change_of_order_with_options_async(
        self,
        request: airticket_open_20230117_models.FlightChangeOfOrderRequest,
        headers: airticket_open_20230117_models.FlightChangeOfOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.FlightChangeOfOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightChangeOfOrder',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/flightchange/of-order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.FlightChangeOfOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flight_change_of_order(
        self,
        request: airticket_open_20230117_models.FlightChangeOfOrderRequest,
    ) -> airticket_open_20230117_models.FlightChangeOfOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.FlightChangeOfOrderHeaders()
        return self.flight_change_of_order_with_options(request, headers, runtime)

    async def flight_change_of_order_async(
        self,
        request: airticket_open_20230117_models.FlightChangeOfOrderRequest,
    ) -> airticket_open_20230117_models.FlightChangeOfOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.FlightChangeOfOrderHeaders()
        return await self.flight_change_of_order_with_options_async(request, headers, runtime)

    def get_token_with_options(
        self,
        request: airticket_open_20230117_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.GetTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['app_key'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: airticket_open_20230117_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.GetTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['app_key'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: airticket_open_20230117_models.GetTokenRequest,
    ) -> airticket_open_20230117_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: airticket_open_20230117_models.GetTokenRequest,
    ) -> airticket_open_20230117_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def order_detail_with_options(
        self,
        request: airticket_open_20230117_models.OrderDetailRequest,
        headers: airticket_open_20230117_models.OrderDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.OrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.out_order_num):
            query['out_order_num'] = request.out_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/order-detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.OrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_detail_with_options_async(
        self,
        request: airticket_open_20230117_models.OrderDetailRequest,
        headers: airticket_open_20230117_models.OrderDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.OrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.out_order_num):
            query['out_order_num'] = request.out_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/order-detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.OrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_detail(
        self,
        request: airticket_open_20230117_models.OrderDetailRequest,
    ) -> airticket_open_20230117_models.OrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.OrderDetailHeaders()
        return self.order_detail_with_options(request, headers, runtime)

    async def order_detail_async(
        self,
        request: airticket_open_20230117_models.OrderDetailRequest,
    ) -> airticket_open_20230117_models.OrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.OrderDetailHeaders()
        return await self.order_detail_with_options_async(request, headers, runtime)

    def order_list_with_options(
        self,
        request: airticket_open_20230117_models.OrderListRequest,
        headers: airticket_open_20230117_models.OrderListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.OrderListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.book_time_end):
            query['book_time_end'] = request.book_time_end
        if not UtilClient.is_unset(request.book_time_start):
            query['book_time_start'] = request.book_time_start
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.OrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_list_with_options_async(
        self,
        request: airticket_open_20230117_models.OrderListRequest,
        headers: airticket_open_20230117_models.OrderListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.OrderListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.book_time_end):
            query['book_time_end'] = request.book_time_end
        if not UtilClient.is_unset(request.book_time_start):
            query['book_time_start'] = request.book_time_start
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.OrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_list(
        self,
        request: airticket_open_20230117_models.OrderListRequest,
    ) -> airticket_open_20230117_models.OrderListResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.OrderListHeaders()
        return self.order_list_with_options(request, headers, runtime)

    async def order_list_async(
        self,
        request: airticket_open_20230117_models.OrderListRequest,
    ) -> airticket_open_20230117_models.OrderListResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.OrderListHeaders()
        return await self.order_list_with_options_async(request, headers, runtime)

    def pricing_with_options(
        self,
        request: airticket_open_20230117_models.PricingRequest,
        headers: airticket_open_20230117_models.PricingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.PricingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Pricing',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-pricing',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.PricingResponse(),
            self.call_api(params, req, runtime)
        )

    async def pricing_with_options_async(
        self,
        request: airticket_open_20230117_models.PricingRequest,
        headers: airticket_open_20230117_models.PricingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.PricingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Pricing',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-pricing',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.PricingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pricing(
        self,
        request: airticket_open_20230117_models.PricingRequest,
    ) -> airticket_open_20230117_models.PricingResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.PricingHeaders()
        return self.pricing_with_options(request, headers, runtime)

    async def pricing_async(
        self,
        request: airticket_open_20230117_models.PricingRequest,
    ) -> airticket_open_20230117_models.PricingResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.PricingHeaders()
        return await self.pricing_with_options_async(request, headers, runtime)

    def refund_apply_with_options(
        self,
        tmp_req: airticket_open_20230117_models.RefundApplyRequest,
        headers: airticket_open_20230117_models.RefundApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.RefundApplyResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.RefundApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.refund_journeys):
            request.refund_journeys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_journeys, 'refund_journeys', 'json')
        if not UtilClient.is_unset(tmp_req.refund_passenger_list):
            request.refund_passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_passenger_list, 'refund_passenger_list', 'json')
        if not UtilClient.is_unset(tmp_req.refund_type):
            request.refund_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_type, 'refund_type', 'json')
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        if not UtilClient.is_unset(request.refund_journeys_shrink):
            body['refund_journeys'] = request.refund_journeys_shrink
        if not UtilClient.is_unset(request.refund_passenger_list_shrink):
            body['refund_passenger_list'] = request.refund_passenger_list_shrink
        if not UtilClient.is_unset(request.refund_type_shrink):
            body['refund_type'] = request.refund_type_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundApply',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/refund/action-apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_apply_with_options_async(
        self,
        tmp_req: airticket_open_20230117_models.RefundApplyRequest,
        headers: airticket_open_20230117_models.RefundApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.RefundApplyResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.RefundApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.refund_journeys):
            request.refund_journeys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_journeys, 'refund_journeys', 'json')
        if not UtilClient.is_unset(tmp_req.refund_passenger_list):
            request.refund_passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_passenger_list, 'refund_passenger_list', 'json')
        if not UtilClient.is_unset(tmp_req.refund_type):
            request.refund_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_type, 'refund_type', 'json')
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        if not UtilClient.is_unset(request.refund_journeys_shrink):
            body['refund_journeys'] = request.refund_journeys_shrink
        if not UtilClient.is_unset(request.refund_passenger_list_shrink):
            body['refund_passenger_list'] = request.refund_passenger_list_shrink
        if not UtilClient.is_unset(request.refund_type_shrink):
            body['refund_type'] = request.refund_type_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundApply',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/refund/action-apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_apply(
        self,
        request: airticket_open_20230117_models.RefundApplyRequest,
    ) -> airticket_open_20230117_models.RefundApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundApplyHeaders()
        return self.refund_apply_with_options(request, headers, runtime)

    async def refund_apply_async(
        self,
        request: airticket_open_20230117_models.RefundApplyRequest,
    ) -> airticket_open_20230117_models.RefundApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundApplyHeaders()
        return await self.refund_apply_with_options_async(request, headers, runtime)

    def refund_detail_with_options(
        self,
        request: airticket_open_20230117_models.RefundDetailRequest,
        headers: airticket_open_20230117_models.RefundDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.RefundDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.refund_order_num):
            query['refund_order_num'] = request.refund_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/refund/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_detail_with_options_async(
        self,
        request: airticket_open_20230117_models.RefundDetailRequest,
        headers: airticket_open_20230117_models.RefundDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.RefundDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.refund_order_num):
            query['refund_order_num'] = request.refund_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/refund/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_detail(
        self,
        request: airticket_open_20230117_models.RefundDetailRequest,
    ) -> airticket_open_20230117_models.RefundDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundDetailHeaders()
        return self.refund_detail_with_options(request, headers, runtime)

    async def refund_detail_async(
        self,
        request: airticket_open_20230117_models.RefundDetailRequest,
    ) -> airticket_open_20230117_models.RefundDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundDetailHeaders()
        return await self.refund_detail_with_options_async(request, headers, runtime)

    def refund_detail_list_with_options(
        self,
        request: airticket_open_20230117_models.RefundDetailListRequest,
        headers: airticket_open_20230117_models.RefundDetailListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.RefundDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.refund_create_begin_time):
            query['refund_create_begin_time'] = request.refund_create_begin_time
        if not UtilClient.is_unset(request.refund_create_end_time):
            query['refund_create_end_time'] = request.refund_create_end_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundDetailList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/refund/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_detail_list_with_options_async(
        self,
        request: airticket_open_20230117_models.RefundDetailListRequest,
        headers: airticket_open_20230117_models.RefundDetailListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.RefundDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.refund_create_begin_time):
            query['refund_create_begin_time'] = request.refund_create_begin_time
        if not UtilClient.is_unset(request.refund_create_end_time):
            query['refund_create_end_time'] = request.refund_create_end_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundDetailList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/refund/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_detail_list(
        self,
        request: airticket_open_20230117_models.RefundDetailListRequest,
    ) -> airticket_open_20230117_models.RefundDetailListResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundDetailListHeaders()
        return self.refund_detail_list_with_options(request, headers, runtime)

    async def refund_detail_list_async(
        self,
        request: airticket_open_20230117_models.RefundDetailListRequest,
    ) -> airticket_open_20230117_models.RefundDetailListResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundDetailListHeaders()
        return await self.refund_detail_list_with_options_async(request, headers, runtime)

    def search_with_options(
        self,
        tmp_req: airticket_open_20230117_models.SearchRequest,
        headers: airticket_open_20230117_models.SearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.SearchResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.SearchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.air_legs):
            request.air_legs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.air_legs, 'air_legs', 'json')
        body = {}
        if not UtilClient.is_unset(request.adults):
            body['adults'] = request.adults
        if not UtilClient.is_unset(request.air_legs_shrink):
            body['air_legs'] = request.air_legs_shrink
        if not UtilClient.is_unset(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.children):
            body['children'] = request.children
        if not UtilClient.is_unset(request.infants):
            body['infants'] = request.infants
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Search',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.SearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_with_options_async(
        self,
        tmp_req: airticket_open_20230117_models.SearchRequest,
        headers: airticket_open_20230117_models.SearchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.SearchResponse:
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.SearchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.air_legs):
            request.air_legs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.air_legs, 'air_legs', 'json')
        body = {}
        if not UtilClient.is_unset(request.adults):
            body['adults'] = request.adults
        if not UtilClient.is_unset(request.air_legs_shrink):
            body['air_legs'] = request.air_legs_shrink
        if not UtilClient.is_unset(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.children):
            body['children'] = request.children
        if not UtilClient.is_unset(request.infants):
            body['infants'] = request.infants
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Search',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.SearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search(
        self,
        request: airticket_open_20230117_models.SearchRequest,
    ) -> airticket_open_20230117_models.SearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.SearchHeaders()
        return self.search_with_options(request, headers, runtime)

    async def search_async(
        self,
        request: airticket_open_20230117_models.SearchRequest,
    ) -> airticket_open_20230117_models.SearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.SearchHeaders()
        return await self.search_with_options_async(request, headers, runtime)

    def ticketing_with_options(
        self,
        request: airticket_open_20230117_models.TicketingRequest,
        headers: airticket_open_20230117_models.TicketingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.TicketingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Ticketing',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-ticketing',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.TicketingResponse(),
            self.call_api(params, req, runtime)
        )

    async def ticketing_with_options_async(
        self,
        request: airticket_open_20230117_models.TicketingRequest,
        headers: airticket_open_20230117_models.TicketingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airticket_open_20230117_models.TicketingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Ticketing',
            version='2023-01-17',
            protocol='HTTPS',
            pathname=f'/airticket/v1/trade/action-ticketing',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.TicketingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ticketing(
        self,
        request: airticket_open_20230117_models.TicketingRequest,
    ) -> airticket_open_20230117_models.TicketingResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.TicketingHeaders()
        return self.ticketing_with_options(request, headers, runtime)

    async def ticketing_async(
        self,
        request: airticket_open_20230117_models.TicketingRequest,
    ) -> airticket_open_20230117_models.TicketingResponse:
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.TicketingHeaders()
        return await self.ticketing_with_options_async(request, headers, runtime)
