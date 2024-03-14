# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dypnsapi_intl20170725 import models as dypnsapi_intl_20170725_models
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
        self._endpoint = self.get_endpoint('dypnsapi-intl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_verification_with_options(
        self,
        request: dypnsapi_intl_20170725_models.CheckVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_intl_20170725_models.CheckVerificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_sid):
            query['ServiceSid'] = request.service_sid
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.verification_id):
            query['VerificationId'] = request.verification_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckVerification',
            version='2017-07-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_intl_20170725_models.CheckVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_verification_with_options_async(
        self,
        request: dypnsapi_intl_20170725_models.CheckVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_intl_20170725_models.CheckVerificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_sid):
            query['ServiceSid'] = request.service_sid
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.verification_id):
            query['VerificationId'] = request.verification_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckVerification',
            version='2017-07-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_intl_20170725_models.CheckVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_verification(
        self,
        request: dypnsapi_intl_20170725_models.CheckVerificationRequest,
    ) -> dypnsapi_intl_20170725_models.CheckVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_verification_with_options(request, runtime)

    async def check_verification_async(
        self,
        request: dypnsapi_intl_20170725_models.CheckVerificationRequest,
    ) -> dypnsapi_intl_20170725_models.CheckVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_verification_with_options_async(request, runtime)

    def search_verification_with_options(
        self,
        request: dypnsapi_intl_20170725_models.SearchVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_intl_20170725_models.SearchVerificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.service_sid):
            query['ServiceSid'] = request.service_sid
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.verification_id):
            query['VerificationId'] = request.verification_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchVerification',
            version='2017-07-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_intl_20170725_models.SearchVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_verification_with_options_async(
        self,
        request: dypnsapi_intl_20170725_models.SearchVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_intl_20170725_models.SearchVerificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.service_sid):
            query['ServiceSid'] = request.service_sid
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.verification_id):
            query['VerificationId'] = request.verification_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchVerification',
            version='2017-07-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_intl_20170725_models.SearchVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_verification(
        self,
        request: dypnsapi_intl_20170725_models.SearchVerificationRequest,
    ) -> dypnsapi_intl_20170725_models.SearchVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_verification_with_options(request, runtime)

    async def search_verification_async(
        self,
        request: dypnsapi_intl_20170725_models.SearchVerificationRequest,
    ) -> dypnsapi_intl_20170725_models.SearchVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_verification_with_options_async(request, runtime)

    def start_verification_with_options(
        self,
        request: dypnsapi_intl_20170725_models.StartVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_intl_20170725_models.StartVerificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_sid):
            query['ServiceSid'] = request.service_sid
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVerification',
            version='2017-07-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_intl_20170725_models.StartVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_verification_with_options_async(
        self,
        request: dypnsapi_intl_20170725_models.StartVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_intl_20170725_models.StartVerificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_sid):
            query['ServiceSid'] = request.service_sid
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVerification',
            version='2017-07-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_intl_20170725_models.StartVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_verification(
        self,
        request: dypnsapi_intl_20170725_models.StartVerificationRequest,
    ) -> dypnsapi_intl_20170725_models.StartVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_verification_with_options(request, runtime)

    async def start_verification_async(
        self,
        request: dypnsapi_intl_20170725_models.StartVerificationRequest,
    ) -> dypnsapi_intl_20170725_models.StartVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_verification_with_options_async(request, runtime)
