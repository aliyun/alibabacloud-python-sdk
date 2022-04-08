# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_address_purification20191118 import models as address_purification_20191118_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('address-purification', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def correct_address_with_options(
        self,
        request: address_purification_20191118_models.CorrectAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.CorrectAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CorrectAddress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.CorrectAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def correct_address_with_options_async(
        self,
        request: address_purification_20191118_models.CorrectAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.CorrectAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CorrectAddress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.CorrectAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def correct_address(
        self,
        request: address_purification_20191118_models.CorrectAddressRequest,
    ) -> address_purification_20191118_models.CorrectAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.correct_address_with_options(request, runtime)

    async def correct_address_async(
        self,
        request: address_purification_20191118_models.CorrectAddressRequest,
    ) -> address_purification_20191118_models.CorrectAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.correct_address_with_options_async(request, runtime)

    def extract_address_with_options(
        self,
        request: address_purification_20191118_models.ExtractAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractAddress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_address_with_options_async(
        self,
        request: address_purification_20191118_models.ExtractAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractAddress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_address(
        self,
        request: address_purification_20191118_models.ExtractAddressRequest,
    ) -> address_purification_20191118_models.ExtractAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_address_with_options(request, runtime)

    async def extract_address_async(
        self,
        request: address_purification_20191118_models.ExtractAddressRequest,
    ) -> address_purification_20191118_models.ExtractAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_address_with_options_async(request, runtime)

    def extract_name_with_options(
        self,
        request: address_purification_20191118_models.ExtractNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractName',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_name_with_options_async(
        self,
        request: address_purification_20191118_models.ExtractNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractName',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_name(
        self,
        request: address_purification_20191118_models.ExtractNameRequest,
    ) -> address_purification_20191118_models.ExtractNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_name_with_options(request, runtime)

    async def extract_name_async(
        self,
        request: address_purification_20191118_models.ExtractNameRequest,
    ) -> address_purification_20191118_models.ExtractNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_name_with_options_async(request, runtime)

    def extract_phone_with_options(
        self,
        request: address_purification_20191118_models.ExtractPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractPhoneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractPhone',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_phone_with_options_async(
        self,
        request: address_purification_20191118_models.ExtractPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractPhoneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractPhone',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_phone(
        self,
        request: address_purification_20191118_models.ExtractPhoneRequest,
    ) -> address_purification_20191118_models.ExtractPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_phone_with_options(request, runtime)

    async def extract_phone_async(
        self,
        request: address_purification_20191118_models.ExtractPhoneRequest,
    ) -> address_purification_20191118_models.ExtractPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_phone_with_options_async(request, runtime)

    def get_address_division_code_with_options(
        self,
        request: address_purification_20191118_models.GetAddressDivisionCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressDivisionCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAddressDivisionCode',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressDivisionCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_address_division_code_with_options_async(
        self,
        request: address_purification_20191118_models.GetAddressDivisionCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressDivisionCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAddressDivisionCode',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressDivisionCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_address_division_code(
        self,
        request: address_purification_20191118_models.GetAddressDivisionCodeRequest,
    ) -> address_purification_20191118_models.GetAddressDivisionCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_address_division_code_with_options(request, runtime)

    async def get_address_division_code_async(
        self,
        request: address_purification_20191118_models.GetAddressDivisionCodeRequest,
    ) -> address_purification_20191118_models.GetAddressDivisionCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_address_division_code_with_options_async(request, runtime)

    def get_address_similarity_with_options(
        self,
        request: address_purification_20191118_models.GetAddressSimilarityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressSimilarityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAddressSimilarity',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressSimilarityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_address_similarity_with_options_async(
        self,
        request: address_purification_20191118_models.GetAddressSimilarityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressSimilarityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAddressSimilarity',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressSimilarityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_address_similarity(
        self,
        request: address_purification_20191118_models.GetAddressSimilarityRequest,
    ) -> address_purification_20191118_models.GetAddressSimilarityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_address_similarity_with_options(request, runtime)

    async def get_address_similarity_async(
        self,
        request: address_purification_20191118_models.GetAddressSimilarityRequest,
    ) -> address_purification_20191118_models.GetAddressSimilarityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_address_similarity_with_options_async(request, runtime)

    def get_zipcode_with_options(
        self,
        request: address_purification_20191118_models.GetZipcodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetZipcodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetZipcode',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetZipcodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_zipcode_with_options_async(
        self,
        request: address_purification_20191118_models.GetZipcodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetZipcodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetZipcode',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetZipcodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_zipcode(
        self,
        request: address_purification_20191118_models.GetZipcodeRequest,
    ) -> address_purification_20191118_models.GetZipcodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_zipcode_with_options(request, runtime)

    async def get_zipcode_async(
        self,
        request: address_purification_20191118_models.GetZipcodeRequest,
    ) -> address_purification_20191118_models.GetZipcodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_zipcode_with_options_async(request, runtime)

    def structure_address_with_options(
        self,
        request: address_purification_20191118_models.StructureAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.StructureAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StructureAddress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.StructureAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def structure_address_with_options_async(
        self,
        request: address_purification_20191118_models.StructureAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.StructureAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.default_city):
            body['DefaultCity'] = request.default_city
        if not UtilClient.is_unset(request.default_district):
            body['DefaultDistrict'] = request.default_district
        if not UtilClient.is_unset(request.default_province):
            body['DefaultProvince'] = request.default_province
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StructureAddress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            address_purification_20191118_models.StructureAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def structure_address(
        self,
        request: address_purification_20191118_models.StructureAddressRequest,
    ) -> address_purification_20191118_models.StructureAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.structure_address_with_options(request, runtime)

    async def structure_address_async(
        self,
        request: address_purification_20191118_models.StructureAddressRequest,
    ) -> address_purification_20191118_models.StructureAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.structure_address_with_options_async(request, runtime)
