# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dytnsapi20200217 import models as dytnsapi_20200217_models
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

    def describe_empty_number_detect_with_options(
        self,
        request: dytnsapi_20200217_models.DescribeEmptyNumberDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribeEmptyNumberDetectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmptyNumberDetect',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribeEmptyNumberDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_empty_number_detect_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribeEmptyNumberDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribeEmptyNumberDetectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmptyNumberDetect',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribeEmptyNumberDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_empty_number_detect(
        self,
        request: dytnsapi_20200217_models.DescribeEmptyNumberDetectRequest,
    ) -> dytnsapi_20200217_models.DescribeEmptyNumberDetectResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_empty_number_detect_with_options(request, runtime)

    async def describe_empty_number_detect_async(
        self,
        request: dytnsapi_20200217_models.DescribeEmptyNumberDetectRequest,
    ) -> dytnsapi_20200217_models.DescribeEmptyNumberDetectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_empty_number_detect_with_options_async(request, runtime)

    def describe_phone_number_analysis_with_options(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAnalysisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.input_number):
            query['InputNumber'] = request.input_number
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.number_type):
            query['NumberType'] = request.number_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rate):
            query['Rate'] = request.rate
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberAnalysis',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_analysis_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAnalysisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.input_number):
            query['InputNumber'] = request.input_number
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.number_type):
            query['NumberType'] = request.number_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rate):
            query['Rate'] = request.rate
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberAnalysis',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_analysis(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAnalysisRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_number_analysis_with_options(request, runtime)

    async def describe_phone_number_analysis_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAnalysisRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_number_analysis_with_options_async(request, runtime)

    def describe_phone_number_attribute_with_options(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberAttribute',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_attribute_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberAttribute',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_attribute(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAttributeRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_number_attribute_with_options(request, runtime)

    async def describe_phone_number_attribute_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAttributeRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_number_attribute_with_options_async(request, runtime)

    def describe_phone_number_online_time_with_options(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.carrier):
            query['Carrier'] = request.carrier
        if not UtilClient.is_unset(request.input_number):
            query['InputNumber'] = request.input_number
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberOnlineTime',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_online_time_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.carrier):
            query['Carrier'] = request.carrier
        if not UtilClient.is_unset(request.input_number):
            query['InputNumber'] = request.input_number
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberOnlineTime',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_online_time(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_number_online_time_with_options(request, runtime)

    async def describe_phone_number_online_time_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberOnlineTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_number_online_time_with_options_async(request, runtime)

    def describe_phone_number_resale_with_options(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberResaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberResaleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.since):
            query['Since'] = request.since
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberResale',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberResaleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_resale_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberResaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberResaleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.since):
            query['Since'] = request.since
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberResale',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberResaleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_resale(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberResaleRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberResaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_number_resale_with_options(request, runtime)

    async def describe_phone_number_resale_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberResaleRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberResaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_number_resale_with_options_async(request, runtime)

    def describe_phone_number_status_with_options(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberStatus',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_status_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneNumberStatus',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_status(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberStatusRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_number_status_with_options(request, runtime)

    async def describe_phone_number_status_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberStatusRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_number_status_with_options_async(request, runtime)

    def invalid_phone_number_filter_with_options(
        self,
        request: dytnsapi_20200217_models.InvalidPhoneNumberFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.InvalidPhoneNumberFilterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.input_number):
            query['InputNumber'] = request.input_number
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvalidPhoneNumberFilter',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.InvalidPhoneNumberFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def invalid_phone_number_filter_with_options_async(
        self,
        request: dytnsapi_20200217_models.InvalidPhoneNumberFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.InvalidPhoneNumberFilterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.input_number):
            query['InputNumber'] = request.input_number
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvalidPhoneNumberFilter',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.InvalidPhoneNumberFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invalid_phone_number_filter(
        self,
        request: dytnsapi_20200217_models.InvalidPhoneNumberFilterRequest,
    ) -> dytnsapi_20200217_models.InvalidPhoneNumberFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.invalid_phone_number_filter_with_options(request, runtime)

    async def invalid_phone_number_filter_async(
        self,
        request: dytnsapi_20200217_models.InvalidPhoneNumberFilterRequest,
    ) -> dytnsapi_20200217_models.InvalidPhoneNumberFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invalid_phone_number_filter_with_options_async(request, runtime)

    def phone_number_encrypt_with_options(
        self,
        request: dytnsapi_20200217_models.PhoneNumberEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.PhoneNumberEncryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.input_number):
            query['InputNumber'] = request.input_number
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PhoneNumberEncrypt',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.PhoneNumberEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def phone_number_encrypt_with_options_async(
        self,
        request: dytnsapi_20200217_models.PhoneNumberEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.PhoneNumberEncryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.input_number):
            query['InputNumber'] = request.input_number
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PhoneNumberEncrypt',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.PhoneNumberEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def phone_number_encrypt(
        self,
        request: dytnsapi_20200217_models.PhoneNumberEncryptRequest,
    ) -> dytnsapi_20200217_models.PhoneNumberEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.phone_number_encrypt_with_options(request, runtime)

    async def phone_number_encrypt_async(
        self,
        request: dytnsapi_20200217_models.PhoneNumberEncryptRequest,
    ) -> dytnsapi_20200217_models.PhoneNumberEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.phone_number_encrypt_with_options_async(request, runtime)

    def pvr_callback_fcuwith_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.PvrCallbackFCUResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='PvrCallbackFCU',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.PvrCallbackFCUResponse(),
            self.call_api(params, req, runtime)
        )

    async def pvr_callback_fcuwith_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.PvrCallbackFCUResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='PvrCallbackFCU',
            version='2020-02-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.PvrCallbackFCUResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pvr_callback_fcu(self) -> dytnsapi_20200217_models.PvrCallbackFCUResponse:
        runtime = util_models.RuntimeOptions()
        return self.pvr_callback_fcuwith_options(runtime)

    async def pvr_callback_fcu_async(self) -> dytnsapi_20200217_models.PvrCallbackFCUResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pvr_callback_fcuwith_options_async(runtime)
