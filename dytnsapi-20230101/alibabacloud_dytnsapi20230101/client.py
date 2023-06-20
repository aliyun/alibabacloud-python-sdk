# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dytnsapi20230101 import models as dytnsapi_20230101_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_phone_number_identification_result_with_options(
        self,
        request: dytnsapi_20230101_models.GetPhoneNumberIdentificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20230101_models.GetPhoneNumberIdentificationResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_payload):
            query['SessionPayload'] = request.session_payload
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneNumberIdentificationResult',
            version='2023-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20230101_models.GetPhoneNumberIdentificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_number_identification_result_with_options_async(
        self,
        request: dytnsapi_20230101_models.GetPhoneNumberIdentificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20230101_models.GetPhoneNumberIdentificationResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_payload):
            query['SessionPayload'] = request.session_payload
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneNumberIdentificationResult',
            version='2023-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20230101_models.GetPhoneNumberIdentificationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_number_identification_result(
        self,
        request: dytnsapi_20230101_models.GetPhoneNumberIdentificationResultRequest,
    ) -> dytnsapi_20230101_models.GetPhoneNumberIdentificationResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_phone_number_identification_result_with_options(request, runtime)

    async def get_phone_number_identification_result_async(
        self,
        request: dytnsapi_20230101_models.GetPhoneNumberIdentificationResultRequest,
    ) -> dytnsapi_20230101_models.GetPhoneNumberIdentificationResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_phone_number_identification_result_with_options_async(request, runtime)

    def get_phone_number_identification_url_with_options(
        self,
        request: dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.remember_phone_number):
            query['RememberPhoneNumber'] = request.remember_phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneNumberIdentificationUrl',
            version='2023-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_number_identification_url_with_options_async(
        self,
        request: dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.remember_phone_number):
            query['RememberPhoneNumber'] = request.remember_phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneNumberIdentificationUrl',
            version='2023-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_number_identification_url(
        self,
        request: dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlRequest,
    ) -> dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_phone_number_identification_url_with_options(request, runtime)

    async def get_phone_number_identification_url_async(
        self,
        request: dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlRequest,
    ) -> dytnsapi_20230101_models.GetPhoneNumberIdentificationUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_phone_number_identification_url_with_options_async(request, runtime)
