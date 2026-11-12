# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aligenieiap_1_0 import models as main_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
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
        self._product_id = 'AliGenie'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('aligenie', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def app_use_time_report_with_options(
        self,
        tmp_req: main_models.AppUseTimeReportRequest,
        headers: main_models.AppUseTimeReportHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AppUseTimeReportResponse:
        tmp_req.validate()
        request = main_models.AppUseTimeReportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AppUseTimeReport',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/vip/use/time/report',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AppUseTimeReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def app_use_time_report_with_options_async(
        self,
        tmp_req: main_models.AppUseTimeReportRequest,
        headers: main_models.AppUseTimeReportHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AppUseTimeReportResponse:
        tmp_req.validate()
        request = main_models.AppUseTimeReportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AppUseTimeReport',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/vip/use/time/report',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AppUseTimeReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def app_use_time_report(
        self,
        request: main_models.AppUseTimeReportRequest,
    ) -> main_models.AppUseTimeReportResponse:
        runtime = RuntimeOptions()
        headers = main_models.AppUseTimeReportHeaders()
        return self.app_use_time_report_with_options(request, headers, runtime)

    async def app_use_time_report_async(
        self,
        request: main_models.AppUseTimeReportRequest,
    ) -> main_models.AppUseTimeReportResponse:
        runtime = RuntimeOptions()
        headers = main_models.AppUseTimeReportHeaders()
        return await self.app_use_time_report_with_options_async(request, headers, runtime)

    def call_back_third_right_send_plan_with_options(
        self,
        tmp_req: main_models.CallBackThirdRightSendPlanRequest,
        headers: main_models.CallBackThirdRightSendPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CallBackThirdRightSendPlanResponse:
        tmp_req.validate()
        request = main_models.CallBackThirdRightSendPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extend_info):
            request.extend_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.card_type):
            query['CardType'] = request.card_type
        if not DaraCore.is_null(request.error_msg):
            query['ErrorMsg'] = request.error_msg
        if not DaraCore.is_null(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not DaraCore.is_null(request.genie_open_id):
            query['GenieOpenId'] = request.genie_open_id
        if not DaraCore.is_null(request.receive_status):
            query['ReceiveStatus'] = request.receive_status
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CallBackThirdRightSendPlan',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/business/CallBackThirdRightSendPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CallBackThirdRightSendPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def call_back_third_right_send_plan_with_options_async(
        self,
        tmp_req: main_models.CallBackThirdRightSendPlanRequest,
        headers: main_models.CallBackThirdRightSendPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CallBackThirdRightSendPlanResponse:
        tmp_req.validate()
        request = main_models.CallBackThirdRightSendPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extend_info):
            request.extend_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.card_type):
            query['CardType'] = request.card_type
        if not DaraCore.is_null(request.error_msg):
            query['ErrorMsg'] = request.error_msg
        if not DaraCore.is_null(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not DaraCore.is_null(request.genie_open_id):
            query['GenieOpenId'] = request.genie_open_id
        if not DaraCore.is_null(request.receive_status):
            query['ReceiveStatus'] = request.receive_status
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CallBackThirdRightSendPlan',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/business/CallBackThirdRightSendPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CallBackThirdRightSendPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def call_back_third_right_send_plan(
        self,
        request: main_models.CallBackThirdRightSendPlanRequest,
    ) -> main_models.CallBackThirdRightSendPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.CallBackThirdRightSendPlanHeaders()
        return self.call_back_third_right_send_plan_with_options(request, headers, runtime)

    async def call_back_third_right_send_plan_async(
        self,
        request: main_models.CallBackThirdRightSendPlanRequest,
    ) -> main_models.CallBackThirdRightSendPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.CallBackThirdRightSendPlanHeaders()
        return await self.call_back_third_right_send_plan_with_options_async(request, headers, runtime)

    def check_third_right_send_plan_with_options(
        self,
        tmp_req: main_models.CheckThirdRightSendPlanRequest,
        headers: main_models.CheckThirdRightSendPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CheckThirdRightSendPlanResponse:
        tmp_req.validate()
        request = main_models.CheckThirdRightSendPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extend_info):
            request.extend_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckThirdRightSendPlan',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/business/CheckThirdRightSendPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckThirdRightSendPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_third_right_send_plan_with_options_async(
        self,
        tmp_req: main_models.CheckThirdRightSendPlanRequest,
        headers: main_models.CheckThirdRightSendPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CheckThirdRightSendPlanResponse:
        tmp_req.validate()
        request = main_models.CheckThirdRightSendPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extend_info):
            request.extend_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckThirdRightSendPlan',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/business/CheckThirdRightSendPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckThirdRightSendPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_third_right_send_plan(
        self,
        request: main_models.CheckThirdRightSendPlanRequest,
    ) -> main_models.CheckThirdRightSendPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.CheckThirdRightSendPlanHeaders()
        return self.check_third_right_send_plan_with_options(request, headers, runtime)

    async def check_third_right_send_plan_async(
        self,
        request: main_models.CheckThirdRightSendPlanRequest,
    ) -> main_models.CheckThirdRightSendPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.CheckThirdRightSendPlanHeaders()
        return await self.check_third_right_send_plan_with_options_async(request, headers, runtime)

    def create_reminder_with_options(
        self,
        tmp_req: main_models.CreateReminderRequest,
        headers: main_models.CreateReminderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReminderResponse:
        tmp_req.validate()
        request = main_models.CreateReminderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateReminder',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReminderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_reminder_with_options_async(
        self,
        tmp_req: main_models.CreateReminderRequest,
        headers: main_models.CreateReminderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReminderResponse:
        tmp_req.validate()
        request = main_models.CreateReminderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateReminder',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReminderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_reminder(
        self,
        request: main_models.CreateReminderRequest,
    ) -> main_models.CreateReminderResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateReminderHeaders()
        return self.create_reminder_with_options(request, headers, runtime)

    async def create_reminder_async(
        self,
        request: main_models.CreateReminderRequest,
    ) -> main_models.CreateReminderResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateReminderHeaders()
        return await self.create_reminder_with_options_async(request, headers, runtime)

    def ctrip_order_push_with_options(
        self,
        request: main_models.CtripOrderPushRequest,
        headers: main_models.CtripOrderPushHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CtripOrderPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.journey_id):
            query['JourneyId'] = request.journey_id
        if not DaraCore.is_null(request.schedule_item):
            query['ScheduleItem'] = request.schedule_item
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CtripOrderPush',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/ctripOrderPush',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CtripOrderPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def ctrip_order_push_with_options_async(
        self,
        request: main_models.CtripOrderPushRequest,
        headers: main_models.CtripOrderPushHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CtripOrderPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.journey_id):
            query['JourneyId'] = request.journey_id
        if not DaraCore.is_null(request.schedule_item):
            query['ScheduleItem'] = request.schedule_item
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CtripOrderPush',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/ctripOrderPush',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CtripOrderPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ctrip_order_push(
        self,
        request: main_models.CtripOrderPushRequest,
    ) -> main_models.CtripOrderPushResponse:
        runtime = RuntimeOptions()
        headers = main_models.CtripOrderPushHeaders()
        return self.ctrip_order_push_with_options(request, headers, runtime)

    async def ctrip_order_push_async(
        self,
        request: main_models.CtripOrderPushRequest,
    ) -> main_models.CtripOrderPushResponse:
        runtime = RuntimeOptions()
        headers = main_models.CtripOrderPushHeaders()
        return await self.ctrip_order_push_with_options_async(request, headers, runtime)

    def delete_reminder_with_options(
        self,
        tmp_req: main_models.DeleteReminderRequest,
        headers: main_models.DeleteReminderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReminderResponse:
        tmp_req.validate()
        request = main_models.DeleteReminderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReminder',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/delete',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReminderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_reminder_with_options_async(
        self,
        tmp_req: main_models.DeleteReminderRequest,
        headers: main_models.DeleteReminderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReminderResponse:
        tmp_req.validate()
        request = main_models.DeleteReminderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReminder',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/delete',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReminderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_reminder(
        self,
        request: main_models.DeleteReminderRequest,
    ) -> main_models.DeleteReminderResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteReminderHeaders()
        return self.delete_reminder_with_options(request, headers, runtime)

    async def delete_reminder_async(
        self,
        request: main_models.DeleteReminderRequest,
    ) -> main_models.DeleteReminderResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteReminderHeaders()
        return await self.delete_reminder_with_options_async(request, headers, runtime)

    def get_account_for_app_with_options(
        self,
        tmp_req: main_models.GetAccountForAppRequest,
        headers: main_models.GetAccountForAppHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountForAppResponse:
        tmp_req.validate()
        request = main_models.GetAccountForAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountForApp',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/vip/account/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountForAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_for_app_with_options_async(
        self,
        tmp_req: main_models.GetAccountForAppRequest,
        headers: main_models.GetAccountForAppHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountForAppResponse:
        tmp_req.validate()
        request = main_models.GetAccountForAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountForApp',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/vip/account/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountForAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_for_app(
        self,
        request: main_models.GetAccountForAppRequest,
    ) -> main_models.GetAccountForAppResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAccountForAppHeaders()
        return self.get_account_for_app_with_options(request, headers, runtime)

    async def get_account_for_app_async(
        self,
        request: main_models.GetAccountForAppRequest,
    ) -> main_models.GetAccountForAppResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAccountForAppHeaders()
        return await self.get_account_for_app_with_options_async(request, headers, runtime)

    def get_bus_app_config_with_options(
        self,
        tmp_req: main_models.GetBusAppConfigRequest,
        headers: main_models.GetBusAppConfigHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetBusAppConfigResponse:
        tmp_req.validate()
        request = main_models.GetBusAppConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBusAppConfig',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/app/config/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBusAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bus_app_config_with_options_async(
        self,
        tmp_req: main_models.GetBusAppConfigRequest,
        headers: main_models.GetBusAppConfigHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetBusAppConfigResponse:
        tmp_req.validate()
        request = main_models.GetBusAppConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBusAppConfig',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/app/config/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBusAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bus_app_config(
        self,
        request: main_models.GetBusAppConfigRequest,
    ) -> main_models.GetBusAppConfigResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetBusAppConfigHeaders()
        return self.get_bus_app_config_with_options(request, headers, runtime)

    async def get_bus_app_config_async(
        self,
        request: main_models.GetBusAppConfigRequest,
    ) -> main_models.GetBusAppConfigResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetBusAppConfigHeaders()
        return await self.get_bus_app_config_with_options_async(request, headers, runtime)

    def get_phone_number_with_options(
        self,
        tmp_req: main_models.GetPhoneNumberRequest,
        headers: main_models.GetPhoneNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneNumberResponse:
        tmp_req.validate()
        request = main_models.GetPhoneNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneNumber',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/profile/phoneNumber',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_number_with_options_async(
        self,
        tmp_req: main_models.GetPhoneNumberRequest,
        headers: main_models.GetPhoneNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneNumberResponse:
        tmp_req.validate()
        request = main_models.GetPhoneNumberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneNumber',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/profile/phoneNumber',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_number(
        self,
        request: main_models.GetPhoneNumberRequest,
    ) -> main_models.GetPhoneNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetPhoneNumberHeaders()
        return self.get_phone_number_with_options(request, headers, runtime)

    async def get_phone_number_async(
        self,
        request: main_models.GetPhoneNumberRequest,
    ) -> main_models.GetPhoneNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetPhoneNumberHeaders()
        return await self.get_phone_number_with_options_async(request, headers, runtime)

    def get_reminder_with_options(
        self,
        tmp_req: main_models.GetReminderRequest,
        headers: main_models.GetReminderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetReminderResponse:
        tmp_req.validate()
        request = main_models.GetReminderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetReminder',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReminderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reminder_with_options_async(
        self,
        tmp_req: main_models.GetReminderRequest,
        headers: main_models.GetReminderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetReminderResponse:
        tmp_req.validate()
        request = main_models.GetReminderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetReminder',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReminderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reminder(
        self,
        request: main_models.GetReminderRequest,
    ) -> main_models.GetReminderResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetReminderHeaders()
        return self.get_reminder_with_options(request, headers, runtime)

    async def get_reminder_async(
        self,
        request: main_models.GetReminderRequest,
    ) -> main_models.GetReminderResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetReminderHeaders()
        return await self.get_reminder_with_options_async(request, headers, runtime)

    def list_reminders_with_options(
        self,
        tmp_req: main_models.ListRemindersRequest,
        headers: main_models.ListRemindersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemindersResponse:
        tmp_req.validate()
        request = main_models.ListRemindersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReminders',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemindersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_reminders_with_options_async(
        self,
        tmp_req: main_models.ListRemindersRequest,
        headers: main_models.ListRemindersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListRemindersResponse:
        tmp_req.validate()
        request = main_models.ListRemindersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReminders',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRemindersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_reminders(
        self,
        request: main_models.ListRemindersRequest,
    ) -> main_models.ListRemindersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListRemindersHeaders()
        return self.list_reminders_with_options(request, headers, runtime)

    async def list_reminders_async(
        self,
        request: main_models.ListRemindersRequest,
    ) -> main_models.ListRemindersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListRemindersHeaders()
        return await self.list_reminders_with_options_async(request, headers, runtime)

    def pull_cashier_with_options(
        self,
        tmp_req: main_models.PullCashierRequest,
        headers: main_models.PullCashierHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PullCashierResponse:
        tmp_req.validate()
        request = main_models.PullCashierShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PullCashier',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/pull/cashier/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PullCashierResponse(),
            self.call_api(params, req, runtime)
        )

    async def pull_cashier_with_options_async(
        self,
        tmp_req: main_models.PullCashierRequest,
        headers: main_models.PullCashierHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PullCashierResponse:
        tmp_req.validate()
        request = main_models.PullCashierShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PullCashier',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/pull/cashier/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PullCashierResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pull_cashier(
        self,
        request: main_models.PullCashierRequest,
    ) -> main_models.PullCashierResponse:
        runtime = RuntimeOptions()
        headers = main_models.PullCashierHeaders()
        return self.pull_cashier_with_options(request, headers, runtime)

    async def pull_cashier_async(
        self,
        request: main_models.PullCashierRequest,
    ) -> main_models.PullCashierResponse:
        runtime = RuntimeOptions()
        headers = main_models.PullCashierHeaders()
        return await self.pull_cashier_with_options_async(request, headers, runtime)

    def push_notifications_with_options(
        self,
        tmp_req: main_models.PushNotificationsRequest,
        headers: main_models.PushNotificationsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushNotificationsResponse:
        tmp_req.validate()
        request = main_models.PushNotificationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not DaraCore.is_null(tmp_req.tenant_info):
            request.tenant_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not DaraCore.is_null(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushNotifications',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/notifications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PushNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_notifications_with_options_async(
        self,
        tmp_req: main_models.PushNotificationsRequest,
        headers: main_models.PushNotificationsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PushNotificationsResponse:
        tmp_req.validate()
        request = main_models.PushNotificationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not DaraCore.is_null(tmp_req.tenant_info):
            request.tenant_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not DaraCore.is_null(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushNotifications',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/notifications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PushNotificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_notifications(
        self,
        request: main_models.PushNotificationsRequest,
    ) -> main_models.PushNotificationsResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushNotificationsHeaders()
        return self.push_notifications_with_options(request, headers, runtime)

    async def push_notifications_async(
        self,
        request: main_models.PushNotificationsRequest,
    ) -> main_models.PushNotificationsResponse:
        runtime = RuntimeOptions()
        headers = main_models.PushNotificationsHeaders()
        return await self.push_notifications_with_options_async(request, headers, runtime)

    def send_notifications_with_options(
        self,
        tmp_req: main_models.SendNotificationsRequest,
        headers: main_models.SendNotificationsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SendNotificationsResponse:
        tmp_req.validate()
        request = main_models.SendNotificationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not DaraCore.is_null(tmp_req.tenant_info):
            request.tenant_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not DaraCore.is_null(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendNotifications',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/general/notifications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.SendNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_notifications_with_options_async(
        self,
        tmp_req: main_models.SendNotificationsRequest,
        headers: main_models.SendNotificationsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SendNotificationsResponse:
        tmp_req.validate()
        request = main_models.SendNotificationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not DaraCore.is_null(tmp_req.tenant_info):
            request.tenant_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not DaraCore.is_null(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendNotifications',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/general/notifications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.SendNotificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_notifications(
        self,
        request: main_models.SendNotificationsRequest,
    ) -> main_models.SendNotificationsResponse:
        runtime = RuntimeOptions()
        headers = main_models.SendNotificationsHeaders()
        return self.send_notifications_with_options(request, headers, runtime)

    async def send_notifications_async(
        self,
        request: main_models.SendNotificationsRequest,
    ) -> main_models.SendNotificationsResponse:
        runtime = RuntimeOptions()
        headers = main_models.SendNotificationsHeaders()
        return await self.send_notifications_with_options_async(request, headers, runtime)

    def third_immediate_msg_push_with_options(
        self,
        request: main_models.ThirdImmediateMsgPushRequest,
        headers: main_models.ThirdImmediateMsgPushHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ThirdImmediateMsgPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.change_detail):
            query['ChangeDetail'] = request.change_detail
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.psg_ids):
            query['PsgIds'] = request.psg_ids
        if not DaraCore.is_null(request.traffic_change_type):
            query['TrafficChangeType'] = request.traffic_change_type
        if not DaraCore.is_null(request.traffic_change_type_desc):
            query['TrafficChangeTypeDesc'] = request.traffic_change_type_desc
        if not DaraCore.is_null(request.traffic_journey_ids):
            query['TrafficJourneyIds'] = request.traffic_journey_ids
        if not DaraCore.is_null(request.traffic_sub_order_ids):
            query['TrafficSubOrderIds'] = request.traffic_sub_order_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ThirdImmediateMsgPush',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/thirdImmediateMsgPush',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ThirdImmediateMsgPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def third_immediate_msg_push_with_options_async(
        self,
        request: main_models.ThirdImmediateMsgPushRequest,
        headers: main_models.ThirdImmediateMsgPushHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ThirdImmediateMsgPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.change_detail):
            query['ChangeDetail'] = request.change_detail
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.psg_ids):
            query['PsgIds'] = request.psg_ids
        if not DaraCore.is_null(request.traffic_change_type):
            query['TrafficChangeType'] = request.traffic_change_type
        if not DaraCore.is_null(request.traffic_change_type_desc):
            query['TrafficChangeTypeDesc'] = request.traffic_change_type_desc
        if not DaraCore.is_null(request.traffic_journey_ids):
            query['TrafficJourneyIds'] = request.traffic_journey_ids
        if not DaraCore.is_null(request.traffic_sub_order_ids):
            query['TrafficSubOrderIds'] = request.traffic_sub_order_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ThirdImmediateMsgPush',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/thirdImmediateMsgPush',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ThirdImmediateMsgPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def third_immediate_msg_push(
        self,
        request: main_models.ThirdImmediateMsgPushRequest,
    ) -> main_models.ThirdImmediateMsgPushResponse:
        runtime = RuntimeOptions()
        headers = main_models.ThirdImmediateMsgPushHeaders()
        return self.third_immediate_msg_push_with_options(request, headers, runtime)

    async def third_immediate_msg_push_async(
        self,
        request: main_models.ThirdImmediateMsgPushRequest,
    ) -> main_models.ThirdImmediateMsgPushResponse:
        runtime = RuntimeOptions()
        headers = main_models.ThirdImmediateMsgPushHeaders()
        return await self.third_immediate_msg_push_with_options_async(request, headers, runtime)

    def update_reminder_with_options(
        self,
        tmp_req: main_models.UpdateReminderRequest,
        headers: main_models.UpdateReminderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateReminderResponse:
        tmp_req.validate()
        request = main_models.UpdateReminderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateReminder',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/update',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateReminderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_reminder_with_options_async(
        self,
        tmp_req: main_models.UpdateReminderRequest,
        headers: main_models.UpdateReminderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateReminderResponse:
        tmp_req.validate()
        request = main_models.UpdateReminderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateReminder',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/reminder/update',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateReminderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_reminder(
        self,
        request: main_models.UpdateReminderRequest,
    ) -> main_models.UpdateReminderResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateReminderHeaders()
        return self.update_reminder_with_options(request, headers, runtime)

    async def update_reminder_async(
        self,
        request: main_models.UpdateReminderRequest,
    ) -> main_models.UpdateReminderResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateReminderHeaders()
        return await self.update_reminder_with_options_async(request, headers, runtime)

    def video_app_report_with_options(
        self,
        tmp_req: main_models.VideoAppReportRequest,
        headers: main_models.VideoAppReportHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.VideoAppReportResponse:
        tmp_req.validate()
        request = main_models.VideoAppReportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoAppReport',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/vip/use/video/report',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoAppReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_app_report_with_options_async(
        self,
        tmp_req: main_models.VideoAppReportRequest,
        headers: main_models.VideoAppReportHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.VideoAppReportResponse:
        tmp_req.validate()
        request = main_models.VideoAppReportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoAppReport',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/vip/use/video/report',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoAppReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_app_report(
        self,
        request: main_models.VideoAppReportRequest,
    ) -> main_models.VideoAppReportResponse:
        runtime = RuntimeOptions()
        headers = main_models.VideoAppReportHeaders()
        return self.video_app_report_with_options(request, headers, runtime)

    async def video_app_report_async(
        self,
        request: main_models.VideoAppReportRequest,
    ) -> main_models.VideoAppReportResponse:
        runtime = RuntimeOptions()
        headers = main_models.VideoAppReportHeaders()
        return await self.video_app_report_with_options_async(request, headers, runtime)

    def wake_up_app_with_options(
        self,
        request: main_models.WakeUpAppRequest,
        headers: main_models.WakeUpAppHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.WakeUpAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_debug):
            body['IsDebug'] = request.is_debug
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.target_info):
            body['TargetInfo'] = request.target_info
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'WakeUpApp',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/wakeup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.WakeUpAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def wake_up_app_with_options_async(
        self,
        request: main_models.WakeUpAppRequest,
        headers: main_models.WakeUpAppHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.WakeUpAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_debug):
            body['IsDebug'] = request.is_debug
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.target_info):
            body['TargetInfo'] = request.target_info
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'WakeUpApp',
            version = 'iap_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/iap/wakeup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.WakeUpAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def wake_up_app(
        self,
        request: main_models.WakeUpAppRequest,
    ) -> main_models.WakeUpAppResponse:
        runtime = RuntimeOptions()
        headers = main_models.WakeUpAppHeaders()
        return self.wake_up_app_with_options(request, headers, runtime)

    async def wake_up_app_async(
        self,
        request: main_models.WakeUpAppRequest,
    ) -> main_models.WakeUpAppResponse:
        runtime = RuntimeOptions()
        headers = main_models.WakeUpAppHeaders()
        return await self.wake_up_app_with_options_async(request, headers, runtime)
