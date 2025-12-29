# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dytnsapi20200217 import models as main_models
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

    def cert_no_three_element_verification_with_options(
        self,
        request: main_models.CertNoThreeElementVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CertNoThreeElementVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.cert_picture):
            query['CertPicture'] = request.cert_picture
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CertNoThreeElementVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CertNoThreeElementVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cert_no_three_element_verification_with_options_async(
        self,
        request: main_models.CertNoThreeElementVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CertNoThreeElementVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.cert_picture):
            query['CertPicture'] = request.cert_picture
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CertNoThreeElementVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CertNoThreeElementVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cert_no_three_element_verification(
        self,
        request: main_models.CertNoThreeElementVerificationRequest,
    ) -> main_models.CertNoThreeElementVerificationResponse:
        runtime = RuntimeOptions()
        return self.cert_no_three_element_verification_with_options(request, runtime)

    async def cert_no_three_element_verification_async(
        self,
        request: main_models.CertNoThreeElementVerificationRequest,
    ) -> main_models.CertNoThreeElementVerificationResponse:
        runtime = RuntimeOptions()
        return await self.cert_no_three_element_verification_with_options_async(request, runtime)

    def cert_no_two_element_verification_with_options(
        self,
        request: main_models.CertNoTwoElementVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CertNoTwoElementVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CertNoTwoElementVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CertNoTwoElementVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cert_no_two_element_verification_with_options_async(
        self,
        request: main_models.CertNoTwoElementVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CertNoTwoElementVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CertNoTwoElementVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CertNoTwoElementVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cert_no_two_element_verification(
        self,
        request: main_models.CertNoTwoElementVerificationRequest,
    ) -> main_models.CertNoTwoElementVerificationResponse:
        runtime = RuntimeOptions()
        return self.cert_no_two_element_verification_with_options(request, runtime)

    async def cert_no_two_element_verification_async(
        self,
        request: main_models.CertNoTwoElementVerificationRequest,
    ) -> main_models.CertNoTwoElementVerificationResponse:
        runtime = RuntimeOptions()
        return await self.cert_no_two_element_verification_with_options_async(request, runtime)

    def company_four_elements_verification_with_options(
        self,
        request: main_models.CompanyFourElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompanyFourElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.ep_cert_name):
            query['EpCertName'] = request.ep_cert_name
        if not DaraCore.is_null(request.ep_cert_no):
            query['EpCertNo'] = request.ep_cert_no
        if not DaraCore.is_null(request.legal_person_cert_name):
            query['LegalPersonCertName'] = request.legal_person_cert_name
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompanyFourElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompanyFourElementsVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_four_elements_verification_with_options_async(
        self,
        request: main_models.CompanyFourElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompanyFourElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.ep_cert_name):
            query['EpCertName'] = request.ep_cert_name
        if not DaraCore.is_null(request.ep_cert_no):
            query['EpCertNo'] = request.ep_cert_no
        if not DaraCore.is_null(request.legal_person_cert_name):
            query['LegalPersonCertName'] = request.legal_person_cert_name
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompanyFourElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompanyFourElementsVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_four_elements_verification(
        self,
        request: main_models.CompanyFourElementsVerificationRequest,
    ) -> main_models.CompanyFourElementsVerificationResponse:
        runtime = RuntimeOptions()
        return self.company_four_elements_verification_with_options(request, runtime)

    async def company_four_elements_verification_async(
        self,
        request: main_models.CompanyFourElementsVerificationRequest,
    ) -> main_models.CompanyFourElementsVerificationResponse:
        runtime = RuntimeOptions()
        return await self.company_four_elements_verification_with_options_async(request, runtime)

    def company_three_elements_verification_with_options(
        self,
        request: main_models.CompanyThreeElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompanyThreeElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.ep_cert_name):
            query['EpCertName'] = request.ep_cert_name
        if not DaraCore.is_null(request.ep_cert_no):
            query['EpCertNo'] = request.ep_cert_no
        if not DaraCore.is_null(request.legal_person_cert_name):
            query['LegalPersonCertName'] = request.legal_person_cert_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompanyThreeElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompanyThreeElementsVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_three_elements_verification_with_options_async(
        self,
        request: main_models.CompanyThreeElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompanyThreeElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.ep_cert_name):
            query['EpCertName'] = request.ep_cert_name
        if not DaraCore.is_null(request.ep_cert_no):
            query['EpCertNo'] = request.ep_cert_no
        if not DaraCore.is_null(request.legal_person_cert_name):
            query['LegalPersonCertName'] = request.legal_person_cert_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompanyThreeElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompanyThreeElementsVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_three_elements_verification(
        self,
        request: main_models.CompanyThreeElementsVerificationRequest,
    ) -> main_models.CompanyThreeElementsVerificationResponse:
        runtime = RuntimeOptions()
        return self.company_three_elements_verification_with_options(request, runtime)

    async def company_three_elements_verification_async(
        self,
        request: main_models.CompanyThreeElementsVerificationRequest,
    ) -> main_models.CompanyThreeElementsVerificationResponse:
        runtime = RuntimeOptions()
        return await self.company_three_elements_verification_with_options_async(request, runtime)

    def company_two_elements_verification_with_options(
        self,
        request: main_models.CompanyTwoElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompanyTwoElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.ep_cert_name):
            query['EpCertName'] = request.ep_cert_name
        if not DaraCore.is_null(request.ep_cert_no):
            query['EpCertNo'] = request.ep_cert_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompanyTwoElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompanyTwoElementsVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_two_elements_verification_with_options_async(
        self,
        request: main_models.CompanyTwoElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompanyTwoElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.ep_cert_name):
            query['EpCertName'] = request.ep_cert_name
        if not DaraCore.is_null(request.ep_cert_no):
            query['EpCertNo'] = request.ep_cert_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompanyTwoElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompanyTwoElementsVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_two_elements_verification(
        self,
        request: main_models.CompanyTwoElementsVerificationRequest,
    ) -> main_models.CompanyTwoElementsVerificationResponse:
        runtime = RuntimeOptions()
        return self.company_two_elements_verification_with_options(request, runtime)

    async def company_two_elements_verification_async(
        self,
        request: main_models.CompanyTwoElementsVerificationRequest,
    ) -> main_models.CompanyTwoElementsVerificationResponse:
        runtime = RuntimeOptions()
        return await self.company_two_elements_verification_with_options_async(request, runtime)

    def delete_contacts_with_options(
        self,
        request: main_models.DeleteContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContacts',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contacts_with_options_async(
        self,
        request: main_models.DeleteContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContacts',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contacts(
        self,
        request: main_models.DeleteContactsRequest,
    ) -> main_models.DeleteContactsResponse:
        runtime = RuntimeOptions()
        return self.delete_contacts_with_options(request, runtime)

    async def delete_contacts_async(
        self,
        request: main_models.DeleteContactsRequest,
    ) -> main_models.DeleteContactsResponse:
        runtime = RuntimeOptions()
        return await self.delete_contacts_with_options_async(request, runtime)

    def describe_empty_number_with_options(
        self,
        request: main_models.DescribeEmptyNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEmptyNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEmptyNumber',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEmptyNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_empty_number_with_options_async(
        self,
        request: main_models.DescribeEmptyNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEmptyNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEmptyNumber',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEmptyNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_empty_number(
        self,
        request: main_models.DescribeEmptyNumberRequest,
    ) -> main_models.DescribeEmptyNumberResponse:
        runtime = RuntimeOptions()
        return self.describe_empty_number_with_options(request, runtime)

    async def describe_empty_number_async(
        self,
        request: main_models.DescribeEmptyNumberRequest,
    ) -> main_models.DescribeEmptyNumberResponse:
        runtime = RuntimeOptions()
        return await self.describe_empty_number_with_options_async(request, runtime)

    def describe_mobile_operator_attribute_with_options(
        self,
        request: main_models.DescribeMobileOperatorAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMobileOperatorAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMobileOperatorAttribute',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMobileOperatorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mobile_operator_attribute_with_options_async(
        self,
        request: main_models.DescribeMobileOperatorAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMobileOperatorAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMobileOperatorAttribute',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMobileOperatorAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mobile_operator_attribute(
        self,
        request: main_models.DescribeMobileOperatorAttributeRequest,
    ) -> main_models.DescribeMobileOperatorAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_mobile_operator_attribute_with_options(request, runtime)

    async def describe_mobile_operator_attribute_async(
        self,
        request: main_models.DescribeMobileOperatorAttributeRequest,
    ) -> main_models.DescribeMobileOperatorAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_mobile_operator_attribute_with_options_async(request, runtime)

    def describe_phone_number_analysis_with_options(
        self,
        request: main_models.DescribePhoneNumberAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.number_type):
            query['NumberType'] = request.number_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rate):
            query['Rate'] = request.rate
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberAnalysis',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_analysis_with_options_async(
        self,
        request: main_models.DescribePhoneNumberAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.number_type):
            query['NumberType'] = request.number_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rate):
            query['Rate'] = request.rate
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberAnalysis',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_analysis(
        self,
        request: main_models.DescribePhoneNumberAnalysisRequest,
    ) -> main_models.DescribePhoneNumberAnalysisResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_analysis_with_options(request, runtime)

    async def describe_phone_number_analysis_async(
        self,
        request: main_models.DescribePhoneNumberAnalysisRequest,
    ) -> main_models.DescribePhoneNumberAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_analysis_with_options_async(request, runtime)

    def describe_phone_number_analysis_aiwith_options(
        self,
        request: main_models.DescribePhoneNumberAnalysisAIRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAnalysisAIResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.model_config):
            query['ModelConfig'] = request.model_config
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rate):
            query['Rate'] = request.rate
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberAnalysisAI',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAnalysisAIResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_analysis_aiwith_options_async(
        self,
        request: main_models.DescribePhoneNumberAnalysisAIRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAnalysisAIResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.model_config):
            query['ModelConfig'] = request.model_config
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rate):
            query['Rate'] = request.rate
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberAnalysisAI',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAnalysisAIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_analysis_ai(
        self,
        request: main_models.DescribePhoneNumberAnalysisAIRequest,
    ) -> main_models.DescribePhoneNumberAnalysisAIResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_analysis_aiwith_options(request, runtime)

    async def describe_phone_number_analysis_ai_async(
        self,
        request: main_models.DescribePhoneNumberAnalysisAIRequest,
    ) -> main_models.DescribePhoneNumberAnalysisAIResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_analysis_aiwith_options_async(request, runtime)

    def describe_phone_number_analysis_pai_with_options(
        self,
        request: main_models.DescribePhoneNumberAnalysisPaiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAnalysisPaiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.model_config):
            query['ModelConfig'] = request.model_config
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rate):
            query['Rate'] = request.rate
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberAnalysisPai',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAnalysisPaiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_analysis_pai_with_options_async(
        self,
        request: main_models.DescribePhoneNumberAnalysisPaiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAnalysisPaiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.model_config):
            query['ModelConfig'] = request.model_config
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rate):
            query['Rate'] = request.rate
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberAnalysisPai',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAnalysisPaiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_analysis_pai(
        self,
        request: main_models.DescribePhoneNumberAnalysisPaiRequest,
    ) -> main_models.DescribePhoneNumberAnalysisPaiResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_analysis_pai_with_options(request, runtime)

    async def describe_phone_number_analysis_pai_async(
        self,
        request: main_models.DescribePhoneNumberAnalysisPaiRequest,
    ) -> main_models.DescribePhoneNumberAnalysisPaiResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_analysis_pai_with_options_async(request, runtime)

    def describe_phone_number_analysis_transparent_with_options(
        self,
        request: main_models.DescribePhoneNumberAnalysisTransparentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAnalysisTransparentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.number_type):
            query['NumberType'] = request.number_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberAnalysisTransparent',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAnalysisTransparentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_analysis_transparent_with_options_async(
        self,
        request: main_models.DescribePhoneNumberAnalysisTransparentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAnalysisTransparentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.number_type):
            query['NumberType'] = request.number_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberAnalysisTransparent',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAnalysisTransparentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_analysis_transparent(
        self,
        request: main_models.DescribePhoneNumberAnalysisTransparentRequest,
    ) -> main_models.DescribePhoneNumberAnalysisTransparentResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_analysis_transparent_with_options(request, runtime)

    async def describe_phone_number_analysis_transparent_async(
        self,
        request: main_models.DescribePhoneNumberAnalysisTransparentRequest,
    ) -> main_models.DescribePhoneNumberAnalysisTransparentResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_analysis_transparent_with_options_async(request, runtime)

    def describe_phone_number_attribute_with_options(
        self,
        request: main_models.DescribePhoneNumberAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAttributeResponse:
        request.validate()
        query = {}
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
            action = 'DescribePhoneNumberAttribute',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_attribute_with_options_async(
        self,
        request: main_models.DescribePhoneNumberAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberAttributeResponse:
        request.validate()
        query = {}
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
            action = 'DescribePhoneNumberAttribute',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_attribute(
        self,
        request: main_models.DescribePhoneNumberAttributeRequest,
    ) -> main_models.DescribePhoneNumberAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_attribute_with_options(request, runtime)

    async def describe_phone_number_attribute_async(
        self,
        request: main_models.DescribePhoneNumberAttributeRequest,
    ) -> main_models.DescribePhoneNumberAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_attribute_with_options_async(request, runtime)

    def describe_phone_number_online_time_with_options(
        self,
        request: main_models.DescribePhoneNumberOnlineTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberOnlineTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberOnlineTime',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberOnlineTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_online_time_with_options_async(
        self,
        request: main_models.DescribePhoneNumberOnlineTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberOnlineTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberOnlineTime',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberOnlineTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_online_time(
        self,
        request: main_models.DescribePhoneNumberOnlineTimeRequest,
    ) -> main_models.DescribePhoneNumberOnlineTimeResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_online_time_with_options(request, runtime)

    async def describe_phone_number_online_time_async(
        self,
        request: main_models.DescribePhoneNumberOnlineTimeRequest,
    ) -> main_models.DescribePhoneNumberOnlineTimeResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_online_time_with_options_async(request, runtime)

    def describe_phone_number_operator_attribute_with_options(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberOperatorAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.result_count):
            query['ResultCount'] = request.result_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberOperatorAttribute',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberOperatorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_operator_attribute_with_options_async(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberOperatorAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.result_count):
            query['ResultCount'] = request.result_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberOperatorAttribute',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberOperatorAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_operator_attribute(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeRequest,
    ) -> main_models.DescribePhoneNumberOperatorAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_operator_attribute_with_options(request, runtime)

    async def describe_phone_number_operator_attribute_async(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeRequest,
    ) -> main_models.DescribePhoneNumberOperatorAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_operator_attribute_with_options_async(request, runtime)

    def describe_phone_number_operator_attribute_annual_with_options(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeAnnualRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberOperatorAttributeAnnualResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberOperatorAttributeAnnual',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberOperatorAttributeAnnualResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_operator_attribute_annual_with_options_async(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeAnnualRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberOperatorAttributeAnnualResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberOperatorAttributeAnnual',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberOperatorAttributeAnnualResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_operator_attribute_annual(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeAnnualRequest,
    ) -> main_models.DescribePhoneNumberOperatorAttributeAnnualResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_operator_attribute_annual_with_options(request, runtime)

    async def describe_phone_number_operator_attribute_annual_async(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeAnnualRequest,
    ) -> main_models.DescribePhoneNumberOperatorAttributeAnnualResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_operator_attribute_annual_with_options_async(request, runtime)

    def describe_phone_number_operator_attribute_annual_use_with_options(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeAnnualUseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberOperatorAttributeAnnualUseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberOperatorAttributeAnnualUse',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberOperatorAttributeAnnualUseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_operator_attribute_annual_use_with_options_async(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeAnnualUseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberOperatorAttributeAnnualUseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberOperatorAttributeAnnualUse',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberOperatorAttributeAnnualUseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_operator_attribute_annual_use(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeAnnualUseRequest,
    ) -> main_models.DescribePhoneNumberOperatorAttributeAnnualUseResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_operator_attribute_annual_use_with_options(request, runtime)

    async def describe_phone_number_operator_attribute_annual_use_async(
        self,
        request: main_models.DescribePhoneNumberOperatorAttributeAnnualUseRequest,
    ) -> main_models.DescribePhoneNumberOperatorAttributeAnnualUseResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_operator_attribute_annual_use_with_options_async(request, runtime)

    def describe_phone_number_risk_with_options(
        self,
        request: main_models.DescribePhoneNumberRiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberRiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberRisk',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_number_risk_with_options_async(
        self,
        request: main_models.DescribePhoneNumberRiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneNumberRiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneNumberRisk',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneNumberRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_number_risk(
        self,
        request: main_models.DescribePhoneNumberRiskRequest,
    ) -> main_models.DescribePhoneNumberRiskResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_number_risk_with_options(request, runtime)

    async def describe_phone_number_risk_async(
        self,
        request: main_models.DescribePhoneNumberRiskRequest,
    ) -> main_models.DescribePhoneNumberRiskResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_number_risk_with_options_async(request, runtime)

    def describe_phone_twice_tel_verify_with_options(
        self,
        request: main_models.DescribePhoneTwiceTelVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneTwiceTelVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneTwiceTelVerify',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneTwiceTelVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_twice_tel_verify_with_options_async(
        self,
        request: main_models.DescribePhoneTwiceTelVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePhoneTwiceTelVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePhoneTwiceTelVerify',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePhoneTwiceTelVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_twice_tel_verify(
        self,
        request: main_models.DescribePhoneTwiceTelVerifyRequest,
    ) -> main_models.DescribePhoneTwiceTelVerifyResponse:
        runtime = RuntimeOptions()
        return self.describe_phone_twice_tel_verify_with_options(request, runtime)

    async def describe_phone_twice_tel_verify_async(
        self,
        request: main_models.DescribePhoneTwiceTelVerifyRequest,
    ) -> main_models.DescribePhoneTwiceTelVerifyResponse:
        runtime = RuntimeOptions()
        return await self.describe_phone_twice_tel_verify_with_options_async(request, runtime)

    def get_uaidapply_token_sign_with_options(
        self,
        request: main_models.GetUAIDApplyTokenSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUAIDApplyTokenSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.format):
            query['Format'] = request.format
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param_key):
            query['ParamKey'] = request.param_key
        if not DaraCore.is_null(request.param_str):
            query['ParamStr'] = request.param_str
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUAIDApplyTokenSign',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUAIDApplyTokenSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_uaidapply_token_sign_with_options_async(
        self,
        request: main_models.GetUAIDApplyTokenSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUAIDApplyTokenSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.format):
            query['Format'] = request.format
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param_key):
            query['ParamKey'] = request.param_key
        if not DaraCore.is_null(request.param_str):
            query['ParamStr'] = request.param_str
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUAIDApplyTokenSign',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUAIDApplyTokenSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_uaidapply_token_sign(
        self,
        request: main_models.GetUAIDApplyTokenSignRequest,
    ) -> main_models.GetUAIDApplyTokenSignResponse:
        runtime = RuntimeOptions()
        return self.get_uaidapply_token_sign_with_options(request, runtime)

    async def get_uaidapply_token_sign_async(
        self,
        request: main_models.GetUAIDApplyTokenSignRequest,
    ) -> main_models.GetUAIDApplyTokenSignResponse:
        runtime = RuntimeOptions()
        return await self.get_uaidapply_token_sign_with_options_async(request, runtime)

    def get_uaidconversion_sign_with_options(
        self,
        request: main_models.GetUAIDConversionSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUAIDConversionSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.format):
            query['Format'] = request.format
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param_key):
            query['ParamKey'] = request.param_key
        if not DaraCore.is_null(request.param_str):
            query['ParamStr'] = request.param_str
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUAIDConversionSign',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUAIDConversionSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_uaidconversion_sign_with_options_async(
        self,
        request: main_models.GetUAIDConversionSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUAIDConversionSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.format):
            query['Format'] = request.format
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param_key):
            query['ParamKey'] = request.param_key
        if not DaraCore.is_null(request.param_str):
            query['ParamStr'] = request.param_str
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUAIDConversionSign',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUAIDConversionSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_uaidconversion_sign(
        self,
        request: main_models.GetUAIDConversionSignRequest,
    ) -> main_models.GetUAIDConversionSignResponse:
        runtime = RuntimeOptions()
        return self.get_uaidconversion_sign_with_options(request, runtime)

    async def get_uaidconversion_sign_async(
        self,
        request: main_models.GetUAIDConversionSignRequest,
    ) -> main_models.GetUAIDConversionSignResponse:
        runtime = RuntimeOptions()
        return await self.get_uaidconversion_sign_with_options_async(request, runtime)

    def invalid_phone_number_filter_with_options(
        self,
        request: main_models.InvalidPhoneNumberFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvalidPhoneNumberFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvalidPhoneNumberFilter',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvalidPhoneNumberFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def invalid_phone_number_filter_with_options_async(
        self,
        request: main_models.InvalidPhoneNumberFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvalidPhoneNumberFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvalidPhoneNumberFilter',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvalidPhoneNumberFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invalid_phone_number_filter(
        self,
        request: main_models.InvalidPhoneNumberFilterRequest,
    ) -> main_models.InvalidPhoneNumberFilterResponse:
        runtime = RuntimeOptions()
        return self.invalid_phone_number_filter_with_options(request, runtime)

    async def invalid_phone_number_filter_async(
        self,
        request: main_models.InvalidPhoneNumberFilterRequest,
    ) -> main_models.InvalidPhoneNumberFilterResponse:
        runtime = RuntimeOptions()
        return await self.invalid_phone_number_filter_with_options_async(request, runtime)

    def list_contacts_with_options(
        self,
        request: main_models.ListContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContacts',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_contacts_with_options_async(
        self,
        request: main_models.ListContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContacts',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_contacts(
        self,
        request: main_models.ListContactsRequest,
    ) -> main_models.ListContactsResponse:
        runtime = RuntimeOptions()
        return self.list_contacts_with_options(request, runtime)

    async def list_contacts_async(
        self,
        request: main_models.ListContactsRequest,
    ) -> main_models.ListContactsResponse:
        runtime = RuntimeOptions()
        return await self.list_contacts_with_options_async(request, runtime)

    def phone_number_convert_service_with_options(
        self,
        request: main_models.PhoneNumberConvertServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberConvertServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberConvertService',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberConvertServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def phone_number_convert_service_with_options_async(
        self,
        request: main_models.PhoneNumberConvertServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberConvertServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberConvertService',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberConvertServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def phone_number_convert_service(
        self,
        request: main_models.PhoneNumberConvertServiceRequest,
    ) -> main_models.PhoneNumberConvertServiceResponse:
        runtime = RuntimeOptions()
        return self.phone_number_convert_service_with_options(request, runtime)

    async def phone_number_convert_service_async(
        self,
        request: main_models.PhoneNumberConvertServiceRequest,
    ) -> main_models.PhoneNumberConvertServiceResponse:
        runtime = RuntimeOptions()
        return await self.phone_number_convert_service_with_options_async(request, runtime)

    def phone_number_encrypt_with_options(
        self,
        request: main_models.PhoneNumberEncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberEncryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberEncrypt',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def phone_number_encrypt_with_options_async(
        self,
        request: main_models.PhoneNumberEncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberEncryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberEncrypt',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def phone_number_encrypt(
        self,
        request: main_models.PhoneNumberEncryptRequest,
    ) -> main_models.PhoneNumberEncryptResponse:
        runtime = RuntimeOptions()
        return self.phone_number_encrypt_with_options(request, runtime)

    async def phone_number_encrypt_async(
        self,
        request: main_models.PhoneNumberEncryptRequest,
    ) -> main_models.PhoneNumberEncryptResponse:
        runtime = RuntimeOptions()
        return await self.phone_number_encrypt_with_options_async(request, runtime)

    def phone_number_status_for_account_with_options(
        self,
        request: main_models.PhoneNumberStatusForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForAccount',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def phone_number_status_for_account_with_options_async(
        self,
        request: main_models.PhoneNumberStatusForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForAccount',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def phone_number_status_for_account(
        self,
        request: main_models.PhoneNumberStatusForAccountRequest,
    ) -> main_models.PhoneNumberStatusForAccountResponse:
        runtime = RuntimeOptions()
        return self.phone_number_status_for_account_with_options(request, runtime)

    async def phone_number_status_for_account_async(
        self,
        request: main_models.PhoneNumberStatusForAccountRequest,
    ) -> main_models.PhoneNumberStatusForAccountResponse:
        runtime = RuntimeOptions()
        return await self.phone_number_status_for_account_with_options_async(request, runtime)

    def phone_number_status_for_public_with_options(
        self,
        request: main_models.PhoneNumberStatusForPublicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForPublicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForPublic',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForPublicResponse(),
            self.call_api(params, req, runtime)
        )

    async def phone_number_status_for_public_with_options_async(
        self,
        request: main_models.PhoneNumberStatusForPublicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForPublicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForPublic',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForPublicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def phone_number_status_for_public(
        self,
        request: main_models.PhoneNumberStatusForPublicRequest,
    ) -> main_models.PhoneNumberStatusForPublicResponse:
        runtime = RuntimeOptions()
        return self.phone_number_status_for_public_with_options(request, runtime)

    async def phone_number_status_for_public_async(
        self,
        request: main_models.PhoneNumberStatusForPublicRequest,
    ) -> main_models.PhoneNumberStatusForPublicResponse:
        runtime = RuntimeOptions()
        return await self.phone_number_status_for_public_with_options_async(request, runtime)

    def phone_number_status_for_real_with_options(
        self,
        request: main_models.PhoneNumberStatusForRealRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForRealResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForReal',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForRealResponse(),
            self.call_api(params, req, runtime)
        )

    async def phone_number_status_for_real_with_options_async(
        self,
        request: main_models.PhoneNumberStatusForRealRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForRealResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForReal',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForRealResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def phone_number_status_for_real(
        self,
        request: main_models.PhoneNumberStatusForRealRequest,
    ) -> main_models.PhoneNumberStatusForRealResponse:
        runtime = RuntimeOptions()
        return self.phone_number_status_for_real_with_options(request, runtime)

    async def phone_number_status_for_real_async(
        self,
        request: main_models.PhoneNumberStatusForRealRequest,
    ) -> main_models.PhoneNumberStatusForRealResponse:
        runtime = RuntimeOptions()
        return await self.phone_number_status_for_real_with_options_async(request, runtime)

    def phone_number_status_for_sms_with_options(
        self,
        request: main_models.PhoneNumberStatusForSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForSms',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def phone_number_status_for_sms_with_options_async(
        self,
        request: main_models.PhoneNumberStatusForSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForSms',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def phone_number_status_for_sms(
        self,
        request: main_models.PhoneNumberStatusForSmsRequest,
    ) -> main_models.PhoneNumberStatusForSmsResponse:
        runtime = RuntimeOptions()
        return self.phone_number_status_for_sms_with_options(request, runtime)

    async def phone_number_status_for_sms_async(
        self,
        request: main_models.PhoneNumberStatusForSmsRequest,
    ) -> main_models.PhoneNumberStatusForSmsResponse:
        runtime = RuntimeOptions()
        return await self.phone_number_status_for_sms_with_options_async(request, runtime)

    def phone_number_status_for_voice_with_options(
        self,
        request: main_models.PhoneNumberStatusForVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForVoiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForVoice',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def phone_number_status_for_voice_with_options_async(
        self,
        request: main_models.PhoneNumberStatusForVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PhoneNumberStatusForVoiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PhoneNumberStatusForVoice',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PhoneNumberStatusForVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def phone_number_status_for_voice(
        self,
        request: main_models.PhoneNumberStatusForVoiceRequest,
    ) -> main_models.PhoneNumberStatusForVoiceResponse:
        runtime = RuntimeOptions()
        return self.phone_number_status_for_voice_with_options(request, runtime)

    async def phone_number_status_for_voice_async(
        self,
        request: main_models.PhoneNumberStatusForVoiceRequest,
    ) -> main_models.PhoneNumberStatusForVoiceResponse:
        runtime = RuntimeOptions()
        return await self.phone_number_status_for_voice_with_options_async(request, runtime)

    def query_available_auth_code_with_options(
        self,
        request: main_models.QueryAvailableAuthCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailableAuthCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvailableAuthCode',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailableAuthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_available_auth_code_with_options_async(
        self,
        request: main_models.QueryAvailableAuthCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailableAuthCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvailableAuthCode',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailableAuthCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_available_auth_code(
        self,
        request: main_models.QueryAvailableAuthCodeRequest,
    ) -> main_models.QueryAvailableAuthCodeResponse:
        runtime = RuntimeOptions()
        return self.query_available_auth_code_with_options(request, runtime)

    async def query_available_auth_code_async(
        self,
        request: main_models.QueryAvailableAuthCodeRequest,
    ) -> main_models.QueryAvailableAuthCodeResponse:
        runtime = RuntimeOptions()
        return await self.query_available_auth_code_with_options_async(request, runtime)

    def query_package_type_info_with_options(
        self,
        request: main_models.QueryPackageTypeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPackageTypeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPackageTypeInfo',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPackageTypeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_package_type_info_with_options_async(
        self,
        request: main_models.QueryPackageTypeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPackageTypeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPackageTypeInfo',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPackageTypeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_package_type_info(
        self,
        request: main_models.QueryPackageTypeInfoRequest,
    ) -> main_models.QueryPackageTypeInfoResponse:
        runtime = RuntimeOptions()
        return self.query_package_type_info_with_options(request, runtime)

    async def query_package_type_info_async(
        self,
        request: main_models.QueryPackageTypeInfoRequest,
    ) -> main_models.QueryPackageTypeInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_package_type_info_with_options_async(request, runtime)

    def query_phone_number_online_time_with_options(
        self,
        request: main_models.QueryPhoneNumberOnlineTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPhoneNumberOnlineTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPhoneNumberOnlineTime',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPhoneNumberOnlineTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_phone_number_online_time_with_options_async(
        self,
        request: main_models.QueryPhoneNumberOnlineTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPhoneNumberOnlineTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPhoneNumberOnlineTime',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPhoneNumberOnlineTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_phone_number_online_time(
        self,
        request: main_models.QueryPhoneNumberOnlineTimeRequest,
    ) -> main_models.QueryPhoneNumberOnlineTimeResponse:
        runtime = RuntimeOptions()
        return self.query_phone_number_online_time_with_options(request, runtime)

    async def query_phone_number_online_time_async(
        self,
        request: main_models.QueryPhoneNumberOnlineTimeRequest,
    ) -> main_models.QueryPhoneNumberOnlineTimeResponse:
        runtime = RuntimeOptions()
        return await self.query_phone_number_online_time_with_options_async(request, runtime)

    def query_phone_twice_tel_verify_with_options(
        self,
        request: main_models.QueryPhoneTwiceTelVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPhoneTwiceTelVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPhoneTwiceTelVerify',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPhoneTwiceTelVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_phone_twice_tel_verify_with_options_async(
        self,
        request: main_models.QueryPhoneTwiceTelVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPhoneTwiceTelVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPhoneTwiceTelVerify',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPhoneTwiceTelVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_phone_twice_tel_verify(
        self,
        request: main_models.QueryPhoneTwiceTelVerifyRequest,
    ) -> main_models.QueryPhoneTwiceTelVerifyResponse:
        runtime = RuntimeOptions()
        return self.query_phone_twice_tel_verify_with_options(request, runtime)

    async def query_phone_twice_tel_verify_async(
        self,
        request: main_models.QueryPhoneTwiceTelVerifyRequest,
    ) -> main_models.QueryPhoneTwiceTelVerifyResponse:
        runtime = RuntimeOptions()
        return await self.query_phone_twice_tel_verify_with_options_async(request, runtime)

    def query_tag_apply_rule_with_options(
        self,
        request: main_models.QueryTagApplyRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagApplyRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagApplyRule',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagApplyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_apply_rule_with_options_async(
        self,
        request: main_models.QueryTagApplyRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagApplyRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagApplyRule',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagApplyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_apply_rule(
        self,
        request: main_models.QueryTagApplyRuleRequest,
    ) -> main_models.QueryTagApplyRuleResponse:
        runtime = RuntimeOptions()
        return self.query_tag_apply_rule_with_options(request, runtime)

    async def query_tag_apply_rule_async(
        self,
        request: main_models.QueryTagApplyRuleRequest,
    ) -> main_models.QueryTagApplyRuleResponse:
        runtime = RuntimeOptions()
        return await self.query_tag_apply_rule_with_options_async(request, runtime)

    def query_tag_info_by_selection_with_options(
        self,
        request: main_models.QueryTagInfoBySelectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagInfoBySelectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry_id):
            query['IndustryId'] = request.industry_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagInfoBySelection',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagInfoBySelectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_info_by_selection_with_options_async(
        self,
        request: main_models.QueryTagInfoBySelectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagInfoBySelectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry_id):
            query['IndustryId'] = request.industry_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagInfoBySelection',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagInfoBySelectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_info_by_selection(
        self,
        request: main_models.QueryTagInfoBySelectionRequest,
    ) -> main_models.QueryTagInfoBySelectionResponse:
        runtime = RuntimeOptions()
        return self.query_tag_info_by_selection_with_options(request, runtime)

    async def query_tag_info_by_selection_async(
        self,
        request: main_models.QueryTagInfoBySelectionRequest,
    ) -> main_models.QueryTagInfoBySelectionResponse:
        runtime = RuntimeOptions()
        return await self.query_tag_info_by_selection_with_options_async(request, runtime)

    def query_tag_list_page_with_options(
        self,
        request: main_models.QueryTagListPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagListPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagListPage',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagListPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_list_page_with_options_async(
        self,
        request: main_models.QueryTagListPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagListPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagListPage',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagListPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_list_page(
        self,
        request: main_models.QueryTagListPageRequest,
    ) -> main_models.QueryTagListPageResponse:
        runtime = RuntimeOptions()
        return self.query_tag_list_page_with_options(request, runtime)

    async def query_tag_list_page_async(
        self,
        request: main_models.QueryTagListPageRequest,
    ) -> main_models.QueryTagListPageResponse:
        runtime = RuntimeOptions()
        return await self.query_tag_list_page_with_options_async(request, runtime)

    def query_task_list_with_options(
        self,
        tmp_req: main_models.QueryTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskListResponse:
        tmp_req.validate()
        request = main_models.QueryTaskListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.result):
            request.result_shrink = Utils.array_to_string_with_specified_style(tmp_req.result, 'Result', 'json')
        if not DaraCore.is_null(tmp_req.task_type):
            request.task_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_type, 'TaskType', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.result_shrink):
            query['Result'] = request.result_shrink
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type_shrink):
            query['TaskType'] = request.task_type_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskList',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_list_with_options_async(
        self,
        tmp_req: main_models.QueryTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskListResponse:
        tmp_req.validate()
        request = main_models.QueryTaskListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.result):
            request.result_shrink = Utils.array_to_string_with_specified_style(tmp_req.result, 'Result', 'json')
        if not DaraCore.is_null(tmp_req.task_type):
            request.task_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_type, 'TaskType', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.result_shrink):
            query['Result'] = request.result_shrink
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type_shrink):
            query['TaskType'] = request.task_type_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskList',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_list(
        self,
        request: main_models.QueryTaskListRequest,
    ) -> main_models.QueryTaskListResponse:
        runtime = RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    async def query_task_list_async(
        self,
        request: main_models.QueryTaskListRequest,
    ) -> main_models.QueryTaskListResponse:
        runtime = RuntimeOptions()
        return await self.query_task_list_with_options_async(request, runtime)

    def query_usage_statistics_by_tag_id_with_options(
        self,
        request: main_models.QueryUsageStatisticsByTagIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUsageStatisticsByTagIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUsageStatisticsByTagId',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUsageStatisticsByTagIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_usage_statistics_by_tag_id_with_options_async(
        self,
        request: main_models.QueryUsageStatisticsByTagIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUsageStatisticsByTagIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUsageStatisticsByTagId',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUsageStatisticsByTagIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_usage_statistics_by_tag_id(
        self,
        request: main_models.QueryUsageStatisticsByTagIdRequest,
    ) -> main_models.QueryUsageStatisticsByTagIdResponse:
        runtime = RuntimeOptions()
        return self.query_usage_statistics_by_tag_id_with_options(request, runtime)

    async def query_usage_statistics_by_tag_id_async(
        self,
        request: main_models.QueryUsageStatisticsByTagIdRequest,
    ) -> main_models.QueryUsageStatisticsByTagIdResponse:
        runtime = RuntimeOptions()
        return await self.query_usage_statistics_by_tag_id_with_options_async(request, runtime)

    def three_elements_verification_with_options(
        self,
        request: main_models.ThreeElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ThreeElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.cert_code):
            query['CertCode'] = request.cert_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ThreeElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ThreeElementsVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def three_elements_verification_with_options_async(
        self,
        request: main_models.ThreeElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ThreeElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.cert_code):
            query['CertCode'] = request.cert_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ThreeElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ThreeElementsVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def three_elements_verification(
        self,
        request: main_models.ThreeElementsVerificationRequest,
    ) -> main_models.ThreeElementsVerificationResponse:
        runtime = RuntimeOptions()
        return self.three_elements_verification_with_options(request, runtime)

    async def three_elements_verification_async(
        self,
        request: main_models.ThreeElementsVerificationRequest,
    ) -> main_models.ThreeElementsVerificationResponse:
        runtime = RuntimeOptions()
        return await self.three_elements_verification_with_options_async(request, runtime)

    def two_elements_verification_with_options(
        self,
        request: main_models.TwoElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TwoElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TwoElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TwoElementsVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def two_elements_verification_with_options_async(
        self,
        request: main_models.TwoElementsVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TwoElementsVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.input_number):
            query['InputNumber'] = request.input_number
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TwoElementsVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TwoElementsVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def two_elements_verification(
        self,
        request: main_models.TwoElementsVerificationRequest,
    ) -> main_models.TwoElementsVerificationResponse:
        runtime = RuntimeOptions()
        return self.two_elements_verification_with_options(request, runtime)

    async def two_elements_verification_async(
        self,
        request: main_models.TwoElementsVerificationRequest,
    ) -> main_models.TwoElementsVerificationResponse:
        runtime = RuntimeOptions()
        return await self.two_elements_verification_with_options_async(request, runtime)

    def u_aidcollection_with_options(
        self,
        request: main_models.UAIDCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UAIDCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_grant_id):
            query['UserGrantId'] = request.user_grant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UAIDCollection',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UAIDCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def u_aidcollection_with_options_async(
        self,
        request: main_models.UAIDCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UAIDCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_grant_id):
            query['UserGrantId'] = request.user_grant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UAIDCollection',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UAIDCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def u_aidcollection(
        self,
        request: main_models.UAIDCollectionRequest,
    ) -> main_models.UAIDCollectionResponse:
        runtime = RuntimeOptions()
        return self.u_aidcollection_with_options(request, runtime)

    async def u_aidcollection_async(
        self,
        request: main_models.UAIDCollectionRequest,
    ) -> main_models.UAIDCollectionResponse:
        runtime = RuntimeOptions()
        return await self.u_aidcollection_with_options_async(request, runtime)

    def u_aidconversion_with_options(
        self,
        request: main_models.UAIDConversionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UAIDConversionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.uaid_list):
            query['UaidList'] = request.uaid_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UAIDConversion',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UAIDConversionResponse(),
            self.call_api(params, req, runtime)
        )

    async def u_aidconversion_with_options_async(
        self,
        request: main_models.UAIDConversionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UAIDConversionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.uaid_list):
            query['UaidList'] = request.uaid_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UAIDConversion',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UAIDConversionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def u_aidconversion(
        self,
        request: main_models.UAIDConversionRequest,
    ) -> main_models.UAIDConversionResponse:
        runtime = RuntimeOptions()
        return self.u_aidconversion_with_options(request, runtime)

    async def u_aidconversion_async(
        self,
        request: main_models.UAIDConversionRequest,
    ) -> main_models.UAIDConversionResponse:
        runtime = RuntimeOptions()
        return await self.u_aidconversion_with_options_async(request, runtime)

    def u_aidverification_with_options(
        self,
        request: main_models.UAIDVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UAIDVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_grant_id):
            query['UserGrantId'] = request.user_grant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UAIDVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UAIDVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def u_aidverification_with_options_async(
        self,
        request: main_models.UAIDVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UAIDVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.carrier):
            query['Carrier'] = request.carrier
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_grant_id):
            query['UserGrantId'] = request.user_grant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UAIDVerification',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UAIDVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def u_aidverification(
        self,
        request: main_models.UAIDVerificationRequest,
    ) -> main_models.UAIDVerificationResponse:
        runtime = RuntimeOptions()
        return self.u_aidverification_with_options(request, runtime)

    async def u_aidverification_async(
        self,
        request: main_models.UAIDVerificationRequest,
    ) -> main_models.UAIDVerificationResponse:
        runtime = RuntimeOptions()
        return await self.u_aidverification_with_options_async(request, runtime)

    def update_contacts_with_options(
        self,
        request: main_models.UpdateContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not DaraCore.is_null(request.mail_status):
            query['MailStatus'] = request.mail_status
        if not DaraCore.is_null(request.open_status_warning):
            query['OpenStatusWarning'] = request.open_status_warning
        if not DaraCore.is_null(request.opent_attribution_warning):
            query['OpentAttributionWarning'] = request.opent_attribution_warning
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_status):
            query['PhoneStatus'] = request.phone_status
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContacts',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_contacts_with_options_async(
        self,
        request: main_models.UpdateContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not DaraCore.is_null(request.mail_status):
            query['MailStatus'] = request.mail_status
        if not DaraCore.is_null(request.open_status_warning):
            query['OpenStatusWarning'] = request.open_status_warning
        if not DaraCore.is_null(request.opent_attribution_warning):
            query['OpentAttributionWarning'] = request.opent_attribution_warning
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_status):
            query['PhoneStatus'] = request.phone_status
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContacts',
            version = '2020-02-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_contacts(
        self,
        request: main_models.UpdateContactsRequest,
    ) -> main_models.UpdateContactsResponse:
        runtime = RuntimeOptions()
        return self.update_contacts_with_options(request, runtime)

    async def update_contacts_async(
        self,
        request: main_models.UpdateContactsRequest,
    ) -> main_models.UpdateContactsResponse:
        runtime = RuntimeOptions()
        return await self.update_contacts_with_options_async(request, runtime)
