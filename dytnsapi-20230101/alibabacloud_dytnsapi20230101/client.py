# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dytnsapi20230101 import models as main_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dytnsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_number_hlrwith_options(
        self,
        request: main_models.DescribeNumberHLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNumberHLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNumberHLR',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNumberHLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_number_hlrwith_options_async(
        self,
        request: main_models.DescribeNumberHLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNumberHLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNumberHLR',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNumberHLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_number_hlr(
        self,
        request: main_models.DescribeNumberHLRRequest,
    ) -> main_models.DescribeNumberHLRResponse:
        runtime = RuntimeOptions()
        return self.describe_number_hlrwith_options(request, runtime)

    async def describe_number_hlr_async(
        self,
        request: main_models.DescribeNumberHLRRequest,
    ) -> main_models.DescribeNumberHLRResponse:
        runtime = RuntimeOptions()
        return await self.describe_number_hlrwith_options_async(request, runtime)

    def describe_number_mcc_mnc_with_options(
        self,
        request: main_models.DescribeNumberMccMncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNumberMccMncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNumberMccMnc',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNumberMccMncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_number_mcc_mnc_with_options_async(
        self,
        request: main_models.DescribeNumberMccMncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNumberMccMncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNumberMccMnc',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNumberMccMncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_number_mcc_mnc(
        self,
        request: main_models.DescribeNumberMccMncRequest,
    ) -> main_models.DescribeNumberMccMncResponse:
        runtime = RuntimeOptions()
        return self.describe_number_mcc_mnc_with_options(request, runtime)

    async def describe_number_mcc_mnc_async(
        self,
        request: main_models.DescribeNumberMccMncRequest,
    ) -> main_models.DescribeNumberMccMncResponse:
        runtime = RuntimeOptions()
        return await self.describe_number_mcc_mnc_with_options_async(request, runtime)

    def get_identification_result_with_options(
        self,
        request: main_models.GetIdentificationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentificationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentificationResult',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identification_result_with_options_async(
        self,
        request: main_models.GetIdentificationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentificationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentificationResult',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentificationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identification_result(
        self,
        request: main_models.GetIdentificationResultRequest,
    ) -> main_models.GetIdentificationResultResponse:
        runtime = RuntimeOptions()
        return self.get_identification_result_with_options(request, runtime)

    async def get_identification_result_async(
        self,
        request: main_models.GetIdentificationResultRequest,
    ) -> main_models.GetIdentificationResultResponse:
        runtime = RuntimeOptions()
        return await self.get_identification_result_with_options_async(request, runtime)

    def get_identification_session_with_options(
        self,
        request: main_models.GetIdentificationSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentificationSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentificationSession',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentificationSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identification_session_with_options_async(
        self,
        request: main_models.GetIdentificationSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentificationSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentificationSession',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentificationSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identification_session(
        self,
        request: main_models.GetIdentificationSessionRequest,
    ) -> main_models.GetIdentificationSessionResponse:
        runtime = RuntimeOptions()
        return self.get_identification_session_with_options(request, runtime)

    async def get_identification_session_async(
        self,
        request: main_models.GetIdentificationSessionRequest,
    ) -> main_models.GetIdentificationSessionResponse:
        runtime = RuntimeOptions()
        return await self.get_identification_session_with_options_async(request, runtime)

    def get_phone_number_identification_result_with_options(
        self,
        request: main_models.GetPhoneNumberIdentificationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneNumberIdentificationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_payload):
            query['SessionPayload'] = request.session_payload
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneNumberIdentificationResult',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneNumberIdentificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_number_identification_result_with_options_async(
        self,
        request: main_models.GetPhoneNumberIdentificationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneNumberIdentificationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_payload):
            query['SessionPayload'] = request.session_payload
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneNumberIdentificationResult',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneNumberIdentificationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_number_identification_result(
        self,
        request: main_models.GetPhoneNumberIdentificationResultRequest,
    ) -> main_models.GetPhoneNumberIdentificationResultResponse:
        runtime = RuntimeOptions()
        return self.get_phone_number_identification_result_with_options(request, runtime)

    async def get_phone_number_identification_result_async(
        self,
        request: main_models.GetPhoneNumberIdentificationResultRequest,
    ) -> main_models.GetPhoneNumberIdentificationResultResponse:
        runtime = RuntimeOptions()
        return await self.get_phone_number_identification_result_with_options_async(request, runtime)

    def get_phone_number_identification_url_with_options(
        self,
        request: main_models.GetPhoneNumberIdentificationUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneNumberIdentificationUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.remember_phone_number):
            query['RememberPhoneNumber'] = request.remember_phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneNumberIdentificationUrl',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneNumberIdentificationUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_number_identification_url_with_options_async(
        self,
        request: main_models.GetPhoneNumberIdentificationUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneNumberIdentificationUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.remember_phone_number):
            query['RememberPhoneNumber'] = request.remember_phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneNumberIdentificationUrl',
            version = '2023-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneNumberIdentificationUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_number_identification_url(
        self,
        request: main_models.GetPhoneNumberIdentificationUrlRequest,
    ) -> main_models.GetPhoneNumberIdentificationUrlResponse:
        runtime = RuntimeOptions()
        return self.get_phone_number_identification_url_with_options(request, runtime)

    async def get_phone_number_identification_url_async(
        self,
        request: main_models.GetPhoneNumberIdentificationUrlRequest,
    ) -> main_models.GetPhoneNumberIdentificationUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_phone_number_identification_url_with_options_async(request, runtime)
