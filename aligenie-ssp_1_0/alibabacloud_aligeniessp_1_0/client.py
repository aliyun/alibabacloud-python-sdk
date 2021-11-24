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

    def list_device_id_by_identitys(
        self,
        request: ali_geniessp__1__0_models.ListDeviceIdByIdentitysRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceIdByIdentitysResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceIdByIdentitysHeaders()
        return self.list_device_id_by_identitys_with_options(request, headers, runtime)

    async def list_device_id_by_identitys_async(
        self,
        request: ali_geniessp__1__0_models.ListDeviceIdByIdentitysRequest,
    ) -> ali_geniessp__1__0_models.ListDeviceIdByIdentitysResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceIdByIdentitysHeaders()
        return await self.list_device_id_by_identitys_with_options_async(request, headers, runtime)

    def list_device_id_by_identitys_with_options(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceIdByIdentitysRequest,
        headers: ali_geniessp__1__0_models.ListDeviceIdByIdentitysHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceIdByIdentitysResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceIdByIdentitysShrinkRequest()
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
            action='ListDeviceIdByIdentitys',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceIdByIdentitys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceIdByIdentitysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_id_by_identitys_with_options_async(
        self,
        tmp_req: ali_geniessp__1__0_models.ListDeviceIdByIdentitysRequest,
        headers: ali_geniessp__1__0_models.ListDeviceIdByIdentitysHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.ListDeviceIdByIdentitysResponse:
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceIdByIdentitysShrinkRequest()
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
            action='ListDeviceIdByIdentitys',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ssp/listDeviceIdByIdentitys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceIdByIdentitysResponse(),
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
