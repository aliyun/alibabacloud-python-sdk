# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligenieiap_1_0 import models as ali_genieiap__1__0_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def app_use_time_report_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.AppUseTimeReportRequest,
        headers: ali_genieiap__1__0_models.AppUseTimeReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.AppUseTimeReportResponse:
        """
        @summary 应用使用时长上报
        
        @param tmp_req: AppUseTimeReportRequest
        @param headers: AppUseTimeReportHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AppUseTimeReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.AppUseTimeReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppUseTimeReport',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/vip/use/time/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.AppUseTimeReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def app_use_time_report_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.AppUseTimeReportRequest,
        headers: ali_genieiap__1__0_models.AppUseTimeReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.AppUseTimeReportResponse:
        """
        @summary 应用使用时长上报
        
        @param tmp_req: AppUseTimeReportRequest
        @param headers: AppUseTimeReportHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AppUseTimeReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.AppUseTimeReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppUseTimeReport',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/vip/use/time/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.AppUseTimeReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def app_use_time_report(
        self,
        request: ali_genieiap__1__0_models.AppUseTimeReportRequest,
    ) -> ali_genieiap__1__0_models.AppUseTimeReportResponse:
        """
        @summary 应用使用时长上报
        
        @param request: AppUseTimeReportRequest
        @return: AppUseTimeReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.AppUseTimeReportHeaders()
        return self.app_use_time_report_with_options(request, headers, runtime)

    async def app_use_time_report_async(
        self,
        request: ali_genieiap__1__0_models.AppUseTimeReportRequest,
    ) -> ali_genieiap__1__0_models.AppUseTimeReportResponse:
        """
        @summary 应用使用时长上报
        
        @param request: AppUseTimeReportRequest
        @return: AppUseTimeReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.AppUseTimeReportHeaders()
        return await self.app_use_time_report_with_options_async(request, headers, runtime)

    def call_back_third_right_send_plan_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.CallBackThirdRightSendPlanRequest,
        headers: ali_genieiap__1__0_models.CallBackThirdRightSendPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.CallBackThirdRightSendPlanResponse:
        """
        @summary 三方领取回调接口
        
        @param tmp_req: CallBackThirdRightSendPlanRequest
        @param headers: CallBackThirdRightSendPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CallBackThirdRightSendPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CallBackThirdRightSendPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_info):
            request.extend_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.card_type):
            query['CardType'] = request.card_type
        if not UtilClient.is_unset(request.error_msg):
            query['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not UtilClient.is_unset(request.genie_open_id):
            query['GenieOpenId'] = request.genie_open_id
        if not UtilClient.is_unset(request.receive_status):
            query['ReceiveStatus'] = request.receive_status
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CallBackThirdRightSendPlan',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/business/CallBackThirdRightSendPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CallBackThirdRightSendPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def call_back_third_right_send_plan_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.CallBackThirdRightSendPlanRequest,
        headers: ali_genieiap__1__0_models.CallBackThirdRightSendPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.CallBackThirdRightSendPlanResponse:
        """
        @summary 三方领取回调接口
        
        @param tmp_req: CallBackThirdRightSendPlanRequest
        @param headers: CallBackThirdRightSendPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CallBackThirdRightSendPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CallBackThirdRightSendPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_info):
            request.extend_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.card_type):
            query['CardType'] = request.card_type
        if not UtilClient.is_unset(request.error_msg):
            query['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not UtilClient.is_unset(request.genie_open_id):
            query['GenieOpenId'] = request.genie_open_id
        if not UtilClient.is_unset(request.receive_status):
            query['ReceiveStatus'] = request.receive_status
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CallBackThirdRightSendPlan',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/business/CallBackThirdRightSendPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CallBackThirdRightSendPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def call_back_third_right_send_plan(
        self,
        request: ali_genieiap__1__0_models.CallBackThirdRightSendPlanRequest,
    ) -> ali_genieiap__1__0_models.CallBackThirdRightSendPlanResponse:
        """
        @summary 三方领取回调接口
        
        @param request: CallBackThirdRightSendPlanRequest
        @return: CallBackThirdRightSendPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CallBackThirdRightSendPlanHeaders()
        return self.call_back_third_right_send_plan_with_options(request, headers, runtime)

    async def call_back_third_right_send_plan_async(
        self,
        request: ali_genieiap__1__0_models.CallBackThirdRightSendPlanRequest,
    ) -> ali_genieiap__1__0_models.CallBackThirdRightSendPlanResponse:
        """
        @summary 三方领取回调接口
        
        @param request: CallBackThirdRightSendPlanRequest
        @return: CallBackThirdRightSendPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CallBackThirdRightSendPlanHeaders()
        return await self.call_back_third_right_send_plan_with_options_async(request, headers, runtime)

    def check_third_right_send_plan_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.CheckThirdRightSendPlanRequest,
        headers: ali_genieiap__1__0_models.CheckThirdRightSendPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.CheckThirdRightSendPlanResponse:
        """
        @summary 商业化移动屏三方app领卡校验
        
        @param tmp_req: CheckThirdRightSendPlanRequest
        @param headers: CheckThirdRightSendPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckThirdRightSendPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CheckThirdRightSendPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_info):
            request.extend_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckThirdRightSendPlan',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/business/CheckThirdRightSendPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CheckThirdRightSendPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_third_right_send_plan_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.CheckThirdRightSendPlanRequest,
        headers: ali_genieiap__1__0_models.CheckThirdRightSendPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.CheckThirdRightSendPlanResponse:
        """
        @summary 商业化移动屏三方app领卡校验
        
        @param tmp_req: CheckThirdRightSendPlanRequest
        @param headers: CheckThirdRightSendPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckThirdRightSendPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CheckThirdRightSendPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_info):
            request.extend_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckThirdRightSendPlan',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/business/CheckThirdRightSendPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CheckThirdRightSendPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_third_right_send_plan(
        self,
        request: ali_genieiap__1__0_models.CheckThirdRightSendPlanRequest,
    ) -> ali_genieiap__1__0_models.CheckThirdRightSendPlanResponse:
        """
        @summary 商业化移动屏三方app领卡校验
        
        @param request: CheckThirdRightSendPlanRequest
        @return: CheckThirdRightSendPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CheckThirdRightSendPlanHeaders()
        return self.check_third_right_send_plan_with_options(request, headers, runtime)

    async def check_third_right_send_plan_async(
        self,
        request: ali_genieiap__1__0_models.CheckThirdRightSendPlanRequest,
    ) -> ali_genieiap__1__0_models.CheckThirdRightSendPlanResponse:
        """
        @summary 商业化移动屏三方app领卡校验
        
        @param request: CheckThirdRightSendPlanRequest
        @return: CheckThirdRightSendPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CheckThirdRightSendPlanHeaders()
        return await self.check_third_right_send_plan_with_options_async(request, headers, runtime)

    def create_reminder_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.CreateReminderRequest,
        headers: ali_genieiap__1__0_models.CreateReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.CreateReminderResponse:
        """
        @summary 创建提醒
        
        @param tmp_req: CreateReminderRequest
        @param headers: CreateReminderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReminderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CreateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CreateReminderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_reminder_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.CreateReminderRequest,
        headers: ali_genieiap__1__0_models.CreateReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.CreateReminderResponse:
        """
        @summary 创建提醒
        
        @param tmp_req: CreateReminderRequest
        @param headers: CreateReminderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReminderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CreateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CreateReminderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_reminder(
        self,
        request: ali_genieiap__1__0_models.CreateReminderRequest,
    ) -> ali_genieiap__1__0_models.CreateReminderResponse:
        """
        @summary 创建提醒
        
        @param request: CreateReminderRequest
        @return: CreateReminderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CreateReminderHeaders()
        return self.create_reminder_with_options(request, headers, runtime)

    async def create_reminder_async(
        self,
        request: ali_genieiap__1__0_models.CreateReminderRequest,
    ) -> ali_genieiap__1__0_models.CreateReminderResponse:
        """
        @summary 创建提醒
        
        @param request: CreateReminderRequest
        @return: CreateReminderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CreateReminderHeaders()
        return await self.create_reminder_with_options_async(request, headers, runtime)

    def delete_reminder_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.DeleteReminderRequest,
        headers: ali_genieiap__1__0_models.DeleteReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.DeleteReminderResponse:
        """
        @summary 删除提醒
        
        @param tmp_req: DeleteReminderRequest
        @param headers: DeleteReminderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteReminderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.DeleteReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.DeleteReminderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_reminder_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.DeleteReminderRequest,
        headers: ali_genieiap__1__0_models.DeleteReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.DeleteReminderResponse:
        """
        @summary 删除提醒
        
        @param tmp_req: DeleteReminderRequest
        @param headers: DeleteReminderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteReminderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.DeleteReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.DeleteReminderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_reminder(
        self,
        request: ali_genieiap__1__0_models.DeleteReminderRequest,
    ) -> ali_genieiap__1__0_models.DeleteReminderResponse:
        """
        @summary 删除提醒
        
        @param request: DeleteReminderRequest
        @return: DeleteReminderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.DeleteReminderHeaders()
        return self.delete_reminder_with_options(request, headers, runtime)

    async def delete_reminder_async(
        self,
        request: ali_genieiap__1__0_models.DeleteReminderRequest,
    ) -> ali_genieiap__1__0_models.DeleteReminderResponse:
        """
        @summary 删除提醒
        
        @param request: DeleteReminderRequest
        @return: DeleteReminderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.DeleteReminderHeaders()
        return await self.delete_reminder_with_options_async(request, headers, runtime)

    def get_account_for_app_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.GetAccountForAppRequest,
        headers: ali_genieiap__1__0_models.GetAccountForAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetAccountForAppResponse:
        """
        @summary 获取会员信息
        
        @param tmp_req: GetAccountForAppRequest
        @param headers: GetAccountForAppHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountForAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetAccountForAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountForApp',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/vip/account/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetAccountForAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_for_app_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.GetAccountForAppRequest,
        headers: ali_genieiap__1__0_models.GetAccountForAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetAccountForAppResponse:
        """
        @summary 获取会员信息
        
        @param tmp_req: GetAccountForAppRequest
        @param headers: GetAccountForAppHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountForAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetAccountForAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountForApp',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/vip/account/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetAccountForAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_for_app(
        self,
        request: ali_genieiap__1__0_models.GetAccountForAppRequest,
    ) -> ali_genieiap__1__0_models.GetAccountForAppResponse:
        """
        @summary 获取会员信息
        
        @param request: GetAccountForAppRequest
        @return: GetAccountForAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetAccountForAppHeaders()
        return self.get_account_for_app_with_options(request, headers, runtime)

    async def get_account_for_app_async(
        self,
        request: ali_genieiap__1__0_models.GetAccountForAppRequest,
    ) -> ali_genieiap__1__0_models.GetAccountForAppResponse:
        """
        @summary 获取会员信息
        
        @param request: GetAccountForAppRequest
        @return: GetAccountForAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetAccountForAppHeaders()
        return await self.get_account_for_app_with_options_async(request, headers, runtime)

    def get_bus_app_config_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.GetBusAppConfigRequest,
        headers: ali_genieiap__1__0_models.GetBusAppConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetBusAppConfigResponse:
        """
        @summary 获取应用配置
        
        @param tmp_req: GetBusAppConfigRequest
        @param headers: GetBusAppConfigHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBusAppConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetBusAppConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusAppConfig',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/app/config/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetBusAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bus_app_config_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.GetBusAppConfigRequest,
        headers: ali_genieiap__1__0_models.GetBusAppConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetBusAppConfigResponse:
        """
        @summary 获取应用配置
        
        @param tmp_req: GetBusAppConfigRequest
        @param headers: GetBusAppConfigHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBusAppConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetBusAppConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusAppConfig',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/app/config/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetBusAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bus_app_config(
        self,
        request: ali_genieiap__1__0_models.GetBusAppConfigRequest,
    ) -> ali_genieiap__1__0_models.GetBusAppConfigResponse:
        """
        @summary 获取应用配置
        
        @param request: GetBusAppConfigRequest
        @return: GetBusAppConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetBusAppConfigHeaders()
        return self.get_bus_app_config_with_options(request, headers, runtime)

    async def get_bus_app_config_async(
        self,
        request: ali_genieiap__1__0_models.GetBusAppConfigRequest,
    ) -> ali_genieiap__1__0_models.GetBusAppConfigResponse:
        """
        @summary 获取应用配置
        
        @param request: GetBusAppConfigRequest
        @return: GetBusAppConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetBusAppConfigHeaders()
        return await self.get_bus_app_config_with_options_async(request, headers, runtime)

    def get_phone_number_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.GetPhoneNumberRequest,
        headers: ali_genieiap__1__0_models.GetPhoneNumberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetPhoneNumberResponse:
        """
        @summary 用户手机号获取
        
        @param tmp_req: GetPhoneNumberRequest
        @param headers: GetPhoneNumberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhoneNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetPhoneNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneNumber',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/profile/phoneNumber',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_number_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.GetPhoneNumberRequest,
        headers: ali_genieiap__1__0_models.GetPhoneNumberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetPhoneNumberResponse:
        """
        @summary 用户手机号获取
        
        @param tmp_req: GetPhoneNumberRequest
        @param headers: GetPhoneNumberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhoneNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetPhoneNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneNumber',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/profile/phoneNumber',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_number(
        self,
        request: ali_genieiap__1__0_models.GetPhoneNumberRequest,
    ) -> ali_genieiap__1__0_models.GetPhoneNumberResponse:
        """
        @summary 用户手机号获取
        
        @param request: GetPhoneNumberRequest
        @return: GetPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetPhoneNumberHeaders()
        return self.get_phone_number_with_options(request, headers, runtime)

    async def get_phone_number_async(
        self,
        request: ali_genieiap__1__0_models.GetPhoneNumberRequest,
    ) -> ali_genieiap__1__0_models.GetPhoneNumberResponse:
        """
        @summary 用户手机号获取
        
        @param request: GetPhoneNumberRequest
        @return: GetPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetPhoneNumberHeaders()
        return await self.get_phone_number_with_options_async(request, headers, runtime)

    def get_reminder_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.GetReminderRequest,
        headers: ali_genieiap__1__0_models.GetReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetReminderResponse:
        """
        @summary 查询提醒
        
        @param tmp_req: GetReminderRequest
        @param headers: GetReminderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetReminderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetReminderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reminder_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.GetReminderRequest,
        headers: ali_genieiap__1__0_models.GetReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetReminderResponse:
        """
        @summary 查询提醒
        
        @param tmp_req: GetReminderRequest
        @param headers: GetReminderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetReminderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetReminderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reminder(
        self,
        request: ali_genieiap__1__0_models.GetReminderRequest,
    ) -> ali_genieiap__1__0_models.GetReminderResponse:
        """
        @summary 查询提醒
        
        @param request: GetReminderRequest
        @return: GetReminderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetReminderHeaders()
        return self.get_reminder_with_options(request, headers, runtime)

    async def get_reminder_async(
        self,
        request: ali_genieiap__1__0_models.GetReminderRequest,
    ) -> ali_genieiap__1__0_models.GetReminderResponse:
        """
        @summary 查询提醒
        
        @param request: GetReminderRequest
        @return: GetReminderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetReminderHeaders()
        return await self.get_reminder_with_options_async(request, headers, runtime)

    def list_reminders_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.ListRemindersRequest,
        headers: ali_genieiap__1__0_models.ListRemindersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.ListRemindersResponse:
        """
        @summary 查询提醒列表
        
        @param tmp_req: ListRemindersRequest
        @param headers: ListRemindersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRemindersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.ListRemindersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReminders',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.ListRemindersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_reminders_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.ListRemindersRequest,
        headers: ali_genieiap__1__0_models.ListRemindersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.ListRemindersResponse:
        """
        @summary 查询提醒列表
        
        @param tmp_req: ListRemindersRequest
        @param headers: ListRemindersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRemindersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.ListRemindersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReminders',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.ListRemindersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_reminders(
        self,
        request: ali_genieiap__1__0_models.ListRemindersRequest,
    ) -> ali_genieiap__1__0_models.ListRemindersResponse:
        """
        @summary 查询提醒列表
        
        @param request: ListRemindersRequest
        @return: ListRemindersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.ListRemindersHeaders()
        return self.list_reminders_with_options(request, headers, runtime)

    async def list_reminders_async(
        self,
        request: ali_genieiap__1__0_models.ListRemindersRequest,
    ) -> ali_genieiap__1__0_models.ListRemindersResponse:
        """
        @summary 查询提醒列表
        
        @param request: ListRemindersRequest
        @return: ListRemindersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.ListRemindersHeaders()
        return await self.list_reminders_with_options_async(request, headers, runtime)

    def pull_cashier_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.PullCashierRequest,
        headers: ali_genieiap__1__0_models.PullCashierHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.PullCashierResponse:
        """
        @summary 拉取收银台
        
        @param tmp_req: PullCashierRequest
        @param headers: PullCashierHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PullCashierResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.PullCashierShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullCashier',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/pull/cashier/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.PullCashierResponse(),
            self.call_api(params, req, runtime)
        )

    async def pull_cashier_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.PullCashierRequest,
        headers: ali_genieiap__1__0_models.PullCashierHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.PullCashierResponse:
        """
        @summary 拉取收银台
        
        @param tmp_req: PullCashierRequest
        @param headers: PullCashierHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PullCashierResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.PullCashierShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullCashier',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/pull/cashier/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.PullCashierResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pull_cashier(
        self,
        request: ali_genieiap__1__0_models.PullCashierRequest,
    ) -> ali_genieiap__1__0_models.PullCashierResponse:
        """
        @summary 拉取收银台
        
        @param request: PullCashierRequest
        @return: PullCashierResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.PullCashierHeaders()
        return self.pull_cashier_with_options(request, headers, runtime)

    async def pull_cashier_async(
        self,
        request: ali_genieiap__1__0_models.PullCashierRequest,
    ) -> ali_genieiap__1__0_models.PullCashierResponse:
        """
        @summary 拉取收银台
        
        @param request: PullCashierRequest
        @return: PullCashierResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.PullCashierHeaders()
        return await self.pull_cashier_with_options_async(request, headers, runtime)

    def push_notifications_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.PushNotificationsRequest,
        headers: ali_genieiap__1__0_models.PushNotificationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.PushNotificationsResponse:
        """
        @summary 猫精系统消息推送
        
        @param tmp_req: PushNotificationsRequest
        @param headers: PushNotificationsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushNotificationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.PushNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not UtilClient.is_unset(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushNotifications',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/notifications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.PushNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_notifications_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.PushNotificationsRequest,
        headers: ali_genieiap__1__0_models.PushNotificationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.PushNotificationsResponse:
        """
        @summary 猫精系统消息推送
        
        @param tmp_req: PushNotificationsRequest
        @param headers: PushNotificationsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushNotificationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.PushNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not UtilClient.is_unset(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushNotifications',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/notifications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.PushNotificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_notifications(
        self,
        request: ali_genieiap__1__0_models.PushNotificationsRequest,
    ) -> ali_genieiap__1__0_models.PushNotificationsResponse:
        """
        @summary 猫精系统消息推送
        
        @param request: PushNotificationsRequest
        @return: PushNotificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.PushNotificationsHeaders()
        return self.push_notifications_with_options(request, headers, runtime)

    async def push_notifications_async(
        self,
        request: ali_genieiap__1__0_models.PushNotificationsRequest,
    ) -> ali_genieiap__1__0_models.PushNotificationsResponse:
        """
        @summary 猫精系统消息推送
        
        @param request: PushNotificationsRequest
        @return: PushNotificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.PushNotificationsHeaders()
        return await self.push_notifications_with_options_async(request, headers, runtime)

    def send_notifications_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.SendNotificationsRequest,
        headers: ali_genieiap__1__0_models.SendNotificationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.SendNotificationsResponse:
        """
        @summary 消息推送服务（普通版）
        
        @param tmp_req: SendNotificationsRequest
        @param headers: SendNotificationsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendNotificationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.SendNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not UtilClient.is_unset(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendNotifications',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/general/notifications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.SendNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_notifications_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.SendNotificationsRequest,
        headers: ali_genieiap__1__0_models.SendNotificationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.SendNotificationsResponse:
        """
        @summary 消息推送服务（普通版）
        
        @param tmp_req: SendNotificationsRequest
        @param headers: SendNotificationsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendNotificationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.SendNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not UtilClient.is_unset(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendNotifications',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/general/notifications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.SendNotificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_notifications(
        self,
        request: ali_genieiap__1__0_models.SendNotificationsRequest,
    ) -> ali_genieiap__1__0_models.SendNotificationsResponse:
        """
        @summary 消息推送服务（普通版）
        
        @param request: SendNotificationsRequest
        @return: SendNotificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.SendNotificationsHeaders()
        return self.send_notifications_with_options(request, headers, runtime)

    async def send_notifications_async(
        self,
        request: ali_genieiap__1__0_models.SendNotificationsRequest,
    ) -> ali_genieiap__1__0_models.SendNotificationsResponse:
        """
        @summary 消息推送服务（普通版）
        
        @param request: SendNotificationsRequest
        @return: SendNotificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.SendNotificationsHeaders()
        return await self.send_notifications_with_options_async(request, headers, runtime)

    def third_immediate_msg_push_with_options(
        self,
        request: ali_genieiap__1__0_models.ThirdImmediateMsgPushRequest,
        headers: ali_genieiap__1__0_models.ThirdImmediateMsgPushHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.ThirdImmediateMsgPushResponse:
        """
        @summary 三方即时信息数据变更事件推送
        
        @param request: ThirdImmediateMsgPushRequest
        @param headers: ThirdImmediateMsgPushHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ThirdImmediateMsgPushResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.change_detail):
            query['ChangeDetail'] = request.change_detail
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.psg_ids):
            query['PsgIds'] = request.psg_ids
        if not UtilClient.is_unset(request.traffic_change_type):
            query['TrafficChangeType'] = request.traffic_change_type
        if not UtilClient.is_unset(request.traffic_change_type_desc):
            query['TrafficChangeTypeDesc'] = request.traffic_change_type_desc
        if not UtilClient.is_unset(request.traffic_journey_ids):
            query['TrafficJourneyIds'] = request.traffic_journey_ids
        if not UtilClient.is_unset(request.traffic_sub_order_ids):
            query['TrafficSubOrderIds'] = request.traffic_sub_order_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ThirdImmediateMsgPush',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/thirdImmediateMsgPush',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.ThirdImmediateMsgPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def third_immediate_msg_push_with_options_async(
        self,
        request: ali_genieiap__1__0_models.ThirdImmediateMsgPushRequest,
        headers: ali_genieiap__1__0_models.ThirdImmediateMsgPushHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.ThirdImmediateMsgPushResponse:
        """
        @summary 三方即时信息数据变更事件推送
        
        @param request: ThirdImmediateMsgPushRequest
        @param headers: ThirdImmediateMsgPushHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ThirdImmediateMsgPushResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.change_detail):
            query['ChangeDetail'] = request.change_detail
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.psg_ids):
            query['PsgIds'] = request.psg_ids
        if not UtilClient.is_unset(request.traffic_change_type):
            query['TrafficChangeType'] = request.traffic_change_type
        if not UtilClient.is_unset(request.traffic_change_type_desc):
            query['TrafficChangeTypeDesc'] = request.traffic_change_type_desc
        if not UtilClient.is_unset(request.traffic_journey_ids):
            query['TrafficJourneyIds'] = request.traffic_journey_ids
        if not UtilClient.is_unset(request.traffic_sub_order_ids):
            query['TrafficSubOrderIds'] = request.traffic_sub_order_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ThirdImmediateMsgPush',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/thirdImmediateMsgPush',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.ThirdImmediateMsgPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def third_immediate_msg_push(
        self,
        request: ali_genieiap__1__0_models.ThirdImmediateMsgPushRequest,
    ) -> ali_genieiap__1__0_models.ThirdImmediateMsgPushResponse:
        """
        @summary 三方即时信息数据变更事件推送
        
        @param request: ThirdImmediateMsgPushRequest
        @return: ThirdImmediateMsgPushResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.ThirdImmediateMsgPushHeaders()
        return self.third_immediate_msg_push_with_options(request, headers, runtime)

    async def third_immediate_msg_push_async(
        self,
        request: ali_genieiap__1__0_models.ThirdImmediateMsgPushRequest,
    ) -> ali_genieiap__1__0_models.ThirdImmediateMsgPushResponse:
        """
        @summary 三方即时信息数据变更事件推送
        
        @param request: ThirdImmediateMsgPushRequest
        @return: ThirdImmediateMsgPushResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.ThirdImmediateMsgPushHeaders()
        return await self.third_immediate_msg_push_with_options_async(request, headers, runtime)

    def update_reminder_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.UpdateReminderRequest,
        headers: ali_genieiap__1__0_models.UpdateReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.UpdateReminderResponse:
        """
        @summary 更新提醒
        
        @param tmp_req: UpdateReminderRequest
        @param headers: UpdateReminderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateReminderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.UpdateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.UpdateReminderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_reminder_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.UpdateReminderRequest,
        headers: ali_genieiap__1__0_models.UpdateReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.UpdateReminderResponse:
        """
        @summary 更新提醒
        
        @param tmp_req: UpdateReminderRequest
        @param headers: UpdateReminderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateReminderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.UpdateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/reminder/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.UpdateReminderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_reminder(
        self,
        request: ali_genieiap__1__0_models.UpdateReminderRequest,
    ) -> ali_genieiap__1__0_models.UpdateReminderResponse:
        """
        @summary 更新提醒
        
        @param request: UpdateReminderRequest
        @return: UpdateReminderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.UpdateReminderHeaders()
        return self.update_reminder_with_options(request, headers, runtime)

    async def update_reminder_async(
        self,
        request: ali_genieiap__1__0_models.UpdateReminderRequest,
    ) -> ali_genieiap__1__0_models.UpdateReminderResponse:
        """
        @summary 更新提醒
        
        @param request: UpdateReminderRequest
        @return: UpdateReminderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.UpdateReminderHeaders()
        return await self.update_reminder_with_options_async(request, headers, runtime)

    def video_app_report_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.VideoAppReportRequest,
        headers: ali_genieiap__1__0_models.VideoAppReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.VideoAppReportResponse:
        """
        @summary 视频类应用会员信息上报
        
        @param tmp_req: VideoAppReportRequest
        @param headers: VideoAppReportHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAppReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.VideoAppReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoAppReport',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/vip/use/video/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.VideoAppReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_app_report_with_options_async(
        self,
        tmp_req: ali_genieiap__1__0_models.VideoAppReportRequest,
        headers: ali_genieiap__1__0_models.VideoAppReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.VideoAppReportResponse:
        """
        @summary 视频类应用会员信息上报
        
        @param tmp_req: VideoAppReportRequest
        @param headers: VideoAppReportHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAppReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.VideoAppReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoAppReport',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/vip/use/video/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.VideoAppReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_app_report(
        self,
        request: ali_genieiap__1__0_models.VideoAppReportRequest,
    ) -> ali_genieiap__1__0_models.VideoAppReportResponse:
        """
        @summary 视频类应用会员信息上报
        
        @param request: VideoAppReportRequest
        @return: VideoAppReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.VideoAppReportHeaders()
        return self.video_app_report_with_options(request, headers, runtime)

    async def video_app_report_async(
        self,
        request: ali_genieiap__1__0_models.VideoAppReportRequest,
    ) -> ali_genieiap__1__0_models.VideoAppReportResponse:
        """
        @summary 视频类应用会员信息上报
        
        @param request: VideoAppReportRequest
        @return: VideoAppReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.VideoAppReportHeaders()
        return await self.video_app_report_with_options_async(request, headers, runtime)

    def wake_up_app_with_options(
        self,
        request: ali_genieiap__1__0_models.WakeUpAppRequest,
        headers: ali_genieiap__1__0_models.WakeUpAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.WakeUpAppResponse:
        """
        @summary 猫精应用唤起
        
        @param request: WakeUpAppRequest
        @param headers: WakeUpAppHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: WakeUpAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_debug):
            body['IsDebug'] = request.is_debug
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.target_info):
            body['TargetInfo'] = request.target_info
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WakeUpApp',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/wakeup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.WakeUpAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def wake_up_app_with_options_async(
        self,
        request: ali_genieiap__1__0_models.WakeUpAppRequest,
        headers: ali_genieiap__1__0_models.WakeUpAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.WakeUpAppResponse:
        """
        @summary 猫精应用唤起
        
        @param request: WakeUpAppRequest
        @param headers: WakeUpAppHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: WakeUpAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_debug):
            body['IsDebug'] = request.is_debug
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.target_info):
            body['TargetInfo'] = request.target_info
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WakeUpApp',
            version='iap_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/iap/wakeup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.WakeUpAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def wake_up_app(
        self,
        request: ali_genieiap__1__0_models.WakeUpAppRequest,
    ) -> ali_genieiap__1__0_models.WakeUpAppResponse:
        """
        @summary 猫精应用唤起
        
        @param request: WakeUpAppRequest
        @return: WakeUpAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.WakeUpAppHeaders()
        return self.wake_up_app_with_options(request, headers, runtime)

    async def wake_up_app_async(
        self,
        request: ali_genieiap__1__0_models.WakeUpAppRequest,
    ) -> ali_genieiap__1__0_models.WakeUpAppResponse:
        """
        @summary 猫精应用唤起
        
        @param request: WakeUpAppRequest
        @return: WakeUpAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.WakeUpAppHeaders()
        return await self.wake_up_app_with_options_async(request, headers, runtime)
