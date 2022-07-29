# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligeniessp_1_0 import models as ali_geniessp__1__0_models
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

    def add_and_remove_favorite_content(
        self,
        request: ali_geniessp__1__0_models.AddAndRemoveFavoriteContentRequest,
    ) -> ali_geniessp__1__0_models.AddAndRemoveFavoriteContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AddAndRemoveFavoriteContentHeaders()
        return self.add_and_remove_favorite_content_with_options(request, headers, runtime)

    async def add_and_remove_favorite_content_async(
        self,
        request: ali_geniessp__1__0_models.AddAndRemoveFavoriteContentRequest,
    ) -> ali_geniessp__1__0_models.AddAndRemoveFavoriteContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AddAndRemoveFavoriteContentHeaders()
        return await self.add_and_remove_favorite_content_with_options_async(request, headers, runtime)

    def add_and_remove_favorite_content_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.AddAndRemoveFavoriteContentRequest,
        headers: ali_geniessp__1__0_models.AddAndRemoveFavoriteContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.AddAndRemoveFavoriteContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.AddAndRemoveFavoriteContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_add_and_remove_favorite_content_request):
            request.open_add_and_remove_favorite_content_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_add_and_remove_favorite_content_request), 'OpenAddAndRemoveFavoriteContentRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_add_and_remove_favorite_content_request_shrink):
            body['OpenAddAndRemoveFavoriteContentRequest'] = request.open_add_and_remove_favorite_content_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAndRemoveFavoriteContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/AddAndRemoveFavoriteContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AddAndRemoveFavoriteContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_and_remove_favorite_content_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.AddAndRemoveFavoriteContentRequest,
        headers: ali_geniessp__1__0_models.AddAndRemoveFavoriteContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.AddAndRemoveFavoriteContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.AddAndRemoveFavoriteContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_add_and_remove_favorite_content_request):
            request.open_add_and_remove_favorite_content_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_add_and_remove_favorite_content_request), 'OpenAddAndRemoveFavoriteContentRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_add_and_remove_favorite_content_request_shrink):
            body['OpenAddAndRemoveFavoriteContentRequest'] = request.open_add_and_remove_favorite_content_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAndRemoveFavoriteContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/AddAndRemoveFavoriteContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AddAndRemoveFavoriteContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sub(
        self,
        request: ali_geniessp__1__0_models.AddSubRequest,
    ) -> ali_geniessp__1__0_models.AddSubResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AddSubHeaders()
        return self.add_sub_with_options(request, headers, runtime)

    async def add_sub_async(
        self,
        request: ali_geniessp__1__0_models.AddSubRequest,
    ) -> ali_geniessp__1__0_models.AddSubResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AddSubHeaders()
        return await self.add_sub_with_options_async(request, headers, runtime)

    def add_sub_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.AddSubRequest,
        headers: ali_geniessp__1__0_models.AddSubHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.AddSubResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.AddSubShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_subscription_info_request):
            request.add_subscription_info_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.add_subscription_info_request), 'AddSubscriptionInfoRequest', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.add_subscription_info_request_shrink):
            query['AddSubscriptionInfoRequest'] = request.add_subscription_info_request_shrink
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
            action='AddSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/addSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AddSubResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sub_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.AddSubRequest,
        headers: ali_geniessp__1__0_models.AddSubHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.AddSubResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.AddSubShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_subscription_info_request):
            request.add_subscription_info_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.add_subscription_info_request), 'AddSubscriptionInfoRequest', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.add_subscription_info_request_shrink):
            query['AddSubscriptionInfoRequest'] = request.add_subscription_info_request_shrink
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
            action='AddSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/addSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AddSubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_auth_code_bind_for_ext(
        self,
        request: ali_geniessp__1__0_models.CheckAuthCodeBindForExtRequest,
    ) -> ali_geniessp__1__0_models.CheckAuthCodeBindForExtResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CheckAuthCodeBindForExtHeaders()
        return self.check_auth_code_bind_for_ext_with_options(request, headers, runtime)

    async def check_auth_code_bind_for_ext_async(
        self,
        request: ali_geniessp__1__0_models.CheckAuthCodeBindForExtRequest,
    ) -> ali_geniessp__1__0_models.CheckAuthCodeBindForExtResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CheckAuthCodeBindForExtHeaders()
        return await self.check_auth_code_bind_for_ext_with_options_async(request, headers, runtime)

    def check_auth_code_bind_for_ext_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.CheckAuthCodeBindForExtRequest,
        headers: ali_geniessp__1__0_models.CheckAuthCodeBindForExtHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.CheckAuthCodeBindForExtResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CheckAuthCodeBindForExtShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
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
            action='CheckAuthCodeBindForExt',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/checkAuthCodeBindForExt',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CheckAuthCodeBindForExtResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_auth_code_bind_for_ext_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.CheckAuthCodeBindForExtRequest,
        headers: ali_geniessp__1__0_models.CheckAuthCodeBindForExtHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.CheckAuthCodeBindForExtResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CheckAuthCodeBindForExtShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
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
            action='CheckAuthCodeBindForExt',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/checkAuthCodeBindForExt',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CheckAuthCodeBindForExtResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alarm(
        self,
        request: ali_geniessp__1__0_models.CreateAlarmRequest,
    ) -> ali_geniessp__1__0_models.CreateAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreateAlarmHeaders()
        return self.create_alarm_with_options(request, headers, runtime)

    async def create_alarm_async(
        self,
        request: ali_geniessp__1__0_models.CreateAlarmRequest,
    ) -> ali_geniessp__1__0_models.CreateAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreateAlarmHeaders()
        return await self.create_alarm_with_options_async(request, headers, runtime)

    def create_alarm_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.CreateAlarmRequest,
        headers: ali_geniessp__1__0_models.CreateAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.CreateAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreateAlarmShrinkRequest()
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
            action='CreateAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/createAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alarm_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.CreateAlarmRequest,
        headers: ali_geniessp__1__0_models.CreateAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.CreateAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreateAlarmShrinkRequest()
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
            action='CreateAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/createAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_playing_list(
        self,
        request: ali_geniessp__1__0_models.CreatePlayingListRequest,
    ) -> ali_geniessp__1__0_models.CreatePlayingListResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreatePlayingListHeaders()
        return self.create_playing_list_with_options(request, headers, runtime)

    async def create_playing_list_async(
        self,
        request: ali_geniessp__1__0_models.CreatePlayingListRequest,
    ) -> ali_geniessp__1__0_models.CreatePlayingListResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreatePlayingListHeaders()
        return await self.create_playing_list_with_options_async(request, headers, runtime)

    def create_playing_list_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.CreatePlayingListRequest,
        headers: ali_geniessp__1__0_models.CreatePlayingListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.CreatePlayingListResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreatePlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_create_playing_list_request), 'OpenCreatePlayingListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/CreatePlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreatePlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_playing_list_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.CreatePlayingListRequest,
        headers: ali_geniessp__1__0_models.CreatePlayingListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.CreatePlayingListResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreatePlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_create_playing_list_request), 'OpenCreatePlayingListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/CreatePlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreatePlayingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedule_task(
        self,
        request: ali_geniessp__1__0_models.CreateScheduleTaskRequest,
    ) -> ali_geniessp__1__0_models.CreateScheduleTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreateScheduleTaskHeaders()
        return self.create_schedule_task_with_options(request, headers, runtime)

    async def create_schedule_task_async(
        self,
        request: ali_geniessp__1__0_models.CreateScheduleTaskRequest,
    ) -> ali_geniessp__1__0_models.CreateScheduleTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreateScheduleTaskHeaders()
        return await self.create_schedule_task_with_options_async(request, headers, runtime)

    def create_schedule_task_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.CreateScheduleTaskRequest,
        headers: ali_geniessp__1__0_models.CreateScheduleTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.CreateScheduleTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreateScheduleTaskShrinkRequest()
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
            action='CreateScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/CreateScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreateScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedule_task_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.CreateScheduleTaskRequest,
        headers: ali_geniessp__1__0_models.CreateScheduleTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.CreateScheduleTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreateScheduleTaskShrinkRequest()
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
            action='CreateScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/CreateScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreateScheduleTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alarms(
        self,
        request: ali_geniessp__1__0_models.DeleteAlarmsRequest,
    ) -> ali_geniessp__1__0_models.DeleteAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteAlarmsHeaders()
        return self.delete_alarms_with_options(request, headers, runtime)

    async def delete_alarms_async(
        self,
        request: ali_geniessp__1__0_models.DeleteAlarmsRequest,
    ) -> ali_geniessp__1__0_models.DeleteAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteAlarmsHeaders()
        return await self.delete_alarms_with_options_async(request, headers, runtime)

    def delete_alarms_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.DeleteAlarmsRequest,
        headers: ali_geniessp__1__0_models.DeleteAlarmsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.DeleteAlarmsResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeleteAlarmsShrinkRequest()
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
            action='DeleteAlarms',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/deleteAlarms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alarms_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.DeleteAlarmsRequest,
        headers: ali_geniessp__1__0_models.DeleteAlarmsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.DeleteAlarmsResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeleteAlarmsShrinkRequest()
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
            action='DeleteAlarms',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/deleteAlarms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schedule_task(
        self,
        request: ali_geniessp__1__0_models.DeleteScheduleTaskRequest,
    ) -> ali_geniessp__1__0_models.DeleteScheduleTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteScheduleTaskHeaders()
        return self.delete_schedule_task_with_options(request, headers, runtime)

    async def delete_schedule_task_async(
        self,
        request: ali_geniessp__1__0_models.DeleteScheduleTaskRequest,
    ) -> ali_geniessp__1__0_models.DeleteScheduleTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteScheduleTaskHeaders()
        return await self.delete_schedule_task_with_options_async(request, headers, runtime)

    def delete_schedule_task_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.DeleteScheduleTaskRequest,
        headers: ali_geniessp__1__0_models.DeleteScheduleTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.DeleteScheduleTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeleteScheduleTaskShrinkRequest()
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
            action='DeleteScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/DeleteScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schedule_task_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.DeleteScheduleTaskRequest,
        headers: ali_geniessp__1__0_models.DeleteScheduleTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.DeleteScheduleTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeleteScheduleTaskShrinkRequest()
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
            action='DeleteScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/DeleteScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteScheduleTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sub(
        self,
        request: ali_geniessp__1__0_models.DeleteSubRequest,
    ) -> ali_geniessp__1__0_models.DeleteSubResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteSubHeaders()
        return self.delete_sub_with_options(request, headers, runtime)

    async def delete_sub_async(
        self,
        request: ali_geniessp__1__0_models.DeleteSubRequest,
    ) -> ali_geniessp__1__0_models.DeleteSubResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteSubHeaders()
        return await self.delete_sub_with_options_async(request, headers, runtime)

    def delete_sub_with_options(
        self,
        request: ali_geniessp__1__0_models.DeleteSubRequest,
        headers: ali_geniessp__1__0_models.DeleteSubHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.DeleteSubResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_id):
            query['SubId'] = request.sub_id
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
            action='DeleteSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/deleteSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteSubResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sub_with_options_async(
        self,
        request: ali_geniessp__1__0_models.DeleteSubRequest,
        headers: ali_geniessp__1__0_models.DeleteSubHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.DeleteSubResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_id):
            query['SubId'] = request.sub_id
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
            action='DeleteSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/deleteSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteSubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def device_control(
        self,
        request: ali_geniessp__1__0_models.DeviceControlRequest,
    ) -> ali_geniessp__1__0_models.DeviceControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeviceControlHeaders()
        return self.device_control_with_options(request, headers, runtime)

    async def device_control_async(
        self,
        request: ali_geniessp__1__0_models.DeviceControlRequest,
    ) -> ali_geniessp__1__0_models.DeviceControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeviceControlHeaders()
        return await self.device_control_with_options_async(request, headers, runtime)

    def device_control_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.DeviceControlRequest,
        headers: ali_geniessp__1__0_models.DeviceControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.DeviceControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeviceControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.control_request):
            request.control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.control_request), 'ControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not UtilClient.is_unset(request.control_request_shrink):
            body['ControlRequest'] = request.control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeviceControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/control',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeviceControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def device_control_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.DeviceControlRequest,
        headers: ali_geniessp__1__0_models.DeviceControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.DeviceControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeviceControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.control_request):
            request.control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.control_request), 'ControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not UtilClient.is_unset(request.control_request_shrink):
            body['ControlRequest'] = request.control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeviceControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/control',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeviceControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alarm(
        self,
        request: ali_geniessp__1__0_models.GetAlarmRequest,
    ) -> ali_geniessp__1__0_models.GetAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlarmHeaders()
        return self.get_alarm_with_options(request, headers, runtime)

    async def get_alarm_async(
        self,
        request: ali_geniessp__1__0_models.GetAlarmRequest,
    ) -> ali_geniessp__1__0_models.GetAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlarmHeaders()
        return await self.get_alarm_with_options_async(request, headers, runtime)

    def get_alarm_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetAlarmRequest,
        headers: ali_geniessp__1__0_models.GetAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetAlarmShrinkRequest()
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
            action='GetAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alarm_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetAlarmRequest,
        headers: ali_geniessp__1__0_models.GetAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetAlarmShrinkRequest()
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
            action='GetAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_album(
        self,
        request: ali_geniessp__1__0_models.GetAlbumRequest,
    ) -> ali_geniessp__1__0_models.GetAlbumResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlbumHeaders()
        return self.get_album_with_options(request, headers, runtime)

    async def get_album_async(
        self,
        request: ali_geniessp__1__0_models.GetAlbumRequest,
    ) -> ali_geniessp__1__0_models.GetAlbumResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlbumHeaders()
        return await self.get_album_with_options_async(request, headers, runtime)

    def get_album_with_options(
        self,
        request: ali_geniessp__1__0_models.GetAlbumRequest,
        headers: ali_geniessp__1__0_models.GetAlbumHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetAlbumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
            action='GetAlbum',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetAlbum',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlbumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_album_with_options_async(
        self,
        request: ali_geniessp__1__0_models.GetAlbumRequest,
        headers: ali_geniessp__1__0_models.GetAlbumHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetAlbumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
            action='GetAlbum',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetAlbum',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlbumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_album_detail_by_id(
        self,
        request: ali_geniessp__1__0_models.GetAlbumDetailByIdRequest,
    ) -> ali_geniessp__1__0_models.GetAlbumDetailByIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlbumDetailByIdHeaders()
        return self.get_album_detail_by_id_with_options(request, headers, runtime)

    async def get_album_detail_by_id_async(
        self,
        request: ali_geniessp__1__0_models.GetAlbumDetailByIdRequest,
    ) -> ali_geniessp__1__0_models.GetAlbumDetailByIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlbumDetailByIdHeaders()
        return await self.get_album_detail_by_id_with_options_async(request, headers, runtime)

    def get_album_detail_by_id_with_options(
        self,
        request: ali_geniessp__1__0_models.GetAlbumDetailByIdRequest,
        headers: ali_geniessp__1__0_models.GetAlbumDetailByIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetAlbumDetailByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.album_id):
            query['AlbumId'] = request.album_id
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
            action='GetAlbumDetailById',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getAlbumDetailById',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlbumDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_album_detail_by_id_with_options_async(
        self,
        request: ali_geniessp__1__0_models.GetAlbumDetailByIdRequest,
        headers: ali_geniessp__1__0_models.GetAlbumDetailByIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetAlbumDetailByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.album_id):
            query['AlbumId'] = request.album_id
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
            action='GetAlbumDetailById',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getAlbumDetailById',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlbumDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_code_enhance(
        self,
        request: ali_geniessp__1__0_models.GetCodeEnhanceRequest,
    ) -> ali_geniessp__1__0_models.GetCodeEnhanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCodeEnhanceHeaders()
        return self.get_code_enhance_with_options(request, headers, runtime)

    async def get_code_enhance_async(
        self,
        request: ali_geniessp__1__0_models.GetCodeEnhanceRequest,
    ) -> ali_geniessp__1__0_models.GetCodeEnhanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCodeEnhanceHeaders()
        return await self.get_code_enhance_with_options_async(request, headers, runtime)

    def get_code_enhance_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetCodeEnhanceRequest,
        headers: ali_geniessp__1__0_models.GetCodeEnhanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetCodeEnhanceResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCodeEnhanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.channel_info):
            request.channel_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.channel_info), 'ChannelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
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
            action='GetCodeEnhance',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getCodeEnhance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCodeEnhanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_code_enhance_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetCodeEnhanceRequest,
        headers: ali_geniessp__1__0_models.GetCodeEnhanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetCodeEnhanceResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCodeEnhanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.channel_info):
            request.channel_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.channel_info), 'ChannelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
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
            action='GetCodeEnhance',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getCodeEnhance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCodeEnhanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_content(
        self,
        request: ali_geniessp__1__0_models.GetContentRequest,
    ) -> ali_geniessp__1__0_models.GetContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetContentHeaders()
        return self.get_content_with_options(request, headers, runtime)

    async def get_content_async(
        self,
        request: ali_geniessp__1__0_models.GetContentRequest,
    ) -> ali_geniessp__1__0_models.GetContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetContentHeaders()
        return await self.get_content_with_options_async(request, headers, runtime)

    def get_content_with_options(
        self,
        request: ali_geniessp__1__0_models.GetContentRequest,
        headers: ali_geniessp__1__0_models.GetContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
            action='GetContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_content_with_options_async(
        self,
        request: ali_geniessp__1__0_models.GetContentRequest,
        headers: ali_geniessp__1__0_models.GetContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
            action='GetContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_current_playing_item(
        self,
        request: ali_geniessp__1__0_models.GetCurrentPlayingItemRequest,
    ) -> ali_geniessp__1__0_models.GetCurrentPlayingItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCurrentPlayingItemHeaders()
        return self.get_current_playing_item_with_options(request, headers, runtime)

    async def get_current_playing_item_async(
        self,
        request: ali_geniessp__1__0_models.GetCurrentPlayingItemRequest,
    ) -> ali_geniessp__1__0_models.GetCurrentPlayingItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCurrentPlayingItemHeaders()
        return await self.get_current_playing_item_with_options_async(request, headers, runtime)

    def get_current_playing_item_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetCurrentPlayingItemRequest,
        headers: ali_geniessp__1__0_models.GetCurrentPlayingItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetCurrentPlayingItemResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCurrentPlayingItemShrinkRequest()
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
            action='GetCurrentPlayingItem',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetCurrentPlayingItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCurrentPlayingItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_current_playing_item_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetCurrentPlayingItemRequest,
        headers: ali_geniessp__1__0_models.GetCurrentPlayingItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetCurrentPlayingItemResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCurrentPlayingItemShrinkRequest()
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
            action='GetCurrentPlayingItem',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetCurrentPlayingItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCurrentPlayingItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_current_playing_list(
        self,
        request: ali_geniessp__1__0_models.GetCurrentPlayingListRequest,
    ) -> ali_geniessp__1__0_models.GetCurrentPlayingListResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCurrentPlayingListHeaders()
        return self.get_current_playing_list_with_options(request, headers, runtime)

    async def get_current_playing_list_async(
        self,
        request: ali_geniessp__1__0_models.GetCurrentPlayingListRequest,
    ) -> ali_geniessp__1__0_models.GetCurrentPlayingListResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCurrentPlayingListHeaders()
        return await self.get_current_playing_list_with_options_async(request, headers, runtime)

    def get_current_playing_list_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetCurrentPlayingListRequest,
        headers: ali_geniessp__1__0_models.GetCurrentPlayingListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetCurrentPlayingListResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCurrentPlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_query_play_list_request):
            request.open_query_play_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_query_play_list_request), 'OpenQueryPlayListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_query_play_list_request_shrink):
            body['OpenQueryPlayListRequest'] = request.open_query_play_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCurrentPlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetCurrentPlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCurrentPlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_current_playing_list_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetCurrentPlayingListRequest,
        headers: ali_geniessp__1__0_models.GetCurrentPlayingListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetCurrentPlayingListResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCurrentPlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_query_play_list_request):
            request.open_query_play_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_query_play_list_request), 'OpenQueryPlayListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_query_play_list_request_shrink):
            body['OpenQueryPlayListRequest'] = request.open_query_play_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCurrentPlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetCurrentPlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCurrentPlayingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_basic_info(
        self,
        request: ali_geniessp__1__0_models.GetDeviceBasicInfoRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceBasicInfoHeaders()
        return self.get_device_basic_info_with_options(request, headers, runtime)

    async def get_device_basic_info_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceBasicInfoRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceBasicInfoHeaders()
        return await self.get_device_basic_info_with_options_async(request, headers, runtime)

    def get_device_basic_info_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceBasicInfoRequest,
        headers: ali_geniessp__1__0_models.GetDeviceBasicInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceBasicInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
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
            action='GetDeviceBasicInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceBasicInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_basic_info_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceBasicInfoRequest,
        headers: ali_geniessp__1__0_models.GetDeviceBasicInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceBasicInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
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
            action='GetDeviceBasicInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceBasicInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_id_by_identity(
        self,
        request: ali_geniessp__1__0_models.GetDeviceIdByIdentityRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders()
        return self.get_device_id_by_identity_with_options(request, headers, runtime)

    async def get_device_id_by_identity_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceIdByIdentityRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders()
        return await self.get_device_id_by_identity_with_options_async(request, headers, runtime)

    def get_device_id_by_identity_with_options(
        self,
        request: ali_geniessp__1__0_models.GetDeviceIdByIdentityRequest,
        headers: ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.identity_id):
            query['IdentityId'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
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
            action='GetDeviceIdByIdentity',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceIdByIdentity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_id_by_identity_with_options_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceIdByIdentityRequest,
        headers: ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.identity_id):
            query['IdentityId'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
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
            action='GetDeviceIdByIdentity',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceIdByIdentity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_setting(
        self,
        request: ali_geniessp__1__0_models.GetDeviceSettingRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceSettingHeaders()
        return self.get_device_setting_with_options(request, headers, runtime)

    async def get_device_setting_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceSettingRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceSettingHeaders()
        return await self.get_device_setting_with_options_async(request, headers, runtime)

    def get_device_setting_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceSettingRequest,
        headers: ali_geniessp__1__0_models.GetDeviceSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceSettingResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
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
            action='GetDeviceSetting',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceSetting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_setting_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceSettingRequest,
        headers: ali_geniessp__1__0_models.GetDeviceSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceSettingResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
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
            action='GetDeviceSetting',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceSetting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_status_detail(
        self,
        request: ali_geniessp__1__0_models.GetDeviceStatusDetailRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceStatusDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceStatusDetailHeaders()
        return self.get_device_status_detail_with_options(request, headers, runtime)

    async def get_device_status_detail_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceStatusDetailRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceStatusDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceStatusDetailHeaders()
        return await self.get_device_status_detail_with_options_async(request, headers, runtime)

    def get_device_status_detail_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceStatusDetailRequest,
        headers: ali_geniessp__1__0_models.GetDeviceStatusDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceStatusDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceStatusDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
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
            action='GetDeviceStatusDetail',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceStatusDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceStatusDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_status_detail_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceStatusDetailRequest,
        headers: ali_geniessp__1__0_models.GetDeviceStatusDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceStatusDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceStatusDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
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
            action='GetDeviceStatusDetail',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceStatusDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceStatusDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_status_info(
        self,
        request: ali_geniessp__1__0_models.GetDeviceStatusInfoRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceStatusInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceStatusInfoHeaders()
        return self.get_device_status_info_with_options(request, headers, runtime)

    async def get_device_status_info_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceStatusInfoRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceStatusInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceStatusInfoHeaders()
        return await self.get_device_status_info_with_options_async(request, headers, runtime)

    def get_device_status_info_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceStatusInfoRequest,
        headers: ali_geniessp__1__0_models.GetDeviceStatusInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceStatusInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceStatusInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
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
            action='GetDeviceStatusInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceStatusInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceStatusInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_status_info_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceStatusInfoRequest,
        headers: ali_geniessp__1__0_models.GetDeviceStatusInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceStatusInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceStatusInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
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
            action='GetDeviceStatusInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceStatusInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceStatusInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_tag(
        self,
        request: ali_geniessp__1__0_models.GetDeviceTagRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceTagHeaders()
        return self.get_device_tag_with_options(request, headers, runtime)

    async def get_device_tag_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceTagRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceTagHeaders()
        return await self.get_device_tag_with_options_async(request, headers, runtime)

    def get_device_tag_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceTagRequest,
        headers: ali_geniessp__1__0_models.GetDeviceTagHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceTagResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
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
            action='GetDeviceTag',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceTag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_tag_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetDeviceTagRequest,
        headers: ali_geniessp__1__0_models.GetDeviceTagHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceTagResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
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
            action='GetDeviceTag',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getDeviceTag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schedule_task(
        self,
        request: ali_geniessp__1__0_models.GetScheduleTaskRequest,
    ) -> ali_geniessp__1__0_models.GetScheduleTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetScheduleTaskHeaders()
        return self.get_schedule_task_with_options(request, headers, runtime)

    async def get_schedule_task_async(
        self,
        request: ali_geniessp__1__0_models.GetScheduleTaskRequest,
    ) -> ali_geniessp__1__0_models.GetScheduleTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetScheduleTaskHeaders()
        return await self.get_schedule_task_with_options_async(request, headers, runtime)

    def get_schedule_task_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetScheduleTaskRequest,
        headers: ali_geniessp__1__0_models.GetScheduleTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetScheduleTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetScheduleTaskShrinkRequest()
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
            action='GetScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schedule_task_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetScheduleTaskRequest,
        headers: ali_geniessp__1__0_models.GetScheduleTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetScheduleTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetScheduleTaskShrinkRequest()
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
            action='GetScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/GetScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetScheduleTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_unread_message_count(
        self,
        request: ali_geniessp__1__0_models.GetUnreadMessageCountRequest,
    ) -> ali_geniessp__1__0_models.GetUnreadMessageCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetUnreadMessageCountHeaders()
        return self.get_unread_message_count_with_options(request, headers, runtime)

    async def get_unread_message_count_async(
        self,
        request: ali_geniessp__1__0_models.GetUnreadMessageCountRequest,
    ) -> ali_geniessp__1__0_models.GetUnreadMessageCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetUnreadMessageCountHeaders()
        return await self.get_unread_message_count_with_options_async(request, headers, runtime)

    def get_unread_message_count_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetUnreadMessageCountRequest,
        headers: ali_geniessp__1__0_models.GetUnreadMessageCountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetUnreadMessageCountResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetUnreadMessageCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
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
            action='GetUnreadMessageCount',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getUnreadMessageCount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetUnreadMessageCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_unread_message_count_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetUnreadMessageCountRequest,
        headers: ali_geniessp__1__0_models.GetUnreadMessageCountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetUnreadMessageCountResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetUnreadMessageCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
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
            action='GetUnreadMessageCount',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getUnreadMessageCount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetUnreadMessageCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_by_device_id(
        self,
        request: ali_geniessp__1__0_models.GetUserByDeviceIdRequest,
    ) -> ali_geniessp__1__0_models.GetUserByDeviceIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetUserByDeviceIdHeaders()
        return self.get_user_by_device_id_with_options(request, headers, runtime)

    async def get_user_by_device_id_async(
        self,
        request: ali_geniessp__1__0_models.GetUserByDeviceIdRequest,
    ) -> ali_geniessp__1__0_models.GetUserByDeviceIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetUserByDeviceIdHeaders()
        return await self.get_user_by_device_id_with_options_async(request, headers, runtime)

    def get_user_by_device_id_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.GetUserByDeviceIdRequest,
        headers: ali_geniessp__1__0_models.GetUserByDeviceIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetUserByDeviceIdResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetUserByDeviceIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
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
            action='GetUserByDeviceId',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getUserByDeviceId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetUserByDeviceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_by_device_id_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.GetUserByDeviceIdRequest,
        headers: ali_geniessp__1__0_models.GetUserByDeviceIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetUserByDeviceIdResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetUserByDeviceIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
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
            action='GetUserByDeviceId',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/getUserByDeviceId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetUserByDeviceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def index_control_playing_list(
        self,
        request: ali_geniessp__1__0_models.IndexControlPlayingListRequest,
    ) -> ali_geniessp__1__0_models.IndexControlPlayingListResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.IndexControlPlayingListHeaders()
        return self.index_control_playing_list_with_options(request, headers, runtime)

    async def index_control_playing_list_async(
        self,
        request: ali_geniessp__1__0_models.IndexControlPlayingListRequest,
    ) -> ali_geniessp__1__0_models.IndexControlPlayingListResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.IndexControlPlayingListHeaders()
        return await self.index_control_playing_list_with_options_async(request, headers, runtime)

    def index_control_playing_list_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.IndexControlPlayingListRequest,
        headers: ali_geniessp__1__0_models.IndexControlPlayingListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.IndexControlPlayingListResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.IndexControlPlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_index_control_request):
            request.open_index_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_index_control_request), 'OpenIndexControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_index_control_request_shrink):
            body['OpenIndexControlRequest'] = request.open_index_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IndexControlPlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/IndexControlPlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.IndexControlPlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def index_control_playing_list_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.IndexControlPlayingListRequest,
        headers: ali_geniessp__1__0_models.IndexControlPlayingListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.IndexControlPlayingListResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.IndexControlPlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_index_control_request):
            request.open_index_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_index_control_request), 'OpenIndexControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_index_control_request_shrink):
            body['OpenIndexControlRequest'] = request.open_index_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IndexControlPlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/IndexControlPlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.IndexControlPlayingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarms(
        self,
        request: ali_geniessp__1__0_models.ListAlarmsRequest,
    ) -> ali_geniessp__1__0_models.ListAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlarmsHeaders()
        return self.list_alarms_with_options(request, headers, runtime)

    async def list_alarms_async(
        self,
        request: ali_geniessp__1__0_models.ListAlarmsRequest,
    ) -> ali_geniessp__1__0_models.ListAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlarmsHeaders()
        return await self.list_alarms_with_options_async(request, headers, runtime)

    def list_alarms_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListAlarmsRequest,
        headers: ali_geniessp__1__0_models.ListAlarmsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListAlarmsResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListAlarmsShrinkRequest()
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
            action='ListAlarms',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarms_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListAlarmsRequest,
        headers: ali_geniessp__1__0_models.ListAlarmsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListAlarmsResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListAlarmsShrinkRequest()
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
            action='ListAlarms',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_album_detail(
        self,
        request: ali_geniessp__1__0_models.ListAlbumDetailRequest,
    ) -> ali_geniessp__1__0_models.ListAlbumDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlbumDetailHeaders()
        return self.list_album_detail_with_options(request, headers, runtime)

    async def list_album_detail_async(
        self,
        request: ali_geniessp__1__0_models.ListAlbumDetailRequest,
    ) -> ali_geniessp__1__0_models.ListAlbumDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlbumDetailHeaders()
        return await self.list_album_detail_with_options_async(request, headers, runtime)

    def list_album_detail_with_options(
        self,
        request: ali_geniessp__1__0_models.ListAlbumDetailRequest,
        headers: ali_geniessp__1__0_models.ListAlbumDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListAlbumDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='ListAlbumDetail',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListAlbumDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlbumDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_album_detail_with_options_async(
        self,
        request: ali_geniessp__1__0_models.ListAlbumDetailRequest,
        headers: ali_geniessp__1__0_models.ListAlbumDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListAlbumDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='ListAlbumDetail',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListAlbumDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlbumDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_album_is_added(
        self,
        request: ali_geniessp__1__0_models.ListAlbumIsAddedRequest,
    ) -> ali_geniessp__1__0_models.ListAlbumIsAddedResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlbumIsAddedHeaders()
        return self.list_album_is_added_with_options(request, headers, runtime)

    async def list_album_is_added_async(
        self,
        request: ali_geniessp__1__0_models.ListAlbumIsAddedRequest,
    ) -> ali_geniessp__1__0_models.ListAlbumIsAddedResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlbumIsAddedHeaders()
        return await self.list_album_is_added_with_options_async(request, headers, runtime)

    def list_album_is_added_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListAlbumIsAddedRequest,
        headers: ali_geniessp__1__0_models.ListAlbumIsAddedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListAlbumIsAddedResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListAlbumIsAddedShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.album_id_list):
            request.album_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.album_id_list, 'AlbumIdList', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.album_id_list_shrink):
            query['AlbumIdList'] = request.album_id_list_shrink
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
            action='ListAlbumIsAdded',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listAlbumIsAdded',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlbumIsAddedResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_album_is_added_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListAlbumIsAddedRequest,
        headers: ali_geniessp__1__0_models.ListAlbumIsAddedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListAlbumIsAddedResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListAlbumIsAddedShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.album_id_list):
            request.album_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.album_id_list, 'AlbumIdList', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.album_id_list_shrink):
            query['AlbumIdList'] = request.album_id_list_shrink
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
            action='ListAlbumIsAdded',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listAlbumIsAdded',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlbumIsAddedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cate_content(
        self,
        request: ali_geniessp__1__0_models.ListCateContentRequest,
    ) -> ali_geniessp__1__0_models.ListCateContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCateContentHeaders()
        return self.list_cate_content_with_options(request, headers, runtime)

    async def list_cate_content_async(
        self,
        request: ali_geniessp__1__0_models.ListCateContentRequest,
    ) -> ali_geniessp__1__0_models.ListCateContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCateContentHeaders()
        return await self.list_cate_content_with_options_async(request, headers, runtime)

    def list_cate_content_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListCateContentRequest,
        headers: ali_geniessp__1__0_models.ListCateContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListCateContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListCateContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request), 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCateContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListCateContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCateContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cate_content_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListCateContentRequest,
        headers: ali_geniessp__1__0_models.ListCateContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListCateContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListCateContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request), 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCateContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListCateContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCateContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cate_info(
        self,
        request: ali_geniessp__1__0_models.ListCateInfoRequest,
    ) -> ali_geniessp__1__0_models.ListCateInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCateInfoHeaders()
        return self.list_cate_info_with_options(request, headers, runtime)

    async def list_cate_info_async(
        self,
        request: ali_geniessp__1__0_models.ListCateInfoRequest,
    ) -> ali_geniessp__1__0_models.ListCateInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCateInfoHeaders()
        return await self.list_cate_info_with_options_async(request, headers, runtime)

    def list_cate_info_with_options(
        self,
        request: ali_geniessp__1__0_models.ListCateInfoRequest,
        headers: ali_geniessp__1__0_models.ListCateInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListCateInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
            action='ListCateInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListCateInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cate_info_with_options_async(
        self,
        request: ali_geniessp__1__0_models.ListCateInfoRequest,
        headers: ali_geniessp__1__0_models.ListCateInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListCateInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
            action='ListCateInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListCateInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_common_cate_first_floor(
        self,
        request: ali_geniessp__1__0_models.ListCommonCateFirstFloorRequest,
    ) -> ali_geniessp__1__0_models.ListCommonCateFirstFloorResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCommonCateFirstFloorHeaders()
        return self.list_common_cate_first_floor_with_options(request, headers, runtime)

    async def list_common_cate_first_floor_async(
        self,
        request: ali_geniessp__1__0_models.ListCommonCateFirstFloorRequest,
    ) -> ali_geniessp__1__0_models.ListCommonCateFirstFloorResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCommonCateFirstFloorHeaders()
        return await self.list_common_cate_first_floor_with_options_async(request, headers, runtime)

    def list_common_cate_first_floor_with_options(
        self,
        request: ali_geniessp__1__0_models.ListCommonCateFirstFloorRequest,
        headers: ali_geniessp__1__0_models.ListCommonCateFirstFloorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListCommonCateFirstFloorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
            action='ListCommonCateFirstFloor',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListCommonCateFirstFloor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCommonCateFirstFloorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_common_cate_first_floor_with_options_async(
        self,
        request: ali_geniessp__1__0_models.ListCommonCateFirstFloorRequest,
        headers: ali_geniessp__1__0_models.ListCommonCateFirstFloorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListCommonCateFirstFloorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
            action='ListCommonCateFirstFloor',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListCommonCateFirstFloor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCommonCateFirstFloorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_common_cate_second_floor(
        self,
        request: ali_geniessp__1__0_models.ListCommonCateSecondFloorRequest,
    ) -> ali_geniessp__1__0_models.ListCommonCateSecondFloorResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCommonCateSecondFloorHeaders()
        return self.list_common_cate_second_floor_with_options(request, headers, runtime)

    async def list_common_cate_second_floor_async(
        self,
        request: ali_geniessp__1__0_models.ListCommonCateSecondFloorRequest,
    ) -> ali_geniessp__1__0_models.ListCommonCateSecondFloorResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCommonCateSecondFloorHeaders()
        return await self.list_common_cate_second_floor_with_options_async(request, headers, runtime)

    def list_common_cate_second_floor_with_options(
        self,
        request: ali_geniessp__1__0_models.ListCommonCateSecondFloorRequest,
        headers: ali_geniessp__1__0_models.ListCommonCateSecondFloorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListCommonCateSecondFloorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_cate_id):
            query['ParentCateId'] = request.parent_cate_id
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
            action='ListCommonCateSecondFloor',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListCommonCateSecondFloor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCommonCateSecondFloorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_common_cate_second_floor_with_options_async(
        self,
        request: ali_geniessp__1__0_models.ListCommonCateSecondFloorRequest,
        headers: ali_geniessp__1__0_models.ListCommonCateSecondFloorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListCommonCateSecondFloorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_cate_id):
            query['ParentCateId'] = request.parent_cate_id
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
            action='ListCommonCateSecondFloor',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListCommonCateSecondFloor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCommonCateSecondFloorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_basic_info(
        self,
        request: ali_geniessp__1__0_models.ListDeviceBasicInfoRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceBasicInfoHeaders()
        return self.list_device_basic_info_with_options(request, headers, runtime)

    async def list_device_basic_info_async(
        self,
        request: ali_geniessp__1__0_models.ListDeviceBasicInfoRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceBasicInfoHeaders()
        return await self.list_device_basic_info_with_options_async(request, headers, runtime)

    def list_device_basic_info_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceBasicInfoRequest,
        headers: ali_geniessp__1__0_models.ListDeviceBasicInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceBasicInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_infos):
            request.device_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_infos), 'DeviceInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_infos_shrink):
            query['DeviceInfos'] = request.device_infos_shrink
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
            action='ListDeviceBasicInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceBasicInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_basic_info_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceBasicInfoRequest,
        headers: ali_geniessp__1__0_models.ListDeviceBasicInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceBasicInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_infos):
            request.device_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_infos), 'DeviceInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_infos_shrink):
            query['DeviceInfos'] = request.device_infos_shrink
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
            action='ListDeviceBasicInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceBasicInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_by_user_id(
        self,
        request: ali_geniessp__1__0_models.ListDeviceByUserIdRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceByUserIdHeaders()
        return self.list_device_by_user_id_with_options(request, headers, runtime)

    async def list_device_by_user_id_async(
        self,
        request: ali_geniessp__1__0_models.ListDeviceByUserIdRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceByUserIdHeaders()
        return await self.list_device_by_user_id_with_options_async(request, headers, runtime)

    def list_device_by_user_id_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceByUserIdRequest,
        headers: ali_geniessp__1__0_models.ListDeviceByUserIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceByUserIdResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceByUserIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
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
            action='ListDeviceByUserId',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceByUserId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_by_user_id_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceByUserIdRequest,
        headers: ali_geniessp__1__0_models.ListDeviceByUserIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceByUserIdResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceByUserIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
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
            action='ListDeviceByUserId',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceByUserId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_by_user_id_and_chanel(
        self,
        request: ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelHeaders()
        return self.list_device_by_user_id_and_chanel_with_options(request, headers, runtime)

    async def list_device_by_user_id_and_chanel_async(
        self,
        request: ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelHeaders()
        return await self.list_device_by_user_id_and_chanel_with_options_async(request, headers, runtime)

    def list_device_by_user_id_and_chanel_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelRequest,
        headers: ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.channel_info):
            request.channel_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.channel_info), 'ChannelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
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
            action='ListDeviceByUserIdAndChanel',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceByUserIdAndChanel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_by_user_id_and_chanel_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelRequest,
        headers: ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.channel_info):
            request.channel_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.channel_info), 'ChannelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
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
            action='ListDeviceByUserIdAndChanel',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceByUserIdAndChanel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_id_by_identities(
        self,
        request: ali_geniessp__1__0_models.ListDeviceIdByIdentitiesRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceIdByIdentitiesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceIdByIdentitiesHeaders()
        return self.list_device_id_by_identities_with_options(request, headers, runtime)

    async def list_device_id_by_identities_async(
        self,
        request: ali_geniessp__1__0_models.ListDeviceIdByIdentitiesRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceIdByIdentitiesResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceIdByIdentitiesHeaders()
        return await self.list_device_id_by_identities_with_options_async(request, headers, runtime)

    def list_device_id_by_identities_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceIdByIdentitiesRequest,
        headers: ali_geniessp__1__0_models.ListDeviceIdByIdentitiesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceIdByIdentitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceIdByIdentitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.identity_ids):
            request.identity_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.identity_ids, 'IdentityIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.identity_ids_shrink):
            query['IdentityIds'] = request.identity_ids_shrink
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
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
            action='ListDeviceIdByIdentities',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceIdByIdentities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceIdByIdentitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_id_by_identities_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceIdByIdentitiesRequest,
        headers: ali_geniessp__1__0_models.ListDeviceIdByIdentitiesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceIdByIdentitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceIdByIdentitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.identity_ids):
            request.identity_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.identity_ids, 'IdentityIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.identity_ids_shrink):
            query['IdentityIds'] = request.identity_ids_shrink
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
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
            action='ListDeviceIdByIdentities',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceIdByIdentities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceIdByIdentitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_music(
        self,
        request: ali_geniessp__1__0_models.ListMusicRequest,
    ) -> ali_geniessp__1__0_models.ListMusicResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListMusicHeaders()
        return self.list_music_with_options(request, headers, runtime)

    async def list_music_async(
        self,
        request: ali_geniessp__1__0_models.ListMusicRequest,
    ) -> ali_geniessp__1__0_models.ListMusicResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListMusicHeaders()
        return await self.list_music_with_options_async(request, headers, runtime)

    def list_music_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListMusicRequest,
        headers: ali_geniessp__1__0_models.ListMusicHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListMusicResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListMusicShrinkRequest()
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
            action='ListMusic',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListMusicResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_music_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListMusicRequest,
        headers: ali_geniessp__1__0_models.ListMusicHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListMusicResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListMusicShrinkRequest()
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
            action='ListMusic',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListMusicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_play_history(
        self,
        request: ali_geniessp__1__0_models.ListPlayHistoryRequest,
    ) -> ali_geniessp__1__0_models.ListPlayHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListPlayHistoryHeaders()
        return self.list_play_history_with_options(request, headers, runtime)

    async def list_play_history_async(
        self,
        request: ali_geniessp__1__0_models.ListPlayHistoryRequest,
    ) -> ali_geniessp__1__0_models.ListPlayHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListPlayHistoryHeaders()
        return await self.list_play_history_with_options_async(request, headers, runtime)

    def list_play_history_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListPlayHistoryRequest,
        headers: ali_geniessp__1__0_models.ListPlayHistoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListPlayHistoryResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListPlayHistoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request), 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlayHistory',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListPlayHistory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListPlayHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_play_history_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListPlayHistoryRequest,
        headers: ali_geniessp__1__0_models.ListPlayHistoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListPlayHistoryResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListPlayHistoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request), 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlayHistory',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListPlayHistory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListPlayHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recommend_content(
        self,
        request: ali_geniessp__1__0_models.ListRecommendContentRequest,
    ) -> ali_geniessp__1__0_models.ListRecommendContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListRecommendContentHeaders()
        return self.list_recommend_content_with_options(request, headers, runtime)

    async def list_recommend_content_async(
        self,
        request: ali_geniessp__1__0_models.ListRecommendContentRequest,
    ) -> ali_geniessp__1__0_models.ListRecommendContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListRecommendContentHeaders()
        return await self.list_recommend_content_with_options_async(request, headers, runtime)

    def list_recommend_content_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListRecommendContentRequest,
        headers: ali_geniessp__1__0_models.ListRecommendContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListRecommendContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListRecommendContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request), 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecommendContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListRecommendContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListRecommendContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recommend_content_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListRecommendContentRequest,
        headers: ali_geniessp__1__0_models.ListRecommendContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListRecommendContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListRecommendContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request), 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecommendContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ListRecommendContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListRecommendContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub(
        self,
        request: ali_geniessp__1__0_models.ListSubRequest,
    ) -> ali_geniessp__1__0_models.ListSubResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubHeaders()
        return self.list_sub_with_options(request, headers, runtime)

    async def list_sub_async(
        self,
        request: ali_geniessp__1__0_models.ListSubRequest,
    ) -> ali_geniessp__1__0_models.ListSubResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubHeaders()
        return await self.list_sub_with_options_async(request, headers, runtime)

    def list_sub_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListSubRequest,
        headers: ali_geniessp__1__0_models.ListSubHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListSubResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListSubShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.page), 'Page', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
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
            action='ListSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListSubRequest,
        headers: ali_geniessp__1__0_models.ListSubHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListSubResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListSubShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.page), 'Page', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
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
            action='ListSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_album(
        self,
        request: ali_geniessp__1__0_models.ListSubAlbumRequest,
    ) -> ali_geniessp__1__0_models.ListSubAlbumResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubAlbumHeaders()
        return self.list_sub_album_with_options(request, headers, runtime)

    async def list_sub_album_async(
        self,
        request: ali_geniessp__1__0_models.ListSubAlbumRequest,
    ) -> ali_geniessp__1__0_models.ListSubAlbumResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubAlbumHeaders()
        return await self.list_sub_album_with_options_async(request, headers, runtime)

    def list_sub_album_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListSubAlbumRequest,
        headers: ali_geniessp__1__0_models.ListSubAlbumHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListSubAlbumResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListSubAlbumShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.query_subscription_album_request):
            request.query_subscription_album_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.query_subscription_album_request), 'QuerySubscriptionAlbumRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.query_subscription_album_request_shrink):
            query['QuerySubscriptionAlbumRequest'] = request.query_subscription_album_request_shrink
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
            action='ListSubAlbum',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listSubAlbum',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubAlbumResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_album_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListSubAlbumRequest,
        headers: ali_geniessp__1__0_models.ListSubAlbumHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListSubAlbumResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListSubAlbumShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.query_subscription_album_request):
            request.query_subscription_album_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.query_subscription_album_request), 'QuerySubscriptionAlbumRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.query_subscription_album_request_shrink):
            query['QuerySubscriptionAlbumRequest'] = request.query_subscription_album_request_shrink
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
            action='ListSubAlbum',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listSubAlbum',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubAlbumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscription_album_category(
        self,
        request: ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryRequest,
    ) -> ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryHeaders()
        return self.list_subscription_album_category_with_options(request, headers, runtime)

    async def list_subscription_album_category_async(
        self,
        request: ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryRequest,
    ) -> ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryHeaders()
        return await self.list_subscription_album_category_with_options_async(request, headers, runtime)

    def list_subscription_album_category_with_options(
        self,
        request: ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryRequest,
        headers: ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
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
            action='ListSubscriptionAlbumCategory',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listSubscriptionAlbumCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscription_album_category_with_options_async(
        self,
        request: ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryRequest,
        headers: ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
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
            action='ListSubscriptionAlbumCategory',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listSubscriptionAlbumCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_message(
        self,
        request: ali_geniessp__1__0_models.ListUserMessageRequest,
    ) -> ali_geniessp__1__0_models.ListUserMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListUserMessageHeaders()
        return self.list_user_message_with_options(request, headers, runtime)

    async def list_user_message_async(
        self,
        request: ali_geniessp__1__0_models.ListUserMessageRequest,
    ) -> ali_geniessp__1__0_models.ListUserMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListUserMessageHeaders()
        return await self.list_user_message_with_options_async(request, headers, runtime)

    def list_user_message_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListUserMessageRequest,
        headers: ali_geniessp__1__0_models.ListUserMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListUserMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListUserMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.before_time):
            query['BeforeTime'] = request.before_time
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
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
            action='ListUserMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listUserMessage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListUserMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_message_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListUserMessageRequest,
        headers: ali_geniessp__1__0_models.ListUserMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListUserMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListUserMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.before_time):
            query['BeforeTime'] = request.before_time
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
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
            action='ListUserMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listUserMessage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListUserMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def play_and_pause_control(
        self,
        request: ali_geniessp__1__0_models.PlayAndPauseControlRequest,
    ) -> ali_geniessp__1__0_models.PlayAndPauseControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PlayAndPauseControlHeaders()
        return self.play_and_pause_control_with_options(request, headers, runtime)

    async def play_and_pause_control_async(
        self,
        request: ali_geniessp__1__0_models.PlayAndPauseControlRequest,
    ) -> ali_geniessp__1__0_models.PlayAndPauseControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PlayAndPauseControlHeaders()
        return await self.play_and_pause_control_with_options_async(request, headers, runtime)

    def play_and_pause_control_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.PlayAndPauseControlRequest,
        headers: ali_geniessp__1__0_models.PlayAndPauseControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.PlayAndPauseControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PlayAndPauseControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_play_and_pause_control_param):
            request.open_play_and_pause_control_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_play_and_pause_control_param), 'OpenPlayAndPauseControlParam', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_play_and_pause_control_param_shrink):
            body['OpenPlayAndPauseControlParam'] = request.open_play_and_pause_control_param_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PlayAndPauseControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/PlayAndPauseControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PlayAndPauseControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def play_and_pause_control_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.PlayAndPauseControlRequest,
        headers: ali_geniessp__1__0_models.PlayAndPauseControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.PlayAndPauseControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PlayAndPauseControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_play_and_pause_control_param):
            request.open_play_and_pause_control_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_play_and_pause_control_param), 'OpenPlayAndPauseControlParam', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_play_and_pause_control_param_shrink):
            body['OpenPlayAndPauseControlParam'] = request.open_play_and_pause_control_param_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PlayAndPauseControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/PlayAndPauseControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PlayAndPauseControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def play_mode_control(
        self,
        request: ali_geniessp__1__0_models.PlayModeControlRequest,
    ) -> ali_geniessp__1__0_models.PlayModeControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PlayModeControlHeaders()
        return self.play_mode_control_with_options(request, headers, runtime)

    async def play_mode_control_async(
        self,
        request: ali_geniessp__1__0_models.PlayModeControlRequest,
    ) -> ali_geniessp__1__0_models.PlayModeControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PlayModeControlHeaders()
        return await self.play_mode_control_with_options_async(request, headers, runtime)

    def play_mode_control_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.PlayModeControlRequest,
        headers: ali_geniessp__1__0_models.PlayModeControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.PlayModeControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PlayModeControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_play_mode_control_request):
            request.open_play_mode_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_play_mode_control_request), 'OpenPlayModeControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_play_mode_control_request_shrink):
            body['OpenPlayModeControlRequest'] = request.open_play_mode_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PlayModeControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/PlayModeControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PlayModeControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def play_mode_control_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.PlayModeControlRequest,
        headers: ali_geniessp__1__0_models.PlayModeControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.PlayModeControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PlayModeControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_play_mode_control_request):
            request.open_play_mode_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_play_mode_control_request), 'OpenPlayModeControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_play_mode_control_request_shrink):
            body['OpenPlayModeControlRequest'] = request.open_play_mode_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PlayModeControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/PlayModeControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PlayModeControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def previous_and_next_control(
        self,
        request: ali_geniessp__1__0_models.PreviousAndNextControlRequest,
    ) -> ali_geniessp__1__0_models.PreviousAndNextControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PreviousAndNextControlHeaders()
        return self.previous_and_next_control_with_options(request, headers, runtime)

    async def previous_and_next_control_async(
        self,
        request: ali_geniessp__1__0_models.PreviousAndNextControlRequest,
    ) -> ali_geniessp__1__0_models.PreviousAndNextControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PreviousAndNextControlHeaders()
        return await self.previous_and_next_control_with_options_async(request, headers, runtime)

    def previous_and_next_control_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.PreviousAndNextControlRequest,
        headers: ali_geniessp__1__0_models.PreviousAndNextControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.PreviousAndNextControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PreviousAndNextControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_control_playing_list_request):
            request.open_control_playing_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_control_playing_list_request), 'OpenControlPlayingListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_control_playing_list_request_shrink):
            body['OpenControlPlayingListRequest'] = request.open_control_playing_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreviousAndNextControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/PreviousAndNextControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PreviousAndNextControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def previous_and_next_control_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.PreviousAndNextControlRequest,
        headers: ali_geniessp__1__0_models.PreviousAndNextControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.PreviousAndNextControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PreviousAndNextControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_control_playing_list_request):
            request.open_control_playing_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_control_playing_list_request), 'OpenControlPlayingListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_control_playing_list_request_shrink):
            body['OpenControlPlayingListRequest'] = request.open_control_playing_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreviousAndNextControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/PreviousAndNextControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PreviousAndNextControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def progress_control(
        self,
        request: ali_geniessp__1__0_models.ProgressControlRequest,
    ) -> ali_geniessp__1__0_models.ProgressControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ProgressControlHeaders()
        return self.progress_control_with_options(request, headers, runtime)

    async def progress_control_async(
        self,
        request: ali_geniessp__1__0_models.ProgressControlRequest,
    ) -> ali_geniessp__1__0_models.ProgressControlResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ProgressControlHeaders()
        return await self.progress_control_with_options_async(request, headers, runtime)

    def progress_control_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ProgressControlRequest,
        headers: ali_geniessp__1__0_models.ProgressControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ProgressControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ProgressControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_progress_control_request):
            request.open_progress_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_progress_control_request), 'OpenProgressControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_progress_control_request_shrink):
            body['OpenProgressControlRequest'] = request.open_progress_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProgressControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ProgressControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ProgressControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def progress_control_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ProgressControlRequest,
        headers: ali_geniessp__1__0_models.ProgressControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ProgressControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ProgressControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_progress_control_request):
            request.open_progress_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_progress_control_request), 'OpenProgressControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_progress_control_request_shrink):
            body['OpenProgressControlRequest'] = request.open_progress_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProgressControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/ProgressControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ProgressControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_music_type(
        self,
        request: ali_geniessp__1__0_models.QueryMusicTypeRequest,
    ) -> ali_geniessp__1__0_models.QueryMusicTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.QueryMusicTypeHeaders()
        return self.query_music_type_with_options(request, headers, runtime)

    async def query_music_type_async(
        self,
        request: ali_geniessp__1__0_models.QueryMusicTypeRequest,
    ) -> ali_geniessp__1__0_models.QueryMusicTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.QueryMusicTypeHeaders()
        return await self.query_music_type_with_options_async(request, headers, runtime)

    def query_music_type_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.QueryMusicTypeRequest,
        headers: ali_geniessp__1__0_models.QueryMusicTypeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.QueryMusicTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.QueryMusicTypeShrinkRequest()
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
            action='QueryMusicType',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/queryMusicType',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.QueryMusicTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_music_type_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.QueryMusicTypeRequest,
        headers: ali_geniessp__1__0_models.QueryMusicTypeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.QueryMusicTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.QueryMusicTypeShrinkRequest()
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
            action='QueryMusicType',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/queryMusicType',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.QueryMusicTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message(
        self,
        request: ali_geniessp__1__0_models.ReadMessageRequest,
    ) -> ali_geniessp__1__0_models.ReadMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ReadMessageHeaders()
        return self.read_message_with_options(request, headers, runtime)

    async def read_message_async(
        self,
        request: ali_geniessp__1__0_models.ReadMessageRequest,
    ) -> ali_geniessp__1__0_models.ReadMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ReadMessageHeaders()
        return await self.read_message_with_options_async(request, headers, runtime)

    def read_message_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ReadMessageRequest,
        headers: ali_geniessp__1__0_models.ReadMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ReadMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ReadMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
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
            action='ReadMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/readMessage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ReadMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ReadMessageRequest,
        headers: ali_geniessp__1__0_models.ReadMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ReadMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ReadMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
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
            action='ReadMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/readMessage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ReadMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_content(
        self,
        request: ali_geniessp__1__0_models.SearchContentRequest,
    ) -> ali_geniessp__1__0_models.SearchContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SearchContentHeaders()
        return self.search_content_with_options(request, headers, runtime)

    async def search_content_async(
        self,
        request: ali_geniessp__1__0_models.SearchContentRequest,
    ) -> ali_geniessp__1__0_models.SearchContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SearchContentHeaders()
        return await self.search_content_with_options_async(request, headers, runtime)

    def search_content_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.SearchContentRequest,
        headers: ali_geniessp__1__0_models.SearchContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.SearchContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SearchContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request), 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/SearchContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SearchContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_content_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.SearchContentRequest,
        headers: ali_geniessp__1__0_models.SearchContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.SearchContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SearchContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request), 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/SearchContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SearchContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: ali_geniessp__1__0_models.SendMessageRequest,
    ) -> ali_geniessp__1__0_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SendMessageHeaders()
        return self.send_message_with_options(request, headers, runtime)

    async def send_message_async(
        self,
        request: ali_geniessp__1__0_models.SendMessageRequest,
    ) -> ali_geniessp__1__0_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SendMessageHeaders()
        return await self.send_message_with_options_async(request, headers, runtime)

    def send_message_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.SendMessageRequest,
        headers: ali_geniessp__1__0_models.SendMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
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
            action='SendMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/sendMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.SendMessageRequest,
        headers: ali_geniessp__1__0_models.SendMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
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
            action='SendMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/sendMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_device_setting(
        self,
        request: ali_geniessp__1__0_models.SetDeviceSettingRequest,
    ) -> ali_geniessp__1__0_models.SetDeviceSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SetDeviceSettingHeaders()
        return self.set_device_setting_with_options(request, headers, runtime)

    async def set_device_setting_async(
        self,
        request: ali_geniessp__1__0_models.SetDeviceSettingRequest,
    ) -> ali_geniessp__1__0_models.SetDeviceSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SetDeviceSettingHeaders()
        return await self.set_device_setting_with_options_async(request, headers, runtime)

    def set_device_setting_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.SetDeviceSettingRequest,
        headers: ali_geniessp__1__0_models.SetDeviceSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.SetDeviceSettingResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SetDeviceSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDeviceSetting',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/setDeviceSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SetDeviceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_device_setting_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.SetDeviceSettingRequest,
        headers: ali_geniessp__1__0_models.SetDeviceSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.SetDeviceSettingResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SetDeviceSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDeviceSetting',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/setDeviceSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SetDeviceSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_device(
        self,
        request: ali_geniessp__1__0_models.UnbindDeviceRequest,
    ) -> ali_geniessp__1__0_models.UnbindDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.UnbindDeviceHeaders()
        return self.unbind_device_with_options(request, headers, runtime)

    async def unbind_device_async(
        self,
        request: ali_geniessp__1__0_models.UnbindDeviceRequest,
    ) -> ali_geniessp__1__0_models.UnbindDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.UnbindDeviceHeaders()
        return await self.unbind_device_with_options_async(request, headers, runtime)

    def unbind_device_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.UnbindDeviceRequest,
        headers: ali_geniessp__1__0_models.UnbindDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.UnbindDeviceResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.UnbindDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
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
            action='UnbindDevice',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/unbindDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.UnbindDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_device_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.UnbindDeviceRequest,
        headers: ali_geniessp__1__0_models.UnbindDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.UnbindDeviceResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.UnbindDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device_info), 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_info), 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
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
            action='UnbindDevice',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/unbindDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.UnbindDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alarm(
        self,
        request: ali_geniessp__1__0_models.UpdateAlarmRequest,
    ) -> ali_geniessp__1__0_models.UpdateAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.UpdateAlarmHeaders()
        return self.update_alarm_with_options(request, headers, runtime)

    async def update_alarm_async(
        self,
        request: ali_geniessp__1__0_models.UpdateAlarmRequest,
    ) -> ali_geniessp__1__0_models.UpdateAlarmResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.UpdateAlarmHeaders()
        return await self.update_alarm_with_options_async(request, headers, runtime)

    def update_alarm_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.UpdateAlarmRequest,
        headers: ali_geniessp__1__0_models.UpdateAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.UpdateAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.UpdateAlarmShrinkRequest()
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
            action='UpdateAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/updateAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.UpdateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alarm_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.UpdateAlarmRequest,
        headers: ali_geniessp__1__0_models.UpdateAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.UpdateAlarmResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.UpdateAlarmShrinkRequest()
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
            action='UpdateAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/updateAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.UpdateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )
