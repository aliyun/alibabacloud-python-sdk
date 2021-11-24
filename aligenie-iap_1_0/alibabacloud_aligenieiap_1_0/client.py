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

    def create_reminder(
        self,
        request: ali_genieiap__1__0_models.CreateReminderRequest,
    ) -> ali_genieiap__1__0_models.CreateReminderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CreateReminderHeaders()
        return self.create_reminder_with_options(request, headers, runtime)

    async def create_reminder_async(
        self,
        request: ali_genieiap__1__0_models.CreateReminderRequest,
    ) -> ali_genieiap__1__0_models.CreateReminderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CreateReminderHeaders()
        return await self.create_reminder_with_options_async(request, headers, runtime)

    def create_reminder_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.CreateReminderRequest,
        headers: ali_genieiap__1__0_models.CreateReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.CreateReminderResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CreateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CreateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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

    def delete_reminder(
        self,
        request: ali_genieiap__1__0_models.DeleteReminderRequest,
    ) -> ali_genieiap__1__0_models.DeleteReminderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.DeleteReminderHeaders()
        return self.delete_reminder_with_options(request, headers, runtime)

    async def delete_reminder_async(
        self,
        request: ali_genieiap__1__0_models.DeleteReminderRequest,
    ) -> ali_genieiap__1__0_models.DeleteReminderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.DeleteReminderHeaders()
        return await self.delete_reminder_with_options_async(request, headers, runtime)

    def delete_reminder_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.DeleteReminderRequest,
        headers: ali_genieiap__1__0_models.DeleteReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.DeleteReminderResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.DeleteReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.DeleteReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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

    def get_phone_number(
        self,
        request: ali_genieiap__1__0_models.GetPhoneNumberRequest,
    ) -> ali_genieiap__1__0_models.GetPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetPhoneNumberHeaders()
        return self.get_phone_number_with_options(request, headers, runtime)

    async def get_phone_number_async(
        self,
        request: ali_genieiap__1__0_models.GetPhoneNumberRequest,
    ) -> ali_genieiap__1__0_models.GetPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetPhoneNumberHeaders()
        return await self.get_phone_number_with_options_async(request, headers, runtime)

    def get_phone_number_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.GetPhoneNumberRequest,
        headers: ali_genieiap__1__0_models.GetPhoneNumberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetPhoneNumberResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetPhoneNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetPhoneNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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

    def get_reminder(
        self,
        request: ali_genieiap__1__0_models.GetReminderRequest,
    ) -> ali_genieiap__1__0_models.GetReminderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetReminderHeaders()
        return self.get_reminder_with_options(request, headers, runtime)

    async def get_reminder_async(
        self,
        request: ali_genieiap__1__0_models.GetReminderRequest,
    ) -> ali_genieiap__1__0_models.GetReminderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetReminderHeaders()
        return await self.get_reminder_with_options_async(request, headers, runtime)

    def get_reminder_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.GetReminderRequest,
        headers: ali_genieiap__1__0_models.GetReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.GetReminderResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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

    def list_reminders(
        self,
        request: ali_genieiap__1__0_models.ListRemindersRequest,
    ) -> ali_genieiap__1__0_models.ListRemindersResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.ListRemindersHeaders()
        return self.list_reminders_with_options(request, headers, runtime)

    async def list_reminders_async(
        self,
        request: ali_genieiap__1__0_models.ListRemindersRequest,
    ) -> ali_genieiap__1__0_models.ListRemindersResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.ListRemindersHeaders()
        return await self.list_reminders_with_options_async(request, headers, runtime)

    def list_reminders_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.ListRemindersRequest,
        headers: ali_genieiap__1__0_models.ListRemindersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.ListRemindersResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.ListRemindersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.ListRemindersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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

    def push_notifications(
        self,
        request: ali_genieiap__1__0_models.PushNotificationsRequest,
    ) -> ali_genieiap__1__0_models.PushNotificationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.PushNotificationsHeaders()
        return self.push_notifications_with_options(request, headers, runtime)

    async def push_notifications_async(
        self,
        request: ali_genieiap__1__0_models.PushNotificationsRequest,
    ) -> ali_genieiap__1__0_models.PushNotificationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.PushNotificationsHeaders()
        return await self.push_notifications_with_options_async(request, headers, runtime)

    def push_notifications_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.PushNotificationsRequest,
        headers: ali_genieiap__1__0_models.PushNotificationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.PushNotificationsResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.PushNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.notification_unicast_request), 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.tenant_info), 'TenantInfo', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.PushNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.notification_unicast_request), 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.tenant_info), 'TenantInfo', 'json')
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

    def send_notifications(
        self,
        request: ali_genieiap__1__0_models.SendNotificationsRequest,
    ) -> ali_genieiap__1__0_models.SendNotificationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.SendNotificationsHeaders()
        return self.send_notifications_with_options(request, headers, runtime)

    async def send_notifications_async(
        self,
        request: ali_genieiap__1__0_models.SendNotificationsRequest,
    ) -> ali_genieiap__1__0_models.SendNotificationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.SendNotificationsHeaders()
        return await self.send_notifications_with_options_async(request, headers, runtime)

    def send_notifications_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.SendNotificationsRequest,
        headers: ali_genieiap__1__0_models.SendNotificationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.SendNotificationsResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.SendNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.notification_unicast_request), 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.tenant_info), 'TenantInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.SendNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.notification_unicast_request), 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.tenant_info), 'TenantInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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

    def update_reminder(
        self,
        request: ali_genieiap__1__0_models.UpdateReminderRequest,
    ) -> ali_genieiap__1__0_models.UpdateReminderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.UpdateReminderHeaders()
        return self.update_reminder_with_options(request, headers, runtime)

    async def update_reminder_async(
        self,
        request: ali_genieiap__1__0_models.UpdateReminderRequest,
    ) -> ali_genieiap__1__0_models.UpdateReminderResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.UpdateReminderHeaders()
        return await self.update_reminder_with_options_async(request, headers, runtime)

    def update_reminder_with_options(
        self,
        tmp_req: ali_genieiap__1__0_models.UpdateReminderRequest,
        headers: ali_genieiap__1__0_models.UpdateReminderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.UpdateReminderResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.UpdateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.UpdateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.payload), 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
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

    def wake_up_app(
        self,
        request: ali_genieiap__1__0_models.WakeUpAppRequest,
    ) -> ali_genieiap__1__0_models.WakeUpAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.WakeUpAppHeaders()
        return self.wake_up_app_with_options(request, headers, runtime)

    async def wake_up_app_async(
        self,
        request: ali_genieiap__1__0_models.WakeUpAppRequest,
    ) -> ali_genieiap__1__0_models.WakeUpAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.WakeUpAppHeaders()
        return await self.wake_up_app_with_options_async(request, headers, runtime)

    def wake_up_app_with_options(
        self,
        request: ali_genieiap__1__0_models.WakeUpAppRequest,
        headers: ali_genieiap__1__0_models.WakeUpAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieiap__1__0_models.WakeUpAppResponse:
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
